# Codex Radar API Monitor — English

[简体中文](api-latest.zh-CN.md) · [Project home](../README.md) · [API history CSV](../data/api/model_iq_history.csv) · [Monitor status](../data/api/monitor_status.json)

**Last successful check:** `2026-08-10T04:18:45+00:00`  
**Current API snapshot:** `4aaf469f850c838d`  
**Source observation:** `2026-07-22T06:57:20.626603+08:00`  
**New snapshot detected:** yes  
**Models returned:** 11

> “Last successful check” confirms that the automation reached the API. “Source observation” is supplied by the upstream endpoint and may be older.

> This is a model-level summary from the Codex Radar API, not the project's task-level difficulty-weighted score.

## Current API model summary

| Rank | Model tier | Source score | Passed | Tasks | Cost | Total tokens | Wall time |
|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | Sol Xhigh | 110.3 | 82/112 | 112 | $739.13 | 901,831,398 | 52.45h |
| 2 | Sol High | 99.5 | 74/112 | 112 | $568.53 | 597,010,782 | 37.04h |
| 3 | Terra Max | 99.5 | 74/112 | 112 | $439.59 | 1,120,535,976 | 49.58h |
| 4 | Gpt-5.5 Xhigh | 98.2 | 73/112 | 112 | $657.85 | 808,548,453 | 41.41h |
| 5 | Sol Medium | 91.5 | 68/112 | 112 | $410.18 | 470,574,946 | 31.70h |
| 6 | Sol Low | 90.1 | 67/112 | 112 | $230.67 | 277,379,015 | 23.79h |
| 7 | Luna Max | 88.8 | 66/112 | 112 | $58.71 | 1,764,116,786 | 62.23h |
| 8 | Terra Xhigh | 86.1 | 64/112 | 112 | $219.88 | 598,708,191 | 34.14h |
| 9 | Gpt-5.5 High | 79.4 | 59/112 | 112 | $405.33 | 475,354,764 | 28.84h |
| 10 | Terra High | 75.3 | 56/112 | 112 | $127.05 | 334,640,379 | 23.11h |
| 11 | Luna High | 71.3 | 53/112 | 112 | $26.22 | 716,922,950 | 32.58h |

## Interpretation

- The endpoint provides model-level `score`, pass counts, task counts, tokens, wall time, and estimated cost.
- It does not expose the ten task-level outcomes, so `Weighted /100` cannot be recomputed from this API summary alone.
- Task-weighted rankings remain based on the repository's task matrix and weight snapshots; this report monitors the latest API summary.
- When source data is unchanged, the automation still updates its heartbeat without presenting it as a new benchmark batch.
- The raw API response is not stored in the public repository; only required model-summary fields are archived.

Archived API snapshots: **223**.
