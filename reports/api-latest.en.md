# Codex Radar API Monitor — English

[简体中文](api-latest.zh-CN.md) · [Project home](../README.md) · [API history CSV](../data/api/model_iq_history.csv) · [Monitor status](../data/api/monitor_status.json)

**Last successful check:** `2026-08-17T07:18:36+00:00`  
**Current API snapshot:** `f03a720c5e524ca9`  
**Source observation:** `2026-07-22T06:57:20.626603+08:00`  
**New snapshot detected:** yes  
**Models returned:** 11

> “Last successful check” confirms that the automation reached the API. “Source observation” is supplied by the upstream endpoint and may be older.

> This is a model-level summary from the Codex Radar API, not the project's task-level difficulty-weighted score.

## Current API model summary

| Rank | Model tier | Source score | Passed | Tasks | Cost | Total tokens | Wall time |
|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | Sol Xhigh | 96.9 | 72/112 | 112 | $724.92 | 857,958,602 | 45.23h |
| 2 | Terra Max | 96.9 | 72/112 | 112 | $435.26 | 1,247,044,382 | 58.60h |
| 3 | Gpt-5.5 Xhigh | 94.2 | 70/112 | 112 | $655.30 | 749,128,725 | 41.96h |
| 4 | Luna Max | 94.2 | 70/112 | 112 | $58.69 | 1,779,093,330 | 64.19h |
| 5 | Gpt-5.5 High | 92.8 | 69/112 | 112 | $403.54 | 496,911,182 | 33.12h |
| 6 | Sol High | 91.5 | 68/112 | 112 | $538.01 | 642,216,687 | 35.90h |
| 7 | Sol Medium | 86.1 | 64/112 | 112 | $382.80 | 470,717,093 | 32.67h |
| 8 | Terra Xhigh | 82.1 | 61/112 | 112 | $216.93 | 593,569,543 | 37.72h |
| 9 | Luna High | 78 | 58/112 | 112 | $26.17 | 772,023,098 | 35.58h |
| 10 | Terra High | 72.6 | 54/112 | 112 | $126.50 | 340,818,220 | 26.24h |
| 11 | Sol Low | 65.9 | 49/112 | 112 | $225.75 | 277,056,940 | 24.30h |

## Interpretation

- The endpoint provides model-level `score`, pass counts, task counts, tokens, wall time, and estimated cost.
- It does not expose the ten task-level outcomes, so `Weighted /100` cannot be recomputed from this API summary alone.
- Task-weighted rankings remain based on the repository's task matrix and weight snapshots; this report monitors the latest API summary.
- When source data is unchanged, the automation still updates its heartbeat without presenting it as a new benchmark batch.
- The raw API response is not stored in the public repository; only required model-summary fields are archived.

Archived API snapshots: **277**.
