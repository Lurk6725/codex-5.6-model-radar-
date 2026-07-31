# Codex Radar API Monitor — English

[简体中文](api-latest.zh-CN.md) · [Project home](../README.md) · [API history CSV](../data/api/model_iq_history.csv) · [Monitor status](../data/api/monitor_status.json)

**Last successful check:** `2026-07-31T20:37:26+00:00`  
**Current API snapshot:** `e865121e075c054b`  
**Source observation:** `2026-07-22T06:57:20.626603+08:00`  
**New snapshot detected:** yes  
**Models returned:** 11

> “Last successful check” confirms that the automation reached the API. “Source observation” is supplied by the upstream endpoint and may be older.

> This is a model-level summary from the Codex Radar API, not the project's task-level difficulty-weighted score.

## Current API model summary

| Rank | Model tier | Source score | Passed | Tasks | Cost | Total tokens | Wall time |
|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | Sol Xhigh | 98.2 | 73/112 | 112 | $774.23 | 1,015,322,841 | 46.84h |
| 2 | Gpt-5.5 Xhigh | 90.1 | 67/112 | 112 | $647.71 | 822,432,450 | 42.55h |
| 3 | Sol High | 87.4 | 65/112 | 112 | $608.52 | 819,955,052 | 41.45h |
| 4 | Sol Medium | 86.1 | 64/112 | 112 | $432.16 | 557,218,611 | 32.13h |
| 5 | Terra High | 84.7 | 63/112 | 112 | $161.51 | 382,508,125 | 24.66h |
| 6 | Terra Max | 84.7 | 63/112 | 112 | $562.75 | 1,557,006,799 | 57.01h |
| 7 | Luna Max | 82.1 | 61/112 | 112 | $145.76 | 1,782,582,273 | 55.36h |
| 8 | Gpt-5.5 High | 79.4 | 59/112 | 112 | $417.76 | 530,254,503 | 32.94h |
| 9 | Terra Xhigh | 75.3 | 56/112 | 112 | $279.26 | 746,375,335 | 34.31h |
| 10 | Luna High | 71.3 | 53/112 | 112 | $73.11 | 782,030,233 | 32.39h |
| 11 | Sol Low | 71.3 | 53/112 | 112 | $251.69 | 290,570,852 | 22.24h |

## Interpretation

- The endpoint provides model-level `score`, pass counts, task counts, tokens, wall time, and estimated cost.
- It does not expose the ten task-level outcomes, so `Weighted /100` cannot be recomputed from this API summary alone.
- Task-weighted rankings remain based on the repository's task matrix and weight snapshots; this report monitors the latest API summary.
- When source data is unchanged, the automation still updates its heartbeat without presenting it as a new benchmark batch.
- The raw API response is not stored in the public repository; only required model-summary fields are archived.

Archived API snapshots: **136**.
