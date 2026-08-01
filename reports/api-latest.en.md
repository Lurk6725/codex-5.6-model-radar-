# Codex Radar API Monitor — English

[简体中文](api-latest.zh-CN.md) · [Project home](../README.md) · [API history CSV](../data/api/model_iq_history.csv) · [Monitor status](../data/api/monitor_status.json)

**Last successful check:** `2026-08-01T01:17:42+00:00`  
**Current API snapshot:** `7e77765876fdc967`  
**Source observation:** `2026-07-22T06:57:20.626603+08:00`  
**New snapshot detected:** yes  
**Models returned:** 11

> “Last successful check” confirms that the automation reached the API. “Source observation” is supplied by the upstream endpoint and may be older.

> This is a model-level summary from the Codex Radar API, not the project's task-level difficulty-weighted score.

## Current API model summary

| Rank | Model tier | Source score | Passed | Tasks | Cost | Total tokens | Wall time |
|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | Sol Xhigh | 96.9 | 72/112 | 112 | $774.04 | 1,020,326,413 | 46.97h |
| 2 | Gpt-5.5 Xhigh | 91.5 | 68/112 | 112 | $649.01 | 821,786,734 | 42.56h |
| 3 | Sol High | 90.1 | 67/112 | 112 | $611.17 | 799,943,083 | 41.04h |
| 4 | Sol Medium | 87.4 | 65/112 | 112 | $428.33 | 554,138,359 | 31.86h |
| 5 | Terra Max | 86.1 | 64/112 | 112 | $557.74 | 1,558,004,282 | 56.95h |
| 6 | Terra High | 82.1 | 61/112 | 112 | $156.97 | 375,845,695 | 24.63h |
| 7 | Luna Max | 80.7 | 60/112 | 112 | $140.26 | 1,782,544,024 | 55.39h |
| 8 | Gpt-5.5 High | 78 | 58/112 | 112 | $412.57 | 530,530,269 | 32.54h |
| 9 | Terra Xhigh | 75.3 | 56/112 | 112 | $276.51 | 741,232,242 | 34.01h |
| 10 | Sol Low | 74 | 55/112 | 112 | $250.77 | 286,220,818 | 21.98h |
| 11 | Luna High | 71.3 | 53/112 | 112 | $72.28 | 783,272,002 | 32.42h |

## Interpretation

- The endpoint provides model-level `score`, pass counts, task counts, tokens, wall time, and estimated cost.
- It does not expose the ten task-level outcomes, so `Weighted /100` cannot be recomputed from this API summary alone.
- Task-weighted rankings remain based on the repository's task matrix and weight snapshots; this report monitors the latest API summary.
- When source data is unchanged, the automation still updates its heartbeat without presenting it as a new benchmark batch.
- The raw API response is not stored in the public repository; only required model-summary fields are archived.

Archived API snapshots: **138**.
