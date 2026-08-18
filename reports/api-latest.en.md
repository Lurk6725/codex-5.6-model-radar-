# Codex Radar API Monitor — English

[简体中文](api-latest.zh-CN.md) · [Project home](../README.md) · [API history CSV](../data/api/model_iq_history.csv) · [Monitor status](../data/api/monitor_status.json)

**Last successful check:** `2026-08-18T12:14:28+00:00`  
**Current API snapshot:** `e419f4f8481e6d08`  
**Source observation:** `2026-07-22T06:57:20.626603+08:00`  
**New snapshot detected:** no; the source returned the same snapshot  
**Models returned:** 11

> “Last successful check” confirms that the automation reached the API. “Source observation” is supplied by the upstream endpoint and may be older.

> This is a model-level summary from the Codex Radar API, not the project's task-level difficulty-weighted score.

## Current API model summary

| Rank | Model tier | Source score | Passed | Tasks | Cost | Total tokens | Wall time |
|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | Terra Max | 99.5 | 74/112 | 112 | $434.03 | 1,271,216,961 | 60.31h |
| 2 | Sol Xhigh | 98.2 | 73/112 | 112 | $729.32 | 849,532,420 | 45.33h |
| 3 | Gpt-5.5 Xhigh | 94.2 | 70/112 | 112 | $654.54 | 772,602,027 | 42.33h |
| 4 | Luna Max | 92.8 | 69/112 | 112 | $55.34 | 1,781,414,081 | 63.71h |
| 5 | Sol High | 91.5 | 68/112 | 112 | $538.21 | 639,355,346 | 36.21h |
| 6 | Gpt-5.5 High | 90.1 | 67/112 | 112 | $403.46 | 495,804,840 | 33.23h |
| 7 | Terra Xhigh | 86.1 | 64/112 | 112 | $215.34 | 605,158,740 | 39.18h |
| 8 | Sol Medium | 84.7 | 63/112 | 112 | $392.22 | 486,689,638 | 34.13h |
| 9 | Luna High | 75.3 | 56/112 | 112 | $23.64 | 768,411,852 | 35.11h |
| 10 | Terra High | 74 | 55/112 | 112 | $125.23 | 348,564,925 | 26.65h |
| 11 | Sol Low | 70 | 52/112 | 112 | $225.74 | 274,303,802 | 24.31h |

## Interpretation

- The endpoint provides model-level `score`, pass counts, task counts, tokens, wall time, and estimated cost.
- It does not expose the ten task-level outcomes, so `Weighted /100` cannot be recomputed from this API summary alone.
- Task-weighted rankings remain based on the repository's task matrix and weight snapshots; this report monitors the latest API summary.
- When source data is unchanged, the automation still updates its heartbeat without presenting it as a new benchmark batch.
- The raw API response is not stored in the public repository; only required model-summary fields are archived.

Archived API snapshots: **290**.
