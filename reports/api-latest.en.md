# Codex Radar API Monitor — English

[简体中文](api-latest.zh-CN.md) · [Project home](../README.md) · [API history CSV](../data/api/model_iq_history.csv) · [Monitor status](../data/api/monitor_status.json)

**Last successful check:** `2026-07-30T14:35:40+00:00`  
**Current API snapshot:** `db57b401a4a0b7c9`  
**Source observation:** `2026-07-22T06:57:20.626603+08:00`  
**New snapshot detected:** yes  
**Models returned:** 11

> “Last successful check” confirms that the automation reached the API. “Source observation” is supplied by the upstream endpoint and may be older.

> This is a model-level summary from the Codex Radar API, not the project's task-level difficulty-weighted score.

## Current API model summary

| Rank | Model tier | Source score | Passed | Tasks | Cost | Total tokens | Wall time |
|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | Gpt-5.5 Xhigh | 94.2 | 70/112 | 112 | $652.45 | 834,239,085 | 44.02h |
| 2 | Sol Xhigh | 94.2 | 70/112 | 112 | $730.59 | 969,473,874 | 45.77h |
| 3 | Luna Max | 87.4 | 65/112 | 112 | $269.88 | 1,841,185,179 | 61.09h |
| 4 | Sol High | 87.4 | 65/112 | 112 | $594.92 | 783,991,765 | 41.34h |
| 5 | Terra Xhigh | 83.4 | 62/112 | 112 | $277.76 | 664,034,599 | 34.89h |
| 6 | Sol Low | 82.1 | 61/112 | 112 | $249.58 | 289,350,040 | 22.59h |
| 7 | Gpt-5.5 High | 80.7 | 60/112 | 112 | $436.99 | 549,563,793 | 31.60h |
| 8 | Sol Medium | 80.7 | 60/112 | 112 | $424.46 | 524,571,248 | 31.74h |
| 9 | Terra Max | 80.7 | 60/112 | 112 | $561.55 | 1,467,356,374 | 55.21h |
| 10 | Terra High | 71.3 | 53/112 | 112 | $164.43 | 375,514,551 | 23.76h |
| 11 | Luna High | 68.6 | 51/112 | 112 | $123.34 | 817,572,245 | 34.62h |

## Interpretation

- The endpoint provides model-level `score`, pass counts, task counts, tokens, wall time, and estimated cost.
- It does not expose the ten task-level outcomes, so `Weighted /100` cannot be recomputed from this API summary alone.
- Task-weighted rankings remain based on the repository's task matrix and weight snapshots; this report monitors the latest API summary.
- When source data is unchanged, the automation still updates its heartbeat without presenting it as a new benchmark batch.
- The raw API response is not stored in the public repository; only required model-summary fields are archived.

Archived API snapshots: **122**.
