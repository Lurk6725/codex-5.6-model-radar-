# Codex Radar API Monitor — English

[简体中文](api-latest.zh-CN.md) · [Project home](../README.md) · [API history CSV](../data/api/model_iq_history.csv) · [Monitor status](../data/api/monitor_status.json)

**Last successful check:** `2026-07-22T12:06:24+00:00`  
**Current API snapshot:** `0486a792b7324449`  
**Source observation:** `2026-07-22T06:57:20.626603+08:00`  
**New snapshot detected:** no; the source returned the same snapshot  
**Models returned:** 11

> “Last successful check” confirms that the automation reached the API. “Source observation” is supplied by the upstream endpoint and may be older.

> This is a model-level summary from the Codex Radar API, not the project's task-level difficulty-weighted score.

## Current API model summary

| Rank | Model tier | Source score | Passed | Tasks | Cost | Total tokens | Wall time |
|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | Terra Max | 100.9 | 75/112 | 112 | $528.69 | 1,365,570,339 | 62.73h |
| 2 | Gpt-5.5 Xhigh | 98.2 | 73/112 | 112 | $654.10 | 841,325,210 | 42.21h |
| 3 | Luna Max | 96.9 | 72/112 | 112 | $286.52 | 1,981,513,748 | 67.10h |
| 4 | Terra Xhigh | 95.5 | 71/112 | 112 | $278.00 | 672,981,784 | 37.21h |
| 5 | Sol Xhigh | 94.2 | 70/112 | 112 | $770.15 | 1,030,604,158 | 51.63h |
| 6 | Sol High | 92.8 | 69/112 | 112 | $562.74 | 723,320,884 | 41.33h |
| 7 | Sol Medium | 90.1 | 67/112 | 112 | $410.00 | 515,678,492 | 32.82h |
| 8 | Gpt-5.5 High | 80.7 | 60/112 | 112 | $401.62 | 500,479,834 | 29.00h |
| 9 | Sol Low | 77.4 | 57/111 | 111 | $230.66 | 266,869,831 | 23.06h |
| 10 | Luna High | 72.6 | 54/112 | 112 | $112.69 | 716,031,289 | 34.44h |
| 11 | Terra High | 63.2 | 47/112 | 112 | $144.67 | 326,096,571 | 25.05h |

## Interpretation

- The endpoint provides model-level `score`, pass counts, task counts, tokens, wall time, and estimated cost.
- It does not expose the ten task-level outcomes, so `Weighted /100` cannot be recomputed from this API summary alone.
- Task-weighted rankings remain based on the repository's task matrix and weight snapshots; this report monitors the latest API summary.
- When source data is unchanged, the automation still updates its heartbeat without presenting it as a new benchmark batch.
- The raw API response is not stored in the public repository; only required model-summary fields are archived.

Archived API snapshots: **50**.
