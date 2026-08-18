# Codex Radar API Monitor — English

[简体中文](api-latest.zh-CN.md) · [Project home](../README.md) · [API history CSV](../data/api/model_iq_history.csv) · [Monitor status](../data/api/monitor_status.json)

**Last successful check:** `2026-08-18T04:54:21+00:00`  
**Current API snapshot:** `99569cad38cd3f7c`  
**Source observation:** `2026-07-22T06:57:20.626603+08:00`  
**New snapshot detected:** yes  
**Models returned:** 11

> “Last successful check” confirms that the automation reached the API. “Source observation” is supplied by the upstream endpoint and may be older.

> This is a model-level summary from the Codex Radar API, not the project's task-level difficulty-weighted score.

## Current API model summary

| Rank | Model tier | Source score | Passed | Tasks | Cost | Total tokens | Wall time |
|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | Sol Xhigh | 98.2 | 73/112 | 112 | $729.49 | 847,993,324 | 45.36h |
| 2 | Terra Max | 98.2 | 73/112 | 112 | $436.02 | 1,267,992,433 | 59.52h |
| 3 | Gpt-5.5 Xhigh | 94.2 | 70/112 | 112 | $654.76 | 770,633,476 | 42.19h |
| 4 | Luna Max | 94.2 | 70/112 | 112 | $58.80 | 1,783,220,494 | 63.81h |
| 5 | Sol High | 91.5 | 68/112 | 112 | $538.15 | 640,471,302 | 36.17h |
| 6 | Gpt-5.5 High | 90.1 | 67/112 | 112 | $403.46 | 495,804,840 | 33.23h |
| 7 | Sol Medium | 84.7 | 63/112 | 112 | $392.17 | 488,309,629 | 33.95h |
| 8 | Terra Xhigh | 83.4 | 62/112 | 112 | $216.90 | 605,527,346 | 38.23h |
| 9 | Luna High | 76.7 | 57/112 | 112 | $26.15 | 767,237,037 | 35.14h |
| 10 | Terra High | 72.6 | 54/112 | 112 | $126.39 | 349,230,176 | 26.52h |
| 11 | Sol Low | 68.6 | 51/112 | 112 | $225.77 | 276,296,616 | 24.23h |

## Interpretation

- The endpoint provides model-level `score`, pass counts, task counts, tokens, wall time, and estimated cost.
- It does not expose the ten task-level outcomes, so `Weighted /100` cannot be recomputed from this API summary alone.
- Task-weighted rankings remain based on the repository's task matrix and weight snapshots; this report monitors the latest API summary.
- When source data is unchanged, the automation still updates its heartbeat without presenting it as a new benchmark batch.
- The raw API response is not stored in the public repository; only required model-summary fields are archived.

Archived API snapshots: **287**.
