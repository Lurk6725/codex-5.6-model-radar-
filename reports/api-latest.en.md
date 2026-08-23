# Codex Radar API Monitor — English

[简体中文](api-latest.zh-CN.md) · [Project home](../README.md) · [API history CSV](../data/api/model_iq_history.csv) · [Monitor status](../data/api/monitor_status.json)

**Last successful check:** `2026-08-23T23:38:50+00:00`  
**Current API snapshot:** `b57ab436bcfd9db9`  
**Source observation:** `2026-07-22T06:57:20.626603+08:00`  
**New snapshot detected:** yes  
**Models returned:** 11

> “Last successful check” confirms that the automation reached the API. “Source observation” is supplied by the upstream endpoint and may be older.

> This is a model-level summary from the Codex Radar API, not the project's task-level difficulty-weighted score.

## Current API model summary

| Rank | Model tier | Source score | Passed | Tasks | Cost | Total tokens | Wall time |
|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | Sol Xhigh | 100.9 | 75/112 | 112 | $717.45 | 806,366,218 | 42.81h |
| 2 | Gpt-5.5 Xhigh | 99.5 | 74/112 | 112 | $649.18 | 778,134,788 | 40.42h |
| 3 | Terra Max | 95.5 | 71/112 | 112 | $426.10 | 1,162,069,554 | 55.06h |
| 4 | Luna Max | 90.1 | 67/112 | 112 | $54.41 | 1,712,398,124 | 58.27h |
| 5 | Gpt-5.5 High | 88.8 | 66/112 | 112 | $400.67 | 498,069,680 | 32.21h |
| 6 | Sol High | 87.4 | 65/112 | 112 | $531.15 | 567,498,903 | 34.61h |
| 7 | Terra Xhigh | 86.1 | 64/112 | 112 | $213.16 | 583,461,987 | 35.95h |
| 8 | Sol Medium | 80.7 | 60/112 | 112 | $403.02 | 444,118,501 | 31.31h |
| 9 | Terra High | 76.7 | 57/112 | 112 | $124.74 | 333,710,697 | 24.36h |
| 10 | Luna High | 75.3 | 56/112 | 112 | $22.62 | 702,769,684 | 29.96h |
| 11 | Sol Low | 72.6 | 54/112 | 112 | $222.74 | 258,968,889 | 22.48h |

## Interpretation

- The endpoint provides model-level `score`, pass counts, task counts, tokens, wall time, and estimated cost.
- It does not expose the ten task-level outcomes, so `Weighted /100` cannot be recomputed from this API summary alone.
- Task-weighted rankings remain based on the repository's task matrix and weight snapshots; this report monitors the latest API summary.
- When source data is unchanged, the automation still updates its heartbeat without presenting it as a new benchmark batch.
- The raw API response is not stored in the public repository; only required model-summary fields are archived.

Archived API snapshots: **337**.
