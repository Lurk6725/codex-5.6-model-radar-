# Codex Radar API Monitor — English

[简体中文](api-latest.zh-CN.md) · [Project home](../README.md) · [API history CSV](../data/api/model_iq_history.csv) · [Monitor status](../data/api/monitor_status.json)

**Last successful check:** `2026-08-23T18:50:25+00:00`  
**Current API snapshot:** `25929dacfd198c06`  
**Source observation:** `2026-07-22T06:57:20.626603+08:00`  
**New snapshot detected:** no; the source returned the same snapshot  
**Models returned:** 11

> “Last successful check” confirms that the automation reached the API. “Source observation” is supplied by the upstream endpoint and may be older.

> This is a model-level summary from the Codex Radar API, not the project's task-level difficulty-weighted score.

## Current API model summary

| Rank | Model tier | Source score | Passed | Tasks | Cost | Total tokens | Wall time |
|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | Sol Xhigh | 102.2 | 76/112 | 112 | $719.32 | 833,936,105 | 43.96h |
| 2 | Gpt-5.5 Xhigh | 98.2 | 73/112 | 112 | $651.15 | 779,497,345 | 41.93h |
| 3 | Terra Max | 95.5 | 71/112 | 112 | $427.42 | 1,156,714,427 | 55.55h |
| 4 | Gpt-5.5 High | 91.5 | 68/112 | 112 | $401.67 | 520,132,088 | 33.94h |
| 5 | Luna Max | 87.4 | 65/112 | 112 | $54.44 | 1,704,463,553 | 59.45h |
| 6 | Terra Xhigh | 87.4 | 65/112 | 112 | $213.63 | 582,963,817 | 37.10h |
| 7 | Sol High | 86.1 | 64/112 | 112 | $534.47 | 582,271,707 | 35.63h |
| 8 | Sol Medium | 83.4 | 62/112 | 112 | $404.68 | 458,081,443 | 33.21h |
| 9 | Terra High | 76.7 | 57/112 | 112 | $124.79 | 338,446,278 | 24.95h |
| 10 | Luna High | 75.3 | 56/112 | 112 | $22.64 | 688,817,532 | 29.96h |
| 11 | Sol Low | 72.6 | 54/112 | 112 | $222.93 | 262,962,744 | 23.91h |

## Interpretation

- The endpoint provides model-level `score`, pass counts, task counts, tokens, wall time, and estimated cost.
- It does not expose the ten task-level outcomes, so `Weighted /100` cannot be recomputed from this API summary alone.
- Task-weighted rankings remain based on the repository's task matrix and weight snapshots; this report monitors the latest API summary.
- When source data is unchanged, the automation still updates its heartbeat without presenting it as a new benchmark batch.
- The raw API response is not stored in the public repository; only required model-summary fields are archived.

Archived API snapshots: **334**.
