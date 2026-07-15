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
OUTPUT_ZH = REPORTS_DIR / "latest.generated.zh-CN.md"
OUTPUT_EN = REPORTS_DIR / "latest.generated.en.md"
OUTPUT_BILINGUAL = REPORTS_DIR / "latest.generated.md"


def as_float(value: str | None) -> float | None:
    value = (value or "").strip()
    return float(value) if value else None


def as_bool(value: str | None) -> bool:
    return (value or "").strip().lower() == "true"


def read_runs(path: Path) -> list[dict[str, object]]:
    if not path.exists():
        return []
    rows: list[dict[str, object]] = []
    with path.open(newline="", encoding="utf-8") as handle:
        for raw in csv.DictReader(handle):
            if not raw.get("batch_id") or not raw.get("model") or not raw.get("effort"):
                continue
            rows.append({
                **raw,
                "passed": int(raw.get("passed") or 0),
                "tasks": int(raw.get("tasks") or 10),
                "cost_usd": as_float(raw.get("cost_usd")),
                "weighted_score": as_float(raw.get("weighted_score")),
                "anomaly": as_bool(raw.get("anomaly")),
            })
    return rows


def load_rows() -> list[dict[str, object]]:
    rows = read_runs(RUNS_PATH)
    for path in sorted(BATCH_DIR.glob("*.csv")):
        rows.extend(read_runs(path))
    deduped: dict[tuple[str, str, str], dict[str, object]] = {}
    for row in rows:
        key = (str(row["batch_id"]), str(row["model"]), str(row["effort"]))
        deduped[key] = row
    if not deduped:
        raise ValueError("no run data found")
    return list(deduped.values())


def load_weights() -> list[dict[str, object]]:
    with WEIGHTS_PATH.open(newline="", encoding="utf-8") as handle:
        rows = [{
            **raw,
            "historical_pass_rate": float(raw["historical_pass_rate"]),
            "soft_inverse_weight": float(raw["soft_inverse_weight"]),
        } for raw in csv.DictReader(handle)]
    if not rows:
        raise ValueError("task_weights.csv contains no rows")
    return rows


def label(row: dict[str, object]) -> str:
    family = str(row["model"]).removeprefix("gpt-5.6-").title()
    effort = str(row["effort"]).title()
    return f"{family} {effort}"


def quality(row: dict[str, object]) -> float:
    score = row["weighted_score"]
    return float(score) if score is not None else 100.0 * int(row["passed"]) / int(row["tasks"])


def efficiency(row: dict[str, object]) -> float | None:
    cost = row["cost_usd"]
    return None if cost is None or float(cost) <= 0 else quality(row) / float(cost)


def latest_batch(rows: list[dict[str, object]]) -> tuple[str, list[dict[str, object]]]:
    grouped: dict[str, list[dict[str, object]]] = defaultdict(list)
    for row in rows:
        grouped[str(row["batch_id"])].append(row)
    batch_id = sorted(grouped)[-1]
    return batch_id, grouped[batch_id]


def append_recommendations(lines: list[str], *, zh: bool) -> None:
    if zh:
        rows = [
            ("低成本、允许重试", "**Sol Low**；重要任务不要停留在 Low"),
            ("日常开发与小项目 Bug 审查", "**Sol Medium**；本轮置信度为中等"),
            ("高难、额度敏感、允许后台长跑", "**Luna Max**"),
            ("Sol 系失败后的升级", "优先 **Sol High**，不要从单轮完美成绩自动升级 XHigh"),
            ("不建议自动升级", "Sol Max"),
        ]
        lines.extend(["## 当前模型推荐", "", "| 场景 | 推荐 |", "|---|---|"])
    else:
        rows = [
            ("Low-cost and retryable", "**Sol Low**; escalate important work"),
            ("Daily development and small-project bug review", "**Sol Medium**, with medium confidence"),
            ("Difficult, quota-sensitive background work", "**Luna Max**"),
            ("Sol-family escalation", "Prefer **Sol High**; do not promote XHigh from one perfect round"),
            ("Do not upgrade automatically", "Sol Max"),
        ]
        lines.extend(["## Current model recommendations", "", "| Work type | Recommendation |", "|---|---|"])
    lines.extend(f"| {left} | {right} |" for left, right in rows)
    lines.append("")


def append_weights(lines: list[str], weights: list[dict[str, object]], *, zh: bool) -> None:
    snapshot = str(weights[0]["weight_snapshot"])
    lines.extend([
        "## 最新任务难度权重" if zh else "## Latest task-difficulty weights", "",
        (f"**权重快照：** `{snapshot}`" if zh else f"**Weight snapshot:** `{snapshot}`"), "",
        "| 题号 | 历史通过率 | 权重 /100 |" if zh else "| Task | Historical pass rate | Weight /100 |",
        "|---:|---:|---:|",
    ])
    for row in weights:
        lines.append(f"| {row['task_id']} | {100 * float(row['historical_pass_rate']):.2f}% | {float(row['soft_inverse_weight']):.2f} |")
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
        lines.append(f"| {rank} | {label(row)} | {row['passed']}/{row['tasks']} | {quality(row):.2f} | {cost} | {'—' if ratio is None else f'{ratio:.2f}'} |")
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
        passed = [int(row["passed"]) for row in sample]
        lines.append(f"| {label(sample[-1])} | {len(sample)} | {median(passed):.1f} | {mean(passed):.2f} | {min(passed)}–{max(passed)} |")
    lines.append("")


def render(rows: list[dict[str, object]], weights: list[dict[str, object]], *, zh: bool) -> str:
    batch_id, batch_rows = latest_batch(rows)
    lines = [
        "# 模型雷达自动汇总报告 — 简体中文" if zh else "# Generated Model Radar Report — English", "",
        "> 根据版本化 CSV 自动生成；正式解释以维护版最新报告为准。" if zh else "> Generated from versioned CSV files; see the maintained latest report for interpretation.", "",
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
