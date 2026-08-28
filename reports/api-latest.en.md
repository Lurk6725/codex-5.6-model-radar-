# Codex Radar API Monitor — English

[简体中文](api-latest.zh-CN.md) · [Project home](../README.md) · [API history CSV](../data/api/model_iq_history.csv) · [Monitor status](../data/api/monitor_status.json)

**Last successful check:** `2026-08-28T12:56:55+00:00`  
**Current API snapshot:** `5dc0f8d65fef3788`  
**Source observation:** `2026-07-22T06:57:20.626603+08:00`  
**New snapshot detected:** yes  
**Models returned:** 11

> “Last successful check” confirms that the automation reached the API. “Source observation” is supplied by the upstream endpoint and may be older.

> This is a model-level summary from the Codex Radar API, not the project's task-level difficulty-weighted score.

## Current API model summary

| Rank | Model tier | Source score | Passed | Tasks | Cost | Total tokens | Wall time |
|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | Luna Max | 102.2 | 76/112 | 112 | $54.03 | 1,822,592,097 | 66.54h |
| 2 | Sol Xhigh | 102.2 | 76/112 | 112 | $647.06 | 793,628,760 | 45.14h |
| 3 | Terra Max | 102.2 | 76/112 | 112 | $425.52 | 1,205,689,302 | 56.89h |
| 4 | Gpt-5.5 Xhigh | 100.9 | 75/112 | 112 | $646.21 | 790,365,648 | 41.71h |
| 5 | Sol Medium | 100.9 | 75/112 | 112 | $311.50 | 415,889,674 | 29.10h |
| 6 | Sol High | 90.1 | 67/112 | 112 | $498.20 | 539,698,064 | 33.21h |
| 7 | Terra Xhigh | 86.1 | 64/112 | 112 | $211.21 | 606,665,762 | 37.61h |
| 8 | Gpt-5.5 High | 84.7 | 63/112 | 112 | $399.94 | 506,583,884 | 32.22h |
| 9 | Sol Low | 82.1 | 61/112 | 112 | $172.61 | 208,322,338 | 17.23h |
| 10 | Terra High | 79.4 | 59/112 | 112 | $122.94 | 342,505,459 | 24.87h |
| 11 | Luna High | 71.3 | 53/112 | 112 | $22.50 | 728,051,301 | 33.33h |

## Interpretation

- The endpoint provides model-level `score`, pass counts, task counts, tokens, wall time, and estimated cost.
- It does not expose the ten task-level outcomes, so `Weighted /100` cannot be recomputed from this API summary alone.
- Task-weighted rankings remain based on the repository's task matrix and weight snapshots; this report monitors the latest API summary.
- When source data is unchanged, the automation still updates its heartbeat without presenting it as a new benchmark batch.
- The raw API response is not stored in the public repository; only required model-summary fields are archived.

Archived API snapshots: **371**.
