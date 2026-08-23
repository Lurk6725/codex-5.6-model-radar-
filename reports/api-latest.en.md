# Codex Radar API Monitor — English

[简体中文](api-latest.zh-CN.md) · [Project home](../README.md) · [API history CSV](../data/api/model_iq_history.csv) · [Monitor status](../data/api/monitor_status.json)

**Last successful check:** `2026-08-23T20:42:04+00:00`  
**Current API snapshot:** `5ff55b102f921bc9`  
**Source observation:** `2026-07-22T06:57:20.626603+08:00`  
**New snapshot detected:** no; the source returned the same snapshot  
**Models returned:** 11

> “Last successful check” confirms that the automation reached the API. “Source observation” is supplied by the upstream endpoint and may be older.

> This is a model-level summary from the Codex Radar API, not the project's task-level difficulty-weighted score.

## Current API model summary

| Rank | Model tier | Source score | Passed | Tasks | Cost | Total tokens | Wall time |
|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | Sol Xhigh | 102.2 | 76/112 | 112 | $718.01 | 829,825,927 | 44.16h |
| 2 | Gpt-5.5 Xhigh | 98.2 | 73/112 | 112 | $650.70 | 777,231,189 | 41.17h |
| 3 | Terra Max | 95.5 | 71/112 | 112 | $426.30 | 1,169,102,727 | 55.24h |
| 4 | Gpt-5.5 High | 94.2 | 70/112 | 112 | $401.36 | 507,439,191 | 33.47h |
| 5 | Luna Max | 86.1 | 64/112 | 112 | $54.38 | 1,693,781,469 | 58.38h |
| 6 | Sol High | 86.1 | 64/112 | 112 | $533.24 | 570,749,469 | 35.06h |
| 7 | Terra Xhigh | 86.1 | 64/112 | 112 | $213.59 | 583,746,238 | 36.80h |
| 8 | Sol Medium | 82.1 | 61/112 | 112 | $403.50 | 455,699,868 | 33.10h |
| 9 | Luna High | 76.7 | 57/112 | 112 | $22.65 | 695,898,274 | 30.07h |
| 10 | Terra High | 76.7 | 57/112 | 112 | $124.90 | 336,338,462 | 24.69h |
| 11 | Sol Low | 72.6 | 54/112 | 112 | $222.81 | 250,043,972 | 23.26h |

## Interpretation

- The endpoint provides model-level `score`, pass counts, task counts, tokens, wall time, and estimated cost.
- It does not expose the ten task-level outcomes, so `Weighted /100` cannot be recomputed from this API summary alone.
- Task-weighted rankings remain based on the repository's task matrix and weight snapshots; this report monitors the latest API summary.
- When source data is unchanged, the automation still updates its heartbeat without presenting it as a new benchmark batch.
- The raw API response is not stored in the public repository; only required model-summary fields are archived.

Archived API snapshots: **335**.
