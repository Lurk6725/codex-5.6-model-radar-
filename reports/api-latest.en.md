# Codex Radar API Monitor — English

[简体中文](api-latest.zh-CN.md) · [Project home](../README.md) · [API history CSV](../data/api/model_iq_history.csv) · [Monitor status](../data/api/monitor_status.json)

**Last successful check:** `2026-08-05T10:16:43+00:00`  
**Current API snapshot:** `81c6c43a0d9fc881`  
**Source observation:** `2026-07-22T06:57:20.626603+08:00`  
**New snapshot detected:** yes  
**Models returned:** 11

> “Last successful check” confirms that the automation reached the API. “Source observation” is supplied by the upstream endpoint and may be older.

> This is a model-level summary from the Codex Radar API, not the project's task-level difficulty-weighted score.

## Current API model summary

| Rank | Model tier | Source score | Passed | Tasks | Cost | Total tokens | Wall time |
|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | Sol Xhigh | 109 | 81/112 | 112 | $762.35 | 953,211,269 | 47.81h |
| 2 | Luna Max | 99.5 | 74/112 | 112 | $58.91 | 1,749,216,995 | 59.12h |
| 3 | Gpt-5.5 Xhigh | 98.2 | 73/112 | 112 | $652.31 | 780,791,806 | 41.92h |
| 4 | Terra Max | 91.5 | 68/112 | 112 | $456.44 | 1,448,084,583 | 58.85h |
| 5 | Gpt-5.5 High | 87.4 | 65/112 | 112 | $407.68 | 496,850,536 | 31.43h |
| 6 | Sol Medium | 87.4 | 65/112 | 112 | $409.42 | 537,101,260 | 31.93h |
| 7 | Terra High | 86.1 | 64/112 | 112 | $139.00 | 335,432,894 | 23.52h |
| 8 | Sol High | 84.7 | 63/112 | 112 | $589.05 | 694,023,103 | 39.68h |
| 9 | Terra Xhigh | 83.4 | 62/112 | 112 | $231.07 | 608,590,229 | 33.46h |
| 10 | Luna High | 72.6 | 54/112 | 112 | $27.59 | 737,882,100 | 29.61h |
| 11 | Sol Low | 71.3 | 53/112 | 112 | $231.32 | 243,548,527 | 20.70h |

## Interpretation

- The endpoint provides model-level `score`, pass counts, task counts, tokens, wall time, and estimated cost.
- It does not expose the ten task-level outcomes, so `Weighted /100` cannot be recomputed from this API summary alone.
- Task-weighted rankings remain based on the repository's task matrix and weight snapshots; this report monitors the latest API summary.
- When source data is unchanged, the automation still updates its heartbeat without presenting it as a new benchmark batch.
- The raw API response is not stored in the public repository; only required model-summary fields are archived.

Archived API snapshots: **175**.
