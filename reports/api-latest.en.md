# Codex Radar API Monitor — English

[简体中文](api-latest.zh-CN.md) · [Project home](../README.md) · [API history CSV](../data/api/model_iq_history.csv) · [Monitor status](../data/api/monitor_status.json)

**Last successful check:** `2026-08-17T13:08:52+00:00`  
**Current API snapshot:** `912b743a9bdd3ad5`  
**Source observation:** `2026-07-22T06:57:20.626603+08:00`  
**New snapshot detected:** yes  
**Models returned:** 11

> “Last successful check” confirms that the automation reached the API. “Source observation” is supplied by the upstream endpoint and may be older.

> This is a model-level summary from the Codex Radar API, not the project's task-level difficulty-weighted score.

## Current API model summary

| Rank | Model tier | Source score | Passed | Tasks | Cost | Total tokens | Wall time |
|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | Sol Xhigh | 98.2 | 73/112 | 112 | $725.53 | 842,631,226 | 44.99h |
| 2 | Terra Max | 98.2 | 73/112 | 112 | $435.37 | 1,260,037,567 | 58.90h |
| 3 | Luna Max | 95.5 | 71/112 | 112 | $58.79 | 1,776,840,287 | 63.68h |
| 4 | Gpt-5.5 Xhigh | 94.2 | 70/112 | 112 | $655.24 | 750,870,108 | 41.88h |
| 5 | Gpt-5.5 High | 91.5 | 68/112 | 112 | $403.43 | 497,429,599 | 33.14h |
| 6 | Sol High | 91.5 | 68/112 | 112 | $538.15 | 640,471,302 | 36.17h |
| 7 | Sol Medium | 84.7 | 63/112 | 112 | $383.04 | 466,206,625 | 33.02h |
| 8 | Terra Xhigh | 82.1 | 61/112 | 112 | $216.83 | 602,369,435 | 38.03h |
| 9 | Luna High | 79.4 | 59/112 | 112 | $26.16 | 774,018,441 | 35.25h |
| 10 | Terra High | 74 | 55/112 | 112 | $126.39 | 349,925,642 | 26.20h |
| 11 | Sol Low | 68.6 | 51/112 | 112 | $225.77 | 276,296,616 | 24.23h |

## Interpretation

- The endpoint provides model-level `score`, pass counts, task counts, tokens, wall time, and estimated cost.
- It does not expose the ten task-level outcomes, so `Weighted /100` cannot be recomputed from this API summary alone.
- Task-weighted rankings remain based on the repository's task matrix and weight snapshots; this report monitors the latest API summary.
- When source data is unchanged, the automation still updates its heartbeat without presenting it as a new benchmark batch.
- The raw API response is not stored in the public repository; only required model-summary fields are archived.

Archived API snapshots: **280**.
