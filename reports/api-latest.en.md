# Codex Radar API Monitor — English

[简体中文](api-latest.zh-CN.md) · [Project home](../README.md) · [API history CSV](../data/api/model_iq_history.csv) · [Monitor status](../data/api/monitor_status.json)

**Last successful check:** `2026-08-08T00:33:24+00:00`  
**Current API snapshot:** `eabcf1666cfdf32a`  
**Source observation:** `2026-07-22T06:57:20.626603+08:00`  
**New snapshot detected:** no; the source returned the same snapshot  
**Models returned:** 11

> “Last successful check” confirms that the automation reached the API. “Source observation” is supplied by the upstream endpoint and may be older.

> This is a model-level summary from the Codex Radar API, not the project's task-level difficulty-weighted score.

## Current API model summary

| Rank | Model tier | Source score | Passed | Tasks | Cost | Total tokens | Wall time |
|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | Sol Xhigh | 107.6 | 80/112 | 112 | $755.42 | 960,886,764 | 47.88h |
| 2 | Luna Max | 96.9 | 72/112 | 112 | $58.70 | 1,812,992,734 | 62.93h |
| 3 | Gpt-5.5 Xhigh | 94.2 | 70/112 | 112 | $648.74 | 809,225,785 | 41.70h |
| 4 | Gpt-5.5 High | 92.8 | 69/112 | 112 | $407.58 | 496,542,665 | 33.22h |
| 5 | Sol High | 91.5 | 68/112 | 112 | $582.89 | 643,748,806 | 38.30h |
| 6 | Sol Medium | 91.5 | 68/112 | 112 | $410.95 | 550,090,601 | 32.56h |
| 7 | Terra Max | 88.8 | 66/112 | 112 | $456.44 | 1,427,535,287 | 60.36h |
| 8 | Sol Low | 84.7 | 63/112 | 112 | $231.33 | 271,573,831 | 23.40h |
| 9 | Terra Xhigh | 82.1 | 61/112 | 112 | $227.90 | 641,263,757 | 36.48h |
| 10 | Luna High | 80.7 | 60/112 | 112 | $26.47 | 741,807,489 | 31.45h |
| 11 | Terra High | 78 | 58/112 | 112 | $129.67 | 352,496,521 | 25.01h |

## Interpretation

- The endpoint provides model-level `score`, pass counts, task counts, tokens, wall time, and estimated cost.
- It does not expose the ten task-level outcomes, so `Weighted /100` cannot be recomputed from this API summary alone.
- Task-weighted rankings remain based on the repository's task matrix and weight snapshots; this report monitors the latest API summary.
- When source data is unchanged, the automation still updates its heartbeat without presenting it as a new benchmark batch.
- The raw API response is not stored in the public repository; only required model-summary fields are archived.

Archived API snapshots: **197**.
