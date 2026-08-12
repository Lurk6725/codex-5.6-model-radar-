# Codex Radar API Monitor — English

[简体中文](api-latest.zh-CN.md) · [Project home](../README.md) · [API history CSV](../data/api/model_iq_history.csv) · [Monitor status](../data/api/monitor_status.json)

**Last successful check:** `2026-08-12T19:29:36+00:00`  
**Current API snapshot:** `955a602cb41507e7`  
**Source observation:** `2026-07-22T06:57:20.626603+08:00`  
**New snapshot detected:** no; the source returned the same snapshot  
**Models returned:** 11

> “Last successful check” confirms that the automation reached the API. “Source observation” is supplied by the upstream endpoint and may be older.

> This is a model-level summary from the Codex Radar API, not the project's task-level difficulty-weighted score.

## Current API model summary

| Rank | Model tier | Source score | Passed | Tasks | Cost | Total tokens | Wall time |
|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | Sol Xhigh | 102.2 | 76/112 | 112 | $731.08 | 869,600,462 | 46.78h |
| 2 | Terra Max | 102.2 | 76/112 | 112 | $436.68 | 1,267,503,512 | 58.90h |
| 3 | Luna Max | 100.9 | 75/112 | 112 | $58.48 | 1,898,783,946 | 68.76h |
| 4 | Gpt-5.5 Xhigh | 98.2 | 73/112 | 112 | $656.86 | 724,544,185 | 40.42h |
| 5 | Sol High | 98.2 | 73/112 | 112 | $561.19 | 685,275,653 | 38.53h |
| 6 | Sol Medium | 92.8 | 69/112 | 112 | $407.22 | 466,261,110 | 32.15h |
| 7 | Gpt-5.5 High | 84.7 | 63/112 | 112 | $403.77 | 489,559,860 | 33.75h |
| 8 | Terra Xhigh | 84.7 | 63/112 | 112 | $218.20 | 580,013,778 | 35.57h |
| 9 | Terra High | 78 | 58/112 | 112 | $126.87 | 337,068,443 | 24.96h |
| 10 | Sol Low | 75.3 | 56/112 | 112 | $228.54 | 264,835,675 | 22.48h |
| 11 | Luna High | 74 | 55/112 | 112 | $26.17 | 770,398,333 | 35.32h |

## Interpretation

- The endpoint provides model-level `score`, pass counts, task counts, tokens, wall time, and estimated cost.
- It does not expose the ten task-level outcomes, so `Weighted /100` cannot be recomputed from this API summary alone.
- Task-weighted rankings remain based on the repository's task matrix and weight snapshots; this report monitors the latest API summary.
- When source data is unchanged, the automation still updates its heartbeat without presenting it as a new benchmark batch.
- The raw API response is not stored in the public repository; only required model-summary fields are archived.

Archived API snapshots: **245**.
