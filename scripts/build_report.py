#!/usr/bin/env python3
from __future__ import annotations

import csv
from collections import defaultdict
from pathlib import Path
from statistics import mean, median

from radar.scoring import ModelPoint, pareto_frontier, quota_efficiency


ROOT = Path(__file__).resolve().parents[1]
RUNS_PATH = ROOT / "data" / "history" / "runs.csv"
REPORTS_DIR = ROOT / "reports"
OUTPUT_EN = REPORTS_DIR / "latest.generated.en.md"
OUTPUT_ZH = REPORTS_DIR / "latest.generated.zh-CN.md"
OUTPUT_BILINGUAL = REPORTS_DIR / "latest.generated.md"


def as_float(value: str) -> float | None:
    value = value.strip()
    return float(value) if value else None


def as_bool(value: str) -> bool:
    return value.strip().lower() == "true"


def load_rows() -> list[dict[str, object]]:
    rows: list[dict[str, object]] = []
    with RUNS_PATH.open(newline="", encoding="utf-8") as handle:
        for raw in csv.DictReader(handle):
            rows.append(
                {
                    **raw,
                    "passed": int(raw["passed"]),
                    "tasks": int(raw["tasks"]),
                    "cost_usd": as_float(raw["cost_usd"]),
                    "weighted_score": as_float(raw["weighted_score"]),
                    "anomaly": as_bool(raw["anomaly"]),
                    "reliability_weight": float(raw["reliability_weight"]),
                }
            )
    return rows


def quality(row: dict[str, object]) -> float:
    explicit = row["weighted_score"]
    if explicit is not None:
        return float(explicit)
    return 100.0 * int(row["passed"]) / int(row["tasks"])


def label(row: dict[str, object]) -> str:
    family = str(row["model"]).removeprefix("gpt-5.6-").title()
    effort = str(row["effort"]).title()
    return f"{family} {effort}"


def prepare(
    rows: list[dict[str, object]],
) -> tuple[
    dict[tuple[str, str], list[dict[str, object]]],
    list[dict[str, object]],
    list[dict[str, object]],
    set[str],
]:
    grouped: dict[tuple[str, str], list[dict[str, object]]] = defaultdict(list)
    for row in rows:
        grouped[(str(row["model"]), str(row["effort"]))].append(row)

    latest_all = [values[-1] for values in grouped.values()]
    latest_valid: list[dict[str, object]] = []
    for values in grouped.values():
        valid = [row for row in values if not bool(row["anomaly"])]
        latest_valid.append(valid[-1] if valid else values[-1])

    points = [
        ModelPoint(label(row), quality(row), float(row["cost_usd"]))
        for row in latest_valid
        if row["cost_usd"] is not None
    ]
    frontier = {point.name for point in pareto_frontier(points)}
    return grouped, latest_all, latest_valid, frontier


def render_english(
    grouped: dict[tuple[str, str], list[dict[str, object]]],
    latest_all: list[dict[str, object]],
    latest_valid: list[dict[str, object]],
    frontier: set[str],
) -> str:
    lines = [
        "# Generated Model Radar Report — English",
        "",
        "> Generated from `data/history/runs.csv`. Rows without task-level weighted scores use raw pass percentage as an interim quality proxy.",
        "",
        "## Latest recorded batch",
        "",
        "| Configuration | Batch | Passed | Quality | Cost | Anomaly |",
        "|---|---:|---:|---:|---:|---:|",
    ]

    for row in sorted(latest_all, key=lambda item: (-quality(item), label(item))):
        cost = "—" if row["cost_usd"] is None else f"${float(row['cost_usd']):.2f}"
        lines.append(
            f"| {label(row)} | {row['batch_id']} | {row['passed']}/{row['tasks']} | "
            f"{quality(row):.2f} | {cost} | {'yes' if row['anomaly'] else 'no'} |"
        )

    lines.extend(
        [
            "",
            "## Latest non-anomalous cost-quality view",
            "",
            "| Configuration | Passed | Quality | Cost | Score / $ | Pareto |",
            "|---|---:|---:|---:|---:|---:|",
        ]
    )

    comparable = [row for row in latest_valid if row["cost_usd"] is not None]
    for row in sorted(comparable, key=lambda item: (-quality(item), float(item["cost_usd"]))):
        score = quality(row)
        cost = float(row["cost_usd"])
        name = label(row)
        lines.append(
            f"| {name} | {row['passed']}/{row['tasks']} | {score:.2f} | ${cost:.2f} | "
            f"{quota_efficiency(score, cost):.2f} | {'yes' if name in frontier else 'no'} |"
        )

    lines.extend(
        [
            "",
            "## Rolling stability",
            "",
            "| Configuration | Runs | Median passed | Mean passed | Range | Latest valid batch |",
            "|---|---:|---:|---:|---:|---:|",
        ]
    )

    for values in sorted(grouped.values(), key=lambda group: label(group[-1])):
        valid = [row for row in values if not bool(row["anomaly"])]
        sample = valid[-5:] if valid else values[-5:]
        pass_values = [int(row["passed"]) for row in sample]
        latest = sample[-1]
        lines.append(
            f"| {label(latest)} | {len(sample)} | {median(pass_values):.1f} | "
            f"{mean(pass_values):.2f} | {min(pass_values)}–{max(pass_values)} | {latest['batch_id']} |"
        )

    lines.extend(
        [
            "",
            "## Interpretation",
            "",
            "- Use the latest complete batch to understand current service behavior.",
            "- Use the rolling table and Pareto frontier for model recommendations.",
            "- Anomalous batches remain visible but do not replace the latest valid comparison.",
            "- A cheap model with a high score-per-dollar value may still have low absolute reliability.",
            "",
            "Data attribution: source benchmark data comes from Codex Radar (`codexradar.com`).",
            "",
        ]
    )
    return "\n".join(lines)


