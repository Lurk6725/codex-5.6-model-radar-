# Codex Radar API Monitor — English

[简体中文](api-latest.zh-CN.md) · [Project home](../README.md) · [API history CSV](../data/api/model_iq_history.csv) · [Monitor status](../data/api/monitor_status.json)

**Last successful check:** `2026-08-19T07:56:06+00:00`  
**Current API snapshot:** `5d48425f35c2a6a6`  
**Source observation:** `2026-07-22T06:57:20.626603+08:00`  
**New snapshot detected:** no; the source returned the same snapshot  
**Models returned:** 11

> “Last successful check” confirms that the automation reached the API. “Source observation” is supplied by the upstream endpoint and may be older.

> This is a model-level summary from the Codex Radar API, not the project's task-level difficulty-weighted score.

## Current API model summary

| Rank | Model tier | Source score | Passed | Tasks | Cost | Total tokens | Wall time |
|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | Terra Max | 99.5 | 74/112 | 112 | $434.13 | 1,269,935,930 | 60.26h |
| 2 | Sol Xhigh | 96.9 | 72/112 | 112 | $728.37 | 847,566,312 | 45.04h |
| 3 | Gpt-5.5 Xhigh | 95.5 | 71/112 | 112 | $654.30 | 770,411,058 | 41.80h |
| 4 | Luna Max | 94.2 | 70/112 | 112 | $55.23 | 1,825,563,593 | 64.68h |
| 5 | Gpt-5.5 High | 90.1 | 67/112 | 112 | $403.30 | 500,251,578 | 33.37h |
| 6 | Terra Xhigh | 87.4 | 65/112 | 112 | $215.32 | 602,876,520 | 39.04h |
| 7 | Sol High | 86.1 | 64/112 | 112 | $538.00 | 627,758,248 | 35.67h |
| 8 | Sol Medium | 84.7 | 63/112 | 112 | $392.23 | 487,251,247 | 34.10h |
| 9 | Terra High | 75.3 | 56/112 | 112 | $125.28 | 348,787,717 | 26.26h |
| 10 | Luna High | 71.3 | 53/112 | 112 | $23.63 | 767,778,088 | 34.67h |
| 11 | Sol Low | 70 | 52/112 | 112 | $225.68 | 274,347,250 | 24.67h |

## Interpretation

- The endpoint provides model-level `score`, pass counts, task counts, tokens, wall time, and estimated cost.
- It does not expose the ten task-level outcomes, so `Weighted /100` cannot be recomputed from this API summary alone.
- Task-weighted rankings remain based on the repository's task matrix and weight snapshots; this report monitors the latest API summary.
- When source data is unchanged, the automation still updates its heartbeat without presenting it as a new benchmark batch.
- The raw API response is not stored in the public repository; only required model-summary fields are archived.

Archived API snapshots: **294**.
