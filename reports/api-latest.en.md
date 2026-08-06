# Codex Radar API Monitor — English

[简体中文](api-latest.zh-CN.md) · [Project home](../README.md) · [API history CSV](../data/api/model_iq_history.csv) · [Monitor status](../data/api/monitor_status.json)

**Last successful check:** `2026-08-06T04:32:32+00:00`  
**Current API snapshot:** `280f97556eda84ba`  
**Source observation:** `2026-07-22T06:57:20.626603+08:00`  
**New snapshot detected:** yes  
**Models returned:** 11

> “Last successful check” confirms that the automation reached the API. “Source observation” is supplied by the upstream endpoint and may be older.

> This is a model-level summary from the Codex Radar API, not the project's task-level difficulty-weighted score.

## Current API model summary

| Rank | Model tier | Source score | Passed | Tasks | Cost | Total tokens | Wall time |
|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | Sol Xhigh | 114.3 | 85/112 | 112 | $762.62 | 957,126,792 | 48.11h |
| 2 | Gpt-5.5 Xhigh | 96.9 | 72/112 | 112 | $652.16 | 806,559,996 | 41.68h |
| 3 | Gpt-5.5 High | 95.5 | 71/112 | 112 | $406.66 | 499,133,671 | 31.86h |
| 4 | Sol Medium | 94.2 | 70/112 | 112 | $409.40 | 520,470,657 | 31.78h |
| 5 | Luna Max | 92.8 | 69/112 | 112 | $58.79 | 1,712,969,502 | 60.05h |
| 6 | Terra Max | 92.8 | 69/112 | 112 | $456.54 | 1,492,516,775 | 61.67h |
| 7 | Sol High | 88.8 | 66/112 | 112 | $587.92 | 695,552,558 | 40.07h |
| 8 | Terra Xhigh | 82.1 | 61/112 | 112 | $226.94 | 625,899,266 | 35.23h |
| 9 | Luna High | 78 | 58/112 | 112 | $27.59 | 724,810,810 | 30.27h |
| 10 | Terra High | 75.3 | 56/112 | 112 | $134.17 | 349,036,693 | 24.56h |
| 11 | Sol Low | 74 | 55/112 | 112 | $231.77 | 262,887,824 | 22.04h |

## Interpretation

- The endpoint provides model-level `score`, pass counts, task counts, tokens, wall time, and estimated cost.
- It does not expose the ten task-level outcomes, so `Weighted /100` cannot be recomputed from this API summary alone.
- Task-weighted rankings remain based on the repository's task matrix and weight snapshots; this report monitors the latest API summary.
- When source data is unchanged, the automation still updates its heartbeat without presenting it as a new benchmark batch.
- The raw API response is not stored in the public repository; only required model-summary fields are archived.

Archived API snapshots: **182**.
