# Codex Radar API Monitor — English

[简体中文](api-latest.zh-CN.md) · [Project home](../README.md) · [API history CSV](../data/api/model_iq_history.csv) · [Monitor status](../data/api/monitor_status.json)

**Last successful check:** `2026-08-03T12:02:24+00:00`  
**Current API snapshot:** `7ca8c820e469aaae`  
**Source observation:** `2026-07-22T06:57:20.626603+08:00`  
**New snapshot detected:** yes  
**Models returned:** 11

> “Last successful check” confirms that the automation reached the API. “Source observation” is supplied by the upstream endpoint and may be older.

> This is a model-level summary from the Codex Radar API, not the project's task-level difficulty-weighted score.

## Current API model summary

| Rank | Model tier | Source score | Passed | Tasks | Cost | Total tokens | Wall time |
|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | Sol Xhigh | 103.6 | 77/112 | 112 | $766.06 | 933,413,409 | 47.95h |
| 2 | Gpt-5.5 Xhigh | 99.5 | 74/112 | 112 | $657.09 | 821,877,951 | 44.12h |
| 3 | Luna Max | 98.2 | 73/112 | 112 | $59.12 | 1,770,073,743 | 61.99h |
| 4 | Terra Max | 95.5 | 71/112 | 112 | $502.86 | 1,496,845,053 | 58.80h |
| 5 | Sol Medium | 88.8 | 66/112 | 112 | $410.41 | 520,098,736 | 32.11h |
| 6 | Terra Xhigh | 86.1 | 64/112 | 112 | $248.48 | 634,200,006 | 34.56h |
| 7 | Gpt-5.5 High | 84.7 | 63/112 | 112 | $413.08 | 501,984,619 | 31.45h |
| 8 | Sol High | 82.1 | 61/112 | 112 | $590.77 | 749,932,579 | 42.26h |
| 9 | Sol Low | 75.3 | 56/112 | 112 | $234.67 | 247,821,145 | 20.62h |
| 10 | Terra High | 71.3 | 53/112 | 112 | $145.65 | 393,370,789 | 25.47h |
| 11 | Luna High | 68.6 | 51/112 | 112 | $41.63 | 744,983,710 | 30.85h |

## Interpretation

- The endpoint provides model-level `score`, pass counts, task counts, tokens, wall time, and estimated cost.
- It does not expose the ten task-level outcomes, so `Weighted /100` cannot be recomputed from this API summary alone.
- Task-weighted rankings remain based on the repository's task matrix and weight snapshots; this report monitors the latest API summary.
- When source data is unchanged, the automation still updates its heartbeat without presenting it as a new benchmark batch.
- The raw API response is not stored in the public repository; only required model-summary fields are archived.

Archived API snapshots: **163**.
