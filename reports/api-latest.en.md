# Codex Radar API Monitor — English

[简体中文](api-latest.zh-CN.md) · [Project home](../README.md) · [API history CSV](../data/api/model_iq_history.csv) · [Monitor status](../data/api/monitor_status.json)

**Last successful check:** `2026-07-24T17:54:36+00:00`  
**Current API snapshot:** `21b3429af6a68bb7`  
**Source observation:** `2026-07-22T06:57:20.626603+08:00`  
**New snapshot detected:** yes  
**Models returned:** 11

> “Last successful check” confirms that the automation reached the API. “Source observation” is supplied by the upstream endpoint and may be older.

> This is a model-level summary from the Codex Radar API, not the project's task-level difficulty-weighted score.

## Current API model summary

| Rank | Model tier | Source score | Passed | Tasks | Cost | Total tokens | Wall time |
|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | Sol High | 96.9 | 72/112 | 112 | $631.53 | 860,162,094 | 39.46h |
| 2 | Sol Xhigh | 96.9 | 72/112 | 112 | $768.72 | 1,042,357,957 | 46.39h |
| 3 | Sol Medium | 95.5 | 71/112 | 112 | $429.65 | 546,039,617 | 30.17h |
| 4 | Terra Xhigh | 91.5 | 68/112 | 112 | $273.60 | 653,595,445 | 35.39h |
| 5 | Terra Max | 90.1 | 67/112 | 112 | $540.17 | 1,425,843,004 | 56.12h |
| 6 | Gpt-5.5 Xhigh | 84.7 | 63/112 | 112 | $652.14 | 838,268,117 | 45.72h |
| 7 | Luna Max | 84.7 | 63/112 | 112 | $286.31 | 1,979,836,136 | 62.40h |
| 8 | Gpt-5.5 High | 80.7 | 60/112 | 112 | $428.68 | 539,099,929 | 32.90h |
| 9 | Sol Low | 76.7 | 57/112 | 112 | $231.28 | 265,982,449 | 19.57h |
| 10 | Luna High | 71.3 | 53/112 | 112 | $111.19 | 710,415,581 | 32.28h |
| 11 | Terra High | 68.6 | 51/112 | 112 | $158.21 | 359,782,325 | 23.14h |

## Interpretation

- The endpoint provides model-level `score`, pass counts, task counts, tokens, wall time, and estimated cost.
- It does not expose the ten task-level outcomes, so `Weighted /100` cannot be recomputed from this API summary alone.
- Task-weighted rankings remain based on the repository's task matrix and weight snapshots; this report monitors the latest API summary.
- When source data is unchanged, the automation still updates its heartbeat without presenting it as a new benchmark batch.
- The raw API response is not stored in the public repository; only required model-summary fields are archived.

Archived API snapshots: **72**.
