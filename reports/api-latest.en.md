# Codex Radar API Monitor — English

[简体中文](api-latest.zh-CN.md) · [Project home](../README.md) · [API history CSV](../data/api/model_iq_history.csv) · [Monitor status](../data/api/monitor_status.json)

**Last successful check:** `2026-08-04T07:26:34+00:00`  
**Current API snapshot:** `8e76c01e52070bc3`  
**Source observation:** `2026-07-22T06:57:20.626603+08:00`  
**New snapshot detected:** yes  
**Models returned:** 11

> “Last successful check” confirms that the automation reached the API. “Source observation” is supplied by the upstream endpoint and may be older.

> This is a model-level summary from the Codex Radar API, not the project's task-level difficulty-weighted score.

## Current API model summary

| Rank | Model tier | Source score | Passed | Tasks | Cost | Total tokens | Wall time |
|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | Sol Xhigh | 109 | 81/112 | 112 | $761.36 | 940,352,658 | 47.26h |
| 2 | Luna Max | 98.2 | 73/112 | 112 | $58.67 | 1,721,775,725 | 58.49h |
| 3 | Gpt-5.5 Xhigh | 96.9 | 72/112 | 112 | $655.53 | 768,283,044 | 41.08h |
| 4 | Sol Medium | 91.5 | 68/112 | 112 | $411.23 | 533,680,646 | 30.84h |
| 5 | Terra Max | 90.1 | 67/112 | 112 | $463.53 | 1,488,941,512 | 59.41h |
| 6 | Terra Xhigh | 84.7 | 63/112 | 112 | $231.15 | 607,504,945 | 33.31h |
| 7 | Gpt-5.5 High | 83.4 | 62/112 | 112 | $408.14 | 487,004,191 | 29.88h |
| 8 | Sol High | 83.4 | 62/112 | 112 | $590.37 | 666,828,277 | 38.79h |
| 9 | Terra High | 78 | 58/112 | 112 | $139.90 | 359,371,150 | 23.65h |
| 10 | Sol Low | 74 | 55/112 | 112 | $229.90 | 239,177,589 | 20.19h |
| 11 | Luna High | 71.3 | 53/112 | 112 | $34.75 | 736,530,250 | 29.54h |

## Interpretation

- The endpoint provides model-level `score`, pass counts, task counts, tokens, wall time, and estimated cost.
- It does not expose the ten task-level outcomes, so `Weighted /100` cannot be recomputed from this API summary alone.
- Task-weighted rankings remain based on the repository's task matrix and weight snapshots; this report monitors the latest API summary.
- When source data is unchanged, the automation still updates its heartbeat without presenting it as a new benchmark batch.
- The raw API response is not stored in the public repository; only required model-summary fields are archived.

Archived API snapshots: **167**.
