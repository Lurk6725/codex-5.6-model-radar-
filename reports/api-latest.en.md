# Codex Radar API Monitor — English

[简体中文](api-latest.zh-CN.md) · [Project home](../README.md) · [API history CSV](../data/api/model_iq_history.csv) · [Monitor status](../data/api/monitor_status.json)

**Last successful check:** `2026-08-20T22:11:27+00:00`  
**Current API snapshot:** `267d0da9afbb1edc`  
**Source observation:** `2026-07-22T06:57:20.626603+08:00`  
**New snapshot detected:** no; the source returned the same snapshot  
**Models returned:** 11

> “Last successful check” confirms that the automation reached the API. “Source observation” is supplied by the upstream endpoint and may be older.

> This is a model-level summary from the Codex Radar API, not the project's task-level difficulty-weighted score.

## Current API model summary

| Rank | Model tier | Source score | Passed | Tasks | Cost | Total tokens | Wall time |
|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | Sol Xhigh | 99.5 | 74/112 | 112 | $723.63 | 838,115,129 | 43.37h |
| 2 | Gpt-5.5 Xhigh | 98.2 | 73/112 | 112 | $652.17 | 780,233,740 | 42.27h |
| 3 | Terra Max | 95.5 | 71/112 | 112 | $433.08 | 1,189,400,145 | 56.65h |
| 4 | Gpt-5.5 High | 92.8 | 69/112 | 112 | $401.19 | 531,851,851 | 34.44h |
| 5 | Luna Max | 90.1 | 67/112 | 112 | $54.74 | 1,775,984,493 | 63.62h |
| 6 | Sol High | 84.7 | 63/112 | 112 | $535.18 | 634,306,989 | 35.95h |
| 7 | Terra Xhigh | 84.7 | 63/112 | 112 | $213.82 | 577,802,223 | 37.00h |
| 8 | Sol Medium | 83.4 | 62/112 | 112 | $404.67 | 465,129,387 | 34.24h |
| 9 | Luna High | 78 | 58/112 | 112 | $22.97 | 727,766,151 | 30.25h |
| 10 | Terra High | 74 | 55/112 | 112 | $125.06 | 339,122,269 | 24.84h |
| 11 | Sol Low | 71.3 | 53/112 | 112 | $223.61 | 261,847,605 | 24.03h |

## Interpretation

- The endpoint provides model-level `score`, pass counts, task counts, tokens, wall time, and estimated cost.
- It does not expose the ten task-level outcomes, so `Weighted /100` cannot be recomputed from this API summary alone.
- Task-weighted rankings remain based on the repository's task matrix and weight snapshots; this report monitors the latest API summary.
- When source data is unchanged, the automation still updates its heartbeat without presenting it as a new benchmark batch.
- The raw API response is not stored in the public repository; only required model-summary fields are archived.

Archived API snapshots: **310**.
