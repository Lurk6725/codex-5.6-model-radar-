# Codex Radar API Monitor — English

[简体中文](api-latest.zh-CN.md) · [Project home](../README.md) · [API history CSV](../data/api/model_iq_history.csv) · [Monitor status](../data/api/monitor_status.json)

**Last successful check:** `2026-08-06T07:27:35+00:00`  
**Current API snapshot:** `080147ae2cf6c725`  
**Source observation:** `2026-07-22T06:57:20.626603+08:00`  
**New snapshot detected:** yes  
**Models returned:** 11

> “Last successful check” confirms that the automation reached the API. “Source observation” is supplied by the upstream endpoint and may be older.

> This is a model-level summary from the Codex Radar API, not the project's task-level difficulty-weighted score.

## Current API model summary

| Rank | Model tier | Source score | Passed | Tasks | Cost | Total tokens | Wall time |
|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | Sol Xhigh | 111.7 | 83/112 | 112 | $761.22 | 966,424,672 | 48.27h |
| 2 | Gpt-5.5 Xhigh | 96.9 | 72/112 | 112 | $652.04 | 810,820,797 | 41.81h |
| 3 | Gpt-5.5 High | 95.5 | 71/112 | 112 | $406.41 | 503,297,310 | 32.21h |
| 4 | Luna Max | 92.8 | 69/112 | 112 | $58.85 | 1,729,172,097 | 60.38h |
| 5 | Sol Medium | 92.8 | 69/112 | 112 | $407.66 | 514,731,429 | 32.03h |
| 6 | Terra Max | 92.8 | 69/112 | 112 | $456.52 | 1,492,354,215 | 61.59h |
| 7 | Sol High | 88.8 | 66/112 | 112 | $588.01 | 689,345,812 | 39.67h |
| 8 | Terra Xhigh | 83.4 | 62/112 | 112 | $227.06 | 622,729,608 | 35.24h |
| 9 | Luna High | 79.4 | 59/112 | 112 | $27.59 | 717,216,555 | 30.30h |
| 10 | Terra High | 75.3 | 56/112 | 112 | $133.20 | 345,789,998 | 24.46h |
| 11 | Sol Low | 74 | 55/112 | 112 | $231.83 | 263,381,802 | 22.05h |

## Interpretation

- The endpoint provides model-level `score`, pass counts, task counts, tokens, wall time, and estimated cost.
- It does not expose the ten task-level outcomes, so `Weighted /100` cannot be recomputed from this API summary alone.
- Task-weighted rankings remain based on the repository's task matrix and weight snapshots; this report monitors the latest API summary.
- When source data is unchanged, the automation still updates its heartbeat without presenting it as a new benchmark batch.
- The raw API response is not stored in the public repository; only required model-summary fields are archived.

Archived API snapshots: **183**.
