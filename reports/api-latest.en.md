# Codex Radar API Monitor — English

[简体中文](api-latest.zh-CN.md) · [Project home](../README.md) · [API history CSV](../data/api/model_iq_history.csv) · [Monitor status](../data/api/monitor_status.json)

**Last successful check:** `2026-07-22T23:17:30+00:00`  
**Current API snapshot:** `7ecc16b525ecf602`  
**Source observation:** `2026-07-22T06:57:20.626603+08:00`  
**New snapshot detected:** yes  
**Models returned:** 11

> “Last successful check” confirms that the automation reached the API. “Source observation” is supplied by the upstream endpoint and may be older.

> This is a model-level summary from the Codex Radar API, not the project's task-level difficulty-weighted score.

## Current API model summary

| Rank | Model tier | Source score | Passed | Tasks | Cost | Total tokens | Wall time |
|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | Terra Max | 98.2 | 73/112 | 112 | $518.01 | 1,341,624,732 | 61.19h |
| 2 | Gpt-5.5 Xhigh | 96.9 | 72/112 | 112 | $654.04 | 843,313,242 | 46.44h |
| 3 | Sol Xhigh | 95.5 | 71/112 | 112 | $759.37 | 1,010,398,477 | 49.28h |
| 4 | Luna Max | 94.2 | 70/112 | 112 | $283.53 | 1,951,300,647 | 65.21h |
| 5 | Sol High | 92.8 | 69/112 | 112 | $607.85 | 812,618,442 | 43.84h |
| 6 | Sol Medium | 91.5 | 68/112 | 112 | $417.98 | 533,527,215 | 32.68h |
| 7 | Terra Xhigh | 88.8 | 66/112 | 112 | $269.57 | 650,472,332 | 35.87h |
| 8 | Gpt-5.5 High | 87.4 | 65/112 | 112 | $420.62 | 527,581,291 | 33.29h |
| 9 | Sol Low | 75.3 | 56/112 | 112 | $238.24 | 278,115,900 | 22.34h |
| 10 | Luna High | 68.6 | 51/112 | 112 | $112.80 | 714,347,015 | 34.66h |
| 11 | Terra High | 65.9 | 49/112 | 112 | $156.30 | 358,877,522 | 24.80h |

## Interpretation

- The endpoint provides model-level `score`, pass counts, task counts, tokens, wall time, and estimated cost.
- It does not expose the ten task-level outcomes, so `Weighted /100` cannot be recomputed from this API summary alone.
- Task-weighted rankings remain based on the repository's task matrix and weight snapshots; this report monitors the latest API summary.
- When source data is unchanged, the automation still updates its heartbeat without presenting it as a new benchmark batch.
- The raw API response is not stored in the public repository; only required model-summary fields are archived.

Archived API snapshots: **56**.
