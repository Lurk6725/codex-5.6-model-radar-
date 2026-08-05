# Codex Radar API Monitor — English

[简体中文](api-latest.zh-CN.md) · [Project home](../README.md) · [API history CSV](../data/api/model_iq_history.csv) · [Monitor status](../data/api/monitor_status.json)

**Last successful check:** `2026-08-05T01:08:11+00:00`  
**Current API snapshot:** `ebc9c83e6f641c18`  
**Source observation:** `2026-07-22T06:57:20.626603+08:00`  
**New snapshot detected:** no; the source returned the same snapshot  
**Models returned:** 11

> “Last successful check” confirms that the automation reached the API. “Source observation” is supplied by the upstream endpoint and may be older.

> This is a model-level summary from the Codex Radar API, not the project's task-level difficulty-weighted score.

## Current API model summary

| Rank | Model tier | Source score | Passed | Tasks | Cost | Total tokens | Wall time |
|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | Sol Xhigh | 107.6 | 80/112 | 112 | $761.86 | 944,616,179 | 47.87h |
| 2 | Gpt-5.5 Xhigh | 98.2 | 73/112 | 112 | $653.83 | 773,317,624 | 41.40h |
| 3 | Luna Max | 98.2 | 73/112 | 112 | $58.85 | 1,718,835,727 | 58.48h |
| 4 | Terra Max | 91.5 | 68/112 | 112 | $459.44 | 1,473,664,322 | 59.49h |
| 5 | Sol Medium | 88.8 | 66/112 | 112 | $409.84 | 538,521,635 | 32.12h |
| 6 | Gpt-5.5 High | 87.4 | 65/112 | 112 | $407.83 | 496,316,494 | 31.31h |
| 7 | Sol High | 86.1 | 64/112 | 112 | $590.76 | 681,311,706 | 39.23h |
| 8 | Terra Xhigh | 84.7 | 63/112 | 112 | $231.10 | 607,693,890 | 33.48h |
| 9 | Terra High | 83.4 | 62/112 | 112 | $139.25 | 351,757,391 | 24.18h |
| 10 | Luna High | 72.6 | 54/112 | 112 | $27.62 | 740,007,348 | 29.89h |
| 11 | Sol Low | 71.3 | 53/112 | 112 | $230.67 | 241,884,378 | 20.50h |

## Interpretation

- The endpoint provides model-level `score`, pass counts, task counts, tokens, wall time, and estimated cost.
- It does not expose the ten task-level outcomes, so `Weighted /100` cannot be recomputed from this API summary alone.
- Task-weighted rankings remain based on the repository's task matrix and weight snapshots; this report monitors the latest API summary.
- When source data is unchanged, the automation still updates its heartbeat without presenting it as a new benchmark batch.
- The raw API response is not stored in the public repository; only required model-summary fields are archived.

Archived API snapshots: **173**.
