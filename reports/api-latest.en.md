# Codex Radar API Monitor — English

[简体中文](api-latest.zh-CN.md) · [Project home](../README.md) · [API history CSV](../data/api/model_iq_history.csv) · [Monitor status](../data/api/monitor_status.json)

**Last successful check:** `2026-07-30T19:54:58+00:00`  
**Current API snapshot:** `422cc99626fbed7e`  
**Source observation:** `2026-07-22T06:57:20.626603+08:00`  
**New snapshot detected:** yes  
**Models returned:** 11

> “Last successful check” confirms that the automation reached the API. “Source observation” is supplied by the upstream endpoint and may be older.

> This is a model-level summary from the Codex Radar API, not the project's task-level difficulty-weighted score.

## Current API model summary

| Rank | Model tier | Source score | Passed | Tasks | Cost | Total tokens | Wall time |
|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | Sol Xhigh | 95.5 | 71/112 | 112 | $743.68 | 983,922,943 | 46.88h |
| 2 | Gpt-5.5 Xhigh | 92.8 | 69/112 | 112 | $663.98 | 851,075,199 | 44.76h |
| 3 | Sol High | 91.5 | 68/112 | 112 | $608.01 | 807,359,742 | 41.48h |
| 4 | Luna Max | 90.1 | 67/112 | 112 | $264.04 | 1,795,681,462 | 60.35h |
| 5 | Gpt-5.5 High | 82.1 | 61/112 | 112 | $428.07 | 533,103,781 | 32.77h |
| 6 | Terra Max | 82.1 | 61/112 | 112 | $571.76 | 1,500,759,679 | 54.92h |
| 7 | Sol Low | 80.7 | 60/112 | 112 | $247.43 | 285,393,943 | 22.38h |
| 8 | Sol Medium | 80.7 | 60/112 | 112 | $427.26 | 529,591,802 | 31.63h |
| 9 | Terra Xhigh | 78 | 58/112 | 112 | $294.84 | 718,391,371 | 34.27h |
| 10 | Terra High | 75.3 | 56/112 | 112 | $164.81 | 373,797,012 | 23.67h |
| 11 | Luna High | 61.9 | 46/112 | 112 | $123.25 | 812,148,787 | 34.75h |

## Interpretation

- The endpoint provides model-level `score`, pass counts, task counts, tokens, wall time, and estimated cost.
- It does not expose the ten task-level outcomes, so `Weighted /100` cannot be recomputed from this API summary alone.
- Task-weighted rankings remain based on the repository's task matrix and weight snapshots; this report monitors the latest API summary.
- When source data is unchanged, the automation still updates its heartbeat without presenting it as a new benchmark batch.
- The raw API response is not stored in the public repository; only required model-summary fields are archived.

Archived API snapshots: **125**.
