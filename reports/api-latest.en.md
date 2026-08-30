# Codex Radar API Monitor — English

[简体中文](api-latest.zh-CN.md) · [Project home](../README.md) · [API history CSV](../data/api/model_iq_history.csv) · [Monitor status](../data/api/monitor_status.json)

**Last successful check:** `2026-08-30T22:06:51+00:00`  
**Current API snapshot:** `04394802a5ee030c`  
**Source observation:** `2026-08-30T20:01:21.823608+08:00`  
**New snapshot detected:** yes  
**Models returned:** 11

> “Last successful check” confirms that the automation reached the API. “Source observation” is supplied by the upstream endpoint and may be older.

> This is a model-level summary from the Codex Radar API, not the project's task-level difficulty-weighted score.

## Current API model summary

| Rank | Model tier | Source score | Passed | Tasks | Cost | Total tokens | Wall time |
|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | Terra Max | 104.9 | 78/112 | 112 | $423.64 | 1,218,744,543 | 57.48h |
| 2 | Luna Max | 103.6 | 77/112 | 112 | $54.10 | 2,024,015,527 | 72.54h |
| 3 | Sol High | 102.2 | 76/112 | 112 | $487.63 | 590,069,136 | 36.23h |
| 4 | Sol Xhigh | 100.9 | 75/112 | 112 | $592.54 | 806,961,625 | 43.58h |
| 5 | Gpt-5.5 Xhigh | 98.2 | 73/112 | 112 | $639.26 | 878,194,519 | 43.24h |
| 6 | Sol Medium | 96.9 | 72/112 | 112 | $312.59 | 426,945,526 | 27.74h |
| 7 | Gpt-5.5 High | 87.4 | 65/112 | 112 | $397.68 | 528,229,497 | 27.95h |
| 8 | Terra Xhigh | 86.1 | 64/112 | 112 | $211.87 | 590,665,128 | 36.78h |
| 9 | Sol Low | 80.7 | 60/112 | 112 | $171.47 | 214,050,549 | 16.83h |
| 10 | Terra High | 76.7 | 57/112 | 112 | $122.31 | 342,350,867 | 25.53h |
| 11 | Luna High | 68.6 | 51/112 | 112 | $22.47 | 805,751,921 | 34.38h |

## Interpretation

- The endpoint provides model-level `score`, pass counts, task counts, tokens, wall time, and estimated cost.
- It does not expose the ten task-level outcomes, so `Weighted /100` cannot be recomputed from this API summary alone.
- Task-weighted rankings remain based on the repository's task matrix and weight snapshots; this report monitors the latest API summary.
- When source data is unchanged, the automation still updates its heartbeat without presenting it as a new benchmark batch.
- The raw API response is not stored in the public repository; only required model-summary fields are archived.

Archived API snapshots: **383**.
