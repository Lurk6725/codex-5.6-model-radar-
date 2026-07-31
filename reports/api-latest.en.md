# Codex Radar API Monitor — English

[简体中文](api-latest.zh-CN.md) · [Project home](../README.md) · [API history CSV](../data/api/model_iq_history.csv) · [Monitor status](../data/api/monitor_status.json)

**Last successful check:** `2026-07-31T12:20:42+00:00`  
**Current API snapshot:** `c0f2c3f356164fea`  
**Source observation:** `2026-07-22T06:57:20.626603+08:00`  
**New snapshot detected:** yes  
**Models returned:** 11

> “Last successful check” confirms that the automation reached the API. “Source observation” is supplied by the upstream endpoint and may be older.

> This is a model-level summary from the Codex Radar API, not the project's task-level difficulty-weighted score.

## Current API model summary

| Rank | Model tier | Source score | Passed | Tasks | Cost | Total tokens | Wall time |
|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | Sol Xhigh | 98.2 | 73/112 | 112 | $782.33 | 1,032,816,064 | 46.41h |
| 2 | Gpt-5.5 Xhigh | 91.5 | 68/112 | 112 | $650.61 | 821,233,190 | 42.93h |
| 3 | Sol High | 87.4 | 65/112 | 112 | $613.56 | 821,087,983 | 41.44h |
| 4 | Terra High | 83.4 | 62/112 | 112 | $164.69 | 389,048,234 | 24.76h |
| 5 | Luna Max | 82.1 | 61/112 | 112 | $151.08 | 1,787,997,485 | 56.01h |
| 6 | Sol Medium | 82.1 | 61/112 | 112 | $433.49 | 550,883,489 | 31.40h |
| 7 | Terra Max | 82.1 | 61/112 | 112 | $568.20 | 1,525,525,964 | 56.55h |
| 8 | Terra Xhigh | 79.4 | 59/112 | 112 | $292.71 | 728,849,552 | 33.59h |
| 9 | Gpt-5.5 High | 76.7 | 57/112 | 112 | $428.10 | 542,355,918 | 33.48h |
| 10 | Sol Low | 72.6 | 54/112 | 112 | $253.85 | 296,801,141 | 21.86h |
| 11 | Luna High | 68.6 | 51/112 | 112 | $79.05 | 783,635,424 | 32.19h |

## Interpretation

- The endpoint provides model-level `score`, pass counts, task counts, tokens, wall time, and estimated cost.
- It does not expose the ten task-level outcomes, so `Weighted /100` cannot be recomputed from this API summary alone.
- Task-weighted rankings remain based on the repository's task matrix and weight snapshots; this report monitors the latest API summary.
- When source data is unchanged, the automation still updates its heartbeat without presenting it as a new benchmark batch.
- The raw API response is not stored in the public repository; only required model-summary fields are archived.

Archived API snapshots: **132**.
