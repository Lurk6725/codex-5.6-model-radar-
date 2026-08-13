# Codex Radar API Monitor — English

[简体中文](api-latest.zh-CN.md) · [Project home](../README.md) · [API history CSV](../data/api/model_iq_history.csv) · [Monitor status](../data/api/monitor_status.json)

**Last successful check:** `2026-08-13T00:44:58+00:00`  
**Current API snapshot:** `59c28e5b311e5be3`  
**Source observation:** `2026-07-22T06:57:20.626603+08:00`  
**New snapshot detected:** yes  
**Models returned:** 11

> “Last successful check” confirms that the automation reached the API. “Source observation” is supplied by the upstream endpoint and may be older.

> This is a model-level summary from the Codex Radar API, not the project's task-level difficulty-weighted score.

## Current API model summary

| Rank | Model tier | Source score | Passed | Tasks | Cost | Total tokens | Wall time |
|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | Luna Max | 100.9 | 75/112 | 112 | $58.48 | 1,898,783,946 | 68.76h |
| 2 | Terra Max | 100.9 | 75/112 | 112 | $436.40 | 1,256,550,377 | 58.50h |
| 3 | Sol Xhigh | 99.5 | 74/112 | 112 | $730.35 | 874,648,914 | 47.30h |
| 4 | Gpt-5.5 Xhigh | 98.2 | 73/112 | 112 | $657.18 | 721,276,469 | 40.80h |
| 5 | Sol High | 95.5 | 71/112 | 112 | $560.95 | 685,505,033 | 38.74h |
| 6 | Sol Medium | 91.5 | 68/112 | 112 | $406.81 | 478,754,912 | 32.75h |
| 7 | Gpt-5.5 High | 86.1 | 64/112 | 112 | $403.74 | 494,135,198 | 33.74h |
| 8 | Terra Xhigh | 83.4 | 62/112 | 112 | $217.66 | 598,981,405 | 36.44h |
| 9 | Terra High | 78 | 58/112 | 112 | $126.56 | 338,532,462 | 24.81h |
| 10 | Luna High | 74 | 55/112 | 112 | $26.18 | 787,622,660 | 35.67h |
| 11 | Sol Low | 74 | 55/112 | 112 | $228.40 | 269,526,521 | 23.09h |

## Interpretation

- The endpoint provides model-level `score`, pass counts, task counts, tokens, wall time, and estimated cost.
- It does not expose the ten task-level outcomes, so `Weighted /100` cannot be recomputed from this API summary alone.
- Task-weighted rankings remain based on the repository's task matrix and weight snapshots; this report monitors the latest API summary.
- When source data is unchanged, the automation still updates its heartbeat without presenting it as a new benchmark batch.
- The raw API response is not stored in the public repository; only required model-summary fields are archived.

Archived API snapshots: **248**.
