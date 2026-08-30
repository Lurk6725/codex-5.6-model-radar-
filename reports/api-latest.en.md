# Codex Radar API Monitor — English

[简体中文](api-latest.zh-CN.md) · [Project home](../README.md) · [API history CSV](../data/api/model_iq_history.csv) · [Monitor status](../data/api/monitor_status.json)

**Last successful check:** `2026-08-30T16:44:55+00:00`  
**Current API snapshot:** `572599197a5c7aae`  
**Source observation:** `2026-08-30T20:01:21.823608+08:00`  
**New snapshot detected:** yes  
**Models returned:** 11

> “Last successful check” confirms that the automation reached the API. “Source observation” is supplied by the upstream endpoint and may be older.

> This is a model-level summary from the Codex Radar API, not the project's task-level difficulty-weighted score.

## Current API model summary

| Rank | Model tier | Source score | Passed | Tasks | Cost | Total tokens | Wall time |
|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | Luna Max | 104.9 | 78/112 | 112 | $54.08 | 2,004,732,838 | 72.24h |
| 2 | Terra Max | 104.9 | 78/112 | 112 | $425.08 | 1,203,448,007 | 57.10h |
| 3 | Sol High | 99.5 | 74/112 | 112 | $489.80 | 588,163,244 | 36.09h |
| 4 | Sol Xhigh | 99.5 | 74/112 | 112 | $597.25 | 822,085,162 | 44.23h |
| 5 | Gpt-5.5 Xhigh | 98.2 | 73/112 | 112 | $639.73 | 879,841,389 | 43.06h |
| 6 | Sol Medium | 96.9 | 72/112 | 112 | $312.59 | 426,945,526 | 27.74h |
| 7 | Gpt-5.5 High | 87.4 | 65/112 | 112 | $397.66 | 527,211,975 | 27.85h |
| 8 | Terra Xhigh | 84.7 | 63/112 | 112 | $211.93 | 589,455,039 | 36.60h |
| 9 | Sol Low | 80.7 | 60/112 | 112 | $171.55 | 214,079,374 | 16.63h |
| 10 | Terra High | 79.4 | 59/112 | 112 | $122.24 | 346,835,437 | 25.48h |
| 11 | Luna High | 68.6 | 51/112 | 112 | $22.48 | 801,010,164 | 33.90h |

## Interpretation

- The endpoint provides model-level `score`, pass counts, task counts, tokens, wall time, and estimated cost.
- It does not expose the ten task-level outcomes, so `Weighted /100` cannot be recomputed from this API summary alone.
- Task-weighted rankings remain based on the repository's task matrix and weight snapshots; this report monitors the latest API summary.
- When source data is unchanged, the automation still updates its heartbeat without presenting it as a new benchmark batch.
- The raw API response is not stored in the public repository; only required model-summary fields are archived.

Archived API snapshots: **381**.
