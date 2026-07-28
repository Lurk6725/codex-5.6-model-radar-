# Codex Radar API Monitor — English

[简体中文](api-latest.zh-CN.md) · [Project home](../README.md) · [API history CSV](../data/api/model_iq_history.csv) · [Monitor status](../data/api/monitor_status.json)

**Last successful check:** `2026-07-28T21:33:51+00:00`  
**Current API snapshot:** `88268857b67f7a8d`  
**Source observation:** `2026-07-22T06:57:20.626603+08:00`  
**New snapshot detected:** yes  
**Models returned:** 11

> “Last successful check” confirms that the automation reached the API. “Source observation” is supplied by the upstream endpoint and may be older.

> This is a model-level summary from the Codex Radar API, not the project's task-level difficulty-weighted score.

## Current API model summary

| Rank | Model tier | Source score | Passed | Tasks | Cost | Total tokens | Wall time |
|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | Sol Xhigh | 99.5 | 74/112 | 112 | $709.77 | 923,413,711 | 43.83h |
| 2 | Gpt-5.5 Xhigh | 90.1 | 67/112 | 112 | $663.74 | 842,920,244 | 45.57h |
| 3 | Luna Max | 90.1 | 67/112 | 112 | $282.18 | 1,943,900,551 | 62.78h |
| 4 | Sol High | 90.1 | 67/112 | 112 | $571.56 | 732,943,530 | 41.04h |
| 5 | Sol Medium | 90.1 | 67/112 | 112 | $410.91 | 505,364,636 | 31.54h |
| 6 | Terra Max | 90.1 | 67/112 | 112 | $542.52 | 1,432,045,289 | 57.85h |
| 7 | Gpt-5.5 High | 84.7 | 63/112 | 112 | $409.92 | 503,275,120 | 29.82h |
| 8 | Terra Xhigh | 83.4 | 62/112 | 112 | $302.18 | 762,182,386 | 37.03h |
| 9 | Sol Low | 82.1 | 61/112 | 112 | $231.97 | 265,206,799 | 17.97h |
| 10 | Luna High | 75.3 | 56/112 | 112 | $124.16 | 819,912,970 | 34.10h |
| 11 | Terra High | 72.6 | 54/112 | 112 | $156.18 | 349,080,291 | 23.72h |

## Interpretation

- The endpoint provides model-level `score`, pass counts, task counts, tokens, wall time, and estimated cost.
- It does not expose the ten task-level outcomes, so `Weighted /100` cannot be recomputed from this API summary alone.
- Task-weighted rankings remain based on the repository's task matrix and weight snapshots; this report monitors the latest API summary.
- When source data is unchanged, the automation still updates its heartbeat without presenting it as a new benchmark batch.
- The raw API response is not stored in the public repository; only required model-summary fields are archived.

Archived API snapshots: **107**.
