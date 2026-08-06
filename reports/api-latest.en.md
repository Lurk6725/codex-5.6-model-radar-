# Codex Radar API Monitor — English

[简体中文](api-latest.zh-CN.md) · [Project home](../README.md) · [API history CSV](../data/api/model_iq_history.csv) · [Monitor status](../data/api/monitor_status.json)

**Last successful check:** `2026-08-06T12:30:44+00:00`  
**Current API snapshot:** `f9d561af98bf1597`  
**Source observation:** `2026-07-22T06:57:20.626603+08:00`  
**New snapshot detected:** no; the source returned the same snapshot  
**Models returned:** 11

> “Last successful check” confirms that the automation reached the API. “Source observation” is supplied by the upstream endpoint and may be older.

> This is a model-level summary from the Codex Radar API, not the project's task-level difficulty-weighted score.

## Current API model summary

| Rank | Model tier | Source score | Passed | Tasks | Cost | Total tokens | Wall time |
|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | Sol Xhigh | 106.3 | 79/112 | 112 | $759.91 | 956,422,635 | 47.87h |
| 2 | Gpt-5.5 High | 95.5 | 71/112 | 112 | $406.63 | 503,189,608 | 32.23h |
| 3 | Sol Medium | 95.5 | 71/112 | 112 | $410.26 | 536,791,168 | 32.06h |
| 4 | Terra Max | 94.2 | 70/112 | 112 | $452.95 | 1,491,544,320 | 61.41h |
| 5 | Gpt-5.5 Xhigh | 91.5 | 68/112 | 112 | $651.47 | 794,240,470 | 41.34h |
| 6 | Luna Max | 90.1 | 67/112 | 112 | $58.86 | 1,731,786,555 | 60.10h |
| 7 | Sol High | 88.8 | 66/112 | 112 | $586.91 | 685,570,810 | 39.91h |
| 8 | Terra Xhigh | 82.1 | 61/112 | 112 | $226.55 | 625,349,615 | 35.92h |
| 9 | Luna High | 78 | 58/112 | 112 | $26.86 | 718,593,167 | 30.88h |
| 10 | Sol Low | 76.7 | 57/112 | 112 | $232.02 | 260,213,460 | 22.30h |
| 11 | Terra High | 75.3 | 56/112 | 112 | $132.45 | 337,815,461 | 24.49h |

## Interpretation

- The endpoint provides model-level `score`, pass counts, task counts, tokens, wall time, and estimated cost.
- It does not expose the ten task-level outcomes, so `Weighted /100` cannot be recomputed from this API summary alone.
- Task-weighted rankings remain based on the repository's task matrix and weight snapshots; this report monitors the latest API summary.
- When source data is unchanged, the automation still updates its heartbeat without presenting it as a new benchmark batch.
- The raw API response is not stored in the public repository; only required model-summary fields are archived.

Archived API snapshots: **184**.
