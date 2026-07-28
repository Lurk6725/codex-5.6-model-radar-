# Codex Radar API Monitor — English

[简体中文](api-latest.zh-CN.md) · [Project home](../README.md) · [API history CSV](../data/api/model_iq_history.csv) · [Monitor status](../data/api/monitor_status.json)

**Last successful check:** `2026-07-28T16:25:51+00:00`  
**Current API snapshot:** `516a8c8c5bb11ed8`  
**Source observation:** `2026-07-22T06:57:20.626603+08:00`  
**New snapshot detected:** no; the source returned the same snapshot  
**Models returned:** 11

> “Last successful check” confirms that the automation reached the API. “Source observation” is supplied by the upstream endpoint and may be older.

> This is a model-level summary from the Codex Radar API, not the project's task-level difficulty-weighted score.

## Current API model summary

| Rank | Model tier | Source score | Passed | Tasks | Cost | Total tokens | Wall time |
|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | Sol Xhigh | 96.9 | 72/112 | 112 | $742.10 | 976,696,672 | 44.89h |
| 2 | Sol High | 92.8 | 69/112 | 112 | $570.22 | 730,086,106 | 40.13h |
| 3 | Sol Medium | 91.5 | 68/112 | 112 | $400.10 | 489,820,161 | 31.45h |
| 4 | Luna Max | 90.1 | 67/112 | 112 | $277.43 | 1,902,154,844 | 61.36h |
| 5 | Terra Max | 90.1 | 67/112 | 112 | $530.92 | 1,394,724,339 | 56.56h |
| 6 | Gpt-5.5 Xhigh | 87.4 | 65/112 | 112 | $668.57 | 854,522,217 | 45.47h |
| 7 | Gpt-5.5 High | 83.4 | 62/112 | 112 | $408.60 | 498,959,739 | 29.97h |
| 8 | Terra Xhigh | 80.7 | 60/112 | 112 | $299.97 | 755,991,057 | 36.89h |
| 9 | Sol Low | 76.7 | 57/112 | 112 | $228.34 | 257,447,415 | 19.38h |
| 10 | Terra High | 74 | 55/112 | 112 | $155.29 | 347,203,910 | 23.44h |
| 11 | Luna High | 72.6 | 54/112 | 112 | $121.58 | 797,056,846 | 32.86h |

## Interpretation

- The endpoint provides model-level `score`, pass counts, task counts, tokens, wall time, and estimated cost.
- It does not expose the ten task-level outcomes, so `Weighted /100` cannot be recomputed from this API summary alone.
- Task-weighted rankings remain based on the repository's task matrix and weight snapshots; this report monitors the latest API summary.
- When source data is unchanged, the automation still updates its heartbeat without presenting it as a new benchmark batch.
- The raw API response is not stored in the public repository; only required model-summary fields are archived.

Archived API snapshots: **104**.
