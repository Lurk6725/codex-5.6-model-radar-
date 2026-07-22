# Codex Radar API Monitor — English

[简体中文](api-latest.zh-CN.md) · [Project home](../README.md) · [API history CSV](../data/api/model_iq_history.csv) · [Monitor status](../data/api/monitor_status.json)

**Last successful check:** `2026-07-22T17:43:47+00:00`  
**Current API snapshot:** `967d0efd2b021927`  
**Source observation:** `2026-07-22T06:57:20.626603+08:00`  
**New snapshot detected:** yes  
**Models returned:** 11

> “Last successful check” confirms that the automation reached the API. “Source observation” is supplied by the upstream endpoint and may be older.

> This is a model-level summary from the Codex Radar API, not the project's task-level difficulty-weighted score.

## Current API model summary

| Rank | Model tier | Source score | Passed | Tasks | Cost | Total tokens | Wall time |
|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | Terra Max | 100.9 | 75/112 | 112 | $508.53 | 1,306,841,489 | 61.23h |
| 2 | Gpt-5.5 Xhigh | 96.9 | 72/112 | 112 | $655.48 | 845,364,356 | 45.59h |
| 3 | Luna Max | 95.5 | 71/112 | 112 | $284.68 | 1,962,217,206 | 65.77h |
| 4 | Sol Xhigh | 94.2 | 70/112 | 112 | $741.30 | 983,626,548 | 49.22h |
| 5 | Terra Xhigh | 92.8 | 69/112 | 112 | $272.23 | 656,078,673 | 37.15h |
| 6 | Sol High | 91.5 | 68/112 | 112 | $592.27 | 785,455,342 | 43.77h |
| 7 | Sol Medium | 91.5 | 68/112 | 112 | $413.55 | 524,779,450 | 32.21h |
| 8 | Gpt-5.5 High | 86.1 | 64/112 | 112 | $411.10 | 513,164,565 | 31.64h |
| 9 | Sol Low | 78.7 | 58/111 | 111 | $236.34 | 274,555,843 | 22.55h |
| 10 | Luna High | 68.6 | 51/112 | 112 | $112.20 | 709,440,206 | 34.36h |
| 11 | Terra High | 67.3 | 50/112 | 112 | $147.26 | 331,122,570 | 24.94h |

## Interpretation

- The endpoint provides model-level `score`, pass counts, task counts, tokens, wall time, and estimated cost.
- It does not expose the ten task-level outcomes, so `Weighted /100` cannot be recomputed from this API summary alone.
- Task-weighted rankings remain based on the repository's task matrix and weight snapshots; this report monitors the latest API summary.
- When source data is unchanged, the automation still updates its heartbeat without presenting it as a new benchmark batch.
- The raw API response is not stored in the public repository; only required model-summary fields are archived.

Archived API snapshots: **52**.
