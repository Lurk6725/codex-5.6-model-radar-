# Codex Radar API Monitor — English

[简体中文](api-latest.zh-CN.md) · [Project home](../README.md) · [API history CSV](../data/api/model_iq_history.csv) · [Monitor status](../data/api/monitor_status.json)

**Last successful check:** `2026-08-02T22:13:01+00:00`  
**Current API snapshot:** `25753bca5ce99573`  
**Source observation:** `2026-07-22T06:57:20.626603+08:00`  
**New snapshot detected:** yes  
**Models returned:** 11

> “Last successful check” confirms that the automation reached the API. “Source observation” is supplied by the upstream endpoint and may be older.

> This is a model-level summary from the Codex Radar API, not the project's task-level difficulty-weighted score.

## Current API model summary

| Rank | Model tier | Source score | Passed | Tasks | Cost | Total tokens | Wall time |
|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | Gpt-5.5 Xhigh | 100.9 | 75/112 | 112 | $656.90 | 816,800,442 | 43.41h |
| 2 | Sol Xhigh | 96.9 | 72/112 | 112 | $772.38 | 964,921,538 | 47.64h |
| 3 | Terra Max | 94.2 | 70/112 | 112 | $517.44 | 1,484,884,105 | 57.69h |
| 4 | Luna Max | 90.1 | 67/112 | 112 | $61.07 | 1,753,780,943 | 60.36h |
| 5 | Sol Medium | 87.4 | 65/112 | 112 | $417.43 | 540,802,918 | 32.65h |
| 6 | Sol High | 84.7 | 63/112 | 112 | $599.61 | 780,087,518 | 42.91h |
| 7 | Gpt-5.5 High | 80.7 | 60/112 | 112 | $412.41 | 501,736,997 | 31.54h |
| 8 | Terra Xhigh | 80.7 | 60/112 | 112 | $262.48 | 687,322,229 | 34.80h |
| 9 | Terra High | 72.6 | 54/112 | 112 | $147.77 | 396,770,492 | 25.81h |
| 10 | Sol Low | 71.3 | 53/112 | 112 | $243.42 | 279,125,699 | 21.48h |
| 11 | Luna High | 67.3 | 50/112 | 112 | $43.17 | 760,703,163 | 31.55h |

## Interpretation

- The endpoint provides model-level `score`, pass counts, task counts, tokens, wall time, and estimated cost.
- It does not expose the ten task-level outcomes, so `Weighted /100` cannot be recomputed from this API summary alone.
- Task-weighted rankings remain based on the repository's task matrix and weight snapshots; this report monitors the latest API summary.
- When source data is unchanged, the automation still updates its heartbeat without presenting it as a new benchmark batch.
- The raw API response is not stored in the public repository; only required model-summary fields are archived.

Archived API snapshots: **159**.
