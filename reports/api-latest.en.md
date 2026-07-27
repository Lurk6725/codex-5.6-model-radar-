# Codex Radar API Monitor — English

[简体中文](api-latest.zh-CN.md) · [Project home](../README.md) · [API history CSV](../data/api/model_iq_history.csv) · [Monitor status](../data/api/monitor_status.json)

**Last successful check:** `2026-07-27T15:32:11+00:00`  
**Current API snapshot:** `26088c2baa70b3bd`  
**Source observation:** `2026-07-22T06:57:20.626603+08:00`  
**New snapshot detected:** yes  
**Models returned:** 11

> “Last successful check” confirms that the automation reached the API. “Source observation” is supplied by the upstream endpoint and may be older.

> This is a model-level summary from the Codex Radar API, not the project's task-level difficulty-weighted score.

## Current API model summary

| Rank | Model tier | Source score | Passed | Tasks | Cost | Total tokens | Wall time |
|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | Luna Max | 96.9 | 72/112 | 112 | $273.90 | 1,874,251,093 | 59.67h |
| 2 | Sol Medium | 95.5 | 71/112 | 112 | $415.79 | 512,544,850 | 31.28h |
| 3 | Terra Max | 94.2 | 70/112 | 112 | $526.45 | 1,398,907,018 | 55.64h |
| 4 | Sol High | 91.5 | 68/112 | 112 | $583.64 | 742,216,066 | 40.89h |
| 5 | Sol Xhigh | 88.8 | 66/112 | 112 | $797.93 | 1,099,465,645 | 52.78h |
| 6 | Gpt-5.5 High | 83.4 | 62/112 | 112 | $414.95 | 514,852,044 | 30.59h |
| 7 | Gpt-5.5 Xhigh | 83.4 | 62/112 | 112 | $657.56 | 843,594,413 | 42.58h |
| 8 | Terra Xhigh | 80.7 | 60/112 | 112 | $295.07 | 738,852,499 | 36.92h |
| 9 | Sol Low | 76.7 | 57/112 | 112 | $221.55 | 249,409,305 | 19.18h |
| 10 | Luna High | 75.3 | 56/112 | 112 | $116.57 | 754,735,421 | 30.60h |
| 11 | Terra High | 68.6 | 51/112 | 112 | $146.10 | 320,251,434 | 21.49h |

## Interpretation

- The endpoint provides model-level `score`, pass counts, task counts, tokens, wall time, and estimated cost.
- It does not expose the ten task-level outcomes, so `Weighted /100` cannot be recomputed from this API summary alone.
- Task-weighted rankings remain based on the repository's task matrix and weight snapshots; this report monitors the latest API summary.
- When source data is unchanged, the automation still updates its heartbeat without presenting it as a new benchmark batch.
- The raw API response is not stored in the public repository; only required model-summary fields are archived.

Archived API snapshots: **96**.
