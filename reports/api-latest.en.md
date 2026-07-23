# Codex Radar API Monitor — English

[简体中文](api-latest.zh-CN.md) · [Project home](../README.md) · [API history CSV](../data/api/model_iq_history.csv) · [Monitor status](../data/api/monitor_status.json)

**Last successful check:** `2026-07-23T10:06:36+00:00`  
**Current API snapshot:** `bcb972340216cc0b`  
**Source observation:** `2026-07-22T06:57:20.626603+08:00`  
**New snapshot detected:** yes  
**Models returned:** 11

> “Last successful check” confirms that the automation reached the API. “Source observation” is supplied by the upstream endpoint and may be older.

> This is a model-level summary from the Codex Radar API, not the project's task-level difficulty-weighted score.

## Current API model summary

| Rank | Model tier | Source score | Passed | Tasks | Cost | Total tokens | Wall time |
|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | Sol Xhigh | 98.2 | 73/112 | 112 | $783.94 | 1,068,818,391 | 48.78h |
| 2 | Terra Max | 98.2 | 73/112 | 112 | $519.61 | 1,350,747,805 | 60.44h |
| 3 | Sol Medium | 95.5 | 71/112 | 112 | $425.00 | 539,198,786 | 31.64h |
| 4 | Sol High | 91.5 | 68/112 | 112 | $656.81 | 906,291,471 | 43.44h |
| 5 | Gpt-5.5 Xhigh | 90.1 | 67/112 | 112 | $647.22 | 833,151,452 | 46.47h |
| 6 | Terra Xhigh | 90.1 | 67/112 | 112 | $270.73 | 653,567,802 | 36.03h |
| 7 | Luna Max | 84.7 | 63/112 | 112 | $281.40 | 1,931,937,671 | 62.73h |
| 8 | Gpt-5.5 High | 83.4 | 62/112 | 112 | $434.14 | 550,733,609 | 35.13h |
| 9 | Sol Low | 76.7 | 57/112 | 112 | $237.34 | 277,414,721 | 21.99h |
| 10 | Luna High | 70 | 52/112 | 112 | $113.29 | 715,444,659 | 34.82h |
| 11 | Terra High | 67.3 | 50/112 | 112 | $156.67 | 358,505,570 | 24.32h |

## Interpretation

- The endpoint provides model-level `score`, pass counts, task counts, tokens, wall time, and estimated cost.
- It does not expose the ten task-level outcomes, so `Weighted /100` cannot be recomputed from this API summary alone.
- Task-weighted rankings remain based on the repository's task matrix and weight snapshots; this report monitors the latest API summary.
- When source data is unchanged, the automation still updates its heartbeat without presenting it as a new benchmark batch.
- The raw API response is not stored in the public repository; only required model-summary fields are archived.

Archived API snapshots: **60**.
