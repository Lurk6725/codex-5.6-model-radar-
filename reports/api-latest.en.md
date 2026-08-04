# Codex Radar API Monitor — English

[简体中文](api-latest.zh-CN.md) · [Project home](../README.md) · [API history CSV](../data/api/model_iq_history.csv) · [Monitor status](../data/api/monitor_status.json)

**Last successful check:** `2026-08-04T01:08:43+00:00`  
**Current API snapshot:** `b600c116f9166506`  
**Source observation:** `2026-07-22T06:57:20.626603+08:00`  
**New snapshot detected:** no; the source returned the same snapshot  
**Models returned:** 11

> “Last successful check” confirms that the automation reached the API. “Source observation” is supplied by the upstream endpoint and may be older.

> This is a model-level summary from the Codex Radar API, not the project's task-level difficulty-weighted score.

## Current API model summary

| Rank | Model tier | Source score | Passed | Tasks | Cost | Total tokens | Wall time |
|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | Sol Xhigh | 102.2 | 76/112 | 112 | $760.93 | 905,895,600 | 47.73h |
| 2 | Gpt-5.5 Xhigh | 98.2 | 73/112 | 112 | $655.54 | 817,451,832 | 43.41h |
| 3 | Luna Max | 98.2 | 73/112 | 112 | $59.13 | 1,776,474,391 | 62.17h |
| 4 | Terra Max | 95.5 | 71/112 | 112 | $498.11 | 1,486,810,959 | 58.83h |
| 5 | Sol Medium | 87.4 | 65/112 | 112 | $410.57 | 515,849,874 | 31.93h |
| 6 | Gpt-5.5 High | 84.7 | 63/112 | 112 | $412.65 | 502,257,672 | 31.28h |
| 7 | Terra Xhigh | 84.7 | 63/112 | 112 | $245.88 | 621,907,696 | 34.10h |
| 8 | Sol High | 82.1 | 61/112 | 112 | $588.11 | 731,840,489 | 42.07h |
| 9 | Sol Low | 78 | 58/112 | 112 | $235.51 | 251,682,081 | 20.42h |
| 10 | Terra High | 72.6 | 54/112 | 112 | $144.08 | 389,851,997 | 25.19h |
| 11 | Luna High | 65.9 | 49/112 | 112 | $35.94 | 724,901,726 | 29.25h |

## Interpretation

- The endpoint provides model-level `score`, pass counts, task counts, tokens, wall time, and estimated cost.
- It does not expose the ten task-level outcomes, so `Weighted /100` cannot be recomputed from this API summary alone.
- Task-weighted rankings remain based on the repository's task matrix and weight snapshots; this report monitors the latest API summary.
- When source data is unchanged, the automation still updates its heartbeat without presenting it as a new benchmark batch.
- The raw API response is not stored in the public repository; only required model-summary fields are archived.

Archived API snapshots: **165**.
