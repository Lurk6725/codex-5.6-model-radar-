# Codex Radar API Monitor — English

[简体中文](api-latest.zh-CN.md) · [Project home](../README.md) · [API history CSV](../data/api/model_iq_history.csv) · [Monitor status](../data/api/monitor_status.json)

**Last successful check:** `2026-07-28T18:04:14+00:00`  
**Current API snapshot:** `3c5450483d6498a4`  
**Source observation:** `2026-07-22T06:57:20.626603+08:00`  
**New snapshot detected:** yes  
**Models returned:** 11

> “Last successful check” confirms that the automation reached the API. “Source observation” is supplied by the upstream endpoint and may be older.

> This is a model-level summary from the Codex Radar API, not the project's task-level difficulty-weighted score.

## Current API model summary

| Rank | Model tier | Source score | Passed | Tasks | Cost | Total tokens | Wall time |
|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | Sol Xhigh | 96.9 | 72/112 | 112 | $726.42 | 949,042,487 | 44.38h |
| 2 | Sol Medium | 91.5 | 68/112 | 112 | $409.83 | 503,750,697 | 31.59h |
| 3 | Terra Max | 90.1 | 67/112 | 112 | $532.08 | 1,390,320,381 | 57.01h |
| 4 | Gpt-5.5 Xhigh | 88.8 | 66/112 | 112 | $664.78 | 844,880,183 | 45.75h |
| 5 | Luna Max | 88.8 | 66/112 | 112 | $277.28 | 1,901,876,895 | 61.41h |
| 6 | Sol High | 88.8 | 66/112 | 112 | $567.87 | 727,470,428 | 41.02h |
| 7 | Gpt-5.5 High | 84.7 | 63/112 | 112 | $411.86 | 505,439,638 | 30.01h |
| 8 | Terra Xhigh | 83.4 | 62/112 | 112 | $301.92 | 761,377,974 | 37.00h |
| 9 | Sol Low | 79.4 | 59/112 | 112 | $234.03 | 267,499,133 | 18.30h |
| 10 | Luna High | 72.6 | 54/112 | 112 | $121.82 | 799,925,406 | 33.16h |
| 11 | Terra High | 72.6 | 54/112 | 112 | $156.01 | 348,651,308 | 23.67h |

## Interpretation

- The endpoint provides model-level `score`, pass counts, task counts, tokens, wall time, and estimated cost.
- It does not expose the ten task-level outcomes, so `Weighted /100` cannot be recomputed from this API summary alone.
- Task-weighted rankings remain based on the repository's task matrix and weight snapshots; this report monitors the latest API summary.
- When source data is unchanged, the automation still updates its heartbeat without presenting it as a new benchmark batch.
- The raw API response is not stored in the public repository; only required model-summary fields are archived.

Archived API snapshots: **105**.
