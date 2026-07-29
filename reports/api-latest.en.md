# Codex Radar API Monitor — English

[简体中文](api-latest.zh-CN.md) · [Project home](../README.md) · [API history CSV](../data/api/model_iq_history.csv) · [Monitor status](../data/api/monitor_status.json)

**Last successful check:** `2026-07-29T04:33:58+00:00`  
**Current API snapshot:** `18a83b48764b6d27`  
**Source observation:** `2026-07-22T06:57:20.626603+08:00`  
**New snapshot detected:** yes  
**Models returned:** 11

> “Last successful check” confirms that the automation reached the API. “Source observation” is supplied by the upstream endpoint and may be older.

> This is a model-level summary from the Codex Radar API, not the project's task-level difficulty-weighted score.

## Current API model summary

| Rank | Model tier | Source score | Passed | Tasks | Cost | Total tokens | Wall time |
|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | Sol Xhigh | 104.9 | 78/112 | 112 | $709.57 | 924,365,937 | 40.22h |
| 2 | Gpt-5.5 Xhigh | 92.8 | 69/112 | 112 | $673.10 | 857,730,945 | 45.90h |
| 3 | Luna Max | 91.5 | 68/112 | 112 | $282.20 | 1,943,505,539 | 62.86h |
| 4 | Terra Max | 91.5 | 68/112 | 112 | $543.22 | 1,435,629,062 | 57.96h |
| 5 | Sol High | 88.8 | 66/112 | 112 | $572.77 | 734,475,082 | 40.95h |
| 6 | Sol Medium | 87.4 | 65/112 | 112 | $418.08 | 514,344,530 | 30.33h |
| 7 | Terra Xhigh | 86.1 | 64/112 | 112 | $307.57 | 776,548,267 | 37.58h |
| 8 | Gpt-5.5 High | 83.4 | 62/112 | 112 | $410.45 | 503,626,681 | 30.27h |
| 9 | Sol Low | 83.4 | 62/112 | 112 | $231.00 | 264,127,189 | 17.60h |
| 10 | Luna High | 75.3 | 56/112 | 112 | $123.93 | 818,052,360 | 34.08h |
| 11 | Terra High | 71.3 | 53/112 | 112 | $155.78 | 348,069,618 | 23.47h |

## Interpretation

- The endpoint provides model-level `score`, pass counts, task counts, tokens, wall time, and estimated cost.
- It does not expose the ten task-level outcomes, so `Weighted /100` cannot be recomputed from this API summary alone.
- Task-weighted rankings remain based on the repository's task matrix and weight snapshots; this report monitors the latest API summary.
- When source data is unchanged, the automation still updates its heartbeat without presenting it as a new benchmark batch.
- The raw API response is not stored in the public repository; only required model-summary fields are archived.

Archived API snapshots: **109**.
