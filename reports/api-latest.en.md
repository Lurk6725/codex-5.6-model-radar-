# Codex Radar API Monitor — English

[简体中文](api-latest.zh-CN.md) · [Project home](../README.md) · [API history CSV](../data/api/model_iq_history.csv) · [Monitor status](../data/api/monitor_status.json)

**Last successful check:** `2026-08-03T04:50:27+00:00`  
**Current API snapshot:** `a2b9ff42cd0c62ad`  
**Source observation:** `2026-07-22T06:57:20.626603+08:00`  
**New snapshot detected:** yes  
**Models returned:** 11

> “Last successful check” confirms that the automation reached the API. “Source observation” is supplied by the upstream endpoint and may be older.

> This is a model-level summary from the Codex Radar API, not the project's task-level difficulty-weighted score.

## Current API model summary

| Rank | Model tier | Source score | Passed | Tasks | Cost | Total tokens | Wall time |
|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | Gpt-5.5 Xhigh | 100.9 | 75/112 | 112 | $656.32 | 815,931,014 | 43.41h |
| 2 | Sol Xhigh | 99.5 | 74/112 | 112 | $772.45 | 950,422,495 | 47.53h |
| 3 | Terra Max | 94.2 | 70/112 | 112 | $517.48 | 1,485,389,314 | 57.63h |
| 4 | Luna Max | 91.5 | 68/112 | 112 | $61.07 | 1,741,992,019 | 60.22h |
| 5 | Sol Medium | 87.4 | 65/112 | 112 | $408.07 | 490,643,314 | 31.51h |
| 6 | Sol High | 86.1 | 64/112 | 112 | $592.42 | 752,103,251 | 42.51h |
| 7 | Gpt-5.5 High | 83.4 | 62/112 | 112 | $412.45 | 501,669,364 | 31.59h |
| 8 | Terra Xhigh | 82.1 | 61/112 | 112 | $262.31 | 690,114,833 | 35.02h |
| 9 | Sol Low | 72.6 | 54/112 | 112 | $243.24 | 278,829,952 | 21.47h |
| 10 | Terra High | 72.6 | 54/112 | 112 | $147.55 | 396,609,510 | 25.88h |
| 11 | Luna High | 67.3 | 50/112 | 112 | $43.17 | 760,703,163 | 31.55h |

## Interpretation

- The endpoint provides model-level `score`, pass counts, task counts, tokens, wall time, and estimated cost.
- It does not expose the ten task-level outcomes, so `Weighted /100` cannot be recomputed from this API summary alone.
- Task-weighted rankings remain based on the repository's task matrix and weight snapshots; this report monitors the latest API summary.
- When source data is unchanged, the automation still updates its heartbeat without presenting it as a new benchmark batch.
- The raw API response is not stored in the public repository; only required model-summary fields are archived.

Archived API snapshots: **161**.
