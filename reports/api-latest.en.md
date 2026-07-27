# Codex Radar API Monitor — English

[简体中文](api-latest.zh-CN.md) · [Project home](../README.md) · [API history CSV](../data/api/model_iq_history.csv) · [Monitor status](../data/api/monitor_status.json)

**Last successful check:** `2026-07-27T20:45:40+00:00`  
**Current API snapshot:** `5c173195313c27db`  
**Source observation:** `2026-07-22T06:57:20.626603+08:00`  
**New snapshot detected:** no; the source returned the same snapshot  
**Models returned:** 11

> “Last successful check” confirms that the automation reached the API. “Source observation” is supplied by the upstream endpoint and may be older.

> This is a model-level summary from the Codex Radar API, not the project's task-level difficulty-weighted score.

## Current API model summary

| Rank | Model tier | Source score | Passed | Tasks | Cost | Total tokens | Wall time |
|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | Luna Max | 96.9 | 72/112 | 112 | $274.74 | 1,881,722,329 | 59.76h |
| 2 | Sol Medium | 95.5 | 71/112 | 112 | $414.70 | 511,104,390 | 31.25h |
| 3 | Terra Max | 94.2 | 70/112 | 112 | $526.45 | 1,398,907,018 | 55.64h |
| 4 | Sol High | 92.8 | 69/112 | 112 | $584.77 | 744,482,338 | 41.07h |
| 5 | Sol Xhigh | 88.8 | 66/112 | 112 | $807.96 | 1,118,056,388 | 53.18h |
| 6 | Gpt-5.5 Xhigh | 86.1 | 64/112 | 112 | $656.82 | 842,324,102 | 42.67h |
| 7 | Gpt-5.5 High | 83.4 | 62/112 | 112 | $415.15 | 515,126,012 | 30.75h |
| 8 | Terra Xhigh | 80.7 | 60/112 | 112 | $295.69 | 741,943,448 | 37.23h |
| 9 | Sol Low | 75.3 | 56/112 | 112 | $218.66 | 244,712,363 | 19.14h |
| 10 | Luna High | 74 | 55/112 | 112 | $116.32 | 751,488,313 | 30.89h |
| 11 | Terra High | 70 | 52/112 | 112 | $146.07 | 320,303,446 | 21.52h |

## Interpretation

- The endpoint provides model-level `score`, pass counts, task counts, tokens, wall time, and estimated cost.
- It does not expose the ten task-level outcomes, so `Weighted /100` cannot be recomputed from this API summary alone.
- Task-weighted rankings remain based on the repository's task matrix and weight snapshots; this report monitors the latest API summary.
- When source data is unchanged, the automation still updates its heartbeat without presenting it as a new benchmark batch.
- The raw API response is not stored in the public repository; only required model-summary fields are archived.

Archived API snapshots: **97**.
