# Codex Radar API Monitor — English

[简体中文](api-latest.zh-CN.md) · [Project home](../README.md) · [API history CSV](../data/api/model_iq_history.csv) · [Monitor status](../data/api/monitor_status.json)

**Last successful check:** `2026-08-23T02:01:44+00:00`  
**Current API snapshot:** `2054016af716a2e0`  
**Source observation:** `2026-07-22T06:57:20.626603+08:00`  
**New snapshot detected:** yes  
**Models returned:** 11

> “Last successful check” confirms that the automation reached the API. “Source observation” is supplied by the upstream endpoint and may be older.

> This is a model-level summary from the Codex Radar API, not the project's task-level difficulty-weighted score.

## Current API model summary

| Rank | Model tier | Source score | Passed | Tasks | Cost | Total tokens | Wall time |
|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | Sol Xhigh | 102.2 | 76/112 | 112 | $722.63 | 843,736,732 | 43.64h |
| 2 | Gpt-5.5 Xhigh | 98.2 | 73/112 | 112 | $652.21 | 777,214,772 | 42.16h |
| 3 | Terra Max | 95.5 | 71/112 | 112 | $431.90 | 1,169,389,607 | 56.40h |
| 4 | Gpt-5.5 High | 94.2 | 70/112 | 112 | $401.53 | 526,928,753 | 34.33h |
| 5 | Luna Max | 87.4 | 65/112 | 112 | $54.38 | 1,717,356,669 | 59.88h |
| 6 | Sol High | 86.1 | 64/112 | 112 | $535.03 | 633,086,093 | 35.95h |
| 7 | Terra Xhigh | 84.7 | 63/112 | 112 | $213.79 | 579,303,874 | 37.07h |
| 8 | Sol Medium | 83.4 | 62/112 | 112 | $404.58 | 464,153,609 | 34.17h |
| 9 | Luna High | 76.7 | 57/112 | 112 | $22.64 | 684,439,628 | 30.09h |
| 10 | Sol Low | 74 | 55/112 | 112 | $223.66 | 261,552,240 | 24.14h |
| 11 | Terra High | 74 | 55/112 | 112 | $124.91 | 335,190,382 | 24.83h |

## Interpretation

- The endpoint provides model-level `score`, pass counts, task counts, tokens, wall time, and estimated cost.
- It does not expose the ten task-level outcomes, so `Weighted /100` cannot be recomputed from this API summary alone.
- Task-weighted rankings remain based on the repository's task matrix and weight snapshots; this report monitors the latest API summary.
- When source data is unchanged, the automation still updates its heartbeat without presenting it as a new benchmark batch.
- The raw API response is not stored in the public repository; only required model-summary fields are archived.

Archived API snapshots: **328**.
