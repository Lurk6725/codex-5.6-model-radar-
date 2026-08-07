# Codex Radar API Monitor — English

[简体中文](api-latest.zh-CN.md) · [Project home](../README.md) · [API history CSV](../data/api/model_iq_history.csv) · [Monitor status](../data/api/monitor_status.json)

**Last successful check:** `2026-08-07T12:30:18+00:00`  
**Current API snapshot:** `07118a60f1c41ad3`  
**Source observation:** `2026-07-22T06:57:20.626603+08:00`  
**New snapshot detected:** no; the source returned the same snapshot  
**Models returned:** 11

> “Last successful check” confirms that the automation reached the API. “Source observation” is supplied by the upstream endpoint and may be older.

> This is a model-level summary from the Codex Radar API, not the project's task-level difficulty-weighted score.

## Current API model summary

| Rank | Model tier | Source score | Passed | Tasks | Cost | Total tokens | Wall time |
|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | Sol Xhigh | 106.3 | 79/112 | 112 | $755.64 | 961,336,862 | 48.23h |
| 2 | Gpt-5.5 High | 95.5 | 71/112 | 112 | $407.73 | 496,713,612 | 33.33h |
| 3 | Gpt-5.5 Xhigh | 95.5 | 71/112 | 112 | $649.00 | 808,542,276 | 41.87h |
| 4 | Luna Max | 95.5 | 71/112 | 112 | $58.85 | 1,782,877,649 | 61.45h |
| 5 | Sol High | 92.8 | 69/112 | 112 | $583.43 | 670,665,804 | 39.06h |
| 6 | Terra Max | 92.8 | 69/112 | 112 | $454.34 | 1,498,430,509 | 62.67h |
| 7 | Sol Medium | 91.5 | 68/112 | 112 | $409.41 | 536,355,782 | 32.00h |
| 8 | Terra Xhigh | 86.1 | 64/112 | 112 | $227.09 | 631,825,249 | 36.49h |
| 9 | Luna High | 82.1 | 61/112 | 112 | $26.79 | 736,110,335 | 31.30h |
| 10 | Sol Low | 82.1 | 61/112 | 112 | $232.72 | 263,989,940 | 22.95h |
| 11 | Terra High | 79.4 | 59/112 | 112 | $130.51 | 350,848,498 | 24.89h |

## Interpretation

- The endpoint provides model-level `score`, pass counts, task counts, tokens, wall time, and estimated cost.
- It does not expose the ten task-level outcomes, so `Weighted /100` cannot be recomputed from this API summary alone.
- Task-weighted rankings remain based on the repository's task matrix and weight snapshots; this report monitors the latest API summary.
- When source data is unchanged, the automation still updates its heartbeat without presenting it as a new benchmark batch.
- The raw API response is not stored in the public repository; only required model-summary fields are archived.

Archived API snapshots: **191**.
