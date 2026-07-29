# Codex Radar API Monitor — English

[简体中文](api-latest.zh-CN.md) · [Project home](../README.md) · [API history CSV](../data/api/model_iq_history.csv) · [Monitor status](../data/api/monitor_status.json)

**Last successful check:** `2026-07-29T10:20:19+00:00`  
**Current API snapshot:** `fe23a87d009a8965`  
**Source observation:** `2026-07-22T06:57:20.626603+08:00`  
**New snapshot detected:** yes  
**Models returned:** 11

> “Last successful check” confirms that the automation reached the API. “Source observation” is supplied by the upstream endpoint and may be older.

> This is a model-level summary from the Codex Radar API, not the project's task-level difficulty-weighted score.

## Current API model summary

| Rank | Model tier | Source score | Passed | Tasks | Cost | Total tokens | Wall time |
|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | Sol Xhigh | 106.3 | 79/112 | 112 | $708.53 | 922,819,141 | 39.82h |
| 2 | Gpt-5.5 Xhigh | 92.8 | 69/112 | 112 | $670.71 | 856,610,306 | 46.52h |
| 3 | Terra Max | 92.8 | 69/112 | 112 | $543.58 | 1,442,497,108 | 55.14h |
| 4 | Luna Max | 91.5 | 68/112 | 112 | $279.29 | 1,916,351,217 | 62.42h |
| 5 | Sol High | 87.4 | 65/112 | 112 | $570.87 | 740,763,779 | 41.42h |
| 6 | Sol Medium | 87.4 | 65/112 | 112 | $416.42 | 510,967,690 | 30.07h |
| 7 | Terra Xhigh | 87.4 | 65/112 | 112 | $295.98 | 732,652,580 | 36.42h |
| 8 | Sol Low | 84.7 | 63/112 | 112 | $233.63 | 266,711,555 | 19.41h |
| 9 | Gpt-5.5 High | 82.1 | 61/112 | 112 | $423.42 | 517,930,503 | 31.25h |
| 10 | Luna High | 74 | 55/112 | 112 | $127.53 | 845,532,113 | 37.09h |
| 11 | Terra High | 72.6 | 54/112 | 112 | $158.86 | 359,020,151 | 23.89h |

## Interpretation

- The endpoint provides model-level `score`, pass counts, task counts, tokens, wall time, and estimated cost.
- It does not expose the ten task-level outcomes, so `Weighted /100` cannot be recomputed from this API summary alone.
- Task-weighted rankings remain based on the repository's task matrix and weight snapshots; this report monitors the latest API summary.
- When source data is unchanged, the automation still updates its heartbeat without presenting it as a new benchmark batch.
- The raw API response is not stored in the public repository; only required model-summary fields are archived.

Archived API snapshots: **111**.
