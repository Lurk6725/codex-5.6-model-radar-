# Codex Radar API Monitor — English

[简体中文](api-latest.zh-CN.md) · [Project home](../README.md) · [API history CSV](../data/api/model_iq_history.csv) · [Monitor status](../data/api/monitor_status.json)

**Last successful check:** `2026-08-15T11:58:59+00:00`  
**Current API snapshot:** `926205f196f975f2`  
**Source observation:** `2026-07-22T06:57:20.626603+08:00`  
**New snapshot detected:** no; the source returned the same snapshot  
**Models returned:** 11

> “Last successful check” confirms that the automation reached the API. “Source observation” is supplied by the upstream endpoint and may be older.

> This is a model-level summary from the Codex Radar API, not the project's task-level difficulty-weighted score.

## Current API model summary

| Rank | Model tier | Source score | Passed | Tasks | Cost | Total tokens | Wall time |
|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | Sol Xhigh | 99.5 | 74/112 | 112 | $725.67 | 851,424,038 | 45.04h |
| 2 | Terra Max | 99.5 | 74/112 | 112 | $435.19 | 1,267,641,591 | 59.59h |
| 3 | Gpt-5.5 Xhigh | 95.5 | 71/112 | 112 | $655.38 | 756,010,585 | 42.47h |
| 4 | Luna Max | 95.5 | 71/112 | 112 | $58.56 | 1,813,948,803 | 65.63h |
| 5 | Gpt-5.5 High | 94.2 | 70/112 | 112 | $403.56 | 497,172,441 | 32.94h |
| 6 | Sol High | 90.1 | 67/112 | 112 | $538.27 | 653,556,950 | 36.26h |
| 7 | Sol Medium | 87.4 | 65/112 | 112 | $382.76 | 455,481,969 | 32.41h |
| 8 | Terra Xhigh | 84.7 | 63/112 | 112 | $217.13 | 590,666,725 | 37.52h |
| 9 | Luna High | 76.7 | 57/112 | 112 | $26.14 | 773,956,923 | 36.21h |
| 10 | Terra High | 75.3 | 56/112 | 112 | $126.50 | 342,336,729 | 26.12h |
| 11 | Sol Low | 64.6 | 48/112 | 112 | $225.36 | 274,226,159 | 24.01h |

## Interpretation

- The endpoint provides model-level `score`, pass counts, task counts, tokens, wall time, and estimated cost.
- It does not expose the ten task-level outcomes, so `Weighted /100` cannot be recomputed from this API summary alone.
- Task-weighted rankings remain based on the repository's task matrix and weight snapshots; this report monitors the latest API summary.
- When source data is unchanged, the automation still updates its heartbeat without presenting it as a new benchmark batch.
- The raw API response is not stored in the public repository; only required model-summary fields are archived.

Archived API snapshots: **265**.
