# Codex Radar API Monitor — English

[简体中文](api-latest.zh-CN.md) · [Project home](../README.md) · [API history CSV](../data/api/model_iq_history.csv) · [Monitor status](../data/api/monitor_status.json)

**Last successful check:** `2026-08-02T14:03:46+00:00`  
**Current API snapshot:** `f7265782b2a9826d`  
**Source observation:** `2026-07-22T06:57:20.626603+08:00`  
**New snapshot detected:** yes  
**Models returned:** 11

> “Last successful check” confirms that the automation reached the API. “Source observation” is supplied by the upstream endpoint and may be older.

> This is a model-level summary from the Codex Radar API, not the project's task-level difficulty-weighted score.

## Current API model summary

| Rank | Model tier | Source score | Passed | Tasks | Cost | Total tokens | Wall time |
|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | Gpt-5.5 Xhigh | 98.2 | 73/112 | 112 | $654.86 | 818,862,354 | 43.62h |
| 2 | Sol Xhigh | 98.2 | 73/112 | 112 | $772.46 | 969,166,078 | 47.59h |
| 3 | Terra Max | 92.8 | 69/112 | 112 | $517.16 | 1,508,682,443 | 57.96h |
| 4 | Luna Max | 90.1 | 67/112 | 112 | $61.02 | 1,753,724,124 | 60.16h |
| 5 | Sol Medium | 90.1 | 67/112 | 112 | $417.97 | 544,840,190 | 32.88h |
| 6 | Sol High | 84.7 | 63/112 | 112 | $599.90 | 765,641,969 | 42.53h |
| 7 | Terra Xhigh | 79.4 | 59/112 | 112 | $268.84 | 700,336,152 | 34.69h |
| 8 | Gpt-5.5 High | 78 | 58/112 | 112 | $411.40 | 500,094,056 | 31.33h |
| 9 | Terra High | 74 | 55/112 | 112 | $147.69 | 401,552,491 | 26.15h |
| 10 | Sol Low | 72.6 | 54/112 | 112 | $244.96 | 282,794,765 | 21.56h |
| 11 | Luna High | 64.6 | 48/112 | 112 | $55.37 | 786,656,993 | 32.49h |

## Interpretation

- The endpoint provides model-level `score`, pass counts, task counts, tokens, wall time, and estimated cost.
- It does not expose the ten task-level outcomes, so `Weighted /100` cannot be recomputed from this API summary alone.
- Task-weighted rankings remain based on the repository's task matrix and weight snapshots; this report monitors the latest API summary.
- When source data is unchanged, the automation still updates its heartbeat without presenting it as a new benchmark batch.
- The raw API response is not stored in the public repository; only required model-summary fields are archived.

Archived API snapshots: **155**.
