# Codex Radar API Monitor — English

[简体中文](api-latest.zh-CN.md) · [Project home](../README.md) · [API history CSV](../data/api/model_iq_history.csv) · [Monitor status](../data/api/monitor_status.json)

**Last successful check:** `2026-07-28T10:15:28+00:00`  
**Current API snapshot:** `0788e8ed83bbb619`  
**Source observation:** `2026-07-22T06:57:20.626603+08:00`  
**New snapshot detected:** yes  
**Models returned:** 11

> “Last successful check” confirms that the automation reached the API. “Source observation” is supplied by the upstream endpoint and may be older.

> This is a model-level summary from the Codex Radar API, not the project's task-level difficulty-weighted score.

## Current API model summary

| Rank | Model tier | Source score | Passed | Tasks | Cost | Total tokens | Wall time |
|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | Sol Xhigh | 94.2 | 70/112 | 112 | $788.26 | 1,065,951,661 | 46.23h |
| 2 | Sol Medium | 92.8 | 69/112 | 112 | $398.64 | 486,412,346 | 30.95h |
| 3 | Sol High | 91.5 | 68/112 | 112 | $571.18 | 731,996,349 | 40.13h |
| 4 | Luna Max | 90.1 | 67/112 | 112 | $277.43 | 1,902,154,844 | 61.36h |
| 5 | Terra Max | 90.1 | 67/112 | 112 | $534.83 | 1,422,888,692 | 56.94h |
| 6 | Gpt-5.5 Xhigh | 88.8 | 66/112 | 112 | $666.55 | 857,311,537 | 44.94h |
| 7 | Gpt-5.5 High | 83.4 | 62/112 | 112 | $407.55 | 496,499,762 | 29.75h |
| 8 | Terra Xhigh | 82.1 | 61/112 | 112 | $300.99 | 758,212,767 | 37.18h |
| 9 | Sol Low | 74 | 55/112 | 112 | $225.18 | 253,183,036 | 19.61h |
| 10 | Luna High | 72.6 | 54/112 | 112 | $121.02 | 791,136,053 | 33.32h |
| 11 | Terra High | 70 | 52/112 | 112 | $154.32 | 344,816,148 | 23.02h |

## Interpretation

- The endpoint provides model-level `score`, pass counts, task counts, tokens, wall time, and estimated cost.
- It does not expose the ten task-level outcomes, so `Weighted /100` cannot be recomputed from this API summary alone.
- Task-weighted rankings remain based on the repository's task matrix and weight snapshots; this report monitors the latest API summary.
- When source data is unchanged, the automation still updates its heartbeat without presenting it as a new benchmark batch.
- The raw API response is not stored in the public repository; only required model-summary fields are archived.

Archived API snapshots: **102**.
