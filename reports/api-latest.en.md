# Codex Radar API Monitor — English

[简体中文](api-latest.zh-CN.md) · [Project home](../README.md) · [API history CSV](../data/api/model_iq_history.csv) · [Monitor status](../data/api/monitor_status.json)

**Last successful check:** `2026-07-19T19:57:12+00:00`  
**Current API snapshot:** `db50eff1d7895170`  
**Source observation:** `2026-07-18T11:35:05.153982+08:00`  
**New snapshot detected:** yes  
**Models returned:** 11

> “Last successful check” confirms that the automation reached the API. “Source observation” is supplied by the upstream endpoint and may be older.

> This is a model-level summary from the Codex Radar API, not the project's task-level difficulty-weighted score.

## Current API model summary

| Rank | Model tier | Source score | Passed | Tasks | Cost | Total tokens | Wall time |
|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | Terra Max | 98.2 | 73/112 | 112 | $515.42 | 1,334,483,734 | 60.74h |
| 2 | Sol High | 96.9 | 72/112 | 112 | $591.51 | 755,391,940 | 43.64h |
| 3 | Sol Xhigh | 92.3 | 68/111 | 111 | $704.30 | 931,551,354 | 50.87h |
| 4 | Gpt-5.5 Xhigh | 91.5 | 68/112 | 112 | $649.00 | 828,937,209 | 41.50h |
| 5 | Sol Medium | 88.8 | 66/112 | 112 | $388.07 | 494,461,281 | 33.97h |
| 6 | Luna Max | 86.1 | 64/112 | 112 | $278.57 | 1,905,426,683 | 69.27h |
| 7 | Gpt-5.5 High | 84.7 | 63/112 | 112 | $411.93 | 521,297,320 | 30.88h |
| 8 | Sol Low | 82.8 | 61/111 | 111 | $225.30 | 265,578,474 | 22.57h |
| 9 | Terra Xhigh | 79.4 | 59/112 | 112 | $258.36 | 614,409,426 | 33.22h |
| 10 | Terra High | 67.3 | 50/112 | 112 | $146.06 | 326,128,420 | 23.39h |
| 11 | Luna High | 64.6 | 48/112 | 112 | $120.69 | 785,694,246 | 34.47h |

## Interpretation

- The endpoint provides model-level `score`, pass counts, task counts, tokens, wall time, and estimated cost.
- It does not expose the ten task-level outcomes, so `Weighted /100` cannot be recomputed from this API summary alone.
- Task-weighted rankings remain based on the repository's task matrix and weight snapshots; this report monitors the latest API summary.
- When source data is unchanged, the automation still updates its heartbeat without presenting it as a new benchmark batch.
- The raw API response is not stored in the public repository; only required model-summary fields are archived.

Archived API snapshots: **33**.
