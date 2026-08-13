# Codex Radar API Monitor — English

[简体中文](api-latest.zh-CN.md) · [Project home](../README.md) · [API history CSV](../data/api/model_iq_history.csv) · [Monitor status](../data/api/monitor_status.json)

**Last successful check:** `2026-08-13T11:12:22+00:00`  
**Current API snapshot:** `a31c539bb9666ecf`  
**Source observation:** `2026-07-22T06:57:20.626603+08:00`  
**New snapshot detected:** yes  
**Models returned:** 11

> “Last successful check” confirms that the automation reached the API. “Source observation” is supplied by the upstream endpoint and may be older.

> This is a model-level summary from the Codex Radar API, not the project's task-level difficulty-weighted score.

## Current API model summary

| Rank | Model tier | Source score | Passed | Tasks | Cost | Total tokens | Wall time |
|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | Terra Max | 102.2 | 76/112 | 112 | $435.30 | 1,215,937,471 | 59.03h |
| 2 | Sol Xhigh | 100.9 | 75/112 | 112 | $726.18 | 840,141,636 | 45.02h |
| 3 | Luna Max | 98.2 | 73/112 | 112 | $58.68 | 1,903,217,951 | 68.35h |
| 4 | Gpt-5.5 Xhigh | 94.2 | 70/112 | 112 | $656.81 | 715,155,525 | 41.23h |
| 5 | Sol Medium | 90.1 | 67/112 | 112 | $382.91 | 445,132,928 | 31.52h |
| 6 | Gpt-5.5 High | 88.8 | 66/112 | 112 | $403.88 | 492,680,023 | 33.63h |
| 7 | Sol High | 88.8 | 66/112 | 112 | $538.05 | 649,296,478 | 36.86h |
| 8 | Terra Xhigh | 82.1 | 61/112 | 112 | $217.40 | 595,047,958 | 37.13h |
| 9 | Terra High | 76.7 | 57/112 | 112 | $126.56 | 341,265,094 | 25.98h |
| 10 | Luna High | 75.3 | 56/112 | 112 | $26.17 | 782,367,196 | 35.65h |
| 11 | Sol Low | 71.3 | 53/112 | 112 | $225.53 | 283,159,384 | 23.59h |

## Interpretation

- The endpoint provides model-level `score`, pass counts, task counts, tokens, wall time, and estimated cost.
- It does not expose the ten task-level outcomes, so `Weighted /100` cannot be recomputed from this API summary alone.
- Task-weighted rankings remain based on the repository's task matrix and weight snapshots; this report monitors the latest API summary.
- When source data is unchanged, the automation still updates its heartbeat without presenting it as a new benchmark batch.
- The raw API response is not stored in the public repository; only required model-summary fields are archived.

Archived API snapshots: **253**.
