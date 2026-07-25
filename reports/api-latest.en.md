# Codex Radar API Monitor — English

[简体中文](api-latest.zh-CN.md) · [Project home](../README.md) · [API history CSV](../data/api/model_iq_history.csv) · [Monitor status](../data/api/monitor_status.json)

**Last successful check:** `2026-07-25T23:15:38+00:00`  
**Current API snapshot:** `add2a3bc8195dd94`  
**Source observation:** `2026-07-22T06:57:20.626603+08:00`  
**New snapshot detected:** yes  
**Models returned:** 11

> “Last successful check” confirms that the automation reached the API. “Source observation” is supplied by the upstream endpoint and may be older.

> This is a model-level summary from the Codex Radar API, not the project's task-level difficulty-weighted score.

## Current API model summary

| Rank | Model tier | Source score | Passed | Tasks | Cost | Total tokens | Wall time |
|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | Sol Xhigh | 96.9 | 72/112 | 112 | $785.81 | 1,072,071,302 | 47.50h |
| 2 | Sol Medium | 94.2 | 70/112 | 112 | $443.18 | 570,811,103 | 30.33h |
| 3 | Sol High | 92.8 | 69/112 | 112 | $577.76 | 766,863,012 | 34.26h |
| 4 | Terra Max | 90.1 | 67/112 | 112 | $564.61 | 1,484,901,971 | 58.13h |
| 5 | Terra Xhigh | 87.4 | 65/112 | 112 | $281.97 | 683,323,480 | 36.30h |
| 6 | Gpt-5.5 Xhigh | 84.7 | 63/112 | 112 | $647.52 | 831,879,518 | 43.41h |
| 7 | Luna Max | 84.7 | 63/112 | 112 | $285.70 | 1,975,903,997 | 61.13h |
| 8 | Gpt-5.5 High | 80.7 | 60/112 | 112 | $415.82 | 519,746,118 | 31.70h |
| 9 | Sol Low | 74 | 55/112 | 112 | $232.42 | 263,394,958 | 19.83h |
| 10 | Terra High | 72.6 | 54/112 | 112 | $156.40 | 354,779,379 | 23.26h |
| 11 | Luna High | 67.3 | 50/112 | 112 | $114.91 | 741,387,720 | 32.17h |

## Interpretation

- The endpoint provides model-level `score`, pass counts, task counts, tokens, wall time, and estimated cost.
- It does not expose the ten task-level outcomes, so `Weighted /100` cannot be recomputed from this API summary alone.
- Task-weighted rankings remain based on the repository's task matrix and weight snapshots; this report monitors the latest API summary.
- When source data is unchanged, the automation still updates its heartbeat without presenting it as a new benchmark batch.
- The raw API response is not stored in the public repository; only required model-summary fields are archived.

Archived API snapshots: **85**.
