# Codex Radar API Monitor — English

[简体中文](api-latest.zh-CN.md) · [Project home](../README.md) · [API history CSV](../data/api/model_iq_history.csv) · [Monitor status](../data/api/monitor_status.json)

**Last successful check:** `2026-08-27T05:07:18+00:00`  
**Current API snapshot:** `c996b3bf9583f525`  
**Source observation:** `2026-07-22T06:57:20.626603+08:00`  
**New snapshot detected:** yes  
**Models returned:** 11

> “Last successful check” confirms that the automation reached the API. “Source observation” is supplied by the upstream endpoint and may be older.

> This is a model-level summary from the Codex Radar API, not the project's task-level difficulty-weighted score.

## Current API model summary

| Rank | Model tier | Source score | Passed | Tasks | Cost | Total tokens | Wall time |
|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | Sol Xhigh | 103.6 | 77/112 | 112 | $674.04 | 807,062,622 | 44.97h |
| 2 | Luna Max | 102.2 | 76/112 | 112 | $54.07 | 1,743,783,029 | 63.72h |
| 3 | Sol Medium | 100.9 | 75/112 | 112 | $311.46 | 416,045,497 | 28.96h |
| 4 | Terra Max | 100.9 | 75/112 | 112 | $425.64 | 1,173,678,843 | 55.51h |
| 5 | Gpt-5.5 Xhigh | 99.5 | 74/112 | 112 | $646.39 | 778,156,012 | 40.49h |
| 6 | Sol High | 90.1 | 67/112 | 112 | $506.37 | 561,471,574 | 33.85h |
| 7 | Gpt-5.5 High | 86.1 | 64/112 | 112 | $400.29 | 504,805,054 | 31.91h |
| 8 | Terra Xhigh | 84.7 | 63/112 | 112 | $211.63 | 595,740,896 | 36.59h |
| 9 | Sol Low | 83.4 | 62/112 | 112 | $172.50 | 209,414,220 | 17.01h |
| 10 | Terra High | 79.4 | 59/112 | 112 | $123.04 | 342,776,522 | 25.32h |
| 11 | Luna High | 75.3 | 56/112 | 112 | $22.47 | 703,300,007 | 32.06h |

## Interpretation

- The endpoint provides model-level `score`, pass counts, task counts, tokens, wall time, and estimated cost.
- It does not expose the ten task-level outcomes, so `Weighted /100` cannot be recomputed from this API summary alone.
- Task-weighted rankings remain based on the repository's task matrix and weight snapshots; this report monitors the latest API summary.
- When source data is unchanged, the automation still updates its heartbeat without presenting it as a new benchmark batch.
- The raw API response is not stored in the public repository; only required model-summary fields are archived.

Archived API snapshots: **368**.
