import csv
import json
from pathlib import Path

from radar.api import append_history, normalize_model_summary, snapshot_id


def sample_payload() -> dict:
    latest = {
        "date": "2026-07-13", "score": 105, "passed": 7, "tasks": 10, "invalid": 0,
        "total_tokens": 123, "input_tokens": 100, "cached_input_tokens": 80, "output_tokens": 23,
        "wall_seconds": 456, "model": "gpt-5.6-sol", "reasoning_effort": "medium",
        "valid_tasks": 10, "cost_usd": 8.2,
    }
    return {
        "monitored_at": "2026-07-13T14:00:00+08:00",
        "model_iq": {"comparisons": {"gpt_56_sol_medium": {"label": "Sol Medium", "latest": latest}}},
    }


def test_snapshot_id_is_stable() -> None:
    payload = sample_payload()
    assert snapshot_id(payload) == snapshot_id(json.loads(json.dumps(payload)))


def test_normalize_model_summary_preserves_model_metrics() -> None:
    rows = normalize_model_summary(sample_payload(), retrieved_at="2026-07-13T06:00:00+00:00")
    assert len(rows) == 1
    assert rows[0]["model"] == "gpt-5.6-sol"
    assert rows[0]["effort"] == "medium"
    assert rows[0]["passed"] == "7"
    assert rows[0]["cost_usd"] == "8.2"
    assert rows[0]["provenance"] == "authorized_api_model_iq_summary"


def test_append_history_deduplicates_same_snapshot(tmp_path: Path) -> None:
    path = tmp_path / "model_iq_history.csv"
    rows = normalize_model_summary(sample_payload(), retrieved_at="2026-07-13T06:00:00+00:00")
    assert append_history(path, rows) == 1
    assert append_history(path, rows) == 0
    with path.open(newline="", encoding="utf-8") as handle:
        assert len(list(csv.DictReader(handle))) == 1
