# Codex Radar API Monitor — English

[简体中文](api-latest.zh-CN.md) · [Project home](../README.md) · [API history CSV](../data/api/model_iq_history.csv) · [Monitor status](../data/api/monitor_status.json)

**Last successful check:** `2026-07-21T12:02:04+00:00`  
**Current API snapshot:** `7b4baef292cb7d43`  
**Source observation:** `2026-07-18T11:35:05.153982+08:00`  
**New snapshot detected:** yes  
**Models returned:** 11

> “Last successful check” confirms that the automation reached the API. “Source observation” is supplied by the upstream endpoint and may be older.

> This is a model-level summary from the Codex Radar API, not the project's task-level difficulty-weighted score.

## Current API model summary

| Rank | Model tier | Source score | Passed | Tasks | Cost | Total tokens | Wall time |
|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | Terra Max | 99.5 | 74/112 | 112 | $520.94 | 1,351,234,756 | 62.21h |
| 2 | Sol Xhigh | 97.7 | 72/111 | 111 | $777.81 | 1,052,381,094 | 54.57h |
| 3 | Gpt-5.5 Xhigh | 94.2 | 70/112 | 112 | $658.14 | 846,411,435 | 41.77h |
| 4 | Sol High | 94.2 | 70/112 | 112 | $570.11 | 728,632,417 | 42.95h |
| 5 | Sol Medium | 94.2 | 70/112 | 112 | $387.27 | 489,169,767 | 34.54h |
| 6 | Luna Max | 92.8 | 69/112 | 112 | $279.18 | 1,905,986,538 | 70.32h |
| 7 | Terra Xhigh | 88.8 | 66/112 | 112 | $283.23 | 694,364,870 | 36.93h |
| 8 | Gpt-5.5 High | 80.7 | 60/112 | 112 | $402.38 | 503,916,646 | 29.85h |
| 9 | Sol Low | 74.7 | 55/111 | 111 | $228.58 | 264,153,638 | 23.77h |
| 10 | Luna High | 71.3 | 53/112 | 112 | $122.19 | 802,681,462 | 36.03h |
| 11 | Terra High | 70 | 52/112 | 112 | $150.20 | 338,287,491 | 24.46h |

## Interpretation

- The endpoint provides model-level `score`, pass counts, task counts, tokens, wall time, and estimated cost.
- It does not expose the ten task-level outcomes, so `Weighted /100` cannot be recomputed from this API summary alone.
- Task-weighted rankings remain based on the repository's task matrix and weight snapshots; this report monitors the latest API summary.
- When source data is unchanged, the automation still updates its heartbeat without presenting it as a new benchmark batch.
- The raw API response is not stored in the public repository; only required model-summary fields are archived.

Archived API snapshots: **42**.
