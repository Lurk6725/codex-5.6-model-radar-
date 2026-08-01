# Codex Radar API Monitor — English

[简体中文](api-latest.zh-CN.md) · [Project home](../README.md) · [API history CSV](../data/api/model_iq_history.csv) · [Monitor status](../data/api/monitor_status.json)

**Last successful check:** `2026-08-01T05:01:42+00:00`  
**Current API snapshot:** `d3f623f533511a39`  
**Source observation:** `2026-07-22T06:57:20.626603+08:00`  
**New snapshot detected:** yes  
**Models returned:** 11

> “Last successful check” confirms that the automation reached the API. “Source observation” is supplied by the upstream endpoint and may be older.

> This is a model-level summary from the Codex Radar API, not the project's task-level difficulty-weighted score.

## Current API model summary

| Rank | Model tier | Source score | Passed | Tasks | Cost | Total tokens | Wall time |
|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | Sol Xhigh | 96.9 | 72/112 | 112 | $768.61 | 1,002,073,967 | 47.05h |
| 2 | Gpt-5.5 Xhigh | 91.5 | 68/112 | 112 | $646.58 | 840,279,919 | 43.70h |
| 3 | Sol High | 90.1 | 67/112 | 112 | $610.63 | 798,218,362 | 40.85h |
| 4 | Terra Max | 86.1 | 64/112 | 112 | $552.90 | 1,558,856,671 | 57.29h |
| 5 | Sol Medium | 84.7 | 63/112 | 112 | $426.44 | 567,975,934 | 32.56h |
| 6 | Luna Max | 80.7 | 60/112 | 112 | $140.26 | 1,782,544,024 | 55.39h |
| 7 | Gpt-5.5 High | 78 | 58/112 | 112 | $414.38 | 532,416,980 | 32.32h |
| 8 | Terra High | 78 | 58/112 | 112 | $153.90 | 400,883,315 | 25.40h |
| 9 | Terra Xhigh | 75.3 | 56/112 | 112 | $274.13 | 735,122,124 | 34.04h |
| 10 | Sol Low | 74 | 55/112 | 112 | $250.83 | 285,443,307 | 22.02h |
| 11 | Luna High | 70 | 52/112 | 112 | $72.35 | 794,686,994 | 33.15h |

## Interpretation

- The endpoint provides model-level `score`, pass counts, task counts, tokens, wall time, and estimated cost.
- It does not expose the ten task-level outcomes, so `Weighted /100` cannot be recomputed from this API summary alone.
- Task-weighted rankings remain based on the repository's task matrix and weight snapshots; this report monitors the latest API summary.
- When source data is unchanged, the automation still updates its heartbeat without presenting it as a new benchmark batch.
- The raw API response is not stored in the public repository; only required model-summary fields are archived.

Archived API snapshots: **139**.
