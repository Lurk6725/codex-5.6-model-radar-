# Codex Radar API Monitor — English

[简体中文](api-latest.zh-CN.md) · [Project home](../README.md) · [API history CSV](../data/api/model_iq_history.csv) · [Monitor status](../data/api/monitor_status.json)

**Last successful check:** `2026-07-31T15:10:27+00:00`  
**Current API snapshot:** `847753542433f5b6`  
**Source observation:** `2026-07-22T06:57:20.626603+08:00`  
**New snapshot detected:** yes  
**Models returned:** 11

> “Last successful check” confirms that the automation reached the API. “Source observation” is supplied by the upstream endpoint and may be older.

> This is a model-level summary from the Codex Radar API, not the project's task-level difficulty-weighted score.

## Current API model summary

| Rank | Model tier | Source score | Passed | Tasks | Cost | Total tokens | Wall time |
|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | Sol Xhigh | 98.2 | 73/112 | 112 | $776.29 | 1,019,788,217 | 46.44h |
| 2 | Gpt-5.5 Xhigh | 90.1 | 67/112 | 112 | $649.98 | 822,340,734 | 42.84h |
| 3 | Sol High | 86.1 | 64/112 | 112 | $614.97 | 823,301,439 | 41.46h |
| 4 | Sol Medium | 83.4 | 62/112 | 112 | $433.64 | 550,591,971 | 31.66h |
| 5 | Terra High | 83.4 | 62/112 | 112 | $164.43 | 388,907,002 | 24.63h |
| 6 | Terra Max | 83.4 | 62/112 | 112 | $568.38 | 1,527,186,589 | 56.44h |
| 7 | Luna Max | 82.1 | 61/112 | 112 | $151.08 | 1,787,997,485 | 56.01h |
| 8 | Terra Xhigh | 80.7 | 60/112 | 112 | $288.72 | 722,477,359 | 33.32h |
| 9 | Gpt-5.5 High | 76.7 | 57/112 | 112 | $428.10 | 542,355,918 | 33.48h |
| 10 | Sol Low | 74 | 55/112 | 112 | $253.41 | 296,198,810 | 21.88h |
| 11 | Luna High | 68.6 | 51/112 | 112 | $79.05 | 783,635,424 | 32.19h |

## Interpretation

- The endpoint provides model-level `score`, pass counts, task counts, tokens, wall time, and estimated cost.
- It does not expose the ten task-level outcomes, so `Weighted /100` cannot be recomputed from this API summary alone.
- Task-weighted rankings remain based on the repository's task matrix and weight snapshots; this report monitors the latest API summary.
- When source data is unchanged, the automation still updates its heartbeat without presenting it as a new benchmark batch.
- The raw API response is not stored in the public repository; only required model-summary fields are archived.

Archived API snapshots: **133**.
