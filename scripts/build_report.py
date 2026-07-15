#!/usr/bin/env python3
from __future__ import annotations

import csv
from collections import defaultdict
from pathlib import Path
from statistics import mean, median

ROOT = Path(__file__).resolve().parents[1]
RUNS_PATH = ROOT / "data" / "history" / "runs.csv"
BATCH_DIR = ROOT / "data" / "history" / "batches"
WEIGHTS_PATH = ROOT / "data" / "weights" / "task_weights.csv"
REPORTS_DIR = ROOT / "reports"
OUTPUT_EN = REPORTS_DIR / "latest.generated.en.md"
OUTPUT_ZH = REPORTS_DIR / "latest.generated.zh-CN.md"
OUTPUT_BILINGUAL = REPORTS_DIR / "latest.generated.md"


def as_float(value: str | None) -> float | None:
    value = (value or "").strip()
    return float(value) if value else None


def as_bool(value: str | None) -> bool:
    return (value or "").strip().lower() == "true"


def read_run_file(path: Path) -> list[dict[str, object]]:
    if not path.exists():
        return []
    rows: list[dict[str, object]] = []
    with path.open(newline="", encoding="utf-8") as handle:
        for raw in csv.DictReader(handle):
            rows.append(
                {
                    **raw,
                    "passed": int(raw["passed"]),
                    "tasks": int(raw["tasks"]),
                    "cost_usd": as_float(raw.get("cost_usd")),
                    "weighted_score": as_float(raw.get("weighted_score")),
                    "anomaly": as_bool(raw.get("anomaly")),
                    "reliability_weight": float(raw.get("reliability_weight") or 1.0),
                }
            )
    return rows


def load_rows() -> list[dict[str, object]]:
    rows = read_run_file(RUNS_PATH)
    for path in sorted(BATCH_DIR.glob("*.csv")):
        rows.extend(read_run_file(path))

    # Per-batch files override matching legacy aggregate rows.
    deduped: dict[tuple[str, str, str], dict[str, object]] = {}
    for row in rows:
        key = (str(row["batch_id"]), str(row["model"]), str(row["effort"]))
        deduped[key] = row
    result = list(deduped.values())
    if not result:
        raise ValueError("no run data found")
    return result


def load_weights() -> list[dict[str, object]]:
    with WEIGHTS_PATH.open(newline="", encoding="utf-8") as handle:
        rows = [
            {
                **raw,
                "historical_pass_rate": float(raw["historical_pass_rate"]),
                "soft_inverse_weight": float(raw["soft_inverse_weight"]),
            }
            for raw in csv.DictReader(handle)
        ]
    if not rows:
        raise ValueError("task_weights.csv contains no rows")
    return rows


def label(row: dict[str, object]) -> str:
    family = str(row["model"]).removeprefix("gpt-5.6-").title()
    effort = str(row["effort"]).title()
    return f"{family} {effort}"


def quality(row: dict[str, object]) -> float:
    score = row["weighted_score"]
    if score is not None:
        return float(score)
    return 100.0 * int(row["passed"]) / int(row["tasks"])


def efficiency(row: dict[str, object]) -> float | None:
    cost = row["cost_usd"]
    if cost is None or float(cost) <= 0:
        return None
    return quality(row) / float(cost)


def grouped_batches(rows: list[dict[str, object]]) -> dict[str, list[dict[str, object]]]:
    grouped: dict[str, list[dict[str, object]]] = defaultdict(list)
    for row in rows:
        grouped[str(row["batch_id"])].append(row)
    return grouped


def latest_batch(rows: list[dict[str, object]]) -> tuple[str, list[dict[str, object]]]:
    grouped = grouped_batches(rows)
    batch_id = sorted(grouped)[-1]
    return batch_id, grouped[batch_id]


def append_recommendations(lines: list[str], *, zh: bool) -> None:
    if zh:
        lines.extend([
            "## 当前模型推荐", "",
            "| 场景 | 推荐 |", "|---|---|",
            "| 低成本、允许重试 | **Sol Low** 仍可用，但本轮回落至 6/10，重要任务应升级 |",
            "| 日常开发与小项目 Bug 审查 | **Sol Medium** |",
            "| 高价值困难任务 | 先用 **Sol Medium**；失败后升级 **Sol XHigh** |",
            "| 最高能力兜底 | **Sol XHigh** 本轮 10/10；不要把 Max 当作自动升级 |", "",
        ])
    else:
        lines.extend([
            "## Current model recommendations", "",
            "| Work type | Recommendation |", "|---|---|",
            "| Low-cost and retryable | **Sol Low** remains usable, but fell to 6/10; escalate important work |",
            "| Daily development and small-project bug review | **Sol Medium** |",
            "| High-value difficult work | Start with **Sol Medium**, then escalate to **Sol XHigh** after failure |",
            "| Maximum-capability fallback | **Sol XHigh** reached 10/10; Max is not an automatic upgrade |", "",
        ])


