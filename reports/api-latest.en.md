# Codex Radar API Monitor — English

[简体中文](api-latest.zh-CN.md) · [Project home](../README.md) · [API history CSV](../data/api/model_iq_history.csv) · [Monitor status](../data/api/monitor_status.json)

**Last successful check:** `2026-07-30T22:47:38+00:00`  
**Current API snapshot:** `91e9e79913d28c98`  
**Source observation:** `2026-07-22T06:57:20.626603+08:00`  
**New snapshot detected:** yes  
**Models returned:** 11

> “Last successful check” confirms that the automation reached the API. “Source observation” is supplied by the upstream endpoint and may be older.

> This is a model-level summary from the Codex Radar API, not the project's task-level difficulty-weighted score.

## Current API model summary

| Rank | Model tier | Source score | Passed | Tasks | Cost | Total tokens | Wall time |
|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | Sol Xhigh | 95.5 | 71/112 | 112 | $743.68 | 983,922,943 | 46.88h |
| 2 | Gpt-5.5 Xhigh | 92.8 | 69/112 | 112 | $654.91 | 835,850,753 | 44.59h |
| 3 | Luna Max | 91.5 | 68/112 | 112 | $263.83 | 1,794,709,097 | 60.51h |
| 4 | Sol High | 90.1 | 67/112 | 112 | $605.28 | 802,380,780 | 41.65h |
| 5 | Gpt-5.5 High | 82.1 | 61/112 | 112 | $429.35 | 536,612,471 | 33.08h |
| 6 | Terra Max | 82.1 | 61/112 | 112 | $571.20 | 1,498,366,267 | 54.74h |
| 7 | Sol Low | 80.7 | 60/112 | 112 | $248.52 | 287,358,775 | 22.56h |
| 8 | Sol Medium | 79.4 | 59/112 | 112 | $439.44 | 554,941,679 | 31.14h |
| 9 | Terra High | 78 | 58/112 | 112 | $166.73 | 378,386,029 | 23.94h |
| 10 | Terra Xhigh | 78 | 58/112 | 112 | $293.90 | 716,275,463 | 33.66h |
| 11 | Luna High | 60.5 | 45/112 | 112 | $123.81 | 816,796,435 | 34.93h |

## Interpretation

- The endpoint provides model-level `score`, pass counts, task counts, tokens, wall time, and estimated cost.
- It does not expose the ten task-level outcomes, so `Weighted /100` cannot be recomputed from this API summary alone.
- Task-weighted rankings remain based on the repository's task matrix and weight snapshots; this report monitors the latest API summary.
- When source data is unchanged, the automation still updates its heartbeat without presenting it as a new benchmark batch.
- The raw API response is not stored in the public repository; only required model-summary fields are archived.

Archived API snapshots: **127**.
