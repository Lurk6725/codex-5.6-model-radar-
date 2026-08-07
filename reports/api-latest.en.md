# Codex Radar API Monitor — English

[简体中文](api-latest.zh-CN.md) · [Project home](../README.md) · [API history CSV](../data/api/model_iq_history.csv) · [Monitor status](../data/api/monitor_status.json)

**Last successful check:** `2026-08-07T06:54:19+00:00`  
**Current API snapshot:** `40df2e49ac641f80`  
**Source observation:** `2026-07-22T06:57:20.626603+08:00`  
**New snapshot detected:** no; the source returned the same snapshot  
**Models returned:** 11

> “Last successful check” confirms that the automation reached the API. “Source observation” is supplied by the upstream endpoint and may be older.

> This is a model-level summary from the Codex Radar API, not the project's task-level difficulty-weighted score.

## Current API model summary

| Rank | Model tier | Source score | Passed | Tasks | Cost | Total tokens | Wall time |
|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | Sol Xhigh | 104.9 | 78/112 | 112 | $755.94 | 965,724,495 | 47.75h |
| 2 | Gpt-5.5 High | 95.5 | 71/112 | 112 | $407.53 | 498,107,316 | 32.59h |
| 3 | Gpt-5.5 Xhigh | 94.2 | 70/112 | 112 | $647.80 | 812,292,285 | 41.71h |
| 4 | Luna Max | 94.2 | 70/112 | 112 | $58.78 | 1,765,839,848 | 60.92h |
| 5 | Sol Medium | 94.2 | 70/112 | 112 | $408.99 | 533,955,988 | 31.96h |
| 6 | Terra Max | 94.2 | 70/112 | 112 | $454.46 | 1,488,801,802 | 62.21h |
| 7 | Sol High | 88.8 | 66/112 | 112 | $583.52 | 680,876,651 | 39.87h |
| 8 | Terra Xhigh | 86.1 | 64/112 | 112 | $226.44 | 631,808,210 | 36.62h |
| 9 | Luna High | 80.7 | 60/112 | 112 | $26.85 | 727,695,035 | 31.34h |
| 10 | Terra High | 79.4 | 59/112 | 112 | $130.55 | 348,713,486 | 24.66h |
| 11 | Sol Low | 78 | 58/112 | 112 | $231.98 | 257,909,171 | 22.38h |

## Interpretation

- The endpoint provides model-level `score`, pass counts, task counts, tokens, wall time, and estimated cost.
- It does not expose the ten task-level outcomes, so `Weighted /100` cannot be recomputed from this API summary alone.
- Task-weighted rankings remain based on the repository's task matrix and weight snapshots; this report monitors the latest API summary.
- When source data is unchanged, the automation still updates its heartbeat without presenting it as a new benchmark batch.
- The raw API response is not stored in the public repository; only required model-summary fields are archived.

Archived API snapshots: **188**.
