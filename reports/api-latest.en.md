# Codex Radar API Monitor — English

[简体中文](api-latest.zh-CN.md) · [Project home](../README.md) · [API history CSV](../data/api/model_iq_history.csv) · [Monitor status](../data/api/monitor_status.json)

**Last successful check:** `2026-08-07T22:19:14+00:00`  
**Current API snapshot:** `5c0c912feddebf97`  
**Source observation:** `2026-07-22T06:57:20.626603+08:00`  
**New snapshot detected:** no; the source returned the same snapshot  
**Models returned:** 11

> “Last successful check” confirms that the automation reached the API. “Source observation” is supplied by the upstream endpoint and may be older.

> This is a model-level summary from the Codex Radar API, not the project's task-level difficulty-weighted score.

## Current API model summary

| Rank | Model tier | Source score | Passed | Tasks | Cost | Total tokens | Wall time |
|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | Sol Xhigh | 106.3 | 79/112 | 112 | $755.46 | 961,013,760 | 48.02h |
| 2 | Luna Max | 96.9 | 72/112 | 112 | $58.70 | 1,812,992,734 | 62.93h |
| 3 | Gpt-5.5 Xhigh | 94.2 | 70/112 | 112 | $648.80 | 812,132,358 | 41.97h |
| 4 | Gpt-5.5 High | 92.8 | 69/112 | 112 | $408.56 | 497,531,959 | 33.31h |
| 5 | Sol Medium | 91.5 | 68/112 | 112 | $409.10 | 539,436,300 | 32.25h |
| 6 | Sol High | 90.1 | 67/112 | 112 | $583.01 | 644,046,647 | 38.33h |
| 7 | Terra Max | 90.1 | 67/112 | 112 | $456.33 | 1,440,459,578 | 60.70h |
| 8 | Luna High | 82.1 | 61/112 | 112 | $26.47 | 744,520,077 | 31.39h |
| 9 | Sol Low | 82.1 | 61/112 | 112 | $231.51 | 266,230,523 | 23.08h |
| 10 | Terra Xhigh | 82.1 | 61/112 | 112 | $227.03 | 634,936,413 | 36.35h |
| 11 | Terra High | 78 | 58/112 | 112 | $129.64 | 352,433,795 | 24.96h |

## Interpretation

- The endpoint provides model-level `score`, pass counts, task counts, tokens, wall time, and estimated cost.
- It does not expose the ten task-level outcomes, so `Weighted /100` cannot be recomputed from this API summary alone.
- Task-weighted rankings remain based on the repository's task matrix and weight snapshots; this report monitors the latest API summary.
- When source data is unchanged, the automation still updates its heartbeat without presenting it as a new benchmark batch.
- The raw API response is not stored in the public repository; only required model-summary fields are archived.

Archived API snapshots: **196**.
