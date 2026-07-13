#!/usr/bin/env python3
from __future__ import annotations

import csv
from collections import defaultdict
from pathlib import Path
from statistics import mean, median


ROOT = Path(__file__).resolve().parents[1]
RUNS_PATH = ROOT / "data" / "history" / "runs.csv"
WEIGHTS_PATH = ROOT / "data" / "weights" / "task_weights.csv"
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
    if not rows:
        raise ValueError("runs.csv contains no rows")
    return rows


def load_weights() -> list[dict[str, object]]:
    weights: list[dict[str, object]] = []
    with WEIGHTS_PATH.open(newline="", encoding="utf-8") as handle:
        for raw in csv.DictReader(handle):
            weights.append(
                {
                    **raw,
                    "historical_pass_rate": float(raw["historical_pass_rate"]),
                    "soft_inverse_weight": float(raw["soft_inverse_weight"]),
                }
            )
    if not weights:
        raise ValueError("task_weights.csv contains no rows")
    return weights


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


def batches(rows: list[dict[str, object]]) -> list[tuple[str, list[dict[str, object]]]]:
    order: list[str] = []
    grouped: dict[str, list[dict[str, object]]] = defaultdict(list)
    for row in rows:
        batch_id = str(row["batch_id"])
        if batch_id not in grouped:
            order.append(batch_id)
        grouped[batch_id].append(row)
    return [(batch_id, grouped[batch_id]) for batch_id in order]


def latest_complete_valid_batch(
    ordered_batches: list[tuple[str, list[dict[str, object]]]],
) -> tuple[str, list[dict[str, object]]]:
    largest_batch = max(len(rows) for _, rows in ordered_batches)
    for batch_id, batch_rows in reversed(ordered_batches):
        if len(batch_rows) == largest_batch and not any(bool(row["anomaly"]) for row in batch_rows):
            return batch_id, batch_rows
    raise ValueError("no complete non-anomalous batch found")


def append_weights(lines: list[str], weights: list[dict[str, object]], *, zh: bool) -> None:
    snapshot = str(weights[0]["weight_snapshot"])
    if zh:
        lines.extend(
            [
                "## 最新任务难度权重",
                "",
                f"**权重快照：** `{snapshot}`  ",
                "**公式：** `weight_i ∝ 1 / sqrt(historical_pass_rate_i)`，归一化总分为 100。",
                "",
                "| 题号 | 任务摘要 | 历史通过率 | 权重 /100 |",
                "|---:|---|---:|---:|",
            ]
        )
    else:
        lines.extend(
            [
                "## Latest task-difficulty weights",
                "",
                f"**Weight snapshot:** `{snapshot}`  ",
                "**Formula:** `weight_i ∝ 1 / sqrt(historical_pass_rate_i)`, normalized to 100.",
                "",
                "| Task | Short description | Historical pass rate | Weight /100 |",
                "|---:|---|---:|---:|",
            ]
        )

    for row in weights:
        lines.append(
            f"| {row['task_id']} | {row['short_description']} | "
            f"{100 * float(row['historical_pass_rate']):.0f}% | "
            f"{float(row['soft_inverse_weight']):.2f} |"
        )
    lines.extend(["|  | **Total** |  | **100.00** |", ""])


def append_ranking(
    lines: list[str],
    batch_id: str,
    batch_rows: list[dict[str, object]],
    *,
    title: str,
    warning: str,
    zh: bool,
) -> None:
    lines.extend([f"## {title}", "", f"**Batch:** `{batch_id}`", ""])
    if warning:
        lines.extend([f"> {warning}", ""])

    if zh:
        lines.extend(
            [
                "| 排名 | 模型档位 | 通过 | 加权分 /100 | 估算费用 | 加权分/$ |",
                "|---:|---|---:|---:|---:|---:|",
            ]
        )
    else:
        lines.extend(
            [
                "| Rank | Model tier | Passed | Weighted /100 | Estimated cost | Weighted/$ |",
                "|---:|---|---:|---:|---:|---:|",
            ]
        )

    ranked = sorted(batch_rows, key=lambda row: (-quality(row), label(row)))
    for rank, row in enumerate(ranked, start=1):
        cost = "—" if row["cost_usd"] is None else f"${float(row['cost_usd']):.2f}"
        ratio = efficiency(row)
        ratio_text = "—" if ratio is None else f"{ratio:.2f}"
        lines.append(
            f"| {rank} | {label(row)} | {row['passed']}/{row['tasks']} | "
            f"{quality(row):.2f} | {cost} | {ratio_text} |"
        )
    lines.append("")


