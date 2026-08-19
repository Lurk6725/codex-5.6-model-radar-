# Codex Radar API Monitor — English

[简体中文](api-latest.zh-CN.md) · [Project home](../README.md) · [API history CSV](../data/api/model_iq_history.csv) · [Monitor status](../data/api/monitor_status.json)

**Last successful check:** `2026-08-19T12:13:39+00:00`  
**Current API snapshot:** `2d6ba7fe4d9f32e2`  
**Source observation:** `2026-07-22T06:57:20.626603+08:00`  
**New snapshot detected:** no; the source returned the same snapshot  
**Models returned:** 11

> “Last successful check” confirms that the automation reached the API. “Source observation” is supplied by the upstream endpoint and may be older.

> This is a model-level summary from the Codex Radar API, not the project's task-level difficulty-weighted score.

## Current API model summary

| Rank | Model tier | Source score | Passed | Tasks | Cost | Total tokens | Wall time |
|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | Terra Max | 100.9 | 75/112 | 112 | $434.58 | 1,251,296,190 | 59.51h |
| 2 | Sol Xhigh | 96.9 | 72/112 | 112 | $726.72 | 853,436,826 | 45.03h |
| 3 | Gpt-5.5 Xhigh | 94.2 | 70/112 | 112 | $653.95 | 768,130,843 | 41.58h |
| 4 | Luna Max | 92.8 | 69/112 | 112 | $55.20 | 1,817,359,264 | 64.67h |
| 5 | Gpt-5.5 High | 91.5 | 68/112 | 112 | $402.04 | 516,711,605 | 34.02h |
| 6 | Sol High | 88.8 | 66/112 | 112 | $536.11 | 635,913,352 | 35.99h |
| 7 | Terra Xhigh | 84.7 | 63/112 | 112 | $214.81 | 592,085,813 | 38.42h |
| 8 | Sol Medium | 83.4 | 62/112 | 112 | $398.37 | 484,446,533 | 34.03h |
| 9 | Terra High | 76.7 | 57/112 | 112 | $125.17 | 345,708,144 | 26.16h |
| 10 | Luna High | 74 | 55/112 | 112 | $23.56 | 760,532,288 | 34.71h |
| 11 | Sol Low | 74 | 55/112 | 112 | $224.18 | 275,712,343 | 25.08h |

## Interpretation

- The endpoint provides model-level `score`, pass counts, task counts, tokens, wall time, and estimated cost.
- It does not expose the ten task-level outcomes, so `Weighted /100` cannot be recomputed from this API summary alone.
- Task-weighted rankings remain based on the repository's task matrix and weight snapshots; this report monitors the latest API summary.
- When source data is unchanged, the automation still updates its heartbeat without presenting it as a new benchmark batch.
- The raw API response is not stored in the public repository; only required model-summary fields are archived.

Archived API snapshots: **296**.
