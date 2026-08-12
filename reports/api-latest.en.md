# Codex Radar API Monitor — English

[简体中文](api-latest.zh-CN.md) · [Project home](../README.md) · [API history CSV](../data/api/model_iq_history.csv) · [Monitor status](../data/api/monitor_status.json)

**Last successful check:** `2026-08-12T22:24:48+00:00`  
**Current API snapshot:** `539238f1cad9199a`  
**Source observation:** `2026-07-22T06:57:20.626603+08:00`  
**New snapshot detected:** yes  
**Models returned:** 11

> “Last successful check” confirms that the automation reached the API. “Source observation” is supplied by the upstream endpoint and may be older.

> This is a model-level summary from the Codex Radar API, not the project's task-level difficulty-weighted score.

## Current API model summary

| Rank | Model tier | Source score | Passed | Tasks | Cost | Total tokens | Wall time |
|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | Terra Max | 102.2 | 76/112 | 112 | $436.46 | 1,269,774,191 | 58.75h |
| 2 | Luna Max | 100.9 | 75/112 | 112 | $58.48 | 1,898,783,946 | 68.76h |
| 3 | Sol Xhigh | 100.9 | 75/112 | 112 | $730.91 | 871,543,178 | 47.30h |
| 4 | Gpt-5.5 Xhigh | 98.2 | 73/112 | 112 | $657.18 | 721,276,469 | 40.80h |
| 5 | Sol High | 98.2 | 73/112 | 112 | $561.16 | 685,697,376 | 38.55h |
| 6 | Sol Medium | 91.5 | 68/112 | 112 | $406.81 | 478,754,912 | 32.75h |
| 7 | Gpt-5.5 High | 84.7 | 63/112 | 112 | $403.74 | 494,111,932 | 34.10h |
| 8 | Terra Xhigh | 83.4 | 62/112 | 112 | $217.82 | 587,160,955 | 35.96h |
| 9 | Terra High | 75.3 | 56/112 | 112 | $126.58 | 338,870,030 | 25.27h |
| 10 | Luna High | 74 | 55/112 | 112 | $26.18 | 786,527,187 | 35.60h |
| 11 | Sol Low | 72.6 | 54/112 | 112 | $228.47 | 265,484,664 | 22.76h |

## Interpretation

- The endpoint provides model-level `score`, pass counts, task counts, tokens, wall time, and estimated cost.
- It does not expose the ten task-level outcomes, so `Weighted /100` cannot be recomputed from this API summary alone.
- Task-weighted rankings remain based on the repository's task matrix and weight snapshots; this report monitors the latest API summary.
- When source data is unchanged, the automation still updates its heartbeat without presenting it as a new benchmark batch.
- The raw API response is not stored in the public repository; only required model-summary fields are archived.

Archived API snapshots: **247**.
