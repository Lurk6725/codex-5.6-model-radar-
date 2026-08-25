# Codex Radar API Monitor — English

[简体中文](api-latest.zh-CN.md) · [Project home](../README.md) · [API history CSV](../data/api/model_iq_history.csv) · [Monitor status](../data/api/monitor_status.json)

**Last successful check:** `2026-08-25T09:02:18+00:00`  
**Current API snapshot:** `f1f2e37fc7eeccf9`  
**Source observation:** `2026-07-22T06:57:20.626603+08:00`  
**New snapshot detected:** no; the source returned the same snapshot  
**Models returned:** 11

> “Last successful check” confirms that the automation reached the API. “Source observation” is supplied by the upstream endpoint and may be older.

> This is a model-level summary from the Codex Radar API, not the project's task-level difficulty-weighted score.

## Current API model summary

| Rank | Model tier | Source score | Passed | Tasks | Cost | Total tokens | Wall time |
|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | Sol Xhigh | 106.3 | 79/112 | 112 | $707.18 | 803,710,536 | 44.49h |
| 2 | Luna Max | 102.2 | 76/112 | 112 | $54.07 | 1,698,096,945 | 58.43h |
| 3 | Gpt-5.5 Xhigh | 100.9 | 75/112 | 112 | $647.54 | 777,859,667 | 40.49h |
| 4 | Sol Medium | 96.9 | 72/112 | 112 | $377.54 | 434,768,956 | 29.17h |
| 5 | Terra Max | 95.5 | 71/112 | 112 | $425.52 | 1,161,065,574 | 54.82h |
| 6 | Sol High | 90.1 | 67/112 | 112 | $515.07 | 567,855,394 | 33.64h |
| 7 | Gpt-5.5 High | 88.8 | 66/112 | 112 | $400.75 | 496,546,495 | 31.53h |
| 8 | Terra Xhigh | 86.1 | 64/112 | 112 | $211.77 | 590,613,178 | 37.18h |
| 9 | Sol Low | 82.1 | 61/112 | 112 | $190.96 | 235,439,460 | 18.62h |
| 10 | Luna High | 75.3 | 56/112 | 112 | $22.48 | 702,772,499 | 31.95h |
| 11 | Terra High | 75.3 | 56/112 | 112 | $124.18 | 326,362,341 | 24.77h |

## Interpretation

- The endpoint provides model-level `score`, pass counts, task counts, tokens, wall time, and estimated cost.
- It does not expose the ten task-level outcomes, so `Weighted /100` cannot be recomputed from this API summary alone.
- Task-weighted rankings remain based on the repository's task matrix and weight snapshots; this report monitors the latest API summary.
- When source data is unchanged, the automation still updates its heartbeat without presenting it as a new benchmark batch.
- The raw API response is not stored in the public repository; only required model-summary fields are archived.

Archived API snapshots: **352**.
