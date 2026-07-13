from __future__ import annotations

from dataclasses import dataclass
from math import sqrt
from statistics import median
from typing import Iterable, Mapping, Sequence


@dataclass(frozen=True)
class ModelPoint:
    """A model configuration represented in cost-quality space."""

    name: str
    score: float
    cost: float


def compute_soft_inverse_weights(
    pass_rates: Mapping[str, float],
    *,
    power: float = 0.5,
    total: float = 100.0,
    min_rate: float = 1e-6,
) -> dict[str, float]:
    """Return normalized task weights based on inverse pass rate.

    The default ``power=0.5`` implements ``1 / sqrt(pass_rate)``. It rewards
    difficult tasks while avoiding the instability of a full ``1 / p`` rule.
    Pass rates must be in the interval ``(0, 1]``.
    """

    if not pass_rates:
        raise ValueError("pass_rates must not be empty")
    if power <= 0:
        raise ValueError("power must be positive")
    if total <= 0:
        raise ValueError("total must be positive")

    raw: dict[str, float] = {}
    for task_id, rate in pass_rates.items():
        if not 0 < rate <= 1:
            raise ValueError(f"pass rate for {task_id!r} must be in (0, 1]")
        raw[task_id] = 1.0 / max(rate, min_rate) ** power

    denominator = sum(raw.values())
    return {task_id: total * value / denominator for task_id, value in raw.items()}


def weighted_score(
    outcomes: Mapping[str, bool | int], weights: Mapping[str, float]
) -> float:
    """Calculate a difficulty-weighted score.

    Every task in ``weights`` must have an outcome. Extra outcomes are ignored
    so historical records remain reproducible when the task set later grows.
    """

    missing = set(weights) - set(outcomes)
    if missing:
        raise ValueError(f"missing outcomes for tasks: {sorted(missing)}")
    return sum(weights[task_id] for task_id in weights if bool(outcomes[task_id]))


def weighted_iq(score: float) -> float:
    """Map a 0-100 weighted score to the source site's 0-150 display scale."""

    return score * 1.5


def quota_efficiency(score: float, estimated_cost_usd: float) -> float:
    """Return weighted score per estimated USD-equivalent quota cost."""

    if estimated_cost_usd <= 0:
        raise ValueError("estimated_cost_usd must be positive")
    return score / estimated_cost_usd


def weighted_average(values: Sequence[float], weights: Sequence[float]) -> float:
    """Calculate a weighted average with validation."""

    if len(values) != len(weights) or not values:
        raise ValueError("values and weights must be non-empty and equal length")
    if any(weight < 0 for weight in weights):
        raise ValueError("weights must be non-negative")
    denominator = sum(weights)
    if denominator == 0:
        raise ValueError("at least one weight must be positive")
    return sum(value * weight for value, weight in zip(values, weights)) / denominator


def exponentially_weighted_score(
    values: Sequence[float],
    *,
    alpha: float = 0.5,
    reliability_weights: Sequence[float] | None = None,
) -> float:
    """Return an EWMA-like score, optionally down-weighting anomalous batches.

    ``values`` are ordered oldest to newest. Recent observations receive more
    weight. Reliability weights are multiplied into the time-decay weights.
    """

    if not values:
        raise ValueError("values must not be empty")
    if not 0 < alpha <= 1:
        raise ValueError("alpha must be in (0, 1]")
    if reliability_weights is None:
        reliability_weights = [1.0] * len(values)
    if len(reliability_weights) != len(values):
        raise ValueError("reliability_weights length must match values")

    n = len(values)
    time_weights = [(1 - alpha) ** (n - index - 1) for index in range(n)]
    combined = [time * reliability for time, reliability in zip(time_weights, reliability_weights)]
    return weighted_average(list(values), combined)


def rolling_median(values: Sequence[float], window: int = 5) -> float:
    """Return the median of the latest ``window`` values."""

    if not values:
        raise ValueError("values must not be empty")
    if window <= 0:
        raise ValueError("window must be positive")
    return float(median(values[-window:]))


def pareto_frontier(points: Iterable[ModelPoint]) -> list[ModelPoint]:
    """Return non-dominated cost-quality points.

    Point A dominates point B when A costs no more, scores no less, and is
    strictly better on at least one dimension.
    """

    candidates = list(points)
    if any(point.cost <= 0 for point in candidates):
        raise ValueError("all costs must be positive")

    frontier: list[ModelPoint] = []
    for candidate in candidates:
        dominated = any(
            other.name != candidate.name
            and other.cost <= candidate.cost
            and other.score >= candidate.score
            and (other.cost < candidate.cost or other.score > candidate.score)
            for other in candidates
        )
        if not dominated:
            frontier.append(candidate)
    return sorted(frontier, key=lambda point: (point.cost, -point.score, point.name))
