# Codex Radar API Monitor — English

[简体中文](api-latest.zh-CN.md) · [Project home](../README.md) · [API history CSV](../data/api/model_iq_history.csv) · [Monitor status](../data/api/monitor_status.json)

**Last successful check:** `2026-08-01T21:11:37+00:00`  
**Current API snapshot:** `60162d653b1c005f`  
**Source observation:** `2026-07-22T06:57:20.626603+08:00`  
**New snapshot detected:** no; the source returned the same snapshot  
**Models returned:** 11

> “Last successful check” confirms that the automation reached the API. “Source observation” is supplied by the upstream endpoint and may be older.

> This is a model-level summary from the Codex Radar API, not the project's task-level difficulty-weighted score.

## Current API model summary

| Rank | Model tier | Source score | Passed | Tasks | Cost | Total tokens | Wall time |
|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | Sol Xhigh | 99.5 | 74/112 | 112 | $771.48 | 985,613,507 | 47.24h |
| 2 | Gpt-5.5 Xhigh | 94.2 | 70/112 | 112 | $648.27 | 836,796,394 | 43.72h |
| 3 | Terra Max | 88.8 | 66/112 | 112 | $526.47 | 1,525,223,779 | 57.42h |
| 4 | Sol High | 86.1 | 64/112 | 112 | $608.45 | 801,737,016 | 41.61h |
| 5 | Sol Medium | 86.1 | 64/112 | 112 | $420.78 | 578,604,697 | 33.40h |
| 6 | Gpt-5.5 High | 79.4 | 59/112 | 112 | $415.70 | 534,362,947 | 32.63h |
| 7 | Luna Max | 78 | 58/112 | 112 | $117.51 | 1,835,008,925 | 57.49h |
| 8 | Terra High | 76.7 | 57/112 | 112 | $151.49 | 402,922,495 | 25.73h |
| 9 | Terra Xhigh | 74 | 55/112 | 112 | $269.91 | 733,067,764 | 35.00h |
| 10 | Sol Low | 72.6 | 54/112 | 112 | $249.52 | 286,409,466 | 21.10h |
| 11 | Luna High | 71.3 | 53/112 | 112 | $68.62 | 805,443,922 | 33.73h |

## Interpretation

- The endpoint provides model-level `score`, pass counts, task counts, tokens, wall time, and estimated cost.
- It does not expose the ten task-level outcomes, so `Weighted /100` cannot be recomputed from this API summary alone.
- Task-weighted rankings remain based on the repository's task matrix and weight snapshots; this report monitors the latest API summary.
- When source data is unchanged, the automation still updates its heartbeat without presenting it as a new benchmark batch.
- The raw API response is not stored in the public repository; only required model-summary fields are archived.

Archived API snapshots: **147**.
