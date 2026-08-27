# Codex Radar API Monitor — English

[简体中文](api-latest.zh-CN.md) · [Project home](../README.md) · [API history CSV](../data/api/model_iq_history.csv) · [Monitor status](../data/api/monitor_status.json)

**Last successful check:** `2026-08-27T16:33:08+00:00`  
**Current API snapshot:** `b1c50f7fbbc2baa1`  
**Source observation:** `2026-07-22T06:57:20.626603+08:00`  
**New snapshot detected:** yes  
**Models returned:** 11

> “Last successful check” confirms that the automation reached the API. “Source observation” is supplied by the upstream endpoint and may be older.

> This is a model-level summary from the Codex Radar API, not the project's task-level difficulty-weighted score.

## Current API model summary

| Rank | Model tier | Source score | Passed | Tasks | Cost | Total tokens | Wall time |
|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | Sol Xhigh | 102.2 | 76/112 | 112 | $670.69 | 803,380,311 | 44.86h |
| 2 | Luna Max | 100.9 | 75/112 | 112 | $54.03 | 1,772,325,682 | 65.04h |
| 3 | Sol Medium | 100.9 | 75/112 | 112 | $311.46 | 416,464,606 | 29.23h |
| 4 | Terra Max | 100.9 | 75/112 | 112 | $425.58 | 1,173,878,235 | 55.54h |
| 5 | Gpt-5.5 Xhigh | 99.5 | 74/112 | 112 | $646.41 | 779,406,030 | 41.35h |
| 6 | Sol High | 90.1 | 67/112 | 112 | $504.59 | 558,033,919 | 33.88h |
| 7 | Gpt-5.5 High | 84.7 | 63/112 | 112 | $400.27 | 503,307,211 | 32.09h |
| 8 | Terra Xhigh | 84.7 | 63/112 | 112 | $211.37 | 594,860,106 | 37.19h |
| 9 | Sol Low | 83.4 | 62/112 | 112 | $172.50 | 209,414,220 | 17.01h |
| 10 | Terra High | 79.4 | 59/112 | 112 | $123.04 | 342,776,522 | 25.32h |
| 11 | Luna High | 75.3 | 56/112 | 112 | $22.47 | 707,051,648 | 32.29h |

## Interpretation

- The endpoint provides model-level `score`, pass counts, task counts, tokens, wall time, and estimated cost.
- It does not expose the ten task-level outcomes, so `Weighted /100` cannot be recomputed from this API summary alone.
- Task-weighted rankings remain based on the repository's task matrix and weight snapshots; this report monitors the latest API summary.
- When source data is unchanged, the automation still updates its heartbeat without presenting it as a new benchmark batch.
- The raw API response is not stored in the public repository; only required model-summary fields are archived.

Archived API snapshots: **369**.
