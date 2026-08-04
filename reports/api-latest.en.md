# Codex Radar API Monitor — English

[简体中文](api-latest.zh-CN.md) · [Project home](../README.md) · [API history CSV](../data/api/model_iq_history.csv) · [Monitor status](../data/api/monitor_status.json)

**Last successful check:** `2026-08-04T17:05:17+00:00`  
**Current API snapshot:** `1ef2dfe60cfe3cd1`  
**Source observation:** `2026-07-22T06:57:20.626603+08:00`  
**New snapshot detected:** yes  
**Models returned:** 11

> “Last successful check” confirms that the automation reached the API. “Source observation” is supplied by the upstream endpoint and may be older.

> This is a model-level summary from the Codex Radar API, not the project's task-level difficulty-weighted score.

## Current API model summary

| Rank | Model tier | Source score | Passed | Tasks | Cost | Total tokens | Wall time |
|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | Sol Xhigh | 107.6 | 80/112 | 112 | $761.35 | 949,220,565 | 47.80h |
| 2 | Gpt-5.5 Xhigh | 99.5 | 74/112 | 112 | $653.95 | 771,545,177 | 41.50h |
| 3 | Luna Max | 98.2 | 73/112 | 112 | $58.85 | 1,718,835,727 | 58.48h |
| 4 | Terra Max | 91.5 | 68/112 | 112 | $459.50 | 1,485,907,668 | 59.63h |
| 5 | Sol Medium | 87.4 | 65/112 | 112 | $409.94 | 537,546,494 | 31.54h |
| 6 | Gpt-5.5 High | 86.1 | 64/112 | 112 | $407.75 | 494,514,853 | 30.69h |
| 7 | Sol High | 86.1 | 64/112 | 112 | $590.80 | 669,116,624 | 38.85h |
| 8 | Terra High | 83.4 | 62/112 | 112 | $139.29 | 351,887,577 | 23.60h |
| 9 | Terra Xhigh | 83.4 | 62/112 | 112 | $231.12 | 607,218,070 | 33.49h |
| 10 | Sol Low | 72.6 | 54/112 | 112 | $230.79 | 241,542,565 | 20.31h |
| 11 | Luna High | 71.3 | 53/112 | 112 | $27.57 | 746,693,600 | 29.47h |

## Interpretation

- The endpoint provides model-level `score`, pass counts, task counts, tokens, wall time, and estimated cost.
- It does not expose the ten task-level outcomes, so `Weighted /100` cannot be recomputed from this API summary alone.
- Task-weighted rankings remain based on the repository's task matrix and weight snapshots; this report monitors the latest API summary.
- When source data is unchanged, the automation still updates its heartbeat without presenting it as a new benchmark batch.
- The raw API response is not stored in the public repository; only required model-summary fields are archived.

Archived API snapshots: **170**.
