# Codex Radar API Monitor — English

[简体中文](api-latest.zh-CN.md) · [Project home](../README.md) · [API history CSV](../data/api/model_iq_history.csv) · [Monitor status](../data/api/monitor_status.json)

**Last successful check:** `2026-08-19T18:02:47+00:00`  
**Current API snapshot:** `9b216736abe805d9`  
**Source observation:** `2026-07-22T06:57:20.626603+08:00`  
**New snapshot detected:** no; the source returned the same snapshot  
**Models returned:** 11

> “Last successful check” confirms that the automation reached the API. “Source observation” is supplied by the upstream endpoint and may be older.

> This is a model-level summary from the Codex Radar API, not the project's task-level difficulty-weighted score.

## Current API model summary

| Rank | Model tier | Source score | Passed | Tasks | Cost | Total tokens | Wall time |
|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | Terra Max | 99.5 | 74/112 | 112 | $434.64 | 1,252,578,558 | 59.50h |
| 2 | Sol Xhigh | 98.2 | 73/112 | 112 | $726.91 | 851,223,756 | 45.08h |
| 3 | Gpt-5.5 Xhigh | 96.9 | 72/112 | 112 | $653.56 | 776,634,717 | 41.61h |
| 4 | Luna Max | 92.8 | 69/112 | 112 | $55.20 | 1,820,675,445 | 64.76h |
| 5 | Gpt-5.5 High | 91.5 | 68/112 | 112 | $401.26 | 531,158,701 | 34.37h |
| 6 | Sol High | 87.4 | 65/112 | 112 | $535.55 | 635,747,332 | 35.68h |
| 7 | Terra Xhigh | 84.7 | 63/112 | 112 | $214.77 | 591,561,621 | 37.88h |
| 8 | Sol Medium | 83.4 | 62/112 | 112 | $398.37 | 484,446,533 | 34.03h |
| 9 | Terra High | 75.3 | 56/112 | 112 | $124.93 | 346,320,453 | 25.90h |
| 10 | Luna High | 74 | 55/112 | 112 | $23.49 | 758,355,912 | 34.47h |
| 11 | Sol Low | 72.6 | 54/112 | 112 | $223.85 | 264,062,354 | 24.43h |

## Interpretation

- The endpoint provides model-level `score`, pass counts, task counts, tokens, wall time, and estimated cost.
- It does not expose the ten task-level outcomes, so `Weighted /100` cannot be recomputed from this API summary alone.
- Task-weighted rankings remain based on the repository's task matrix and weight snapshots; this report monitors the latest API summary.
- When source data is unchanged, the automation still updates its heartbeat without presenting it as a new benchmark batch.
- The raw API response is not stored in the public repository; only required model-summary fields are archived.

Archived API snapshots: **298**.
