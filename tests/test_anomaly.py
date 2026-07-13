from radar.anomaly import BatchSummary, detect_batch_anomaly


def test_batch_anomaly_when_quality_falls_and_resources_rise() -> None:
    previous = BatchSummary(total_passes=61, total_cost_usd=143.7, total_tokens=253_700_000)
    current = BatchSummary(total_passes=49, total_cost_usd=205.2, total_tokens=369_000_000)
    result = detect_batch_anomaly(current, previous)
    assert result.is_anomaly
    assert result.reliability_weight == 0.35
    assert result.pass_drop > 0.15
    assert result.cost_increase > 0.30
    assert result.token_increase > 0.30


def test_quality_drop_without_resource_spike_is_not_flagged() -> None:
    previous = BatchSummary(total_passes=60, total_cost_usd=100, total_tokens=1000)
    current = BatchSummary(total_passes=45, total_cost_usd=110, total_tokens=1050)
    result = detect_batch_anomaly(current, previous)
    assert not result.is_anomaly
    assert result.reliability_weight == 1.0
