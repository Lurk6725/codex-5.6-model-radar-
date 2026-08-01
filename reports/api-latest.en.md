# Codex Radar API Monitor — English

[简体中文](api-latest.zh-CN.md) · [Project home](../README.md) · [API history CSV](../data/api/model_iq_history.csv) · [Monitor status](../data/api/monitor_status.json)

**Last successful check:** `2026-08-01T16:39:47+00:00`  
**Current API snapshot:** `5b8a0934d7e46bc2`  
**Source observation:** `2026-07-22T06:57:20.626603+08:00`  
**New snapshot detected:** yes  
**Models returned:** 11

> “Last successful check” confirms that the automation reached the API. “Source observation” is supplied by the upstream endpoint and may be older.

> This is a model-level summary from the Codex Radar API, not the project's task-level difficulty-weighted score.

## Current API model summary

| Rank | Model tier | Source score | Passed | Tasks | Cost | Total tokens | Wall time |
|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | Sol Xhigh | 98.2 | 73/112 | 112 | $770.96 | 1,001,985,367 | 47.14h |
| 2 | Gpt-5.5 Xhigh | 92.8 | 69/112 | 112 | $646.24 | 835,363,457 | 43.89h |
| 3 | Sol High | 87.4 | 65/112 | 112 | $609.32 | 800,747,608 | 41.36h |
| 4 | Terra Max | 87.4 | 65/112 | 112 | $529.99 | 1,519,676,372 | 57.11h |
| 5 | Sol Medium | 86.1 | 64/112 | 112 | $421.71 | 583,676,746 | 33.68h |
| 6 | Gpt-5.5 High | 79.4 | 59/112 | 112 | $415.21 | 533,551,635 | 32.58h |
| 7 | Luna Max | 76.7 | 57/112 | 112 | $133.77 | 1,785,637,068 | 56.40h |
| 8 | Terra High | 76.7 | 57/112 | 112 | $151.95 | 401,799,654 | 25.62h |
| 9 | Terra Xhigh | 75.3 | 56/112 | 112 | $271.82 | 737,807,833 | 35.20h |
| 10 | Sol Low | 71.3 | 53/112 | 112 | $250.06 | 288,450,870 | 21.18h |
| 11 | Luna High | 68.6 | 51/112 | 112 | $69.91 | 808,804,159 | 33.85h |

## Interpretation

- The endpoint provides model-level `score`, pass counts, task counts, tokens, wall time, and estimated cost.
- It does not expose the ten task-level outcomes, so `Weighted /100` cannot be recomputed from this API summary alone.
- Task-weighted rankings remain based on the repository's task matrix and weight snapshots; this report monitors the latest API summary.
- When source data is unchanged, the automation still updates its heartbeat without presenting it as a new benchmark batch.
- The raw API response is not stored in the public repository; only required model-summary fields are archived.

Archived API snapshots: **145**.
