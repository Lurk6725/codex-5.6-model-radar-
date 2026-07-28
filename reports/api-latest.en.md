# Codex Radar API Monitor — English

[简体中文](api-latest.zh-CN.md) · [Project home](../README.md) · [API history CSV](../data/api/model_iq_history.csv) · [Monitor status](../data/api/monitor_status.json)

**Last successful check:** `2026-07-28T19:54:56+00:00`  
**Current API snapshot:** `c896489673a3c431`  
**Source observation:** `2026-07-22T06:57:20.626603+08:00`  
**New snapshot detected:** yes  
**Models returned:** 11

> “Last successful check” confirms that the automation reached the API. “Source observation” is supplied by the upstream endpoint and may be older.

> This is a model-level summary from the Codex Radar API, not the project's task-level difficulty-weighted score.

## Current API model summary

| Rank | Model tier | Source score | Passed | Tasks | Cost | Total tokens | Wall time |
|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | Sol Xhigh | 98.2 | 73/112 | 112 | $711.84 | 925,490,402 | 43.91h |
| 2 | Gpt-5.5 Xhigh | 90.1 | 67/112 | 112 | $663.71 | 843,138,254 | 45.66h |
| 3 | Luna Max | 90.1 | 67/112 | 112 | $277.52 | 1,904,562,286 | 61.62h |
| 4 | Sol High | 90.1 | 67/112 | 112 | $571.56 | 732,943,530 | 41.04h |
| 5 | Sol Medium | 90.1 | 67/112 | 112 | $410.91 | 505,364,636 | 31.54h |
| 6 | Terra Max | 90.1 | 67/112 | 112 | $542.52 | 1,432,045,289 | 57.85h |
| 7 | Gpt-5.5 High | 84.7 | 63/112 | 112 | $412.43 | 505,678,496 | 30.05h |
| 8 | Terra Xhigh | 83.4 | 62/112 | 112 | $302.18 | 762,182,386 | 37.03h |
| 9 | Sol Low | 80.7 | 60/112 | 112 | $233.57 | 266,873,116 | 18.13h |
| 10 | Luna High | 74 | 55/112 | 112 | $124.22 | 820,437,758 | 34.08h |
| 11 | Terra High | 72.6 | 54/112 | 112 | $156.18 | 349,080,291 | 23.72h |

## Interpretation

- The endpoint provides model-level `score`, pass counts, task counts, tokens, wall time, and estimated cost.
- It does not expose the ten task-level outcomes, so `Weighted /100` cannot be recomputed from this API summary alone.
- Task-weighted rankings remain based on the repository's task matrix and weight snapshots; this report monitors the latest API summary.
- When source data is unchanged, the automation still updates its heartbeat without presenting it as a new benchmark batch.
- The raw API response is not stored in the public repository; only required model-summary fields are archived.

Archived API snapshots: **106**.
