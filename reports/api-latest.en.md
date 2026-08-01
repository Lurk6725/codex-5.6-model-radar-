# Codex Radar API Monitor — English

[简体中文](api-latest.zh-CN.md) · [Project home](../README.md) · [API history CSV](../data/api/model_iq_history.csv) · [Monitor status](../data/api/monitor_status.json)

**Last successful check:** `2026-08-01T15:29:51+00:00`  
**Current API snapshot:** `25a491deb50d6c24`  
**Source observation:** `2026-07-22T06:57:20.626603+08:00`  
**New snapshot detected:** no; the source returned the same snapshot  
**Models returned:** 11

> “Last successful check” confirms that the automation reached the API. “Source observation” is supplied by the upstream endpoint and may be older.

> This is a model-level summary from the Codex Radar API, not the project's task-level difficulty-weighted score.

## Current API model summary

| Rank | Model tier | Source score | Passed | Tasks | Cost | Total tokens | Wall time |
|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | Sol Xhigh | 98.2 | 73/112 | 112 | $769.89 | 1,000,095,903 | 47.01h |
| 2 | Gpt-5.5 Xhigh | 92.8 | 69/112 | 112 | $646.21 | 836,072,424 | 43.72h |
| 3 | Sol High | 88.8 | 66/112 | 112 | $610.04 | 799,071,666 | 41.15h |
| 4 | Terra Max | 87.4 | 65/112 | 112 | $532.83 | 1,531,541,319 | 57.33h |
| 5 | Sol Medium | 86.1 | 64/112 | 112 | $422.51 | 580,370,463 | 33.09h |
| 6 | Gpt-5.5 High | 79.4 | 59/112 | 112 | $415.21 | 533,551,635 | 32.58h |
| 7 | Terra High | 78 | 58/112 | 112 | $152.59 | 402,556,657 | 25.69h |
| 8 | Luna Max | 76.7 | 57/112 | 112 | $136.63 | 1,775,738,642 | 56.06h |
| 9 | Sol Low | 74 | 55/112 | 112 | $250.29 | 288,973,750 | 21.56h |
| 10 | Terra Xhigh | 74 | 55/112 | 112 | $271.04 | 735,473,939 | 34.58h |
| 11 | Luna High | 68.6 | 51/112 | 112 | $70.23 | 808,700,439 | 33.70h |

## Interpretation

- The endpoint provides model-level `score`, pass counts, task counts, tokens, wall time, and estimated cost.
- It does not expose the ten task-level outcomes, so `Weighted /100` cannot be recomputed from this API summary alone.
- Task-weighted rankings remain based on the repository's task matrix and weight snapshots; this report monitors the latest API summary.
- When source data is unchanged, the automation still updates its heartbeat without presenting it as a new benchmark batch.
- The raw API response is not stored in the public repository; only required model-summary fields are archived.

Archived API snapshots: **144**.
