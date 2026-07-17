# Codex Radar API Monitor — English

[简体中文](api-latest.zh-CN.md) · [Project home](../README.md) · [API history CSV](../data/api/model_iq_history.csv) · [Monitor status](../data/api/monitor_status.json)

**Last successful check:** `2026-07-17T06:05:45+00:00`  
**Current API snapshot:** `931636456d7e2c15`  
**Source observation:** `2026-07-13T22:08:07.261261+08:00`  
**New snapshot detected:** yes  
**Models returned:** 9

> “Last successful check” confirms that the automation reached the API. “Source observation” is supplied by the upstream endpoint and may be older.

> This is a model-level summary from the Codex Radar API, not the project's task-level difficulty-weighted score.

## Current API model summary

| Rank | Model tier | Source score | Passed | Tasks | Cost | Total tokens | Wall time |
|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | Terra Max | 99.8 | 51/77 | 77 | $369.68 | 960,656,935 | 39.46h |
| 2 | Luna Max | 98.2 | 58/89 | 89 | $211.11 | 1,434,314,805 | 49.53h |
| 3 | Sol Xhigh | 93.1 | 63/102 | 102 | $685.15 | 906,162,723 | 46.79h |
| 4 | Sol High | 88 | 59/101 | 101 | $531.52 | 695,318,246 | 39.55h |
| 5 | Sol Medium | 85.3 | 60/106 | 106 | $352.95 | 445,307,222 | 30.27h |
| 6 | Gpt-5.5 High | 84.9 | 62/110 | 110 | $387.37 | 486,362,154 | 50.30h |
| 7 | Terra High | 78.9 | 44/84 | 84 | $111.23 | 254,871,996 | 19.49h |
| 8 | Sol Low | 72.1 | 45/94 | 94 | $169.60 | 185,291,853 | 16.25h |
| 9 | Luna High | 63.7 | 33/78 | 78 | $89.17 | 578,781,139 | 23.80h |

## Interpretation

- The endpoint provides model-level `score`, pass counts, task counts, tokens, wall time, and estimated cost.
- It does not expose the ten task-level outcomes, so `Weighted /100` cannot be recomputed from this API summary alone.
- Task-weighted rankings remain based on the repository's task matrix and weight snapshots; this report monitors the latest API summary.
- When source data is unchanged, the automation still updates its heartbeat without presenting it as a new benchmark batch.
- The raw API response is not stored in the public repository; only required model-summary fields are archived.

Archived API snapshots: **8**.
