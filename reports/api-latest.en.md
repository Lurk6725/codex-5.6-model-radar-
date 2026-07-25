# Codex Radar API Monitor — English

[简体中文](api-latest.zh-CN.md) · [Project home](../README.md) · [API history CSV](../data/api/model_iq_history.csv) · [Monitor status](../data/api/monitor_status.json)

**Last successful check:** `2026-07-25T22:12:16+00:00`  
**Current API snapshot:** `efbcbd3ba87b3d0d`  
**Source observation:** `2026-07-22T06:57:20.626603+08:00`  
**New snapshot detected:** no; the source returned the same snapshot  
**Models returned:** 11

> “Last successful check” confirms that the automation reached the API. “Source observation” is supplied by the upstream endpoint and may be older.

> This is a model-level summary from the Codex Radar API, not the project's task-level difficulty-weighted score.

## Current API model summary

| Rank | Model tier | Source score | Passed | Tasks | Cost | Total tokens | Wall time |
|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | Sol Xhigh | 96.9 | 72/112 | 112 | $786.04 | 1,072,835,239 | 47.38h |
| 2 | Sol Medium | 95.5 | 71/112 | 112 | $440.84 | 566,479,480 | 30.70h |
| 3 | Sol High | 92.8 | 69/112 | 112 | $577.57 | 765,718,354 | 34.38h |
| 4 | Terra Max | 90.1 | 67/112 | 112 | $566.48 | 1,491,877,474 | 58.46h |
| 5 | Terra Xhigh | 87.4 | 65/112 | 112 | $281.54 | 681,878,965 | 36.40h |
| 6 | Luna Max | 84.7 | 63/112 | 112 | $287.68 | 1,989,775,433 | 61.36h |
| 7 | Gpt-5.5 Xhigh | 83.4 | 62/112 | 112 | $649.92 | 834,310,464 | 44.35h |
| 8 | Gpt-5.5 High | 79.4 | 59/112 | 112 | $417.12 | 521,716,482 | 32.03h |
| 9 | Sol Low | 75.3 | 56/112 | 112 | $231.98 | 263,333,397 | 20.03h |
| 10 | Terra High | 71.3 | 53/112 | 112 | $157.72 | 358,844,339 | 23.42h |
| 11 | Luna High | 65.9 | 49/112 | 112 | $114.65 | 739,486,330 | 32.18h |

## Interpretation

- The endpoint provides model-level `score`, pass counts, task counts, tokens, wall time, and estimated cost.
- It does not expose the ten task-level outcomes, so `Weighted /100` cannot be recomputed from this API summary alone.
- Task-weighted rankings remain based on the repository's task matrix and weight snapshots; this report monitors the latest API summary.
- When source data is unchanged, the automation still updates its heartbeat without presenting it as a new benchmark batch.
- The raw API response is not stored in the public repository; only required model-summary fields are archived.

Archived API snapshots: **84**.
