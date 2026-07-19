# Codex Radar API Monitor — English

[简体中文](api-latest.zh-CN.md) · [Project home](../README.md) · [API history CSV](../data/api/model_iq_history.csv) · [Monitor status](../data/api/monitor_status.json)

**Last successful check:** `2026-07-19T11:45:08+00:00`  
**Current API snapshot:** `0efa4232b1e8f3c2`  
**Source observation:** `2026-07-18T11:35:05.153982+08:00`  
**New snapshot detected:** yes  
**Models returned:** 9

> “Last successful check” confirms that the automation reached the API. “Source observation” is supplied by the upstream endpoint and may be older.

> This is a model-level summary from the Codex Radar API, not the project's task-level difficulty-weighted score.

## Current API model summary

| Rank | Model tier | Source score | Passed | Tasks | Cost | Total tokens | Wall time |
|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | Terra Max | 98.2 | 73/112 | 112 | $515.19 | 1,332,284,288 | 61.00h |
| 2 | Sol High | 96.9 | 72/112 | 112 | $608.54 | 777,424,936 | 44.35h |
| 3 | Sol Xhigh | 95 | 70/111 | 111 | $763.17 | 1,056,432,784 | 53.07h |
| 4 | Sol Medium | 88.8 | 66/112 | 112 | $390.64 | 497,783,619 | 34.24h |
| 5 | Luna Max | 87.4 | 65/112 | 112 | $276.70 | 1,895,368,882 | 68.19h |
| 6 | Gpt-5.5 High | 84.7 | 63/112 | 112 | $415.06 | 525,956,797 | 30.94h |
| 7 | Sol Low | 80.1 | 59/111 | 111 | $223.87 | 267,038,517 | 22.28h |
| 8 | Terra High | 67.3 | 50/112 | 112 | $146.09 | 325,691,509 | 23.36h |
| 9 | Luna High | 64.6 | 48/112 | 112 | $122.12 | 796,982,720 | 34.30h |

## Interpretation

- The endpoint provides model-level `score`, pass counts, task counts, tokens, wall time, and estimated cost.
- It does not expose the ten task-level outcomes, so `Weighted /100` cannot be recomputed from this API summary alone.
- Task-weighted rankings remain based on the repository's task matrix and weight snapshots; this report monitors the latest API summary.
- When source data is unchanged, the automation still updates its heartbeat without presenting it as a new benchmark batch.
- The raw API response is not stored in the public repository; only required model-summary fields are archived.

Archived API snapshots: **29**.