def render_chinese(
    grouped: dict[tuple[str, str], list[dict[str, object]]],
    latest_all: list[dict[str, object]],
    latest_valid: list[dict[str, object]],
    frontier: set[str],
) -> str:
    lines = [
        "# 模型雷达自动汇总报告 — 简体中文",
        "",
        "> 根据 `data/history/runs.csv` 自动生成。缺少逐题加权分的历史行暂时使用原始通过百分比作为质量代理。",
        "",
        "## 最新记录批次",
        "",
        "| 模型配置 | 批次 | 通过 | 质量分 | 费用 | 异常 |",
        "|---|---:|---:|---:|---:|---:|",
    ]

    for row in sorted(latest_all, key=lambda item: (-quality(item), label(item))):
        cost = "—" if row["cost_usd"] is None else f"${float(row['cost_usd']):.2f}"
        lines.append(
            f"| {label(row)} | {row['batch_id']} | {row['passed']}/{row['tasks']} | "
            f"{quality(row):.2f} | {cost} | {'是' if row['anomaly'] else '否'} |"
        )

    lines.extend(
        [
            "",
            "## 最新非异常批次成本—质量视图",
            "",
            "| 模型配置 | 通过 | 质量分 | 费用 | 每美元得分 | Pareto 前沿 |",
            "|---|---:|---:|---:|---:|---:|",
        ]
    )

    comparable = [row for row in latest_valid if row["cost_usd"] is not None]
    for row in sorted(comparable, key=lambda item: (-quality(item), float(item["cost_usd"]))):
        score = quality(row)
        cost = float(row["cost_usd"])
        name = label(row)
        lines.append(
            f"| {name} | {row['passed']}/{row['tasks']} | {score:.2f} | ${cost:.2f} | "
            f"{quota_efficiency(score, cost):.2f} | {'是' if name in frontier else '否'} |"
        )

    lines.extend(
        [
            "",
            "## 滚动稳定性",
            "",
            "| 模型配置 | 样本数 | 通过数中位数 | 通过数均值 | 范围 | 最新有效批次 |",
            "|---|---:|---:|---:|---:|---:|",
        ]
    )

    for values in sorted(grouped.values(), key=lambda group: label(group[-1])):
        valid = [row for row in values if not bool(row["anomaly"])]
        sample = valid[-5:] if valid else values[-5:]
        pass_values = [int(row["passed"]) for row in sample]
        latest = sample[-1]
        lines.append(
            f"| {label(latest)} | {len(sample)} | {median(pass_values):.1f} | "
            f"{mean(pass_values):.2f} | {min(pass_values)}–{max(pass_values)} | {latest['batch_id']} |"
        )

    lines.extend(
        [
            "",
            "## 解读原则",
            "",
            "- 使用最新完整批次判断当前服务状态。",
            "- 使用滚动统计和 Pareto 前沿形成模型推荐。",
            "- 异常批次继续展示，但不替代最新有效批次的横向比较。",
            "- 便宜模型即使每美元得分很高，也可能仍然缺乏足够的绝对可靠性。",
            "",
            "数据来源：Codex Radar（`codexradar.com`）。",
            "",
        ]
    )
    return "\n".join(lines)


def main() -> None:
    rows = load_rows()
    grouped, latest_all, latest_valid, frontier = prepare(rows)

    english = render_english(grouped, latest_all, latest_valid, frontier)
    chinese = render_chinese(grouped, latest_all, latest_valid, frontier)
    bilingual = "\n".join(
        [
            "# Generated Model Radar Report / 模型雷达自动汇总报告",
            "",
            "[简体中文](#简体中文) · [English](#english)",
            "",
            "<a id=\"简体中文\"></a>",
            chinese,
            "",
            "---",
            "",
            "<a id=\"english\"></a>",
            english,
            "",
        ]
    )

    REPORTS_DIR.mkdir(parents=True, exist_ok=True)
    OUTPUT_EN.write_text(english, encoding="utf-8")
    OUTPUT_ZH.write_text(chinese, encoding="utf-8")
    OUTPUT_BILINGUAL.write_text(bilingual, encoding="utf-8")

    for output in (OUTPUT_ZH, OUTPUT_EN, OUTPUT_BILINGUAL):
        print(f"Wrote {output.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
