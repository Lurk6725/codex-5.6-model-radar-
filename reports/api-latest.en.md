# Codex Radar API Monitor — English

[简体中文](api-latest.zh-CN.md) · [Project home](../README.md) · [API history CSV](../data/api/model_iq_history.csv) · [Monitor status](../data/api/monitor_status.json)

**Last successful check:** `2026-08-31T00:38:51+00:00`  
**Current API snapshot:** `ac44216b33771aa2`  
**Source observation:** `2026-08-30T20:01:21.823608+08:00`  
**New snapshot detected:** yes  
**Models returned:** 11

> “Last successful check” confirms that the automation reached the API. “Source observation” is supplied by the upstream endpoint and may be older.

> This is a model-level summary from the Codex Radar API, not the project's task-level difficulty-weighted score.

## Current API model summary

| Rank | Model tier | Source score | Passed | Tasks | Cost | Total tokens | Wall time |
|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | Luna Max | 103.6 | 77/112 | 112 | $54.12 | 2,024,002,846 | 72.41h |
| 2 | Terra Max | 103.6 | 77/112 | 112 | $423.73 | 1,217,325,728 | 57.33h |
| 3 | Sol High | 102.2 | 76/112 | 112 | $486.99 | 585,979,740 | 36.01h |
| 4 | Sol Xhigh | 100.9 | 75/112 | 112 | $591.57 | 800,634,654 | 43.38h |
| 5 | Gpt-5.5 Xhigh | 99.5 | 74/112 | 112 | $639.23 | 882,048,919 | 43.06h |
| 6 | Sol Medium | 95.5 | 71/112 | 112 | $312.62 | 428,318,602 | 27.73h |
| 7 | Gpt-5.5 High | 88.8 | 66/112 | 112 | $397.58 | 529,374,487 | 28.10h |
| 8 | Terra Xhigh | 87.4 | 65/112 | 112 | $211.41 | 588,277,381 | 36.43h |
| 9 | Sol Low | 80.7 | 60/112 | 112 | $171.21 | 209,369,741 | 16.61h |
| 10 | Terra High | 76.7 | 57/112 | 112 | $122.30 | 344,192,452 | 25.61h |
| 11 | Luna High | 68.6 | 51/112 | 112 | $22.48 | 809,103,069 | 34.39h |

## Interpretation

- The endpoint provides model-level `score`, pass counts, task counts, tokens, wall time, and estimated cost.
- It does not expose the ten task-level outcomes, so `Weighted /100` cannot be recomputed from this API summary alone.
- Task-weighted rankings remain based on the repository's task matrix and weight snapshots; this report monitors the latest API summary.
- When source data is unchanged, the automation still updates its heartbeat without presenting it as a new benchmark batch.
- The raw API response is not stored in the public repository; only required model-summary fields are archived.

Archived API snapshots: **384**.
