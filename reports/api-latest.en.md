# Codex Radar API Monitor — English

[简体中文](api-latest.zh-CN.md) · [Project home](../README.md) · [API history CSV](../data/api/model_iq_history.csv) · [Monitor status](../data/api/monitor_status.json)

**Last successful check:** `2026-08-03T15:20:15+00:00`  
**Current API snapshot:** `4d82419f2191b249`  
**Source observation:** `2026-07-22T06:57:20.626603+08:00`  
**New snapshot detected:** yes  
**Models returned:** 11

> “Last successful check” confirms that the automation reached the API. “Source observation” is supplied by the upstream endpoint and may be older.

> This is a model-level summary from the Codex Radar API, not the project's task-level difficulty-weighted score.

## Current API model summary

| Rank | Model tier | Source score | Passed | Tasks | Cost | Total tokens | Wall time |
|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | Sol Xhigh | 102.2 | 76/112 | 112 | $762.20 | 915,918,924 | 48.17h |
| 2 | Luna Max | 98.2 | 73/112 | 112 | $59.12 | 1,775,774,263 | 62.16h |
| 3 | Gpt-5.5 Xhigh | 96.9 | 72/112 | 112 | $656.94 | 813,364,574 | 43.83h |
| 4 | Terra Max | 95.5 | 71/112 | 112 | $502.82 | 1,496,714,888 | 59.08h |
| 5 | Sol Medium | 88.8 | 66/112 | 112 | $410.41 | 520,098,736 | 32.11h |
| 6 | Gpt-5.5 High | 84.7 | 63/112 | 112 | $413.69 | 505,451,276 | 31.93h |
| 7 | Terra Xhigh | 84.7 | 63/112 | 112 | $248.43 | 634,887,026 | 34.57h |
| 8 | Sol High | 82.1 | 61/112 | 112 | $591.32 | 750,088,312 | 42.22h |
| 9 | Sol Low | 78 | 58/112 | 112 | $234.82 | 250,674,682 | 20.71h |
| 10 | Terra High | 71.3 | 53/112 | 112 | $145.69 | 392,497,334 | 25.39h |
| 11 | Luna High | 63.2 | 47/112 | 112 | $36.61 | 727,457,851 | 29.43h |

## Interpretation

- The endpoint provides model-level `score`, pass counts, task counts, tokens, wall time, and estimated cost.
- It does not expose the ten task-level outcomes, so `Weighted /100` cannot be recomputed from this API summary alone.
- Task-weighted rankings remain based on the repository's task matrix and weight snapshots; this report monitors the latest API summary.
- When source data is unchanged, the automation still updates its heartbeat without presenting it as a new benchmark batch.
- The raw API response is not stored in the public repository; only required model-summary fields are archived.

Archived API snapshots: **164**.
