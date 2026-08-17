# Codex Radar API Monitor — English

[简体中文](api-latest.zh-CN.md) · [Project home](../README.md) · [API history CSV](../data/api/model_iq_history.csv) · [Monitor status](../data/api/monitor_status.json)

**Last successful check:** `2026-08-17T10:16:28+00:00`  
**Current API snapshot:** `83c06117be8ab7a8`  
**Source observation:** `2026-07-22T06:57:20.626603+08:00`  
**New snapshot detected:** no; the source returned the same snapshot  
**Models returned:** 11

> “Last successful check” confirms that the automation reached the API. “Source observation” is supplied by the upstream endpoint and may be older.

> This is a model-level summary from the Codex Radar API, not the project's task-level difficulty-weighted score.

## Current API model summary

| Rank | Model tier | Source score | Passed | Tasks | Cost | Total tokens | Wall time |
|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | Sol Xhigh | 98.2 | 73/112 | 112 | $724.97 | 855,165,861 | 45.11h |
| 2 | Terra Max | 96.9 | 72/112 | 112 | $435.26 | 1,247,044,382 | 58.60h |
| 3 | Gpt-5.5 Xhigh | 94.2 | 70/112 | 112 | $655.27 | 750,004,193 | 41.97h |
| 4 | Luna Max | 94.2 | 70/112 | 112 | $58.69 | 1,779,093,330 | 64.19h |
| 5 | Gpt-5.5 High | 92.8 | 69/112 | 112 | $403.50 | 495,489,634 | 33.12h |
| 6 | Sol High | 91.5 | 68/112 | 112 | $538.01 | 643,235,271 | 35.83h |
| 7 | Sol Medium | 84.7 | 63/112 | 112 | $383.04 | 466,206,625 | 33.02h |
| 8 | Terra Xhigh | 82.1 | 61/112 | 112 | $216.91 | 598,970,793 | 37.90h |
| 9 | Luna High | 78 | 58/112 | 112 | $26.17 | 773,567,465 | 35.33h |
| 10 | Terra High | 72.6 | 54/112 | 112 | $126.48 | 341,911,361 | 26.00h |
| 11 | Sol Low | 65.9 | 49/112 | 112 | $225.75 | 277,056,940 | 24.30h |

## Interpretation

- The endpoint provides model-level `score`, pass counts, task counts, tokens, wall time, and estimated cost.
- It does not expose the ten task-level outcomes, so `Weighted /100` cannot be recomputed from this API summary alone.
- Task-weighted rankings remain based on the repository's task matrix and weight snapshots; this report monitors the latest API summary.
- When source data is unchanged, the automation still updates its heartbeat without presenting it as a new benchmark batch.
- The raw API response is not stored in the public repository; only required model-summary fields are archived.

Archived API snapshots: **278**.
