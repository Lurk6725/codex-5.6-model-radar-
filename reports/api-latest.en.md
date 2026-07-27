# Codex Radar API Monitor — English

[简体中文](api-latest.zh-CN.md) · [Project home](../README.md) · [API history CSV](../data/api/model_iq_history.csv) · [Monitor status](../data/api/monitor_status.json)

**Last successful check:** `2026-07-27T12:38:08+00:00`  
**Current API snapshot:** `025054fcb9a36936`  
**Source observation:** `2026-07-22T06:57:20.626603+08:00`  
**New snapshot detected:** yes  
**Models returned:** 11

> “Last successful check” confirms that the automation reached the API. “Source observation” is supplied by the upstream endpoint and may be older.

> This is a model-level summary from the Codex Radar API, not the project's task-level difficulty-weighted score.

## Current API model summary

| Rank | Model tier | Source score | Passed | Tasks | Cost | Total tokens | Wall time |
|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | Luna Max | 95.5 | 71/112 | 112 | $277.97 | 1,904,192,290 | 60.01h |
| 2 | Sol Medium | 94.2 | 70/112 | 112 | $416.17 | 513,455,869 | 30.72h |
| 3 | Terra Max | 94.2 | 70/112 | 112 | $533.79 | 1,418,488,755 | 56.01h |
| 4 | Sol High | 92.8 | 69/112 | 112 | $582.13 | 740,379,985 | 40.34h |
| 5 | Sol Xhigh | 91.5 | 68/112 | 112 | $786.92 | 1,082,963,181 | 52.57h |
| 6 | Gpt-5.5 High | 86.1 | 64/112 | 112 | $412.55 | 513,005,396 | 30.02h |
| 7 | Gpt-5.5 Xhigh | 82.1 | 61/112 | 112 | $660.97 | 849,269,987 | 42.77h |
| 8 | Sol Low | 76.7 | 57/112 | 112 | $220.15 | 247,559,959 | 18.81h |
| 9 | Terra Xhigh | 76.7 | 57/112 | 112 | $289.93 | 721,024,599 | 35.86h |
| 10 | Luna High | 72.6 | 54/112 | 112 | $113.74 | 728,013,399 | 29.93h |
| 11 | Terra High | 67.3 | 50/112 | 112 | $147.10 | 322,433,325 | 21.03h |

## Interpretation

- The endpoint provides model-level `score`, pass counts, task counts, tokens, wall time, and estimated cost.
- It does not expose the ten task-level outcomes, so `Weighted /100` cannot be recomputed from this API summary alone.
- Task-weighted rankings remain based on the repository's task matrix and weight snapshots; this report monitors the latest API summary.
- When source data is unchanged, the automation still updates its heartbeat without presenting it as a new benchmark batch.
- The raw API response is not stored in the public repository; only required model-summary fields are archived.

Archived API snapshots: **95**.
