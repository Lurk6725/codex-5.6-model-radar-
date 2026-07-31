# Codex Radar API Monitor — English

[简体中文](api-latest.zh-CN.md) · [Project home](../README.md) · [API history CSV](../data/api/model_iq_history.csv) · [Monitor status](../data/api/monitor_status.json)

**Last successful check:** `2026-07-31T03:56:46+00:00`  
**Current API snapshot:** `225845cf1f6258fd`  
**Source observation:** `2026-07-22T06:57:20.626603+08:00`  
**New snapshot detected:** yes  
**Models returned:** 11

> “Last successful check” confirms that the automation reached the API. “Source observation” is supplied by the upstream endpoint and may be older.

> This is a model-level summary from the Codex Radar API, not the project's task-level difficulty-weighted score.

## Current API model summary

| Rank | Model tier | Source score | Passed | Tasks | Cost | Total tokens | Wall time |
|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | Sol Xhigh | 94.2 | 70/112 | 112 | $743.33 | 980,577,312 | 46.81h |
| 2 | Luna Max | 92.8 | 69/112 | 112 | $265.67 | 1,805,505,661 | 59.37h |
| 3 | Gpt-5.5 Xhigh | 90.1 | 67/112 | 112 | $649.83 | 826,889,822 | 43.11h |
| 4 | Sol High | 88.8 | 66/112 | 112 | $624.02 | 835,503,810 | 41.68h |
| 5 | Terra Max | 82.1 | 61/112 | 112 | $572.15 | 1,502,429,698 | 54.81h |
| 6 | Gpt-5.5 High | 80.7 | 60/112 | 112 | $427.00 | 533,622,357 | 32.85h |
| 7 | Terra Xhigh | 80.7 | 60/112 | 112 | $298.54 | 732,516,583 | 33.67h |
| 8 | Sol Medium | 79.4 | 59/112 | 112 | $438.59 | 555,909,926 | 31.16h |
| 9 | Terra High | 78 | 58/112 | 112 | $167.23 | 380,876,712 | 24.04h |
| 10 | Sol Low | 75.3 | 56/112 | 112 | $252.14 | 293,181,372 | 22.41h |
| 11 | Luna High | 64.6 | 48/112 | 112 | $127.30 | 846,511,871 | 35.38h |

## Interpretation

- The endpoint provides model-level `score`, pass counts, task counts, tokens, wall time, and estimated cost.
- It does not expose the ten task-level outcomes, so `Weighted /100` cannot be recomputed from this API summary alone.
- Task-weighted rankings remain based on the repository's task matrix and weight snapshots; this report monitors the latest API summary.
- When source data is unchanged, the automation still updates its heartbeat without presenting it as a new benchmark batch.
- The raw API response is not stored in the public repository; only required model-summary fields are archived.

Archived API snapshots: **129**.
