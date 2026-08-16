# Codex Radar API Monitor — English

[简体中文](api-latest.zh-CN.md) · [Project home](../README.md) · [API history CSV](../data/api/model_iq_history.csv) · [Monitor status](../data/api/monitor_status.json)

**Last successful check:** `2026-08-16T15:39:54+00:00`  
**Current API snapshot:** `c92bb340fcf22ab4`  
**Source observation:** `2026-07-22T06:57:20.626603+08:00`  
**New snapshot detected:** no; the source returned the same snapshot  
**Models returned:** 11

> “Last successful check” confirms that the automation reached the API. “Source observation” is supplied by the upstream endpoint and may be older.

> This is a model-level summary from the Codex Radar API, not the project's task-level difficulty-weighted score.

## Current API model summary

| Rank | Model tier | Source score | Passed | Tasks | Cost | Total tokens | Wall time |
|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | Terra Max | 99.5 | 74/112 | 112 | $435.18 | 1,258,814,821 | 58.91h |
| 2 | Sol Xhigh | 98.2 | 73/112 | 112 | $724.93 | 856,436,109 | 45.21h |
| 3 | Gpt-5.5 Xhigh | 95.5 | 71/112 | 112 | $655.46 | 750,344,086 | 42.20h |
| 4 | Gpt-5.5 High | 94.2 | 70/112 | 112 | $403.54 | 497,510,501 | 33.09h |
| 5 | Luna Max | 94.2 | 70/112 | 112 | $58.54 | 1,798,964,345 | 65.21h |
| 6 | Sol High | 90.1 | 67/112 | 112 | $538.01 | 647,068,874 | 36.23h |
| 7 | Sol Medium | 87.4 | 65/112 | 112 | $382.82 | 471,222,662 | 32.74h |
| 8 | Terra Xhigh | 83.4 | 62/112 | 112 | $217.00 | 591,056,172 | 37.53h |
| 9 | Luna High | 76.7 | 57/112 | 112 | $26.16 | 763,964,888 | 35.30h |
| 10 | Terra High | 75.3 | 56/112 | 112 | $126.49 | 341,936,024 | 26.13h |
| 11 | Sol Low | 64.6 | 48/112 | 112 | $225.48 | 280,420,021 | 24.48h |

## Interpretation

- The endpoint provides model-level `score`, pass counts, task counts, tokens, wall time, and estimated cost.
- It does not expose the ten task-level outcomes, so `Weighted /100` cannot be recomputed from this API summary alone.
- Task-weighted rankings remain based on the repository's task matrix and weight snapshots; this report monitors the latest API summary.
- When source data is unchanged, the automation still updates its heartbeat without presenting it as a new benchmark batch.
- The raw API response is not stored in the public repository; only required model-summary fields are archived.

Archived API snapshots: **272**.
