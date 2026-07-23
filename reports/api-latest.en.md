# Codex Radar API Monitor — English

[简体中文](api-latest.zh-CN.md) · [Project home](../README.md) · [API history CSV](../data/api/model_iq_history.csv) · [Monitor status](../data/api/monitor_status.json)

**Last successful check:** `2026-07-23T16:15:27+00:00`  
**Current API snapshot:** `21308b6ea407c53e`  
**Source observation:** `2026-07-22T06:57:20.626603+08:00`  
**New snapshot detected:** yes  
**Models returned:** 11

> “Last successful check” confirms that the automation reached the API. “Source observation” is supplied by the upstream endpoint and may be older.

> This is a model-level summary from the Codex Radar API, not the project's task-level difficulty-weighted score.

## Current API model summary

| Rank | Model tier | Source score | Passed | Tasks | Cost | Total tokens | Wall time |
|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | Sol Xhigh | 96.9 | 72/112 | 112 | $798.42 | 1,091,668,493 | 49.20h |
| 2 | Sol High | 94.2 | 70/112 | 112 | $671.35 | 931,896,321 | 43.80h |
| 3 | Terra Max | 94.2 | 70/112 | 112 | $525.15 | 1,369,025,348 | 59.15h |
| 4 | Gpt-5.5 Xhigh | 91.5 | 68/112 | 112 | $644.63 | 827,675,465 | 46.87h |
| 5 | Sol Medium | 91.5 | 68/112 | 112 | $435.31 | 555,992,526 | 32.09h |
| 6 | Terra Xhigh | 90.1 | 67/112 | 112 | $264.29 | 634,728,385 | 36.35h |
| 7 | Luna Max | 86.1 | 64/112 | 112 | $277.30 | 1,892,754,736 | 62.00h |
| 8 | Gpt-5.5 High | 84.7 | 63/112 | 112 | $434.06 | 548,693,348 | 35.08h |
| 9 | Sol Low | 76.7 | 57/112 | 112 | $230.24 | 267,115,526 | 21.21h |
| 10 | Luna High | 72.6 | 54/112 | 112 | $111.48 | 703,827,199 | 33.80h |
| 11 | Terra High | 68.6 | 51/112 | 112 | $158.87 | 365,629,356 | 24.75h |

## Interpretation

- The endpoint provides model-level `score`, pass counts, task counts, tokens, wall time, and estimated cost.
- It does not expose the ten task-level outcomes, so `Weighted /100` cannot be recomputed from this API summary alone.
- Task-weighted rankings remain based on the repository's task matrix and weight snapshots; this report monitors the latest API summary.
- When source data is unchanged, the automation still updates its heartbeat without presenting it as a new benchmark batch.
- The raw API response is not stored in the public repository; only required model-summary fields are archived.

Archived API snapshots: **62**.
