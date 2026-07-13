#!/usr/bin/env python3
from __future__ import annotations

import csv
from collections import defaultdict
from pathlib import Path
from statistics import mean, median

from radar.scoring import ModelPoint, pareto_frontier, quota_efficiency


ROOT = Path(__file__).resolve().parents[1]
RUNS_PATH = ROOT / "data" / "history" / "runs.csv"
OUTPUT_PATH = ROOT / "reports" / "latest.generated.md"


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


def main() -> None:
    rows = load_rows()
    grouped: dict[tuple[str, str], list[dict[str, object]]] = defaultdict(list)
    for row in rows:
        grouped[(str(row["model"]), str(row["effort"]))].append(row)

    latest_all = [values[-1] for values in grouped.values()]
    latest_valid = []
    for values in grouped.values():
        valid = [row for row in values if not bool(row["anomaly"])]
        latest_valid.append(valid[-1] if valid else values[-1])

    points = [
        ModelPoint(label(row), quality(row), float(row["cost_usd"]))
        for row in latest_valid
        if row["cost_usd"] is not None
    ]
    frontier = {point.name for point in pareto_frontier(points)}

    lines = [
        "# Generated Model Radar Report",
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
            "Data attribution: 数据来自 Codex 雷达 codexradar.com",
            "",
        ]
    )

    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text("\n".join(lines), encoding="utf-8")
    print(f"Wrote {OUTPUT_PATH.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
