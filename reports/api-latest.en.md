# Codex Radar API Monitor — English

[简体中文](api-latest.zh-CN.md) · [Project home](../README.md) · [API history CSV](../data/api/model_iq_history.csv) · [Monitor status](../data/api/monitor_status.json)

**Last successful check:** `2026-08-13T09:49:43+00:00`  
**Current API snapshot:** `972cf9023f94d3f8`  
**Source observation:** `2026-07-22T06:57:20.626603+08:00`  
**New snapshot detected:** no; the source returned the same snapshot  
**Models returned:** 11

> “Last successful check” confirms that the automation reached the API. “Source observation” is supplied by the upstream endpoint and may be older.

> This is a model-level summary from the Codex Radar API, not the project's task-level difficulty-weighted score.

## Current API model summary

| Rank | Model tier | Source score | Passed | Tasks | Cost | Total tokens | Wall time |
|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | Terra Max | 102.2 | 76/112 | 112 | $435.07 | 1,228,974,679 | 58.70h |
| 2 | Luna Max | 99.5 | 74/112 | 112 | $58.59 | 1,886,657,734 | 67.47h |
| 3 | Sol Xhigh | 99.5 | 74/112 | 112 | $726.52 | 840,755,853 | 44.87h |
| 4 | Gpt-5.5 Xhigh | 94.2 | 70/112 | 112 | $656.94 | 712,717,654 | 41.17h |
| 5 | Gpt-5.5 High | 91.5 | 68/112 | 112 | $403.92 | 494,955,104 | 33.27h |
| 6 | Sol High | 88.8 | 66/112 | 112 | $538.03 | 648,238,871 | 36.85h |
| 7 | Sol Medium | 88.8 | 66/112 | 112 | $382.88 | 447,515,464 | 31.56h |
| 8 | Terra Xhigh | 83.4 | 62/112 | 112 | $217.51 | 595,380,202 | 37.02h |
| 9 | Terra High | 76.7 | 57/112 | 112 | $126.57 | 339,389,162 | 25.78h |
| 10 | Luna High | 74 | 55/112 | 112 | $26.16 | 784,501,418 | 35.71h |
| 11 | Sol Low | 70 | 52/112 | 112 | $225.52 | 281,920,773 | 23.52h |

## Interpretation

- The endpoint provides model-level `score`, pass counts, task counts, tokens, wall time, and estimated cost.
- It does not expose the ten task-level outcomes, so `Weighted /100` cannot be recomputed from this API summary alone.
- Task-weighted rankings remain based on the repository's task matrix and weight snapshots; this report monitors the latest API summary.
- When source data is unchanged, the automation still updates its heartbeat without presenting it as a new benchmark batch.
- The raw API response is not stored in the public repository; only required model-summary fields are archived.

Archived API snapshots: **252**.
