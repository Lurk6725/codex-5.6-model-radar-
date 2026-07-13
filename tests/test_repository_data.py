import csv
from math import isclose
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def test_task_weight_snapshot_sums_to_100() -> None:
    path = ROOT / "data" / "weights" / "task_weights.csv"
    with path.open(newline="", encoding="utf-8") as handle:
        rows = list(csv.DictReader(handle))

    assert len(rows) == 10
    total = sum(float(row["soft_inverse_weight"]) for row in rows)
    assert isclose(total, 100.0, abs_tol=0.02)


def test_history_index_links_every_recorded_batch() -> None:
    runs_path = ROOT / "data" / "history" / "runs.csv"
    history_path = ROOT / "reports" / "history" / "README.md"

    with runs_path.open(newline="", encoding="utf-8") as handle:
        batch_ids = {row["batch_id"] for row in csv.DictReader(handle)}

    history = history_path.read_text(encoding="utf-8")
    for batch_id in batch_ids:
        assert f'id="{batch_id}"' in history
        assert f"#{batch_id}" in history


def test_latest_reports_publish_required_rank_metrics() -> None:
    chinese = (ROOT / "reports" / "latest.zh-CN.md").read_text(encoding="utf-8")
    english = (ROOT / "reports" / "latest.en.md").read_text(encoding="utf-8")

    assert "模型推荐" in chinese
    assert "加权分 /100" in chinese
    assert "加权分/$" in chinese
    assert "最新任务难度权重" in chinese

    assert "Model recommendations" in english
    assert "Weighted /100" in english
    assert "Weighted/$" in english
    assert "Latest task-difficulty weights" in english
