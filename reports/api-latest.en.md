# Codex Radar API Monitor — English

[简体中文](api-latest.zh-CN.md) · [Project home](../README.md) · [API history CSV](../data/api/model_iq_history.csv) · [Monitor status](../data/api/monitor_status.json)

**Last successful check:** `2026-07-28T12:16:49+00:00`  
**Current API snapshot:** `e1ed0ac13b2152f3`  
**Source observation:** `2026-07-22T06:57:20.626603+08:00`  
**New snapshot detected:** yes  
**Models returned:** 11

> “Last successful check” confirms that the automation reached the API. “Source observation” is supplied by the upstream endpoint and may be older.

> This is a model-level summary from the Codex Radar API, not the project's task-level difficulty-weighted score.

## Current API model summary

| Rank | Model tier | Source score | Passed | Tasks | Cost | Total tokens | Wall time |
|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | Sol Xhigh | 96.9 | 72/112 | 112 | $743.08 | 979,223,065 | 45.00h |
| 2 | Sol High | 92.8 | 69/112 | 112 | $572.19 | 732,755,729 | 40.12h |
| 3 | Sol Medium | 92.8 | 69/112 | 112 | $398.78 | 487,246,336 | 30.88h |
| 4 | Luna Max | 90.1 | 67/112 | 112 | $277.43 | 1,902,154,844 | 61.36h |
| 5 | Terra Max | 90.1 | 67/112 | 112 | $535.85 | 1,414,015,297 | 57.14h |
| 6 | Gpt-5.5 Xhigh | 88.8 | 66/112 | 112 | $664.26 | 854,183,865 | 44.84h |
| 7 | Gpt-5.5 High | 83.4 | 62/112 | 112 | $407.55 | 496,499,762 | 29.75h |
| 8 | Terra Xhigh | 80.7 | 60/112 | 112 | $300.22 | 756,344,118 | 36.88h |
| 9 | Sol Low | 75.3 | 56/112 | 112 | $225.19 | 252,927,104 | 19.63h |
| 10 | Luna High | 72.6 | 54/112 | 112 | $122.50 | 804,224,844 | 33.27h |
| 11 | Terra High | 71.3 | 53/112 | 112 | $154.79 | 345,996,896 | 23.03h |

## Interpretation

- The endpoint provides model-level `score`, pass counts, task counts, tokens, wall time, and estimated cost.
- It does not expose the ten task-level outcomes, so `Weighted /100` cannot be recomputed from this API summary alone.
- Task-weighted rankings remain based on the repository's task matrix and weight snapshots; this report monitors the latest API summary.
- When source data is unchanged, the automation still updates its heartbeat without presenting it as a new benchmark batch.
- The raw API response is not stored in the public repository; only required model-summary fields are archived.

Archived API snapshots: **103**.
