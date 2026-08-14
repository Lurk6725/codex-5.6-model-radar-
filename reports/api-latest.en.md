# Codex Radar API Monitor — English

[简体中文](api-latest.zh-CN.md) · [Project home](../README.md) · [API history CSV](../data/api/model_iq_history.csv) · [Monitor status](../data/api/monitor_status.json)

**Last successful check:** `2026-08-14T19:16:27+00:00`  
**Current API snapshot:** `3732e38715d18845`  
**Source observation:** `2026-07-22T06:57:20.626603+08:00`  
**New snapshot detected:** yes  
**Models returned:** 11

> “Last successful check” confirms that the automation reached the API. “Source observation” is supplied by the upstream endpoint and may be older.

> This is a model-level summary from the Codex Radar API, not the project's task-level difficulty-weighted score.

## Current API model summary

| Rank | Model tier | Source score | Passed | Tasks | Cost | Total tokens | Wall time |
|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | Terra Max | 100.9 | 75/112 | 112 | $435.44 | 1,254,016,951 | 59.85h |
| 2 | Sol Xhigh | 98.2 | 73/112 | 112 | $725.64 | 841,819,650 | 44.86h |
| 3 | Gpt-5.5 Xhigh | 96.9 | 72/112 | 112 | $656.01 | 742,118,949 | 42.27h |
| 4 | Luna Max | 95.5 | 71/112 | 112 | $58.57 | 1,811,800,870 | 65.44h |
| 5 | Gpt-5.5 High | 92.8 | 69/112 | 112 | $403.56 | 494,162,979 | 33.12h |
| 6 | Sol Medium | 92.8 | 69/112 | 112 | $382.73 | 460,331,349 | 32.39h |
| 7 | Sol High | 91.5 | 68/112 | 112 | $538.22 | 647,502,822 | 36.42h |
| 8 | Terra Xhigh | 84.7 | 63/112 | 112 | $217.16 | 590,965,936 | 37.47h |
| 9 | Luna High | 75.3 | 56/112 | 112 | $26.18 | 784,298,643 | 36.34h |
| 10 | Terra High | 74 | 55/112 | 112 | $126.40 | 340,603,570 | 26.39h |
| 11 | Sol Low | 68.6 | 51/112 | 112 | $225.37 | 275,060,734 | 24.54h |

## Interpretation

- The endpoint provides model-level `score`, pass counts, task counts, tokens, wall time, and estimated cost.
- It does not expose the ten task-level outcomes, so `Weighted /100` cannot be recomputed from this API summary alone.
- Task-weighted rankings remain based on the repository's task matrix and weight snapshots; this report monitors the latest API summary.
- When source data is unchanged, the automation still updates its heartbeat without presenting it as a new benchmark batch.
- The raw API response is not stored in the public repository; only required model-summary fields are archived.

Archived API snapshots: **258**.
