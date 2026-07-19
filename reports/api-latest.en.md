# Codex Radar API Monitor — English

[简体中文](api-latest.zh-CN.md) · [Project home](../README.md) · [API history CSV](../data/api/model_iq_history.csv) · [Monitor status](../data/api/monitor_status.json)

**Last successful check:** `2026-07-19T16:38:03+00:00`  
**Current API snapshot:** `2d2dcff2a4b51133`  
**Source observation:** `2026-07-18T11:35:05.153982+08:00`  
**New snapshot detected:** no; the source returned the same snapshot  
**Models returned:** 11

> “Last successful check” confirms that the automation reached the API. “Source observation” is supplied by the upstream endpoint and may be older.

> This is a model-level summary from the Codex Radar API, not the project's task-level difficulty-weighted score.

## Current API model summary

| Rank | Model tier | Source score | Passed | Tasks | Cost | Total tokens | Wall time |
|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | Terra Max | 98.2 | 73/112 | 112 | $515.26 | 1,333,366,950 | 60.77h |
| 2 | Sol High | 96.9 | 72/112 | 112 | $608.74 | 777,268,287 | 44.18h |
| 3 | Sol Xhigh | 95 | 70/111 | 111 | $773.03 | 1,057,247,465 | 53.33h |
| 4 | Gpt-5.5 Xhigh | 91.5 | 68/112 | 112 | $645.12 | 824,050,419 | 41.19h |
| 5 | Luna Max | 88.8 | 66/112 | 112 | $279.26 | 1,915,537,704 | 69.19h |
| 6 | Sol Medium | 88.8 | 66/112 | 112 | $390.97 | 497,288,307 | 34.28h |
| 7 | Gpt-5.5 High | 83.4 | 62/112 | 112 | $419.23 | 531,216,438 | 31.38h |
| 8 | Sol Low | 78.7 | 58/111 | 111 | $223.85 | 263,426,102 | 22.26h |
| 9 | Terra Xhigh | 78.7 | 58/111 | 111 | $255.59 | 606,048,573 | 32.66h |
| 10 | Terra High | 67.3 | 50/112 | 112 | $146.06 | 326,128,420 | 23.39h |
| 11 | Luna High | 63.2 | 47/112 | 112 | $122.12 | 797,696,342 | 34.71h |

## Interpretation

- The endpoint provides model-level `score`, pass counts, task counts, tokens, wall time, and estimated cost.
- It does not expose the ten task-level outcomes, so `Weighted /100` cannot be recomputed from this API summary alone.
- Task-weighted rankings remain based on the repository's task matrix and weight snapshots; this report monitors the latest API summary.
- When source data is unchanged, the automation still updates its heartbeat without presenting it as a new benchmark batch.
- The raw API response is not stored in the public repository; only required model-summary fields are archived.

Archived API snapshots: **31**.
