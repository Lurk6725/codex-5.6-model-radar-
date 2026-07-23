# Codex Radar API Monitor — English

[简体中文](api-latest.zh-CN.md) · [Project home](../README.md) · [API history CSV](../data/api/model_iq_history.csv) · [Monitor status](../data/api/monitor_status.json)

**Last successful check:** `2026-07-23T01:16:22+00:00`  
**Current API snapshot:** `ea8acaf98f4c07ef`  
**Source observation:** `2026-07-22T06:57:20.626603+08:00`  
**New snapshot detected:** yes  
**Models returned:** 11

> “Last successful check” confirms that the automation reached the API. “Source observation” is supplied by the upstream endpoint and may be older.

> This is a model-level summary from the Codex Radar API, not the project's task-level difficulty-weighted score.

## Current API model summary

| Rank | Model tier | Source score | Passed | Tasks | Cost | Total tokens | Wall time |
|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | Terra Max | 98.2 | 73/112 | 112 | $514.52 | 1,331,349,998 | 60.89h |
| 2 | Gpt-5.5 Xhigh | 96.9 | 72/112 | 112 | $654.08 | 843,471,087 | 46.38h |
| 3 | Sol Xhigh | 95.5 | 71/112 | 112 | $771.83 | 1,036,087,223 | 48.86h |
| 4 | Luna Max | 92.8 | 69/112 | 112 | $281.25 | 1,930,658,706 | 65.13h |
| 5 | Sol High | 92.8 | 69/112 | 112 | $641.05 | 878,918,562 | 44.56h |
| 6 | Sol Medium | 91.5 | 68/112 | 112 | $417.38 | 532,606,411 | 32.37h |
| 7 | Terra Xhigh | 88.8 | 66/112 | 112 | $269.57 | 650,472,332 | 35.87h |
| 8 | Gpt-5.5 High | 86.1 | 64/112 | 112 | $428.50 | 540,759,298 | 34.11h |
| 9 | Sol Low | 75.3 | 56/112 | 112 | $238.24 | 278,115,900 | 22.34h |
| 10 | Luna High | 70 | 52/112 | 112 | $112.85 | 714,817,642 | 34.49h |
| 11 | Terra High | 65.9 | 49/112 | 112 | $156.85 | 360,926,427 | 24.61h |

## Interpretation

- The endpoint provides model-level `score`, pass counts, task counts, tokens, wall time, and estimated cost.
- It does not expose the ten task-level outcomes, so `Weighted /100` cannot be recomputed from this API summary alone.
- Task-weighted rankings remain based on the repository's task matrix and weight snapshots; this report monitors the latest API summary.
- When source data is unchanged, the automation still updates its heartbeat without presenting it as a new benchmark batch.
- The raw API response is not stored in the public repository; only required model-summary fields are archived.

Archived API snapshots: **57**.
