# Codex Radar API Monitor — English

[简体中文](api-latest.zh-CN.md) · [Project home](../README.md) · [API history CSV](../data/api/model_iq_history.csv) · [Monitor status](../data/api/monitor_status.json)

**Last successful check:** `2026-08-02T18:45:13+00:00`  
**Current API snapshot:** `26e1e7fb5fda397b`  
**Source observation:** `2026-07-22T06:57:20.626603+08:00`  
**New snapshot detected:** yes  
**Models returned:** 11

> “Last successful check” confirms that the automation reached the API. “Source observation” is supplied by the upstream endpoint and may be older.

> This is a model-level summary from the Codex Radar API, not the project's task-level difficulty-weighted score.

## Current API model summary

| Rank | Model tier | Source score | Passed | Tasks | Cost | Total tokens | Wall time |
|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | Gpt-5.5 Xhigh | 100.9 | 75/112 | 112 | $656.34 | 817,595,857 | 44.08h |
| 2 | Sol Xhigh | 96.9 | 72/112 | 112 | $772.78 | 967,917,576 | 47.85h |
| 3 | Terra Max | 94.2 | 70/112 | 112 | $517.44 | 1,484,884,105 | 57.69h |
| 4 | Luna Max | 90.1 | 67/112 | 112 | $61.02 | 1,753,724,124 | 60.16h |
| 5 | Sol Medium | 87.4 | 65/112 | 112 | $417.43 | 540,802,918 | 32.65h |
| 6 | Sol High | 84.7 | 63/112 | 112 | $599.99 | 764,658,383 | 42.53h |
| 7 | Terra Xhigh | 80.7 | 60/112 | 112 | $262.52 | 680,703,236 | 34.54h |
| 8 | Gpt-5.5 High | 79.4 | 59/112 | 112 | $412.10 | 500,843,540 | 31.39h |
| 9 | Terra High | 72.6 | 54/112 | 112 | $147.77 | 396,770,492 | 25.81h |
| 10 | Sol Low | 71.3 | 53/112 | 112 | $243.42 | 279,125,699 | 21.48h |
| 11 | Luna High | 68.6 | 51/112 | 112 | $43.19 | 768,794,314 | 31.90h |

## Interpretation

- The endpoint provides model-level `score`, pass counts, task counts, tokens, wall time, and estimated cost.
- It does not expose the ten task-level outcomes, so `Weighted /100` cannot be recomputed from this API summary alone.
- Task-weighted rankings remain based on the repository's task matrix and weight snapshots; this report monitors the latest API summary.
- When source data is unchanged, the automation still updates its heartbeat without presenting it as a new benchmark batch.
- The raw API response is not stored in the public repository; only required model-summary fields are archived.

Archived API snapshots: **157**.