def append_weights(lines: list[str], weights: list[dict[str, object]], *, zh: bool) -> None:
    snapshot = str(weights[0]["weight_snapshot"])
    lines.extend([
        "## 最新任务难度权重" if zh else "## Latest task-difficulty weights", "",
        (f"**权重快照：** `{snapshot}`" if zh else f"**Weight snapshot:** `{snapshot}`"), "",
        "| 题号 | 历史通过率 | 权重 /100 |" if zh else "| Task | Historical pass rate | Weight /100 |",
        "|---:|---:|---:|",
    ])
    for row in weights:
        lines.append(
            f"| {row['task_id']} | {100 * float(row['historical_pass_rate']):.2f}% | "
            f"{float(row['soft_inverse_weight']):.2f} |"
        )
    lines.extend(["|  |  | **100.00** |", ""])


def append_ranking(lines: list[str], batch_id: str, rows: list[dict[str, object]], *, zh: bool) -> None:
    lines.extend([
        "## 最新模型加权排名" if zh else "## Latest weighted ranking", "",
        f"**{'批次' if zh else 'Batch'}:** `{batch_id}`", "",
        "| 排名 | 模型档位 | 通过 | 加权分 /100 | 费用 | 加权分/$ |" if zh else "| Rank | Model tier | Passed | Weighted /100 | Cost | Weighted/$ |",
        "|---:|---|---:|---:|---:|---:|",
    ])
    ranked = sorted(rows, key=lambda row: (-quality(row), float(row["cost_usd"] or 1e9), label(row)))
    for rank, row in enumerate(ranked, start=1):
        cost = "—" if row["cost_usd"] is None else f"${float(row['cost_usd']):.2f}"
        ratio = efficiency(row)
        lines.append(
            f"| {rank} | {label(row)} | {row['passed']}/{row['tasks']} | {quality(row):.2f} | "
            f"{cost} | {'—' if ratio is None else f'{ratio:.2f}'} |"
        )
    lines.append("")


def append_stability(lines: list[str], rows: list[dict[str, object]], *, zh: bool) -> None:
    grouped: dict[tuple[str, str], list[dict[str, object]]] = defaultdict(list)
    for row in rows:
        grouped[(str(row["model"]), str(row["effort"]))].append(row)
    lines.extend([
        "## 最近五轮稳定性" if zh else "## Five-run stability", "",
        "| 模型档位 | 有效样本 | 通过数中位数 | 均值 | 范围 |" if zh else "| Model tier | Valid runs | Median passed | Mean | Range |",
        "|---|---:|---:|---:|---:|",
    ])
    for values in sorted(grouped.values(), key=lambda group: label(group[-1])):
        values.sort(key=lambda row: str(row["batch_id"]))
        valid = [row for row in values if not bool(row["anomaly"])]
        sample = (valid or values)[-5:]
        p = [int(row["passed"]) for row in sample]
        lines.append(f"| {label(sample[-1])} | {len(sample)} | {median(p):.1f} | {mean(p):.2f} | {min(p)}–{max(p)} |")
    lines.append("")


def render(rows: list[dict[str, object]], weights: list[dict[str, object]], *, zh: bool) -> str:
    batch_id, batch_rows = latest_batch(rows)
    lines = [
        "# 模型雷达自动汇总报告 — 简体中文" if zh else "# Generated Model Radar Report — English", "",
        ("> 根据版本化 CSV 自动生成；正式解释以维护版最新报告为准。" if zh else "> Generated from versioned CSV files; see the maintained latest report for interpretation."), "",
    ]
    append_recommendations(lines, zh=zh)
    append_weights(lines, weights, zh=zh)
    append_ranking(lines, batch_id, batch_rows, zh=zh)
    append_stability(lines, rows, zh=zh)
    lines.extend([
        "## 历史数据" if zh else "## Historical data", "",
        "[查看历史批次索引](history/README.md)。" if zh else "[Browse the historical batch index](history/README.md).", "",
        "数据来源：Codex Radar（`codexradar.com`）。" if zh else "Data attribution: Codex Radar (`codexradar.com`).", "",
    ])
    return "\n".join(lines)


def main() -> None:
    rows = load_rows()
    weights = load_weights()
    chinese = render(rows, weights, zh=True)
    english = render(rows, weights, zh=False)
    bilingual = "\n".join([
        "# Generated Model Radar Report / 模型雷达自动汇总报告", "",
        "[简体中文](#简体中文) · [English](#english) · [历史数据 / History](history/README.md)", "",
        '<a id="简体中文"></a>', chinese, "", "---", "", '<a id="english"></a>', english, "",
    ])
    REPORTS_DIR.mkdir(parents=True, exist_ok=True)
    OUTPUT_ZH.write_text(chinese, encoding="utf-8")
    OUTPUT_EN.write_text(english, encoding="utf-8")
    OUTPUT_BILINGUAL.write_text(bilingual, encoding="utf-8")
    for output in (OUTPUT_ZH, OUTPUT_EN, OUTPUT_BILINGUAL):
        print(f"Wrote {output.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
