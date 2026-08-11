# Codex Radar API Monitor — English

[简体中文](api-latest.zh-CN.md) · [Project home](../README.md) · [API history CSV](../data/api/model_iq_history.csv) · [Monitor status](../data/api/monitor_status.json)

**Last successful check:** `2026-08-11T17:43:51+00:00`  
**Current API snapshot:** `f0b8937eaef84bd6`  
**Source observation:** `2026-07-22T06:57:20.626603+08:00`  
**New snapshot detected:** no; the source returned the same snapshot  
**Models returned:** 11

> “Last successful check” confirms that the automation reached the API. “Source observation” is supplied by the upstream endpoint and may be older.

> This is a model-level summary from the Codex Radar API, not the project's task-level difficulty-weighted score.

## Current API model summary

| Rank | Model tier | Source score | Passed | Tasks | Cost | Total tokens | Wall time |
|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | Sol Xhigh | 106.3 | 79/112 | 112 | $736.33 | 889,963,587 | 49.86h |
| 2 | Sol High | 102.2 | 76/112 | 112 | $565.42 | 640,454,222 | 38.36h |
| 3 | Terra Max | 96.9 | 72/112 | 112 | $438.24 | 1,194,824,612 | 54.11h |
| 4 | Gpt-5.5 High | 92.8 | 69/112 | 112 | $404.11 | 486,748,386 | 32.99h |
| 5 | Luna Max | 92.8 | 69/112 | 112 | $58.61 | 1,818,314,856 | 63.38h |
| 6 | Sol Medium | 90.1 | 67/112 | 112 | $408.05 | 471,108,454 | 31.64h |
| 7 | Gpt-5.5 Xhigh | 86.1 | 64/112 | 112 | $657.21 | 763,135,330 | 40.90h |
| 8 | Terra Xhigh | 84.7 | 63/112 | 112 | $219.52 | 562,860,690 | 33.08h |
| 9 | Sol Low | 79.4 | 59/112 | 112 | $229.63 | 281,465,638 | 23.02h |
| 10 | Terra High | 78 | 58/112 | 112 | $127.22 | 331,182,971 | 23.58h |
| 11 | Luna High | 65.9 | 49/112 | 112 | $26.23 | 749,330,450 | 34.41h |

## Interpretation

- The endpoint provides model-level `score`, pass counts, task counts, tokens, wall time, and estimated cost.
- It does not expose the ten task-level outcomes, so `Weighted /100` cannot be recomputed from this API summary alone.
- Task-weighted rankings remain based on the repository's task matrix and weight snapshots; this report monitors the latest API summary.
- When source data is unchanged, the automation still updates its heartbeat without presenting it as a new benchmark batch.
- The raw API response is not stored in the public repository; only required model-summary fields are archived.

Archived API snapshots: **233**.
