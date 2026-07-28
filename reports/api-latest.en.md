# Codex Radar API Monitor — English

[简体中文](api-latest.zh-CN.md) · [Project home](../README.md) · [API history CSV](../data/api/model_iq_history.csv) · [Monitor status](../data/api/monitor_status.json)

**Last successful check:** `2026-07-28T07:26:32+00:00`  
**Current API snapshot:** `ec9df26d5aa6b124`  
**Source observation:** `2026-07-22T06:57:20.626603+08:00`  
**New snapshot detected:** yes  
**Models returned:** 11

> “Last successful check” confirms that the automation reached the API. “Source observation” is supplied by the upstream endpoint and may be older.

> This is a model-level summary from the Codex Radar API, not the project's task-level difficulty-weighted score.

## Current API model summary

| Rank | Model tier | Source score | Passed | Tasks | Cost | Total tokens | Wall time |
|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | Sol Medium | 94.2 | 70/112 | 112 | $409.98 | 503,336,535 | 31.32h |
| 2 | Luna Max | 92.8 | 69/112 | 112 | $277.05 | 1,902,870,938 | 60.61h |
| 3 | Sol High | 91.5 | 68/112 | 112 | $575.50 | 737,298,835 | 40.63h |
| 4 | Sol Xhigh | 90.1 | 67/112 | 112 | $822.61 | 1,142,277,376 | 50.23h |
| 5 | Terra Max | 90.1 | 67/112 | 112 | $532.81 | 1,419,038,560 | 56.70h |
| 6 | Gpt-5.5 Xhigh | 87.4 | 65/112 | 112 | $661.18 | 848,232,523 | 43.48h |
| 7 | Gpt-5.5 High | 83.4 | 62/112 | 112 | $415.53 | 509,789,151 | 30.46h |
| 8 | Terra Xhigh | 80.7 | 60/112 | 112 | $291.40 | 726,280,524 | 36.27h |
| 9 | Luna High | 74 | 55/112 | 112 | $119.06 | 774,153,352 | 32.38h |
| 10 | Sol Low | 72.6 | 54/112 | 112 | $221.41 | 248,511,701 | 19.55h |
| 11 | Terra High | 65.9 | 49/112 | 112 | $150.53 | 334,127,527 | 22.31h |

## Interpretation

- The endpoint provides model-level `score`, pass counts, task counts, tokens, wall time, and estimated cost.
- It does not expose the ten task-level outcomes, so `Weighted /100` cannot be recomputed from this API summary alone.
- Task-weighted rankings remain based on the repository's task matrix and weight snapshots; this report monitors the latest API summary.
- When source data is unchanged, the automation still updates its heartbeat without presenting it as a new benchmark batch.
- The raw API response is not stored in the public repository; only required model-summary fields are archived.

Archived API snapshots: **101**.
