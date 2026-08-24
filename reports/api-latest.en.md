# Codex Radar API Monitor — English

[简体中文](api-latest.zh-CN.md) · [Project home](../README.md) · [API history CSV](../data/api/model_iq_history.csv) · [Monitor status](../data/api/monitor_status.json)

**Last successful check:** `2026-08-24T17:17:19+00:00`  
**Current API snapshot:** `bd46c403b5a8211b`  
**Source observation:** `2026-07-22T06:57:20.626603+08:00`  
**New snapshot detected:** no; the source returned the same snapshot  
**Models returned:** 11

> “Last successful check” confirms that the automation reached the API. “Source observation” is supplied by the upstream endpoint and may be older.

> This is a model-level summary from the Codex Radar API, not the project's task-level difficulty-weighted score.

## Current API model summary

| Rank | Model tier | Source score | Passed | Tasks | Cost | Total tokens | Wall time |
|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | Sol Xhigh | 104.9 | 78/112 | 112 | $713.06 | 806,295,391 | 45.22h |
| 2 | Gpt-5.5 Xhigh | 99.5 | 74/112 | 112 | $648.58 | 772,565,312 | 40.45h |
| 3 | Luna Max | 98.2 | 73/112 | 112 | $54.35 | 1,645,772,933 | 56.74h |
| 4 | Terra Max | 95.5 | 71/112 | 112 | $425.52 | 1,161,065,574 | 54.82h |
| 5 | Gpt-5.5 High | 88.8 | 66/112 | 112 | $400.49 | 496,314,317 | 31.82h |
| 6 | Sol High | 86.1 | 64/112 | 112 | $530.43 | 572,020,545 | 34.65h |
| 7 | Terra Xhigh | 86.1 | 64/112 | 112 | $212.52 | 595,955,880 | 36.35h |
| 8 | Sol Medium | 82.1 | 61/112 | 112 | $402.39 | 445,166,718 | 31.58h |
| 9 | Terra High | 75.3 | 56/112 | 112 | $124.35 | 327,377,512 | 24.56h |
| 10 | Luna High | 74 | 55/112 | 112 | $22.48 | 702,020,476 | 31.93h |
| 11 | Sol Low | 72.6 | 54/112 | 112 | $222.41 | 254,308,848 | 22.27h |

## Interpretation

- The endpoint provides model-level `score`, pass counts, task counts, tokens, wall time, and estimated cost.
- It does not expose the ten task-level outcomes, so `Weighted /100` cannot be recomputed from this API summary alone.
- Task-weighted rankings remain based on the repository's task matrix and weight snapshots; this report monitors the latest API summary.
- When source data is unchanged, the automation still updates its heartbeat without presenting it as a new benchmark batch.
- The raw API response is not stored in the public repository; only required model-summary fields are archived.

Archived API snapshots: **345**.
