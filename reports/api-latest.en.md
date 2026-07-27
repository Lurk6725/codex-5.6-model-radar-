# Codex Radar API Monitor — English

[简体中文](api-latest.zh-CN.md) · [Project home](../README.md) · [API history CSV](../data/api/model_iq_history.csv) · [Monitor status](../data/api/monitor_status.json)

**Last successful check:** `2026-07-27T04:55:01+00:00`  
**Current API snapshot:** `a9f43f95bcecc74b`  
**Source observation:** `2026-07-22T06:57:20.626603+08:00`  
**New snapshot detected:** yes  
**Models returned:** 11

> “Last successful check” confirms that the automation reached the API. “Source observation” is supplied by the upstream endpoint and may be older.

> This is a model-level summary from the Codex Radar API, not the project's task-level difficulty-weighted score.

## Current API model summary

| Rank | Model tier | Source score | Passed | Tasks | Cost | Total tokens | Wall time |
|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | Sol High | 95.5 | 71/112 | 112 | $591.28 | 758,173,863 | 39.82h |
| 2 | Sol Medium | 95.5 | 71/112 | 112 | $418.00 | 517,073,778 | 30.62h |
| 3 | Terra Max | 95.5 | 71/112 | 112 | $533.95 | 1,419,454,073 | 56.09h |
| 4 | Sol Xhigh | 92.8 | 69/112 | 112 | $792.25 | 1,084,274,449 | 51.77h |
| 5 | Gpt-5.5 High | 91.5 | 68/112 | 112 | $409.21 | 512,604,184 | 28.46h |
| 6 | Luna Max | 91.5 | 68/112 | 112 | $275.60 | 1,883,584,850 | 59.47h |
| 7 | Gpt-5.5 Xhigh | 86.1 | 64/112 | 112 | $671.08 | 865,936,718 | 43.14h |
| 8 | Sol Low | 76.7 | 57/112 | 112 | $221.34 | 250,467,168 | 18.71h |
| 9 | Terra Xhigh | 75.3 | 56/112 | 112 | $287.45 | 712,894,630 | 34.48h |
| 10 | Luna High | 72.6 | 54/112 | 112 | $114.29 | 731,729,693 | 29.57h |
| 11 | Terra High | 65.9 | 49/112 | 112 | $144.56 | 315,521,474 | 20.30h |

## Interpretation

- The endpoint provides model-level `score`, pass counts, task counts, tokens, wall time, and estimated cost.
- It does not expose the ten task-level outcomes, so `Weighted /100` cannot be recomputed from this API summary alone.
- Task-weighted rankings remain based on the repository's task matrix and weight snapshots; this report monitors the latest API summary.
- When source data is unchanged, the automation still updates its heartbeat without presenting it as a new benchmark batch.
- The raw API response is not stored in the public repository; only required model-summary fields are archived.

Archived API snapshots: **93**.
