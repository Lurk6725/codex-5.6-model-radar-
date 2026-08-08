# Codex Radar API Monitor — English

[简体中文](api-latest.zh-CN.md) · [Project home](../README.md) · [API history CSV](../data/api/model_iq_history.csv) · [Monitor status](../data/api/monitor_status.json)

**Last successful check:** `2026-08-08T14:18:13+00:00`  
**Current API snapshot:** `33c63e1648a719f6`  
**Source observation:** `2026-07-22T06:57:20.626603+08:00`  
**New snapshot detected:** no; the source returned the same snapshot  
**Models returned:** 11

> “Last successful check” confirms that the automation reached the API. “Source observation” is supplied by the upstream endpoint and may be older.

> This is a model-level summary from the Codex Radar API, not the project's task-level difficulty-weighted score.

## Current API model summary

| Rank | Model tier | Source score | Passed | Tasks | Cost | Total tokens | Wall time |
|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | Sol Xhigh | 106.3 | 79/112 | 112 | $751.42 | 909,978,782 | 47.08h |
| 2 | Luna Max | 96.9 | 72/112 | 112 | $58.73 | 1,795,576,445 | 62.44h |
| 3 | Gpt-5.5 Xhigh | 94.2 | 70/112 | 112 | $654.91 | 787,042,180 | 40.70h |
| 4 | Sol High | 94.2 | 70/112 | 112 | $581.96 | 620,587,465 | 36.56h |
| 5 | Sol Medium | 92.8 | 69/112 | 112 | $410.93 | 547,358,062 | 32.21h |
| 6 | Gpt-5.5 High | 91.5 | 68/112 | 112 | $407.59 | 494,874,645 | 32.16h |
| 7 | Terra Max | 90.1 | 67/112 | 112 | $448.60 | 1,372,920,729 | 57.58h |
| 8 | Sol Low | 86.1 | 64/112 | 112 | $230.17 | 267,876,922 | 22.62h |
| 9 | Terra Xhigh | 79.4 | 59/112 | 112 | $226.33 | 643,791,683 | 37.07h |
| 10 | Terra High | 76.7 | 57/112 | 112 | $128.53 | 337,949,051 | 23.64h |
| 11 | Luna High | 72.6 | 54/112 | 112 | $26.09 | 729,671,283 | 32.21h |

## Interpretation

- The endpoint provides model-level `score`, pass counts, task counts, tokens, wall time, and estimated cost.
- It does not expose the ten task-level outcomes, so `Weighted /100` cannot be recomputed from this API summary alone.
- Task-weighted rankings remain based on the repository's task matrix and weight snapshots; this report monitors the latest API summary.
- When source data is unchanged, the automation still updates its heartbeat without presenting it as a new benchmark batch.
- The raw API response is not stored in the public repository; only required model-summary fields are archived.

Archived API snapshots: **204**.
