# Codex Radar API Monitor — English

[简体中文](api-latest.zh-CN.md) · [Project home](../README.md) · [API history CSV](../data/api/model_iq_history.csv) · [Monitor status](../data/api/monitor_status.json)

**Last successful check:** `2026-07-25T17:18:19+00:00`  
**Current API snapshot:** `4eb9f978419d0fa2`  
**Source observation:** `2026-07-22T06:57:20.626603+08:00`  
**New snapshot detected:** yes  
**Models returned:** 11

> “Last successful check” confirms that the automation reached the API. “Source observation” is supplied by the upstream endpoint and may be older.

> This is a model-level summary from the Codex Radar API, not the project's task-level difficulty-weighted score.

## Current API model summary

| Rank | Model tier | Source score | Passed | Tasks | Cost | Total tokens | Wall time |
|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | Sol Xhigh | 99.5 | 74/112 | 112 | $769.87 | 1,040,870,639 | 46.80h |
| 2 | Sol Medium | 95.5 | 71/112 | 112 | $441.91 | 568,153,141 | 30.73h |
| 3 | Sol High | 92.8 | 69/112 | 112 | $578.55 | 766,810,610 | 34.84h |
| 4 | Terra Max | 90.1 | 67/112 | 112 | $568.04 | 1,496,296,086 | 58.84h |
| 5 | Terra Xhigh | 90.1 | 67/112 | 112 | $282.08 | 684,534,756 | 37.22h |
| 6 | Luna Max | 83.4 | 62/112 | 112 | $285.90 | 1,970,347,789 | 61.31h |
| 7 | Gpt-5.5 Xhigh | 82.1 | 61/112 | 112 | $650.98 | 836,141,035 | 44.53h |
| 8 | Gpt-5.5 High | 79.4 | 59/112 | 112 | $421.44 | 526,421,474 | 32.41h |
| 9 | Sol Low | 76.7 | 57/112 | 112 | $235.09 | 268,143,883 | 20.32h |
| 10 | Terra High | 72.6 | 54/112 | 112 | $156.81 | 356,299,155 | 23.16h |
| 11 | Luna High | 67.3 | 50/112 | 112 | $114.45 | 738,375,126 | 32.36h |

## Interpretation

- The endpoint provides model-level `score`, pass counts, task counts, tokens, wall time, and estimated cost.
- It does not expose the ten task-level outcomes, so `Weighted /100` cannot be recomputed from this API summary alone.
- Task-weighted rankings remain based on the repository's task matrix and weight snapshots; this report monitors the latest API summary.
- When source data is unchanged, the automation still updates its heartbeat without presenting it as a new benchmark batch.
- The raw API response is not stored in the public repository; only required model-summary fields are archived.

Archived API snapshots: **82**.
