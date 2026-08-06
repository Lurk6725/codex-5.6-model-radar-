# Codex Radar API Monitor — English

[简体中文](api-latest.zh-CN.md) · [Project home](../README.md) · [API history CSV](../data/api/model_iq_history.csv) · [Monitor status](../data/api/monitor_status.json)

**Last successful check:** `2026-08-06T15:00:27+00:00`  
**Current API snapshot:** `dd687c6ca54ad710`  
**Source observation:** `2026-07-22T06:57:20.626603+08:00`  
**New snapshot detected:** yes  
**Models returned:** 11

> “Last successful check” confirms that the automation reached the API. “Source observation” is supplied by the upstream endpoint and may be older.

> This is a model-level summary from the Codex Radar API, not the project's task-level difficulty-weighted score.

## Current API model summary

| Rank | Model tier | Source score | Passed | Tasks | Cost | Total tokens | Wall time |
|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | Sol Xhigh | 106.3 | 79/112 | 112 | $754.62 | 960,958,921 | 47.69h |
| 2 | Gpt-5.5 High | 95.5 | 71/112 | 112 | $407.42 | 505,868,684 | 32.62h |
| 3 | Sol Medium | 95.5 | 71/112 | 112 | $410.18 | 536,421,314 | 31.70h |
| 4 | Gpt-5.5 Xhigh | 94.2 | 70/112 | 112 | $649.07 | 824,187,526 | 42.25h |
| 5 | Terra Max | 94.2 | 70/112 | 112 | $453.04 | 1,483,928,770 | 61.51h |
| 6 | Luna Max | 90.1 | 67/112 | 112 | $58.72 | 1,765,290,473 | 60.62h |
| 7 | Sol High | 87.4 | 65/112 | 112 | $586.81 | 684,656,575 | 39.65h |
| 8 | Terra Xhigh | 83.4 | 62/112 | 112 | $226.45 | 623,391,258 | 35.95h |
| 9 | Luna High | 80.7 | 60/112 | 112 | $26.86 | 726,527,781 | 31.28h |
| 10 | Sol Low | 78 | 58/112 | 112 | $232.00 | 259,852,056 | 22.22h |
| 11 | Terra High | 76.7 | 57/112 | 112 | $131.14 | 341,983,926 | 24.51h |

## Interpretation

- The endpoint provides model-level `score`, pass counts, task counts, tokens, wall time, and estimated cost.
- It does not expose the ten task-level outcomes, so `Weighted /100` cannot be recomputed from this API summary alone.
- Task-weighted rankings remain based on the repository's task matrix and weight snapshots; this report monitors the latest API summary.
- When source data is unchanged, the automation still updates its heartbeat without presenting it as a new benchmark batch.
- The raw API response is not stored in the public repository; only required model-summary fields are archived.

Archived API snapshots: **185**.
