# Codex Radar API Monitor — English

[简体中文](api-latest.zh-CN.md) · [Project home](../README.md) · [API history CSV](../data/api/model_iq_history.csv) · [Monitor status](../data/api/monitor_status.json)

**Last successful check:** `2026-07-22T20:38:37+00:00`  
**Current API snapshot:** `10e480fde1a53a8a`  
**Source observation:** `2026-07-22T06:57:20.626603+08:00`  
**New snapshot detected:** yes  
**Models returned:** 11

> “Last successful check” confirms that the automation reached the API. “Source observation” is supplied by the upstream endpoint and may be older.

> This is a model-level summary from the Codex Radar API, not the project's task-level difficulty-weighted score.

## Current API model summary

| Rank | Model tier | Source score | Passed | Tasks | Cost | Total tokens | Wall time |
|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | Terra Max | 99.5 | 74/112 | 112 | $512.76 | 1,321,212,844 | 61.35h |
| 2 | Gpt-5.5 Xhigh | 95.5 | 71/112 | 112 | $653.75 | 842,998,447 | 46.50h |
| 3 | Sol Xhigh | 95.5 | 71/112 | 112 | $750.78 | 997,740,725 | 49.12h |
| 4 | Luna Max | 92.8 | 69/112 | 112 | $283.11 | 1,951,338,419 | 65.25h |
| 5 | Sol High | 92.8 | 69/112 | 112 | $611.53 | 818,093,223 | 44.50h |
| 6 | Terra Xhigh | 92.8 | 69/112 | 112 | $269.79 | 652,041,174 | 36.58h |
| 7 | Sol Medium | 91.5 | 68/112 | 112 | $417.73 | 533,379,720 | 32.68h |
| 8 | Gpt-5.5 High | 86.1 | 64/112 | 112 | $415.46 | 520,999,382 | 32.65h |
| 9 | Sol Low | 75.3 | 56/112 | 112 | $239.03 | 278,916,604 | 22.69h |
| 10 | Luna High | 68.6 | 51/112 | 112 | $112.44 | 711,669,110 | 34.55h |
| 11 | Terra High | 64.6 | 48/112 | 112 | $152.97 | 348,378,628 | 24.72h |

## Interpretation

- The endpoint provides model-level `score`, pass counts, task counts, tokens, wall time, and estimated cost.
- It does not expose the ten task-level outcomes, so `Weighted /100` cannot be recomputed from this API summary alone.
- Task-weighted rankings remain based on the repository's task matrix and weight snapshots; this report monitors the latest API summary.
- When source data is unchanged, the automation still updates its heartbeat without presenting it as a new benchmark batch.
- The raw API response is not stored in the public repository; only required model-summary fields are archived.

Archived API snapshots: **54**.
