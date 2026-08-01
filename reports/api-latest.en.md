# Codex Radar API Monitor — English

[简体中文](api-latest.zh-CN.md) · [Project home](../README.md) · [API history CSV](../data/api/model_iq_history.csv) · [Monitor status](../data/api/monitor_status.json)

**Last successful check:** `2026-08-01T17:45:08+00:00`  
**Current API snapshot:** `8ba78a744cc7c440`  
**Source observation:** `2026-07-22T06:57:20.626603+08:00`  
**New snapshot detected:** yes  
**Models returned:** 11

> “Last successful check” confirms that the automation reached the API. “Source observation” is supplied by the upstream endpoint and may be older.

> This is a model-level summary from the Codex Radar API, not the project's task-level difficulty-weighted score.

## Current API model summary

| Rank | Model tier | Source score | Passed | Tasks | Cost | Total tokens | Wall time |
|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | Sol Xhigh | 98.2 | 73/112 | 112 | $771.84 | 1,000,746,285 | 47.19h |
| 2 | Gpt-5.5 Xhigh | 92.8 | 69/112 | 112 | $647.22 | 834,154,793 | 43.72h |
| 3 | Sol High | 87.4 | 65/112 | 112 | $608.56 | 801,863,457 | 41.45h |
| 4 | Sol Medium | 86.1 | 64/112 | 112 | $421.00 | 581,068,733 | 33.62h |
| 5 | Terra Max | 86.1 | 64/112 | 112 | $529.63 | 1,518,621,248 | 57.16h |
| 6 | Gpt-5.5 High | 79.4 | 59/112 | 112 | $416.57 | 535,386,092 | 32.75h |
| 7 | Luna Max | 76.7 | 57/112 | 112 | $119.73 | 1,809,312,616 | 56.84h |
| 8 | Terra High | 76.7 | 57/112 | 112 | $151.44 | 401,053,895 | 25.62h |
| 9 | Terra Xhigh | 75.3 | 56/112 | 112 | $271.45 | 736,266,777 | 35.04h |
| 10 | Sol Low | 72.6 | 54/112 | 112 | $249.52 | 286,409,466 | 21.10h |
| 11 | Luna High | 70 | 52/112 | 112 | $69.90 | 810,113,511 | 33.79h |

## Interpretation

- The endpoint provides model-level `score`, pass counts, task counts, tokens, wall time, and estimated cost.
- It does not expose the ten task-level outcomes, so `Weighted /100` cannot be recomputed from this API summary alone.
- Task-weighted rankings remain based on the repository's task matrix and weight snapshots; this report monitors the latest API summary.
- When source data is unchanged, the automation still updates its heartbeat without presenting it as a new benchmark batch.
- The raw API response is not stored in the public repository; only required model-summary fields are archived.

Archived API snapshots: **146**.
