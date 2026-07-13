from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class BatchSummary:
    """Aggregate metrics for one benchmark batch."""

    total_passes: int
    total_cost_usd: float
    total_tokens: int

    def validate(self) -> None:
        if self.total_passes < 0:
            raise ValueError("total_passes must be non-negative")
        if self.total_cost_usd <= 0:
            raise ValueError("total_cost_usd must be positive")
        if self.total_tokens <= 0:
            raise ValueError("total_tokens must be positive")


@dataclass(frozen=True)
class AnomalyResult:
    is_anomaly: bool
    pass_drop: float
    cost_increase: float
    token_increase: float
    reliability_weight: float
    reasons: tuple[str, ...]


def _relative_change(current: float, previous: float) -> float:
    if previous <= 0:
        raise ValueError("previous value must be positive")
    return (current - previous) / previous


def detect_batch_anomaly(
    current: BatchSummary,
    previous: BatchSummary,
    *,
    pass_drop_threshold: float = 0.15,
    resource_increase_threshold: float = 0.30,
    anomalous_weight: float = 0.35,
) -> AnomalyResult:
    """Flag batches where quality drops while resource use rises.

    The default rule marks a batch anomalous when:

    - total passes fall by at least 15%, and
    - either estimated cost or total tokens rise by at least 30%.

    Data is retained. The returned reliability weight can be used in rolling
    trend calculations instead of deleting the observation.
    """

    current.validate()
    previous.validate()
    if not 0 <= anomalous_weight <= 1:
        raise ValueError("anomalous_weight must be in [0, 1]")

    pass_change = _relative_change(current.total_passes, previous.total_passes)
    cost_change = _relative_change(current.total_cost_usd, previous.total_cost_usd)
    token_change = _relative_change(current.total_tokens, previous.total_tokens)

    pass_drop = max(0.0, -pass_change)
    quality_drop = pass_drop >= pass_drop_threshold
    resource_spike = (
        cost_change >= resource_increase_threshold
        or token_change >= resource_increase_threshold
    )
    is_anomaly = quality_drop and resource_spike

    reasons: list[str] = []
    if quality_drop:
        reasons.append(f"passes dropped {pass_drop:.1%}")
    if cost_change >= resource_increase_threshold:
        reasons.append(f"cost increased {cost_change:.1%}")
    if token_change >= resource_increase_threshold:
        reasons.append(f"tokens increased {token_change:.1%}")

    return AnomalyResult(
        is_anomaly=is_anomaly,
        pass_drop=pass_drop,
        cost_increase=cost_change,
        token_increase=token_change,
        reliability_weight=anomalous_weight if is_anomaly else 1.0,
        reasons=tuple(reasons),
    )
