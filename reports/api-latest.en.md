# Codex Radar API Monitor — English

[简体中文](api-latest.zh-CN.md) · [Project home](../README.md) · [API history CSV](../data/api/model_iq_history.csv) · [Monitor status](../data/api/monitor_status.json)

**Last successful check:** `2026-07-26T12:18:28+00:00`  
**Current API snapshot:** `4c0a20f761e12dbd`  
**Source observation:** `2026-07-22T06:57:20.626603+08:00`  
**New snapshot detected:** no; the source returned the same snapshot  
**Models returned:** 11

> “Last successful check” confirms that the automation reached the API. “Source observation” is supplied by the upstream endpoint and may be older.

> This is a model-level summary from the Codex Radar API, not the project's task-level difficulty-weighted score.

## Current API model summary

| Rank | Model tier | Source score | Passed | Tasks | Cost | Total tokens | Wall time |
|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | Sol Xhigh | 96.9 | 72/112 | 112 | $794.63 | 1,095,664,724 | 50.33h |
| 2 | Luna Max | 92.8 | 69/112 | 112 | $282.44 | 1,943,749,015 | 61.45h |
| 3 | Sol Medium | 92.8 | 69/112 | 112 | $438.03 | 560,032,415 | 30.60h |
| 4 | Sol High | 91.5 | 68/112 | 112 | $583.49 | 773,077,216 | 35.12h |
| 5 | Gpt-5.5 High | 90.1 | 67/112 | 112 | $422.68 | 532,233,312 | 29.81h |
| 6 | Terra Max | 88.8 | 66/112 | 112 | $538.40 | 1,418,038,059 | 56.45h |
| 7 | Gpt-5.5 Xhigh | 83.4 | 62/112 | 112 | $646.31 | 829,917,248 | 41.11h |
| 8 | Terra Xhigh | 79.4 | 59/112 | 112 | $281.89 | 681,839,782 | 36.02h |
| 9 | Sol Low | 74 | 55/112 | 112 | $225.49 | 253,810,370 | 18.84h |
| 10 | Luna High | 68.6 | 51/112 | 112 | $116.82 | 753,210,995 | 29.48h |
| 11 | Terra High | 67.3 | 50/112 | 112 | $149.40 | 332,225,353 | 21.94h |

## Interpretation

- The endpoint provides model-level `score`, pass counts, task counts, tokens, wall time, and estimated cost.
- It does not expose the ten task-level outcomes, so `Weighted /100` cannot be recomputed from this API summary alone.
- Task-weighted rankings remain based on the repository's task matrix and weight snapshots; this report monitors the latest API summary.
- When source data is unchanged, the automation still updates its heartbeat without presenting it as a new benchmark batch.
- The raw API response is not stored in the public repository; only required model-summary fields are archived.

Archived API snapshots: **89**.