def append_stability(
    lines: list[str], rows: list[dict[str, object]], *, zh: bool
) -> None:
    grouped: dict[tuple[str, str], list[dict[str, object]]] = defaultdict(list)
    for row in rows:
        grouped[(str(row["model"]), str(row["effort"]))].append(row)

    if zh:
        lines.extend(
            [
                "## 最近五轮稳定性",
                "",
                "| 模型档位 | 有效样本 | 通过数中位数 | 通过数均值 | 范围 |",
                "|---|---:|---:|---:|---:|",
            ]
        )
    else:
        lines.extend(
            [
                "## Five-run stability",
                "",
                "| Model tier | Valid runs | Median passed | Mean passed | Range |",
                "|---|---:|---:|---:|---:|",
            ]
        )

    for values in sorted(grouped.values(), key=lambda group: label(group[-1])):
        valid = [row for row in values if not bool(row["anomaly"])]
        sample = valid[-5:] if valid else values[-5:]
        pass_values = [int(row["passed"]) for row in sample]
        lines.append(
            f"| {label(sample[-1])} | {len(sample)} | {median(pass_values):.1f} | "
            f"{mean(pass_values):.2f} | {min(pass_values)}–{max(pass_values)} |"
        )
    lines.append("")


def render_chinese(
    rows: list[dict[str, object]], weights: list[dict[str, object]]
) -> str:
    ordered_batches = batches(rows)
    latest_id, latest_rows = ordered_batches[-1]
    valid_id, valid_rows = latest_complete_valid_batch(ordered_batches)

    lines = [
        "# 模型雷达自动汇总报告 — 简体中文",
        "",
        "> 根据版本化 CSV 自动生成；正式解释和推荐仍以 `reports/latest.zh-CN.md` 为准。",
        "",
        "## 当前模型推荐",
        "",
        "| 场景 | 推荐 |",
        "|---|---|",
        "| 机械、低风险、允许重试 | Luna Medium 或 Terra Medium，先看近期稳定性 |",
        "| 日常开发 | **Sol Medium** |",
        "| 高难、额度敏感、允许长时间运行 | **Luna Max** |",
        "| 最高能力兜底 | 较低档失败后使用 **Sol Max** |",
        "",
    ]
    append_weights(lines, weights, zh=True)
    append_ranking(
        lines,
        latest_id,
        latest_rows,
        title="最新观测批次排名",
        warning="异常批次继续展示，但不应直接替代长期模型排序。"
        if any(bool(row["anomaly"]) for row in latest_rows)
        else "",
        zh=True,
    )
    append_ranking(
        lines,
        valid_id,
        valid_rows,
        title="最近正常完整批次排名",
        warning="该表用于辅助长期推荐，不代表所有私人项目。",
        zh=True,
    )
    append_stability(lines, rows, zh=True)
    lines.extend(
        [
            "## 历史数据",
            "",
            "[查看全部历史批次及跳转索引](history/README.md)。",
            "",
            "数据来源：Codex Radar（`codexradar.com`）。",
            "",
        ]
    )
    return "\n".join(lines)


def render_english(
    rows: list[dict[str, object]], weights: list[dict[str, object]]
) -> str:
    ordered_batches = batches(rows)
    latest_id, latest_rows = ordered_batches[-1]
    valid_id, valid_rows = latest_complete_valid_batch(ordered_batches)

    lines = [
        "# Generated Model Radar Report — English",
        "",
        "> Generated from versioned CSV files; the maintained interpretation remains in `reports/latest.en.md`.",
        "",
        "## Current model recommendations",
        "",
        "| Work type | Recommendation |",
        "|---|---|",
        "| Mechanical, low-risk, retryable | Luna Medium or Terra Medium; check recent stability |",
        "| General daily development | **Sol Medium** |",
        "| Difficult, quota-sensitive, long-running | **Luna Max** |",
        "| Maximum-capability fallback | **Sol Max** after cheaper tiers fail |",
        "",
    ]
    append_weights(lines, weights, zh=False)
    append_ranking(
        lines,
        latest_id,
        latest_rows,
        title="Latest observed weighted ranking",
        warning="An anomalous batch remains visible but should not directly replace the long-term hierarchy."
        if any(bool(row["anomaly"]) for row in latest_rows)
        else "",
        zh=False,
    )
    append_ranking(
        lines,
        valid_id,
        valid_rows,
        title="Latest complete non-anomalous ranking",
        warning="This table supports the long-term recommendation but does not represent every private repository.",
        zh=False,
    )
    append_stability(lines, rows, zh=False)
    lines.extend(
        [
            "## Historical data",
            "",
            "[Browse every recorded batch through the history index](history/README.md).",
            "",
            "Data attribution: source benchmark data comes from Codex Radar (`codexradar.com`).",
            "",
        ]
    )
    return "\n".join(lines)


def main() -> None:
    rows = load_rows()
    weights = load_weights()
    chinese = render_chinese(rows, weights)
    english = render_english(rows, weights)
    bilingual = "\n".join(
        [
            "# Generated Model Radar Report / 模型雷达自动汇总报告",
            "",
            "[简体中文](#简体中文) · [English](#english) · [历史数据 / History](history/README.md)",
            "",
            '<a id="简体中文"></a>',
            chinese,
            "",
            "---",
            "",
            '<a id="english"></a>',
            english,
            "",
        ]
    )

    REPORTS_DIR.mkdir(parents=True, exist_ok=True)
    OUTPUT_ZH.write_text(chinese, encoding="utf-8")
    OUTPUT_EN.write_text(english, encoding="utf-8")
    OUTPUT_BILINGUAL.write_text(bilingual, encoding="utf-8")

    for output in (OUTPUT_ZH, OUTPUT_EN, OUTPUT_BILINGUAL):
        print(f"Wrote {output.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
