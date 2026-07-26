# Codex Radar API Monitor — English

[简体中文](api-latest.zh-CN.md) · [Project home](../README.md) · [API history CSV](../data/api/model_iq_history.csv) · [Monitor status](../data/api/monitor_status.json)

**Last successful check:** `2026-07-26T22:15:38+00:00`  
**Current API snapshot:** `b5235d9bd664c7bb`  
**Source observation:** `2026-07-22T06:57:20.626603+08:00`  
**New snapshot detected:** no; the source returned the same snapshot  
**Models returned:** 11

> “Last successful check” confirms that the automation reached the API. “Source observation” is supplied by the upstream endpoint and may be older.

> This is a model-level summary from the Codex Radar API, not the project's task-level difficulty-weighted score.

## Current API model summary

| Rank | Model tier | Source score | Passed | Tasks | Cost | Total tokens | Wall time |
|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | Sol High | 95.5 | 71/112 | 112 | $584.19 | 747,280,137 | 39.55h |
| 2 | Terra Max | 95.5 | 71/112 | 112 | $533.99 | 1,417,817,680 | 56.08h |
| 3 | Sol Medium | 94.2 | 70/112 | 112 | $423.42 | 527,025,657 | 31.10h |
| 4 | Luna Max | 91.5 | 68/112 | 112 | $275.60 | 1,883,584,850 | 59.47h |
| 5 | Sol Xhigh | 91.5 | 68/112 | 112 | $781.61 | 1,065,940,852 | 51.71h |
| 6 | Gpt-5.5 High | 90.1 | 67/112 | 112 | $408.48 | 512,685,107 | 28.30h |
| 7 | Gpt-5.5 Xhigh | 88.8 | 66/112 | 112 | $672.53 | 873,796,266 | 43.00h |
| 8 | Sol Low | 78 | 58/112 | 112 | $221.67 | 250,329,466 | 18.49h |
| 9 | Terra Xhigh | 76.7 | 57/112 | 112 | $286.80 | 710,804,898 | 34.47h |
| 10 | Luna High | 72.6 | 54/112 | 112 | $114.87 | 736,064,176 | 29.72h |
| 11 | Terra High | 65.9 | 49/112 | 112 | $144.76 | 316,049,497 | 20.30h |

## Interpretation

- The endpoint provides model-level `score`, pass counts, task counts, tokens, wall time, and estimated cost.
- It does not expose the ten task-level outcomes, so `Weighted /100` cannot be recomputed from this API summary alone.
- Task-weighted rankings remain based on the repository's task matrix and weight snapshots; this report monitors the latest API summary.
- When source data is unchanged, the automation still updates its heartbeat without presenting it as a new benchmark batch.
- The raw API response is not stored in the public repository; only required model-summary fields are archived.

Archived API snapshots: **92**.
