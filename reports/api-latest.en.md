# Codex Radar API Monitor — English

[简体中文](api-latest.zh-CN.md) · [Project home](../README.md) · [API history CSV](../data/api/model_iq_history.csv) · [Monitor status](../data/api/monitor_status.json)

**Last successful check:** `2026-08-30T11:58:59+00:00`  
**Current API snapshot:** `384480696925ecf3`  
**Source observation:** `2026-08-30T17:57:08.624495+08:00`  
**New snapshot detected:** yes  
**Models returned:** 11

> “Last successful check” confirms that the automation reached the API. “Source observation” is supplied by the upstream endpoint and may be older.

> This is a model-level summary from the Codex Radar API, not the project's task-level difficulty-weighted score.

## Current API model summary

| Rank | Model tier | Source score | Passed | Tasks | Cost | Total tokens | Wall time |
|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | Luna Max | 104.9 | 78/112 | 112 | $54.08 | 1,989,164,146 | 71.86h |
| 2 | Terra Max | 104.9 | 78/112 | 112 | $425.07 | 1,203,326,471 | 57.15h |
| 3 | Gpt-5.5 Xhigh | 99.5 | 74/112 | 112 | $639.52 | 848,195,764 | 42.21h |
| 4 | Sol High | 98.2 | 73/112 | 112 | $492.99 | 589,574,120 | 35.65h |
| 5 | Sol Medium | 96.9 | 72/112 | 112 | $312.62 | 423,753,006 | 27.63h |
| 6 | Sol Xhigh | 96.9 | 72/112 | 112 | $610.04 | 833,718,724 | 44.61h |
| 7 | Gpt-5.5 High | 87.4 | 65/112 | 112 | $397.67 | 527,586,653 | 27.93h |
| 8 | Terra Xhigh | 83.4 | 62/112 | 112 | $211.96 | 587,876,312 | 36.56h |
| 9 | Sol Low | 80.7 | 60/112 | 112 | $171.60 | 214,150,773 | 16.62h |
| 10 | Terra High | 80.7 | 60/112 | 112 | $122.48 | 344,181,958 | 25.51h |
| 11 | Luna High | 68.6 | 51/112 | 112 | $22.49 | 787,066,485 | 33.83h |

## Interpretation

- The endpoint provides model-level `score`, pass counts, task counts, tokens, wall time, and estimated cost.
- It does not expose the ten task-level outcomes, so `Weighted /100` cannot be recomputed from this API summary alone.
- Task-weighted rankings remain based on the repository's task matrix and weight snapshots; this report monitors the latest API summary.
- When source data is unchanged, the automation still updates its heartbeat without presenting it as a new benchmark batch.
- The raw API response is not stored in the public repository; only required model-summary fields are archived.

Archived API snapshots: **380**.
