# Codex Radar API Monitor — English

[简体中文](api-latest.zh-CN.md) · [Project home](../README.md) · [API history CSV](../data/api/model_iq_history.csv) · [Monitor status](../data/api/monitor_status.json)

**Last successful check:** `2026-08-23T10:43:48+00:00`  
**Current API snapshot:** `4f98982e25f5bc21`  
**Source observation:** `2026-07-22T06:57:20.626603+08:00`  
**New snapshot detected:** no; the source returned the same snapshot  
**Models returned:** 11

> “Last successful check” confirms that the automation reached the API. “Source observation” is supplied by the upstream endpoint and may be older.

> This is a model-level summary from the Codex Radar API, not the project's task-level difficulty-weighted score.

## Current API model summary

| Rank | Model tier | Source score | Passed | Tasks | Cost | Total tokens | Wall time |
|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | Sol Xhigh | 102.2 | 76/112 | 112 | $722.51 | 842,077,143 | 43.68h |
| 2 | Gpt-5.5 Xhigh | 98.2 | 73/112 | 112 | $652.21 | 777,214,772 | 42.16h |
| 3 | Terra Max | 95.5 | 71/112 | 112 | $431.74 | 1,179,118,065 | 56.47h |
| 4 | Gpt-5.5 High | 92.8 | 69/112 | 112 | $401.48 | 527,750,911 | 34.26h |
| 5 | Luna Max | 86.1 | 64/112 | 112 | $54.41 | 1,703,218,758 | 59.67h |
| 6 | Sol High | 86.1 | 64/112 | 112 | $534.11 | 585,033,307 | 35.73h |
| 7 | Terra Xhigh | 84.7 | 63/112 | 112 | $213.79 | 580,140,602 | 37.05h |
| 8 | Sol Medium | 83.4 | 62/112 | 112 | $404.84 | 462,003,596 | 33.58h |
| 9 | Luna High | 76.7 | 57/112 | 112 | $22.64 | 684,439,628 | 30.09h |
| 10 | Terra High | 74 | 55/112 | 112 | $124.91 | 335,190,382 | 24.83h |
| 11 | Sol Low | 72.6 | 54/112 | 112 | $223.26 | 261,529,059 | 23.91h |

## Interpretation

- The endpoint provides model-level `score`, pass counts, task counts, tokens, wall time, and estimated cost.
- It does not expose the ten task-level outcomes, so `Weighted /100` cannot be recomputed from this API summary alone.
- Task-weighted rankings remain based on the repository's task matrix and weight snapshots; this report monitors the latest API summary.
- When source data is unchanged, the automation still updates its heartbeat without presenting it as a new benchmark batch.
- The raw API response is not stored in the public repository; only required model-summary fields are archived.

Archived API snapshots: **330**.
