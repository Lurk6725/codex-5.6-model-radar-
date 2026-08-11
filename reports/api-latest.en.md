# Codex Radar API Monitor — English

[简体中文](api-latest.zh-CN.md) · [Project home](../README.md) · [API history CSV](../data/api/model_iq_history.csv) · [Monitor status](../data/api/monitor_status.json)

**Last successful check:** `2026-08-11T18:39:46+00:00`  
**Current API snapshot:** `f18a69f3514be035`  
**Source observation:** `2026-07-22T06:57:20.626603+08:00`  
**New snapshot detected:** yes  
**Models returned:** 11

> “Last successful check” confirms that the automation reached the API. “Source observation” is supplied by the upstream endpoint and may be older.

> This is a model-level summary from the Codex Radar API, not the project's task-level difficulty-weighted score.

## Current API model summary

| Rank | Model tier | Source score | Passed | Tasks | Cost | Total tokens | Wall time |
|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | Sol Xhigh | 107.6 | 80/112 | 112 | $736.25 | 895,044,783 | 50.08h |
| 2 | Sol High | 100.9 | 75/112 | 112 | $563.00 | 644,409,787 | 38.22h |
| 3 | Luna Max | 99.5 | 74/112 | 112 | $58.66 | 1,810,286,029 | 62.76h |
| 4 | Terra Max | 98.2 | 73/112 | 112 | $437.83 | 1,192,960,454 | 54.03h |
| 5 | Gpt-5.5 High | 94.2 | 70/112 | 112 | $404.10 | 486,871,531 | 32.27h |
| 6 | Gpt-5.5 Xhigh | 90.1 | 67/112 | 112 | $657.10 | 745,491,495 | 40.56h |
| 7 | Sol Medium | 90.1 | 67/112 | 112 | $407.73 | 467,899,354 | 31.40h |
| 8 | Terra Xhigh | 84.7 | 63/112 | 112 | $219.59 | 564,044,868 | 33.68h |
| 9 | Sol Low | 79.4 | 59/112 | 112 | $229.66 | 276,738,822 | 22.91h |
| 10 | Terra High | 78 | 58/112 | 112 | $127.23 | 330,271,540 | 23.52h |
| 11 | Luna High | 65.9 | 49/112 | 112 | $26.22 | 748,247,572 | 34.34h |

## Interpretation

- The endpoint provides model-level `score`, pass counts, task counts, tokens, wall time, and estimated cost.
- It does not expose the ten task-level outcomes, so `Weighted /100` cannot be recomputed from this API summary alone.
- Task-weighted rankings remain based on the repository's task matrix and weight snapshots; this report monitors the latest API summary.
- When source data is unchanged, the automation still updates its heartbeat without presenting it as a new benchmark batch.
- The raw API response is not stored in the public repository; only required model-summary fields are archived.

Archived API snapshots: **234**.
