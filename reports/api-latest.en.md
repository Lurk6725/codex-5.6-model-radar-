# Codex Radar API Monitor — English

[简体中文](api-latest.zh-CN.md) · [Project home](../README.md) · [API history CSV](../data/api/model_iq_history.csv) · [Monitor status](../data/api/monitor_status.json)

**Last successful check:** `2026-08-08T16:55:17+00:00`  
**Current API snapshot:** `c7c5c0e4c01860eb`  
**Source observation:** `2026-07-22T06:57:20.626603+08:00`  
**New snapshot detected:** no; the source returned the same snapshot  
**Models returned:** 11

> “Last successful check” confirms that the automation reached the API. “Source observation” is supplied by the upstream endpoint and may be older.

> This is a model-level summary from the Codex Radar API, not the project's task-level difficulty-weighted score.

## Current API model summary

| Rank | Model tier | Source score | Passed | Tasks | Cost | Total tokens | Wall time |
|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | Sol Xhigh | 104.9 | 78/112 | 112 | $751.50 | 911,484,747 | 47.26h |
| 2 | Luna Max | 96.9 | 72/112 | 112 | $58.73 | 1,798,197,787 | 62.32h |
| 3 | Sol High | 96.9 | 72/112 | 112 | $582.08 | 621,349,726 | 36.55h |
| 4 | Gpt-5.5 Xhigh | 92.8 | 69/112 | 112 | $655.66 | 788,545,515 | 41.35h |
| 5 | Sol Medium | 91.5 | 68/112 | 112 | $410.23 | 542,323,956 | 32.04h |
| 6 | Terra Max | 91.5 | 68/112 | 112 | $448.67 | 1,363,448,158 | 56.92h |
| 7 | Gpt-5.5 High | 90.1 | 67/112 | 112 | $407.56 | 494,813,103 | 32.17h |
| 8 | Sol Low | 84.7 | 63/112 | 112 | $230.17 | 266,647,199 | 22.35h |
| 9 | Terra Xhigh | 79.4 | 59/112 | 112 | $226.37 | 640,706,833 | 36.67h |
| 10 | Terra High | 76.7 | 57/112 | 112 | $128.53 | 338,230,602 | 23.56h |
| 11 | Luna High | 74 | 55/112 | 112 | $26.09 | 726,744,577 | 32.09h |

## Interpretation

- The endpoint provides model-level `score`, pass counts, task counts, tokens, wall time, and estimated cost.
- It does not expose the ten task-level outcomes, so `Weighted /100` cannot be recomputed from this API summary alone.
- Task-weighted rankings remain based on the repository's task matrix and weight snapshots; this report monitors the latest API summary.
- When source data is unchanged, the automation still updates its heartbeat without presenting it as a new benchmark batch.
- The raw API response is not stored in the public repository; only required model-summary fields are archived.

Archived API snapshots: **205**.
