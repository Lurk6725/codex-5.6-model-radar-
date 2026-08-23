# Codex Radar API Monitor — English

[简体中文](api-latest.zh-CN.md) · [Project home](../README.md) · [API history CSV](../data/api/model_iq_history.csv) · [Monitor status](../data/api/monitor_status.json)

**Last successful check:** `2026-08-23T23:01:00+00:00`  
**Current API snapshot:** `cad2675d1cfb7412`  
**Source observation:** `2026-07-22T06:57:20.626603+08:00`  
**New snapshot detected:** no; the source returned the same snapshot  
**Models returned:** 11

> “Last successful check” confirms that the automation reached the API. “Source observation” is supplied by the upstream endpoint and may be older.

> This is a model-level summary from the Codex Radar API, not the project's task-level difficulty-weighted score.

## Current API model summary

| Rank | Model tier | Source score | Passed | Tasks | Cost | Total tokens | Wall time |
|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | Sol Xhigh | 100.9 | 75/112 | 112 | $717.35 | 804,967,153 | 43.01h |
| 2 | Gpt-5.5 Xhigh | 98.2 | 73/112 | 112 | $650.20 | 779,169,976 | 40.66h |
| 3 | Terra Max | 95.5 | 71/112 | 112 | $426.10 | 1,162,069,554 | 55.06h |
| 4 | Gpt-5.5 High | 92.8 | 69/112 | 112 | $400.85 | 498,126,737 | 32.35h |
| 5 | Luna Max | 88.8 | 66/112 | 112 | $54.40 | 1,705,720,003 | 58.12h |
| 6 | Sol High | 87.4 | 65/112 | 112 | $531.50 | 567,320,758 | 34.57h |
| 7 | Terra Xhigh | 86.1 | 64/112 | 112 | $213.16 | 583,461,987 | 35.95h |
| 8 | Sol Medium | 80.7 | 60/112 | 112 | $403.12 | 448,516,891 | 31.85h |
| 9 | Luna High | 76.7 | 57/112 | 112 | $22.64 | 701,016,690 | 30.02h |
| 10 | Terra High | 76.7 | 57/112 | 112 | $124.76 | 334,774,221 | 24.38h |
| 11 | Sol Low | 74 | 55/112 | 112 | $222.56 | 251,007,355 | 22.39h |

## Interpretation

- The endpoint provides model-level `score`, pass counts, task counts, tokens, wall time, and estimated cost.
- It does not expose the ten task-level outcomes, so `Weighted /100` cannot be recomputed from this API summary alone.
- Task-weighted rankings remain based on the repository's task matrix and weight snapshots; this report monitors the latest API summary.
- When source data is unchanged, the automation still updates its heartbeat without presenting it as a new benchmark batch.
- The raw API response is not stored in the public repository; only required model-summary fields are archived.

Archived API snapshots: **336**.
