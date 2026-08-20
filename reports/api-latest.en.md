# Codex Radar API Monitor — English

[简体中文](api-latest.zh-CN.md) · [Project home](../README.md) · [API history CSV](../data/api/model_iq_history.csv) · [Monitor status](../data/api/monitor_status.json)

**Last successful check:** `2026-08-20T04:55:55+00:00`  
**Current API snapshot:** `91372997b7d37906`  
**Source observation:** `2026-07-22T06:57:20.626603+08:00`  
**New snapshot detected:** no; the source returned the same snapshot  
**Models returned:** 11

> “Last successful check” confirms that the automation reached the API. “Source observation” is supplied by the upstream endpoint and may be older.

> This is a model-level summary from the Codex Radar API, not the project's task-level difficulty-weighted score.

## Current API model summary

| Rank | Model tier | Source score | Passed | Tasks | Cost | Total tokens | Wall time |
|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | Gpt-5.5 Xhigh | 98.2 | 73/112 | 112 | $652.58 | 780,518,242 | 41.60h |
| 2 | Sol Xhigh | 96.9 | 72/112 | 112 | $724.95 | 838,114,553 | 43.85h |
| 3 | Terra Max | 95.5 | 71/112 | 112 | $433.24 | 1,203,352,793 | 57.24h |
| 4 | Gpt-5.5 High | 90.1 | 67/112 | 112 | $401.18 | 531,290,071 | 34.81h |
| 5 | Luna Max | 88.8 | 66/112 | 112 | $54.87 | 1,758,016,017 | 61.96h |
| 6 | Terra Xhigh | 86.1 | 64/112 | 112 | $213.82 | 576,881,480 | 37.31h |
| 7 | Sol High | 84.7 | 63/112 | 112 | $535.92 | 628,763,536 | 35.42h |
| 8 | Sol Medium | 82.1 | 61/112 | 112 | $405.18 | 462,452,035 | 34.04h |
| 9 | Luna High | 75.3 | 56/112 | 112 | $23.37 | 747,287,124 | 33.32h |
| 10 | Terra High | 72.6 | 54/112 | 112 | $125.01 | 341,285,586 | 25.11h |
| 11 | Sol Low | 70 | 52/112 | 112 | $223.75 | 262,351,610 | 24.12h |

## Interpretation

- The endpoint provides model-level `score`, pass counts, task counts, tokens, wall time, and estimated cost.
- It does not expose the ten task-level outcomes, so `Weighted /100` cannot be recomputed from this API summary alone.
- Task-weighted rankings remain based on the repository's task matrix and weight snapshots; this report monitors the latest API summary.
- When source data is unchanged, the automation still updates its heartbeat without presenting it as a new benchmark batch.
- The raw API response is not stored in the public repository; only required model-summary fields are archived.

Archived API snapshots: **303**.
