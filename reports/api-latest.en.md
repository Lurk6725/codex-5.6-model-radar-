# Codex Radar API Monitor — English

[简体中文](api-latest.zh-CN.md) · [Project home](../README.md) · [API history CSV](../data/api/model_iq_history.csv) · [Monitor status](../data/api/monitor_status.json)

**Last successful check:** `2026-08-01T09:45:12+00:00`  
**Current API snapshot:** `74fa3bb8113b2968`  
**Source observation:** `2026-07-22T06:57:20.626603+08:00`  
**New snapshot detected:** yes  
**Models returned:** 11

> “Last successful check” confirms that the automation reached the API. “Source observation” is supplied by the upstream endpoint and may be older.

> This is a model-level summary from the Codex Radar API, not the project's task-level difficulty-weighted score.

## Current API model summary

| Rank | Model tier | Source score | Passed | Tasks | Cost | Total tokens | Wall time |
|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | Sol Xhigh | 96.9 | 72/112 | 112 | $768.61 | 1,002,073,967 | 47.05h |
| 2 | Gpt-5.5 Xhigh | 91.5 | 68/112 | 112 | $646.20 | 837,867,189 | 43.70h |
| 3 | Sol High | 90.1 | 67/112 | 112 | $610.63 | 798,218,362 | 40.85h |
| 4 | Terra Max | 87.4 | 65/112 | 112 | $545.21 | 1,542,079,773 | 57.00h |
| 5 | Sol Medium | 84.7 | 63/112 | 112 | $424.34 | 561,593,803 | 32.58h |
| 6 | Gpt-5.5 High | 79.4 | 59/112 | 112 | $413.99 | 531,243,444 | 32.52h |
| 7 | Luna Max | 79.4 | 59/112 | 112 | $138.47 | 1,792,895,476 | 55.75h |
| 8 | Terra High | 78 | 58/112 | 112 | $153.25 | 400,519,708 | 25.69h |
| 9 | Sol Low | 74 | 55/112 | 112 | $251.01 | 285,350,216 | 21.95h |
| 10 | Terra Xhigh | 74 | 55/112 | 112 | $272.93 | 737,340,047 | 34.37h |
| 11 | Luna High | 67.3 | 50/112 | 112 | $72.34 | 800,617,398 | 33.56h |

## Interpretation

- The endpoint provides model-level `score`, pass counts, task counts, tokens, wall time, and estimated cost.
- It does not expose the ten task-level outcomes, so `Weighted /100` cannot be recomputed from this API summary alone.
- Task-weighted rankings remain based on the repository's task matrix and weight snapshots; this report monitors the latest API summary.
- When source data is unchanged, the automation still updates its heartbeat without presenting it as a new benchmark batch.
- The raw API response is not stored in the public repository; only required model-summary fields are archived.

Archived API snapshots: **141**.
