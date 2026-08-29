# Codex Radar API Monitor — English

[简体中文](api-latest.zh-CN.md) · [Project home](../README.md) · [API history CSV](../data/api/model_iq_history.csv) · [Monitor status](../data/api/monitor_status.json)

**Last successful check:** `2026-08-29T15:39:21+00:00`  
**Current API snapshot:** `47f93820cad5233e`  
**Source observation:** `2026-07-22T06:57:20.626603+08:00`  
**New snapshot detected:** yes  
**Models returned:** 11

> “Last successful check” confirms that the automation reached the API. “Source observation” is supplied by the upstream endpoint and may be older.

> This is a model-level summary from the Codex Radar API, not the project's task-level difficulty-weighted score.

## Current API model summary

| Rank | Model tier | Source score | Passed | Tasks | Cost | Total tokens | Wall time |
|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | Luna Max | 104.9 | 78/112 | 112 | $54.02 | 1,857,883,868 | 67.36h |
| 2 | Sol Medium | 104.9 | 78/112 | 112 | $313.16 | 421,592,112 | 29.32h |
| 3 | Sol Xhigh | 104.9 | 78/112 | 112 | $629.51 | 815,699,593 | 45.81h |
| 4 | Terra Max | 103.6 | 77/112 | 112 | $426.13 | 1,218,908,604 | 57.70h |
| 5 | Gpt-5.5 Xhigh | 100.9 | 75/112 | 112 | $642.63 | 824,059,814 | 43.32h |
| 6 | Sol High | 95.5 | 71/112 | 112 | $510.58 | 599,719,419 | 35.54h |
| 7 | Terra Xhigh | 87.4 | 65/112 | 112 | $212.39 | 617,466,514 | 38.05h |
| 8 | Gpt-5.5 High | 84.7 | 63/112 | 112 | $400.04 | 504,762,396 | 32.25h |
| 9 | Terra High | 82.1 | 61/112 | 112 | $122.93 | 345,200,718 | 26.01h |
| 10 | Sol Low | 79.4 | 59/112 | 112 | $172.51 | 208,350,832 | 17.66h |
| 11 | Luna High | 72.6 | 54/112 | 112 | $22.51 | 728,334,900 | 33.41h |

## Interpretation

- The endpoint provides model-level `score`, pass counts, task counts, tokens, wall time, and estimated cost.
- It does not expose the ten task-level outcomes, so `Weighted /100` cannot be recomputed from this API summary alone.
- Task-weighted rankings remain based on the repository's task matrix and weight snapshots; this report monitors the latest API summary.
- When source data is unchanged, the automation still updates its heartbeat without presenting it as a new benchmark batch.
- The raw API response is not stored in the public repository; only required model-summary fields are archived.

Archived API snapshots: **375**.
