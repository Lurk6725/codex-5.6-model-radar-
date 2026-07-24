# Codex Radar API Monitor — English

[简体中文](api-latest.zh-CN.md) · [Project home](../README.md) · [API history CSV](../data/api/model_iq_history.csv) · [Monitor status](../data/api/monitor_status.json)

**Last successful check:** `2026-07-24T19:49:35+00:00`  
**Current API snapshot:** `eabb7ee65fd372d8`  
**Source observation:** `2026-07-22T06:57:20.626603+08:00`  
**New snapshot detected:** yes  
**Models returned:** 11

> “Last successful check” confirms that the automation reached the API. “Source observation” is supplied by the upstream endpoint and may be older.

> This is a model-level summary from the Codex Radar API, not the project's task-level difficulty-weighted score.

## Current API model summary

| Rank | Model tier | Source score | Passed | Tasks | Cost | Total tokens | Wall time |
|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | Sol High | 96.9 | 72/112 | 112 | $631.23 | 859,931,277 | 39.40h |
| 2 | Sol Xhigh | 96.9 | 72/112 | 112 | $768.72 | 1,042,357,957 | 46.39h |
| 3 | Sol Medium | 95.5 | 71/112 | 112 | $429.65 | 546,039,617 | 30.17h |
| 4 | Terra Xhigh | 91.5 | 68/112 | 112 | $273.78 | 653,888,810 | 35.38h |
| 5 | Terra Max | 90.1 | 67/112 | 112 | $540.17 | 1,425,843,004 | 56.12h |
| 6 | Gpt-5.5 Xhigh | 84.7 | 63/112 | 112 | $652.14 | 838,268,117 | 45.72h |
| 7 | Luna Max | 84.7 | 63/112 | 112 | $286.31 | 1,979,836,136 | 62.40h |
| 8 | Gpt-5.5 High | 79.4 | 59/112 | 112 | $422.86 | 528,627,627 | 32.29h |
| 9 | Sol Low | 76.7 | 57/112 | 112 | $230.51 | 265,022,735 | 19.66h |
| 10 | Luna High | 70 | 52/112 | 112 | $110.68 | 707,039,669 | 32.07h |
| 11 | Terra High | 68.6 | 51/112 | 112 | $158.31 | 360,206,812 | 23.14h |

## Interpretation

- The endpoint provides model-level `score`, pass counts, task counts, tokens, wall time, and estimated cost.
- It does not expose the ten task-level outcomes, so `Weighted /100` cannot be recomputed from this API summary alone.
- Task-weighted rankings remain based on the repository's task matrix and weight snapshots; this report monitors the latest API summary.
- When source data is unchanged, the automation still updates its heartbeat without presenting it as a new benchmark batch.
- The raw API response is not stored in the public repository; only required model-summary fields are archived.

Archived API snapshots: **73**.
