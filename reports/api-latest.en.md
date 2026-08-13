# Codex Radar API Monitor — English

[简体中文](api-latest.zh-CN.md) · [Project home](../README.md) · [API history CSV](../data/api/model_iq_history.csv) · [Monitor status](../data/api/monitor_status.json)

**Last successful check:** `2026-08-13T23:25:42+00:00`  
**Current API snapshot:** `0c8d49214223ef61`  
**Source observation:** `2026-07-22T06:57:20.626603+08:00`  
**New snapshot detected:** no; the source returned the same snapshot  
**Models returned:** 11

> “Last successful check” confirms that the automation reached the API. “Source observation” is supplied by the upstream endpoint and may be older.

> This is a model-level summary from the Codex Radar API, not the project's task-level difficulty-weighted score.

## Current API model summary

| Rank | Model tier | Source score | Passed | Tasks | Cost | Total tokens | Wall time |
|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | Terra Max | 102.2 | 76/112 | 112 | $435.30 | 1,221,558,791 | 59.08h |
| 2 | Sol Xhigh | 99.5 | 74/112 | 112 | $726.19 | 839,569,464 | 45.11h |
| 3 | Luna Max | 98.2 | 73/112 | 112 | $58.68 | 1,903,217,951 | 68.35h |
| 4 | Gpt-5.5 Xhigh | 95.5 | 71/112 | 112 | $656.76 | 716,080,579 | 41.20h |
| 5 | Sol Medium | 91.5 | 68/112 | 112 | $382.84 | 457,592,873 | 32.35h |
| 6 | Gpt-5.5 High | 88.8 | 66/112 | 112 | $403.90 | 494,089,041 | 32.94h |
| 7 | Sol High | 88.8 | 66/112 | 112 | $538.05 | 649,296,478 | 36.86h |
| 8 | Terra Xhigh | 80.7 | 60/112 | 112 | $217.42 | 593,000,585 | 37.15h |
| 9 | Terra High | 75.3 | 56/112 | 112 | $126.59 | 339,648,136 | 25.89h |
| 10 | Luna High | 74 | 55/112 | 112 | $26.18 | 781,522,493 | 35.64h |
| 11 | Sol Low | 71.3 | 53/112 | 112 | $225.53 | 283,159,384 | 23.59h |

## Interpretation

- The endpoint provides model-level `score`, pass counts, task counts, tokens, wall time, and estimated cost.
- It does not expose the ten task-level outcomes, so `Weighted /100` cannot be recomputed from this API summary alone.
- Task-weighted rankings remain based on the repository's task matrix and weight snapshots; this report monitors the latest API summary.
- When source data is unchanged, the automation still updates its heartbeat without presenting it as a new benchmark batch.
- The raw API response is not stored in the public repository; only required model-summary fields are archived.

Archived API snapshots: **254**.
