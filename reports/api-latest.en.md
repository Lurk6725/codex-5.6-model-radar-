# Codex Radar API Monitor — English

[简体中文](api-latest.zh-CN.md) · [Project home](../README.md) · [API history CSV](../data/api/model_iq_history.csv) · [Monitor status](../data/api/monitor_status.json)

**Last successful check:** `2026-07-31T16:58:52+00:00`  
**Current API snapshot:** `c2ef10b816aadeec`  
**Source observation:** `2026-07-22T06:57:20.626603+08:00`  
**New snapshot detected:** yes  
**Models returned:** 11

> “Last successful check” confirms that the automation reached the API. “Source observation” is supplied by the upstream endpoint and may be older.

> This is a model-level summary from the Codex Radar API, not the project's task-level difficulty-weighted score.

## Current API model summary

| Rank | Model tier | Source score | Passed | Tasks | Cost | Total tokens | Wall time |
|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | Sol Xhigh | 96.9 | 72/112 | 112 | $776.92 | 1,018,576,171 | 46.66h |
| 2 | Gpt-5.5 Xhigh | 88.8 | 66/112 | 112 | $650.89 | 824,509,482 | 42.74h |
| 3 | Sol High | 86.1 | 64/112 | 112 | $611.53 | 824,953,211 | 41.70h |
| 4 | Sol Medium | 83.4 | 62/112 | 112 | $431.60 | 556,666,773 | 31.97h |
| 5 | Terra Max | 83.4 | 62/112 | 112 | $566.24 | 1,547,146,610 | 56.72h |
| 6 | Luna Max | 82.1 | 61/112 | 112 | $151.08 | 1,787,997,485 | 56.01h |
| 7 | Terra High | 82.1 | 61/112 | 112 | $163.31 | 386,745,809 | 24.86h |
| 8 | Terra Xhigh | 79.4 | 59/112 | 112 | $286.48 | 719,474,429 | 33.82h |
| 9 | Gpt-5.5 High | 75.3 | 56/112 | 112 | $425.09 | 539,211,832 | 33.61h |
| 10 | Sol Low | 71.3 | 53/112 | 112 | $252.74 | 290,187,351 | 22.24h |
| 11 | Luna High | 68.6 | 51/112 | 112 | $77.15 | 781,516,181 | 32.09h |

## Interpretation

- The endpoint provides model-level `score`, pass counts, task counts, tokens, wall time, and estimated cost.
- It does not expose the ten task-level outcomes, so `Weighted /100` cannot be recomputed from this API summary alone.
- Task-weighted rankings remain based on the repository's task matrix and weight snapshots; this report monitors the latest API summary.
- When source data is unchanged, the automation still updates its heartbeat without presenting it as a new benchmark batch.
- The raw API response is not stored in the public repository; only required model-summary fields are archived.

Archived API snapshots: **134**.
