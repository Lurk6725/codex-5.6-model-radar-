#!/usr/bin/env python3
"""Build bilingual reports from the Codex Radar API-derived history."""

from __future__ import annotations

import csv
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
HISTORY_PATH = ROOT / "data" / "api" / "model_iq_history.csv"
REPORTS_DIR = ROOT / "reports"
OUTPUT_ZH = REPORTS_DIR / "api-latest.zh-CN.md"
OUTPUT_EN = REPORTS_DIR / "api-latest.en.md"
OUTPUT_BILINGUAL = REPORTS_DIR / "api-latest.md"


def as_int(row: dict[str, str], key: str) -> int | None:
    value = row.get(key, "").strip()
    return int(value) if value else None


def as_float(row: dict[str, str], key: str) -> float | None:
    value = row.get(key, "").strip()
    return float(value) if value else None


def load_rows() -> list[dict[str, str]]:
    if not HISTORY_PATH.exists():
        return []
    with HISTORY_PATH.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def latest_snapshot(rows: list[dict[str, str]]) -> tuple[str, list[dict[str, str]]]:
    snapshot = max(rows, key=lambda row: row.get("retrieved_at", "")).get("snapshot_id", "")
    return snapshot, [row for row in rows if row.get("snapshot_id") == snapshot]


def label(row: dict[str, str]) -> str:
    model = row.get("model", "").removeprefix("gpt-5.6-").title()
    effort = row.get("effort", "").title()
    return f"{model} {effort}"


def fmt_number(value: int | None) -> str:
    return "—" if value is None else f"{value:,}"


def fmt_cost(value: float | None) -> str:
    return "—" if value is None else f"${value:.2f}"


def render(rows: list[dict[str, str]], *, zh: bool) -> str:
    snapshot, current = latest_snapshot(rows)
    current.sort(key=lambda row: (-(as_float(row, "source_score") or -1), label(row)))
    observed_at = current[0].get("observed_at", "")
    retrieved_at = current[0].get("retrieved_at", "")
    if zh:
        lines = [
            "# Codex Radar API 自动监控 — 简体中文", "",
            "[English](api-latest.en.md) · [项目首页](../README.md) · [API 历史 CSV](../data/api/model_iq_history.csv)", "",
            f"**API 快照：** `{snapshot}`  ", f"**源站观测时间：** `{observed_at}`  ", f"**本次抓取时间：** `{retrieved_at}`", "",
            "> 这是 Codex Radar API 返回的模型级摘要，不是本项目根据逐题矩阵计算的难度加权分。", "",
            "## 当前 API 模型摘要", "",
            "| 排名 | 模型档位 | 源站分数 | 通过 | 任务数 | 费用 | 总 Token | 耗时 |",
            "|---:|---|---:|---:|---:|---:|---:|---:|",
        ]
        for rank, row in enumerate(current, start=1):
            passed, tasks = as_int(row, "passed"), as_int(row, "tasks")
            passed_text = "—" if passed is None or tasks is None else f"{passed}/{tasks}"
            wall = as_int(row, "wall_seconds")
            wall_text = "—" if wall is None else f"{wall / 3600:.2f}h"
            lines.append(f"| {rank} | {label(row)} | {row.get('source_score') or '—'} | {passed_text} | {fmt_number(tasks)} | {fmt_cost(as_float(row, 'cost_usd'))} | {fmt_number(as_int(row, 'total_tokens'))} | {wall_text} |")
        lines.extend([
            "", "## 口径说明", "",
            "- 当前接口提供模型级 `score`、通过数、任务数、Token、耗时和估算费用。",
            "- 当前接口没有返回十道任务的逐题通过矩阵，因此不能仅凭 API 摘要重新计算 `加权分 /100`。",
            "- 加权排名仍以仓库中的逐题数据和权重快照为准；本报告用于自动监控源站最新摘要。",
            "- 原始 API 响应不写入公开仓库，只保存必要的模型摘要字段。", "",
            f"当前已归档 API 快照数：**{len({row.get('snapshot_id') for row in rows})}**。", "",
        ])
    else:
        lines = [
            "# Codex Radar API Monitor — English", "",
            "[简体中文](api-latest.zh-CN.md) · [Project home](../README.md) · [API history CSV](../data/api/model_iq_history.csv)", "",
            f"**API snapshot:** `{snapshot}`  ", f"**Source observation:** `{observed_at}`  ", f"**Retrieved:** `{retrieved_at}`", "",
            "> This is a model-level summary from the Codex Radar API, not the project's task-level difficulty-weighted score.", "",
            "## Current API model summary", "",
            "| Rank | Model tier | Source score | Passed | Tasks | Cost | Total tokens | Wall time |",
            "|---:|---|---:|---:|---:|---:|---:|---:|",
        ]
        for rank, row in enumerate(current, start=1):
            passed, tasks = as_int(row, "passed"), as_int(row, "tasks")
            passed_text = "—" if passed is None or tasks is None else f"{passed}/{tasks}"
            wall = as_int(row, "wall_seconds")
            wall_text = "—" if wall is None else f"{wall / 3600:.2f}h"
            lines.append(f"| {rank} | {label(row)} | {row.get('source_score') or '—'} | {passed_text} | {fmt_number(tasks)} | {fmt_cost(as_float(row, 'cost_usd'))} | {fmt_number(as_int(row, 'total_tokens'))} | {wall_text} |")
        lines.extend([
            "", "## Interpretation", "",
            "- The endpoint provides model-level `score`, pass counts, task counts, tokens, wall time, and estimated cost.",
            "- It does not expose the ten task-level outcomes, so `Weighted /100` cannot be recomputed from this API summary alone.",
            "- Task-weighted rankings remain based on the repository's task matrix and weight snapshots; this report monitors the latest API summary.",
            "- The raw API response is not stored in the public repository; only required model-summary fields are archived.", "",
            f"Archived API snapshots: **{len({row.get('snapshot_id') for row in rows})}**.", "",
        ])
    return "\n".join(lines)


def main() -> None:
    rows = load_rows()
    if not rows:
        print("No API history yet; skipping API report")
        return
    chinese, english = render(rows, zh=True), render(rows, zh=False)
    bilingual = "\n".join(["# Codex Radar API Monitor / API 自动监控", "", "[简体中文](#简体中文) · [English](#english)", "", '<a id="简体中文"></a>', chinese, "", "---", "", '<a id="english"></a>', english, ""])
    REPORTS_DIR.mkdir(parents=True, exist_ok=True)
    OUTPUT_ZH.write_text(chinese, encoding="utf-8")
    OUTPUT_EN.write_text(english, encoding="utf-8")
    OUTPUT_BILINGUAL.write_text(bilingual, encoding="utf-8")
    for output in (OUTPUT_ZH, OUTPUT_EN, OUTPUT_BILINGUAL):
        print(f"Wrote {output.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
