# Codex Radar API Monitor — English

[简体中文](api-latest.zh-CN.md) · [Project home](../README.md) · [API history CSV](../data/api/model_iq_history.csv) · [Monitor status](../data/api/monitor_status.json)

**Last successful check:** `2026-08-13T05:23:01+00:00`  
**Current API snapshot:** `2c9efe63b1e93b49`  
**Source observation:** `2026-07-22T06:57:20.626603+08:00`  
**New snapshot detected:** yes  
**Models returned:** 11

> “Last successful check” confirms that the automation reached the API. “Source observation” is supplied by the upstream endpoint and may be older.

> This is a model-level summary from the Codex Radar API, not the project's task-level difficulty-weighted score.

## Current API model summary

| Rank | Model tier | Source score | Passed | Tasks | Cost | Total tokens | Wall time |
|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | Sol Xhigh | 100.9 | 75/112 | 112 | $726.57 | 844,187,724 | 45.49h |
| 2 | Terra Max | 100.9 | 75/112 | 112 | $435.06 | 1,239,626,909 | 58.44h |
| 3 | Luna Max | 96.9 | 72/112 | 112 | $58.53 | 1,899,990,201 | 67.80h |
| 4 | Gpt-5.5 Xhigh | 94.2 | 70/112 | 112 | $657.03 | 707,995,306 | 41.22h |
| 5 | Sol High | 91.5 | 68/112 | 112 | $538.24 | 654,060,006 | 37.06h |
| 6 | Gpt-5.5 High | 87.4 | 65/112 | 112 | $403.66 | 495,815,765 | 33.67h |
| 7 | Sol Medium | 87.4 | 65/112 | 112 | $383.13 | 435,020,723 | 31.18h |
| 8 | Terra Xhigh | 83.4 | 62/112 | 112 | $217.49 | 597,357,404 | 36.93h |
| 9 | Terra High | 76.7 | 57/112 | 112 | $126.58 | 338,232,100 | 25.37h |
| 10 | Luna High | 74 | 55/112 | 112 | $26.17 | 787,593,553 | 35.78h |
| 11 | Sol Low | 70 | 52/112 | 112 | $225.52 | 281,920,773 | 23.52h |

## Interpretation

- The endpoint provides model-level `score`, pass counts, task counts, tokens, wall time, and estimated cost.
- It does not expose the ten task-level outcomes, so `Weighted /100` cannot be recomputed from this API summary alone.
- Task-weighted rankings remain based on the repository's task matrix and weight snapshots; this report monitors the latest API summary.
- When source data is unchanged, the automation still updates its heartbeat without presenting it as a new benchmark batch.
- The raw API response is not stored in the public repository; only required model-summary fields are archived.

Archived API snapshots: **250**.
