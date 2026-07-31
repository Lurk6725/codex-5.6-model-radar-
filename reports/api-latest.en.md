# Codex Radar API Monitor — English

[简体中文](api-latest.zh-CN.md) · [Project home](../README.md) · [API history CSV](../data/api/model_iq_history.csv) · [Monitor status](../data/api/monitor_status.json)

**Last successful check:** `2026-07-31T21:49:08+00:00`  
**Current API snapshot:** `7eb576aff71fe9cb`  
**Source observation:** `2026-07-22T06:57:20.626603+08:00`  
**New snapshot detected:** yes  
**Models returned:** 11

> “Last successful check” confirms that the automation reached the API. “Source observation” is supplied by the upstream endpoint and may be older.

> This is a model-level summary from the Codex Radar API, not the project's task-level difficulty-weighted score.

## Current API model summary

| Rank | Model tier | Source score | Passed | Tasks | Cost | Total tokens | Wall time |
|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | Sol Xhigh | 96.9 | 72/112 | 112 | $774.04 | 1,020,326,413 | 46.97h |
| 2 | Gpt-5.5 Xhigh | 91.5 | 68/112 | 112 | $649.01 | 821,786,734 | 42.56h |
| 3 | Sol High | 90.1 | 67/112 | 112 | $612.12 | 806,861,983 | 41.41h |
| 4 | Sol Medium | 86.1 | 64/112 | 112 | $431.80 | 555,681,015 | 32.01h |
| 5 | Terra Max | 86.1 | 64/112 | 112 | $559.38 | 1,565,737,285 | 56.99h |
| 6 | Terra High | 84.7 | 63/112 | 112 | $158.73 | 375,167,752 | 24.61h |
| 7 | Luna Max | 82.1 | 61/112 | 112 | $145.76 | 1,782,582,273 | 55.36h |
| 8 | Gpt-5.5 High | 79.4 | 59/112 | 112 | $417.84 | 530,010,386 | 32.79h |
| 9 | Terra Xhigh | 75.3 | 56/112 | 112 | $277.36 | 743,263,563 | 34.29h |
| 10 | Sol Low | 74 | 55/112 | 112 | $251.06 | 289,781,283 | 22.30h |
| 11 | Luna High | 71.3 | 53/112 | 112 | $73.11 | 782,030,233 | 32.39h |

## Interpretation

- The endpoint provides model-level `score`, pass counts, task counts, tokens, wall time, and estimated cost.
- It does not expose the ten task-level outcomes, so `Weighted /100` cannot be recomputed from this API summary alone.
- Task-weighted rankings remain based on the repository's task matrix and weight snapshots; this report monitors the latest API summary.
- When source data is unchanged, the automation still updates its heartbeat without presenting it as a new benchmark batch.
- The raw API response is not stored in the public repository; only required model-summary fields are archived.

Archived API snapshots: **137**.
