# Codex Radar API Monitor — English

[简体中文](api-latest.zh-CN.md) · [Project home](../README.md) · [API history CSV](../data/api/model_iq_history.csv) · [Monitor status](../data/api/monitor_status.json)

**Last successful check:** `2026-07-24T11:57:11+00:00`  
**Current API snapshot:** `8915b8551ade01d9`  
**Source observation:** `2026-07-22T06:57:20.626603+08:00`  
**New snapshot detected:** yes  
**Models returned:** 11

> “Last successful check” confirms that the automation reached the API. “Source observation” is supplied by the upstream endpoint and may be older.

> This is a model-level summary from the Codex Radar API, not the project's task-level difficulty-weighted score.

## Current API model summary

| Rank | Model tier | Source score | Passed | Tasks | Cost | Total tokens | Wall time |
|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | Sol High | 98.2 | 73/112 | 112 | $628.42 | 848,864,486 | 39.59h |
| 2 | Sol Medium | 96.9 | 72/112 | 112 | $424.22 | 536,528,447 | 29.78h |
| 3 | Sol Xhigh | 94.2 | 70/112 | 112 | $767.98 | 1,041,666,787 | 46.38h |
| 4 | Terra Max | 91.5 | 68/112 | 112 | $538.61 | 1,413,971,331 | 55.35h |
| 5 | Terra Xhigh | 91.5 | 68/112 | 112 | $273.02 | 651,703,608 | 35.32h |
| 6 | Gpt-5.5 Xhigh | 84.7 | 63/112 | 112 | $653.26 | 839,779,854 | 45.76h |
| 7 | Luna Max | 84.7 | 63/112 | 112 | $285.81 | 1,974,708,007 | 62.13h |
| 8 | Gpt-5.5 High | 79.4 | 59/112 | 112 | $428.66 | 539,025,557 | 32.89h |
| 9 | Sol Low | 76.7 | 57/112 | 112 | $231.85 | 266,219,727 | 19.67h |
| 10 | Luna High | 71.3 | 53/112 | 112 | $110.95 | 707,116,852 | 32.31h |
| 11 | Terra High | 67.3 | 50/112 | 112 | $155.66 | 351,441,083 | 22.79h |

## Interpretation

- The endpoint provides model-level `score`, pass counts, task counts, tokens, wall time, and estimated cost.
- It does not expose the ten task-level outcomes, so `Weighted /100` cannot be recomputed from this API summary alone.
- Task-weighted rankings remain based on the repository's task matrix and weight snapshots; this report monitors the latest API summary.
- When source data is unchanged, the automation still updates its heartbeat without presenting it as a new benchmark batch.
- The raw API response is not stored in the public repository; only required model-summary fields are archived.

Archived API snapshots: **69**.
