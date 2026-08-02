# Codex Radar API Monitor — English

[简体中文](api-latest.zh-CN.md) · [Project home](../README.md) · [API history CSV](../data/api/model_iq_history.csv) · [Monitor status](../data/api/monitor_status.json)

**Last successful check:** `2026-08-02T06:47:26+00:00`  
**Current API snapshot:** `380cdad236a21292`  
**Source observation:** `2026-07-22T06:57:20.626603+08:00`  
**New snapshot detected:** yes  
**Models returned:** 11

> “Last successful check” confirms that the automation reached the API. “Source observation” is supplied by the upstream endpoint and may be older.

> This is a model-level summary from the Codex Radar API, not the project's task-level difficulty-weighted score.

## Current API model summary

| Rank | Model tier | Source score | Passed | Tasks | Cost | Total tokens | Wall time |
|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | Sol Xhigh | 99.5 | 74/112 | 112 | $773.90 | 987,774,471 | 47.25h |
| 2 | Gpt-5.5 Xhigh | 94.2 | 70/112 | 112 | $652.72 | 833,095,536 | 44.12h |
| 3 | Sol Medium | 88.8 | 66/112 | 112 | $422.74 | 585,797,627 | 33.78h |
| 4 | Terra Max | 88.8 | 66/112 | 112 | $524.94 | 1,520,488,530 | 57.61h |
| 5 | Sol High | 87.4 | 65/112 | 112 | $601.91 | 786,664,924 | 41.60h |
| 6 | Luna Max | 84.7 | 63/112 | 112 | $109.92 | 1,781,710,922 | 58.61h |
| 7 | Gpt-5.5 High | 79.4 | 59/112 | 112 | $415.75 | 527,463,741 | 32.29h |
| 8 | Luna High | 72.6 | 54/112 | 112 | $66.03 | 798,022,260 | 33.60h |
| 9 | Terra High | 72.6 | 54/112 | 112 | $150.78 | 402,712,657 | 26.15h |
| 10 | Terra Xhigh | 72.6 | 54/112 | 112 | $268.49 | 728,985,873 | 35.12h |
| 11 | Sol Low | 71.3 | 53/112 | 112 | $248.42 | 285,451,509 | 21.11h |

## Interpretation

- The endpoint provides model-level `score`, pass counts, task counts, tokens, wall time, and estimated cost.
- It does not expose the ten task-level outcomes, so `Weighted /100` cannot be recomputed from this API summary alone.
- Task-weighted rankings remain based on the repository's task matrix and weight snapshots; this report monitors the latest API summary.
- When source data is unchanged, the automation still updates its heartbeat without presenting it as a new benchmark batch.
- The raw API response is not stored in the public repository; only required model-summary fields are archived.

Archived API snapshots: **151**.
