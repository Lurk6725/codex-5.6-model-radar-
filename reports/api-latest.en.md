# Codex Radar API Monitor — English

[简体中文](api-latest.zh-CN.md) · [Project home](../README.md) · [API history CSV](../data/api/model_iq_history.csv) · [Monitor status](../data/api/monitor_status.json)

**Last successful check:** `2026-08-29T11:09:11+00:00`  
**Current API snapshot:** `8de308b33b4c26ce`  
**Source observation:** `2026-07-22T06:57:20.626603+08:00`  
**New snapshot detected:** yes  
**Models returned:** 11

> “Last successful check” confirms that the automation reached the API. “Source observation” is supplied by the upstream endpoint and may be older.

> This is a model-level summary from the Codex Radar API, not the project's task-level difficulty-weighted score.

## Current API model summary

| Rank | Model tier | Source score | Passed | Tasks | Cost | Total tokens | Wall time |
|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | Luna Max | 104.9 | 78/112 | 112 | $54.02 | 1,843,982,557 | 67.02h |
| 2 | Sol Medium | 103.6 | 77/112 | 112 | $313.21 | 422,943,366 | 29.44h |
| 3 | Terra Max | 103.6 | 77/112 | 112 | $426.20 | 1,219,511,127 | 57.75h |
| 4 | Sol Xhigh | 102.2 | 76/112 | 112 | $641.21 | 813,188,283 | 45.62h |
| 5 | Gpt-5.5 Xhigh | 100.9 | 75/112 | 112 | $643.37 | 803,093,230 | 42.17h |
| 6 | Sol High | 98.2 | 73/112 | 112 | $519.61 | 579,701,889 | 35.10h |
| 7 | Terra Xhigh | 87.4 | 65/112 | 112 | $212.45 | 630,154,770 | 38.84h |
| 8 | Gpt-5.5 High | 84.7 | 63/112 | 112 | $400.02 | 505,295,934 | 32.06h |
| 9 | Terra High | 82.1 | 61/112 | 112 | $122.96 | 344,700,258 | 25.84h |
| 10 | Sol Low | 80.7 | 60/112 | 112 | $172.57 | 208,637,765 | 17.49h |
| 11 | Luna High | 72.6 | 54/112 | 112 | $22.51 | 728,334,900 | 33.41h |

## Interpretation

- The endpoint provides model-level `score`, pass counts, task counts, tokens, wall time, and estimated cost.
- It does not expose the ten task-level outcomes, so `Weighted /100` cannot be recomputed from this API summary alone.
- Task-weighted rankings remain based on the repository's task matrix and weight snapshots; this report monitors the latest API summary.
- When source data is unchanged, the automation still updates its heartbeat without presenting it as a new benchmark batch.
- The raw API response is not stored in the public repository; only required model-summary fields are archived.

Archived API snapshots: **374**.
