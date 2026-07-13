from math import isclose

import pytest

from radar.scoring import (
    ModelPoint,
    compute_soft_inverse_weights,
    exponentially_weighted_score,
    pareto_frontier,
    quota_efficiency,
    rolling_median,
    weighted_iq,
    weighted_score,
)


def test_weights_normalize_to_100_and_reward_harder_tasks() -> None:
    weights = compute_soft_inverse_weights({"easy": 0.90, "hard": 0.10})
    assert isclose(sum(weights.values()), 100.0)
    assert weights["hard"] > weights["easy"]


def test_weighted_score_and_iq() -> None:
    weights = {"a": 30.0, "b": 70.0}
    score = weighted_score({"a": True, "b": False}, weights)
    assert score == 30.0
    assert weighted_iq(score) == 45.0


def test_missing_task_is_rejected() -> None:
    with pytest.raises(ValueError, match="missing outcomes"):
        weighted_score({"a": True}, {"a": 50.0, "b": 50.0})


def test_quota_efficiency() -> None:
    assert quota_efficiency(80.0, 10.0) == 8.0
    with pytest.raises(ValueError):
        quota_efficiency(80.0, 0.0)


def test_anomaly_reliability_can_downweight_latest_observation() -> None:
    normal = exponentially_weighted_score([70.0, 90.0], alpha=0.5)
    downweighted = exponentially_weighted_score(
        [70.0, 90.0], alpha=0.5, reliability_weights=[1.0, 0.35]
    )
    assert downweighted < normal


def test_rolling_median_uses_latest_window() -> None:
    assert rolling_median([1, 9, 3, 7], window=3) == 7.0


def test_pareto_frontier_removes_dominated_points() -> None:
    points = [
        ModelPoint("cheap", score=50, cost=5),
        ModelPoint("dominated", score=45, cost=6),
        ModelPoint("strong", score=80, cost=10),
    ]
    assert [point.name for point in pareto_frontier(points)] == ["cheap", "strong"]
