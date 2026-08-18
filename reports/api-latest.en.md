# Codex Radar API Monitor — English

[简体中文](api-latest.zh-CN.md) · [Project home](../README.md) · [API history CSV](../data/api/model_iq_history.csv) · [Monitor status](../data/api/monitor_status.json)

**Last successful check:** `2026-08-18T07:56:08+00:00`  
**Current API snapshot:** `fc062c89003333d7`  
**Source observation:** `2026-07-22T06:57:20.626603+08:00`  
**New snapshot detected:** no; the source returned the same snapshot  
**Models returned:** 11

> “Last successful check” confirms that the automation reached the API. “Source observation” is supplied by the upstream endpoint and may be older.

> This is a model-level summary from the Codex Radar API, not the project's task-level difficulty-weighted score.

## Current API model summary

| Rank | Model tier | Source score | Passed | Tasks | Cost | Total tokens | Wall time |
|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | Terra Max | 99.5 | 74/112 | 112 | $436.20 | 1,267,334,223 | 60.09h |
| 2 | Sol Xhigh | 98.2 | 73/112 | 112 | $729.57 | 846,042,232 | 45.24h |
| 3 | Gpt-5.5 Xhigh | 94.2 | 70/112 | 112 | $654.68 | 768,828,555 | 42.21h |
| 4 | Luna Max | 94.2 | 70/112 | 112 | $58.81 | 1,784,176,549 | 63.81h |
| 5 | Sol High | 91.5 | 68/112 | 112 | $538.14 | 639,022,620 | 36.42h |
| 6 | Gpt-5.5 High | 90.1 | 67/112 | 112 | $403.46 | 495,804,840 | 33.23h |
| 7 | Sol Medium | 84.7 | 63/112 | 112 | $392.17 | 488,309,629 | 33.95h |
| 8 | Terra Xhigh | 83.4 | 62/112 | 112 | $216.96 | 604,206,036 | 38.54h |
| 9 | Luna High | 75.3 | 56/112 | 112 | $26.13 | 767,486,203 | 34.81h |
| 10 | Terra High | 74 | 55/112 | 112 | $126.37 | 348,564,925 | 26.65h |
| 11 | Sol Low | 68.6 | 51/112 | 112 | $225.77 | 276,296,616 | 24.23h |

## Interpretation

- The endpoint provides model-level `score`, pass counts, task counts, tokens, wall time, and estimated cost.
- It does not expose the ten task-level outcomes, so `Weighted /100` cannot be recomputed from this API summary alone.
- Task-weighted rankings remain based on the repository's task matrix and weight snapshots; this report monitors the latest API summary.
- When source data is unchanged, the automation still updates its heartbeat without presenting it as a new benchmark batch.
- The raw API response is not stored in the public repository; only required model-summary fields are archived.

Archived API snapshots: **288**.
