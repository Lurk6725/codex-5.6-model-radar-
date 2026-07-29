# Codex Radar API Monitor — English

[简体中文](api-latest.zh-CN.md) · [Project home](../README.md) · [API history CSV](../data/api/model_iq_history.csv) · [Monitor status](../data/api/monitor_status.json)

**Last successful check:** `2026-07-29T19:47:13+00:00`  
**Current API snapshot:** `e474dd5e8781660d`  
**Source observation:** `2026-07-22T06:57:20.626603+08:00`  
**New snapshot detected:** yes  
**Models returned:** 11

> “Last successful check” confirms that the automation reached the API. “Source observation” is supplied by the upstream endpoint and may be older.

> This is a model-level summary from the Codex Radar API, not the project's task-level difficulty-weighted score.

## Current API model summary

| Rank | Model tier | Source score | Passed | Tasks | Cost | Total tokens | Wall time |
|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | Terra Max | 99.5 | 74/112 | 112 | $543.12 | 1,433,280,601 | 54.99h |
| 2 | Sol Xhigh | 98.2 | 73/112 | 112 | $738.57 | 975,857,019 | 45.52h |
| 3 | Gpt-5.5 Xhigh | 96.9 | 72/112 | 112 | $656.39 | 836,573,916 | 45.38h |
| 4 | Sol High | 91.5 | 68/112 | 112 | $562.89 | 725,745,813 | 39.85h |
| 5 | Gpt-5.5 High | 88.8 | 66/112 | 112 | $440.22 | 541,819,196 | 32.26h |
| 6 | Terra Xhigh | 84.7 | 63/112 | 112 | $282.61 | 688,656,468 | 35.00h |
| 7 | Sol Medium | 83.4 | 62/112 | 112 | $418.83 | 521,687,916 | 31.70h |
| 8 | Luna Max | 80.7 | 60/112 | 112 | $275.43 | 1,881,546,316 | 63.58h |
| 9 | Sol Low | 80.7 | 60/112 | 112 | $233.76 | 268,537,133 | 21.68h |
| 10 | Terra High | 68.6 | 51/112 | 112 | $154.39 | 346,230,456 | 23.32h |
| 11 | Luna High | 67.3 | 50/112 | 112 | $125.57 | 829,299,537 | 37.12h |

## Interpretation

- The endpoint provides model-level `score`, pass counts, task counts, tokens, wall time, and estimated cost.
- It does not expose the ten task-level outcomes, so `Weighted /100` cannot be recomputed from this API summary alone.
- Task-weighted rankings remain based on the repository's task matrix and weight snapshots; this report monitors the latest API summary.
- When source data is unchanged, the automation still updates its heartbeat without presenting it as a new benchmark batch.
- The raw API response is not stored in the public repository; only required model-summary fields are archived.

Archived API snapshots: **116**.
