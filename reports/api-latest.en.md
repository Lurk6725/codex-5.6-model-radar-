# Codex Radar API Monitor — English

[简体中文](api-latest.zh-CN.md) · [Project home](../README.md) · [API history CSV](../data/api/model_iq_history.csv) · [Monitor status](../data/api/monitor_status.json)

**Last successful check:** `2026-07-28T04:30:42+00:00`  
**Current API snapshot:** `b2b2f07ad1e23195`  
**Source observation:** `2026-07-22T06:57:20.626603+08:00`  
**New snapshot detected:** yes  
**Models returned:** 11

> “Last successful check” confirms that the automation reached the API. “Source observation” is supplied by the upstream endpoint and may be older.

> This is a model-level summary from the Codex Radar API, not the project's task-level difficulty-weighted score.

## Current API model summary

| Rank | Model tier | Source score | Passed | Tasks | Cost | Total tokens | Wall time |
|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | Sol Medium | 95.5 | 71/112 | 112 | $411.41 | 505,867,904 | 31.51h |
| 2 | Terra Max | 94.2 | 70/112 | 112 | $531.99 | 1,417,784,791 | 56.04h |
| 3 | Luna Max | 92.8 | 69/112 | 112 | $275.46 | 1,889,715,941 | 60.30h |
| 4 | Sol High | 92.8 | 69/112 | 112 | $580.26 | 744,639,049 | 41.55h |
| 5 | Sol Xhigh | 90.1 | 67/112 | 112 | $818.80 | 1,138,511,283 | 52.67h |
| 6 | Gpt-5.5 Xhigh | 84.7 | 63/112 | 112 | $661.20 | 848,298,869 | 43.76h |
| 7 | Gpt-5.5 High | 83.4 | 62/112 | 112 | $416.49 | 515,270,977 | 31.42h |
| 8 | Terra Xhigh | 80.7 | 60/112 | 112 | $297.88 | 749,524,650 | 37.40h |
| 9 | Luna High | 74 | 55/112 | 112 | $119.07 | 772,957,315 | 32.56h |
| 10 | Sol Low | 72.6 | 54/112 | 112 | $220.42 | 247,030,660 | 19.34h |
| 11 | Terra High | 68.6 | 51/112 | 112 | $149.16 | 330,583,115 | 21.91h |

## Interpretation

- The endpoint provides model-level `score`, pass counts, task counts, tokens, wall time, and estimated cost.
- It does not expose the ten task-level outcomes, so `Weighted /100` cannot be recomputed from this API summary alone.
- Task-weighted rankings remain based on the repository's task matrix and weight snapshots; this report monitors the latest API summary.
- When source data is unchanged, the automation still updates its heartbeat without presenting it as a new benchmark batch.
- The raw API response is not stored in the public repository; only required model-summary fields are archived.

Archived API snapshots: **100**.
