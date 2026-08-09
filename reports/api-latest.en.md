# Codex Radar API Monitor — English

[简体中文](api-latest.zh-CN.md) · [Project home](../README.md) · [API history CSV](../data/api/model_iq_history.csv) · [Monitor status](../data/api/monitor_status.json)

**Last successful check:** `2026-08-09T13:18:09+00:00`  
**Current API snapshot:** `85d02f052bddc98b`  
**Source observation:** `2026-07-22T06:57:20.626603+08:00`  
**New snapshot detected:** no; the source returned the same snapshot  
**Models returned:** 11

> “Last successful check” confirms that the automation reached the API. “Source observation” is supplied by the upstream endpoint and may be older.

> This is a model-level summary from the Codex Radar API, not the project's task-level difficulty-weighted score.

## Current API model summary

| Rank | Model tier | Source score | Passed | Tasks | Cost | Total tokens | Wall time |
|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | Sol Xhigh | 111.7 | 83/112 | 112 | $744.22 | 944,299,376 | 50.52h |
| 2 | Sol High | 100.9 | 75/112 | 112 | $571.53 | 578,050,235 | 35.56h |
| 3 | Sol Medium | 95.5 | 71/112 | 112 | $409.29 | 523,456,433 | 31.97h |
| 4 | Gpt-5.5 Xhigh | 92.8 | 69/112 | 112 | $658.21 | 808,640,078 | 41.70h |
| 5 | Luna Max | 92.8 | 69/112 | 112 | $58.71 | 1,752,645,733 | 59.71h |
| 6 | Terra Max | 91.5 | 68/112 | 112 | $439.61 | 1,249,058,881 | 52.97h |
| 7 | Sol Low | 88.8 | 66/112 | 112 | $229.62 | 280,165,635 | 21.69h |
| 8 | Gpt-5.5 High | 86.1 | 64/112 | 112 | $405.88 | 473,048,619 | 27.51h |
| 9 | Terra Xhigh | 86.1 | 64/112 | 112 | $222.31 | 595,198,638 | 32.59h |
| 10 | Terra High | 79.4 | 59/112 | 112 | $126.85 | 336,139,374 | 21.99h |
| 11 | Luna High | 72.6 | 54/112 | 112 | $26.24 | 722,666,987 | 31.12h |

## Interpretation

- The endpoint provides model-level `score`, pass counts, task counts, tokens, wall time, and estimated cost.
- It does not expose the ten task-level outcomes, so `Weighted /100` cannot be recomputed from this API summary alone.
- Task-weighted rankings remain based on the repository's task matrix and weight snapshots; this report monitors the latest API summary.
- When source data is unchanged, the automation still updates its heartbeat without presenting it as a new benchmark batch.
- The raw API response is not stored in the public repository; only required model-summary fields are archived.

Archived API snapshots: **215**.
