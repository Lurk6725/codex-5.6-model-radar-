# Codex Radar API Monitor — English

[简体中文](api-latest.zh-CN.md) · [Project home](../README.md) · [API history CSV](../data/api/model_iq_history.csv) · [Monitor status](../data/api/monitor_status.json)

**Last successful check:** `2026-07-31T10:01:20+00:00`  
**Current API snapshot:** `964ea813120c4943`  
**Source observation:** `2026-07-22T06:57:20.626603+08:00`  
**New snapshot detected:** yes  
**Models returned:** 11

> “Last successful check” confirms that the automation reached the API. “Source observation” is supplied by the upstream endpoint and may be older.

> This is a model-level summary from the Codex Radar API, not the project's task-level difficulty-weighted score.

## Current API model summary

| Rank | Model tier | Source score | Passed | Tasks | Cost | Total tokens | Wall time |
|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | Sol Xhigh | 98.2 | 73/112 | 112 | $766.02 | 998,074,545 | 46.77h |
| 2 | Gpt-5.5 Xhigh | 92.8 | 69/112 | 112 | $653.07 | 826,800,948 | 42.53h |
| 3 | Luna Max | 90.1 | 67/112 | 112 | $206.98 | 1,726,245,459 | 55.71h |
| 4 | Sol High | 86.1 | 64/112 | 112 | $607.40 | 805,929,536 | 41.28h |
| 5 | Terra High | 84.7 | 63/112 | 112 | $166.03 | 387,462,660 | 24.55h |
| 6 | Sol Medium | 80.7 | 60/112 | 112 | $435.36 | 552,637,632 | 31.51h |
| 7 | Terra Max | 80.7 | 60/112 | 112 | $571.06 | 1,499,249,633 | 55.74h |
| 8 | Terra Xhigh | 79.4 | 59/112 | 112 | $294.34 | 729,908,169 | 33.52h |
| 9 | Gpt-5.5 High | 76.7 | 57/112 | 112 | $423.07 | 528,365,248 | 32.91h |
| 10 | Luna High | 70 | 52/112 | 112 | $97.03 | 821,014,702 | 33.66h |
| 11 | Sol Low | 70 | 52/112 | 112 | $253.41 | 294,234,809 | 21.84h |

## Interpretation

- The endpoint provides model-level `score`, pass counts, task counts, tokens, wall time, and estimated cost.
- It does not expose the ten task-level outcomes, so `Weighted /100` cannot be recomputed from this API summary alone.
- Task-weighted rankings remain based on the repository's task matrix and weight snapshots; this report monitors the latest API summary.
- When source data is unchanged, the automation still updates its heartbeat without presenting it as a new benchmark batch.
- The raw API response is not stored in the public repository; only required model-summary fields are archived.

Archived API snapshots: **131**.
