# Codex Radar API Monitor — English

[简体中文](api-latest.zh-CN.md) · [Project home](../README.md) · [API history CSV](../data/api/model_iq_history.csv) · [Monitor status](../data/api/monitor_status.json)

**Last successful check:** `2026-07-26T15:47:26+00:00`  
**Current API snapshot:** `1063bbc49f9a8565`  
**Source observation:** `2026-07-22T06:57:20.626603+08:00`  
**New snapshot detected:** yes  
**Models returned:** 11

> “Last successful check” confirms that the automation reached the API. “Source observation” is supplied by the upstream endpoint and may be older.

> This is a model-level summary from the Codex Radar API, not the project's task-level difficulty-weighted score.

## Current API model summary

| Rank | Model tier | Source score | Passed | Tasks | Cost | Total tokens | Wall time |
|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | Terra Max | 96.9 | 72/112 | 112 | $532.54 | 1,414,874,058 | 55.91h |
| 2 | Sol High | 94.2 | 70/112 | 112 | $572.83 | 733,435,191 | 37.36h |
| 3 | Sol Medium | 91.5 | 68/112 | 112 | $436.29 | 558,099,778 | 31.12h |
| 4 | Sol Xhigh | 91.5 | 68/112 | 112 | $785.11 | 1,078,006,263 | 50.11h |
| 5 | Luna Max | 90.1 | 67/112 | 112 | $278.87 | 1,903,716,052 | 60.38h |
| 6 | Gpt-5.5 High | 88.8 | 66/112 | 112 | $408.52 | 512,738,907 | 28.35h |
| 7 | Gpt-5.5 Xhigh | 87.4 | 65/112 | 112 | $654.37 | 846,123,584 | 41.88h |
| 8 | Sol Low | 78 | 58/112 | 112 | $221.81 | 249,579,022 | 18.04h |
| 9 | Terra Xhigh | 75.3 | 56/112 | 112 | $277.35 | 677,766,055 | 34.41h |
| 10 | Luna High | 71.3 | 53/112 | 112 | $114.64 | 735,735,621 | 29.56h |
| 11 | Terra High | 68.6 | 51/112 | 112 | $144.59 | 315,397,704 | 20.24h |

## Interpretation

- The endpoint provides model-level `score`, pass counts, task counts, tokens, wall time, and estimated cost.
- It does not expose the ten task-level outcomes, so `Weighted /100` cannot be recomputed from this API summary alone.
- Task-weighted rankings remain based on the repository's task matrix and weight snapshots; this report monitors the latest API summary.
- When source data is unchanged, the automation still updates its heartbeat without presenting it as a new benchmark batch.
- The raw API response is not stored in the public repository; only required model-summary fields are archived.

Archived API snapshots: **91**.
