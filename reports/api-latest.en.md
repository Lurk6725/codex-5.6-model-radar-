# Codex Radar API Monitor — English

[简体中文](api-latest.zh-CN.md) · [Project home](../README.md) · [API history CSV](../data/api/model_iq_history.csv) · [Monitor status](../data/api/monitor_status.json)

**Last successful check:** `2026-07-29T23:26:50+00:00`  
**Current API snapshot:** `f4ac509d0c1546a8`  
**Source observation:** `2026-07-22T06:57:20.626603+08:00`  
**New snapshot detected:** yes  
**Models returned:** 11

> “Last successful check” confirms that the automation reached the API. “Source observation” is supplied by the upstream endpoint and may be older.

> This is a model-level summary from the Codex Radar API, not the project's task-level difficulty-weighted score.

## Current API model summary

| Rank | Model tier | Source score | Passed | Tasks | Cost | Total tokens | Wall time |
|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | Terra Max | 98.2 | 73/112 | 112 | $543.35 | 1,432,919,805 | 54.84h |
| 2 | Gpt-5.5 Xhigh | 95.5 | 71/112 | 112 | $655.20 | 835,213,272 | 45.03h |
| 3 | Sol Xhigh | 95.5 | 71/112 | 112 | $722.60 | 947,885,845 | 45.12h |
| 4 | Sol High | 91.5 | 68/112 | 112 | $567.07 | 731,962,259 | 39.48h |
| 5 | Gpt-5.5 High | 88.8 | 66/112 | 112 | $438.66 | 538,896,798 | 32.08h |
| 6 | Terra Xhigh | 86.1 | 64/112 | 112 | $275.87 | 664,100,694 | 33.84h |
| 7 | Sol Medium | 84.7 | 63/112 | 112 | $419.03 | 522,060,663 | 31.72h |
| 8 | Luna Max | 80.7 | 60/112 | 112 | $277.79 | 1,899,713,158 | 63.66h |
| 9 | Sol Low | 80.7 | 60/112 | 112 | $233.15 | 267,946,502 | 20.87h |
| 10 | Terra High | 72.6 | 54/112 | 112 | $155.72 | 352,178,575 | 23.13h |
| 11 | Luna High | 65.9 | 49/112 | 112 | $123.30 | 811,428,078 | 36.18h |

## Interpretation

- The endpoint provides model-level `score`, pass counts, task counts, tokens, wall time, and estimated cost.
- It does not expose the ten task-level outcomes, so `Weighted /100` cannot be recomputed from this API summary alone.
- Task-weighted rankings remain based on the repository's task matrix and weight snapshots; this report monitors the latest API summary.
- When source data is unchanged, the automation still updates its heartbeat without presenting it as a new benchmark batch.
- The raw API response is not stored in the public repository; only required model-summary fields are archived.

Archived API snapshots: **117**.
