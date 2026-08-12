# Codex Radar API Monitor — English

[简体中文](api-latest.zh-CN.md) · [Project home](../README.md) · [API history CSV](../data/api/model_iq_history.csv) · [Monitor status](../data/api/monitor_status.json)

**Last successful check:** `2026-08-12T11:34:37+00:00`  
**Current API snapshot:** `b3ba3a615bdf9619`  
**Source observation:** `2026-07-22T06:57:20.626603+08:00`  
**New snapshot detected:** no; the source returned the same snapshot  
**Models returned:** 11

> “Last successful check” confirms that the automation reached the API. “Source observation” is supplied by the upstream endpoint and may be older.

> This is a model-level summary from the Codex Radar API, not the project's task-level difficulty-weighted score.

## Current API model summary

| Rank | Model tier | Source score | Passed | Tasks | Cost | Total tokens | Wall time |
|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | Terra Max | 104.9 | 78/112 | 112 | $437.06 | 1,231,640,299 | 57.13h |
| 2 | Sol Xhigh | 103.6 | 77/112 | 112 | $734.02 | 897,052,726 | 48.41h |
| 3 | Sol High | 100.9 | 75/112 | 112 | $561.88 | 685,391,632 | 37.83h |
| 4 | Luna Max | 99.5 | 74/112 | 112 | $58.56 | 1,867,326,431 | 66.93h |
| 5 | Gpt-5.5 Xhigh | 94.2 | 70/112 | 112 | $657.09 | 722,623,276 | 40.12h |
| 6 | Sol Medium | 94.2 | 70/112 | 112 | $407.66 | 471,222,674 | 31.51h |
| 7 | Gpt-5.5 High | 87.4 | 65/112 | 112 | $404.14 | 492,858,809 | 32.32h |
| 8 | Terra Xhigh | 86.1 | 64/112 | 112 | $218.33 | 584,214,412 | 35.79h |
| 9 | Terra High | 82.1 | 61/112 | 112 | $126.91 | 347,215,688 | 24.40h |
| 10 | Sol Low | 76.7 | 57/112 | 112 | $228.84 | 271,918,887 | 22.45h |
| 11 | Luna High | 67.3 | 50/112 | 112 | $26.20 | 765,945,745 | 34.54h |

## Interpretation

- The endpoint provides model-level `score`, pass counts, task counts, tokens, wall time, and estimated cost.
- It does not expose the ten task-level outcomes, so `Weighted /100` cannot be recomputed from this API summary alone.
- Task-weighted rankings remain based on the repository's task matrix and weight snapshots; this report monitors the latest API summary.
- When source data is unchanged, the automation still updates its heartbeat without presenting it as a new benchmark batch.
- The raw API response is not stored in the public repository; only required model-summary fields are archived.

Archived API snapshots: **242**.
