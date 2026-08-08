# Codex Radar API Monitor — English

[简体中文](api-latest.zh-CN.md) · [Project home](../README.md) · [API history CSV](../data/api/model_iq_history.csv) · [Monitor status](../data/api/monitor_status.json)

**Last successful check:** `2026-08-08T11:46:44+00:00`  
**Current API snapshot:** `fd7adf94d6d430d8`  
**Source observation:** `2026-07-22T06:57:20.626603+08:00`  
**New snapshot detected:** yes  
**Models returned:** 11

> “Last successful check” confirms that the automation reached the API. “Source observation” is supplied by the upstream endpoint and may be older.

> This is a model-level summary from the Codex Radar API, not the project's task-level difficulty-weighted score.

## Current API model summary

| Rank | Model tier | Source score | Passed | Tasks | Cost | Total tokens | Wall time |
|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | Sol Xhigh | 107.6 | 80/112 | 112 | $752.18 | 914,029,404 | 47.13h |
| 2 | Luna Max | 96.9 | 72/112 | 112 | $58.72 | 1,794,181,459 | 62.40h |
| 3 | Sol High | 94.2 | 70/112 | 112 | $583.41 | 619,938,882 | 36.38h |
| 4 | Gpt-5.5 Xhigh | 92.8 | 69/112 | 112 | $654.50 | 798,648,002 | 41.04h |
| 5 | Gpt-5.5 High | 91.5 | 68/112 | 112 | $407.58 | 492,174,091 | 31.75h |
| 6 | Sol Medium | 91.5 | 68/112 | 112 | $411.04 | 546,692,859 | 32.08h |
| 7 | Terra Max | 88.8 | 66/112 | 112 | $454.46 | 1,404,199,545 | 58.49h |
| 8 | Sol Low | 86.1 | 64/112 | 112 | $230.19 | 266,942,740 | 22.68h |
| 9 | Terra Xhigh | 80.7 | 60/112 | 112 | $226.38 | 645,546,637 | 37.02h |
| 10 | Luna High | 75.3 | 56/112 | 112 | $26.09 | 724,670,888 | 32.09h |
| 11 | Terra High | 74 | 55/112 | 112 | $128.61 | 335,887,111 | 23.91h |

## Interpretation

- The endpoint provides model-level `score`, pass counts, task counts, tokens, wall time, and estimated cost.
- It does not expose the ten task-level outcomes, so `Weighted /100` cannot be recomputed from this API summary alone.
- Task-weighted rankings remain based on the repository's task matrix and weight snapshots; this report monitors the latest API summary.
- When source data is unchanged, the automation still updates its heartbeat without presenting it as a new benchmark batch.
- The raw API response is not stored in the public repository; only required model-summary fields are archived.

Archived API snapshots: **203**.
