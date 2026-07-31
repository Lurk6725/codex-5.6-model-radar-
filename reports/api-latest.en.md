# Codex Radar API Monitor — English

[简体中文](api-latest.zh-CN.md) · [Project home](../README.md) · [API history CSV](../data/api/model_iq_history.csv) · [Monitor status](../data/api/monitor_status.json)

**Last successful check:** `2026-07-31T07:16:52+00:00`  
**Current API snapshot:** `7197895a98e926fb`  
**Source observation:** `2026-07-22T06:57:20.626603+08:00`  
**New snapshot detected:** yes  
**Models returned:** 11

> “Last successful check” confirms that the automation reached the API. “Source observation” is supplied by the upstream endpoint and may be older.

> This is a model-level summary from the Codex Radar API, not the project's task-level difficulty-weighted score.

## Current API model summary

| Rank | Model tier | Source score | Passed | Tasks | Cost | Total tokens | Wall time |
|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | Sol Xhigh | 96.9 | 72/112 | 112 | $756.46 | 999,700,735 | 47.41h |
| 2 | Gpt-5.5 Xhigh | 95.5 | 71/112 | 112 | $652.48 | 828,844,704 | 42.31h |
| 3 | Luna Max | 94.2 | 70/112 | 112 | $247.11 | 1,757,752,517 | 57.22h |
| 4 | Sol High | 84.7 | 63/112 | 112 | $611.43 | 812,484,523 | 41.51h |
| 5 | Terra High | 82.1 | 61/112 | 112 | $166.43 | 387,482,121 | 24.64h |
| 6 | Sol Medium | 80.7 | 60/112 | 112 | $439.50 | 556,546,059 | 31.37h |
| 7 | Terra Max | 79.4 | 59/112 | 112 | $574.79 | 1,521,587,272 | 56.01h |
| 8 | Terra Xhigh | 79.4 | 59/112 | 112 | $295.69 | 730,834,435 | 33.59h |
| 9 | Gpt-5.5 High | 76.7 | 57/112 | 112 | $425.53 | 532,456,402 | 32.86h |
| 10 | Sol Low | 74 | 55/112 | 112 | $254.05 | 295,049,672 | 22.45h |
| 11 | Luna High | 68.6 | 51/112 | 112 | $116.81 | 829,736,522 | 34.39h |

## Interpretation

- The endpoint provides model-level `score`, pass counts, task counts, tokens, wall time, and estimated cost.
- It does not expose the ten task-level outcomes, so `Weighted /100` cannot be recomputed from this API summary alone.
- Task-weighted rankings remain based on the repository's task matrix and weight snapshots; this report monitors the latest API summary.
- When source data is unchanged, the automation still updates its heartbeat without presenting it as a new benchmark batch.
- The raw API response is not stored in the public repository; only required model-summary fields are archived.

Archived API snapshots: **130**.
