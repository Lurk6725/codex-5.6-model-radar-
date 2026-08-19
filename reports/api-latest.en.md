# Codex Radar API Monitor — English

[简体中文](api-latest.zh-CN.md) · [Project home](../README.md) · [API history CSV](../data/api/model_iq_history.csv) · [Monitor status](../data/api/monitor_status.json)

**Last successful check:** `2026-08-19T18:55:54+00:00`  
**Current API snapshot:** `cc354e8995fb5abf`  
**Source observation:** `2026-07-22T06:57:20.626603+08:00`  
**New snapshot detected:** yes  
**Models returned:** 11

> “Last successful check” confirms that the automation reached the API. “Source observation” is supplied by the upstream endpoint and may be older.

> This is a model-level summary from the Codex Radar API, not the project's task-level difficulty-weighted score.

## Current API model summary

| Rank | Model tier | Source score | Passed | Tasks | Cost | Total tokens | Wall time |
|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | Terra Max | 99.5 | 74/112 | 112 | $434.37 | 1,246,401,709 | 59.24h |
| 2 | Gpt-5.5 Xhigh | 98.2 | 73/112 | 112 | $653.45 | 776,225,288 | 41.53h |
| 3 | Sol Xhigh | 98.2 | 73/112 | 112 | $726.94 | 851,940,197 | 44.73h |
| 4 | Luna Max | 94.2 | 70/112 | 112 | $55.16 | 1,819,657,359 | 64.91h |
| 5 | Gpt-5.5 High | 91.5 | 68/112 | 112 | $401.11 | 530,255,968 | 34.31h |
| 6 | Sol High | 86.1 | 64/112 | 112 | $535.72 | 634,044,032 | 35.52h |
| 7 | Terra Xhigh | 84.7 | 63/112 | 112 | $214.69 | 591,280,440 | 37.77h |
| 8 | Sol Medium | 82.1 | 61/112 | 112 | $397.67 | 462,768,781 | 33.65h |
| 9 | Terra High | 75.3 | 56/112 | 112 | $125.02 | 347,134,301 | 25.84h |
| 10 | Luna High | 74 | 55/112 | 112 | $23.48 | 758,509,727 | 34.45h |
| 11 | Sol Low | 72.6 | 54/112 | 112 | $223.85 | 264,062,354 | 24.43h |

## Interpretation

- The endpoint provides model-level `score`, pass counts, task counts, tokens, wall time, and estimated cost.
- It does not expose the ten task-level outcomes, so `Weighted /100` cannot be recomputed from this API summary alone.
- Task-weighted rankings remain based on the repository's task matrix and weight snapshots; this report monitors the latest API summary.
- When source data is unchanged, the automation still updates its heartbeat without presenting it as a new benchmark batch.
- The raw API response is not stored in the public repository; only required model-summary fields are archived.

Archived API snapshots: **299**.
