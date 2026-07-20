# Codex Radar API Monitor — English

[简体中文](api-latest.zh-CN.md) · [Project home](../README.md) · [API history CSV](../data/api/model_iq_history.csv) · [Monitor status](../data/api/monitor_status.json)

**Last successful check:** `2026-07-20T21:51:56+00:00`  
**Current API snapshot:** `5207691914472b1b`  
**Source observation:** `2026-07-18T11:35:05.153982+08:00`  
**New snapshot detected:** no; the source returned the same snapshot  
**Models returned:** 11

> “Last successful check” confirms that the automation reached the API. “Source observation” is supplied by the upstream endpoint and may be older.

> This is a model-level summary from the Codex Radar API, not the project's task-level difficulty-weighted score.

## Current API model summary

| Rank | Model tier | Source score | Passed | Tasks | Cost | Total tokens | Wall time |
|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | Terra Max | 99.5 | 74/112 | 112 | $513.41 | 1,332,096,409 | 60.45h |
| 2 | Sol High | 95.5 | 71/112 | 112 | $549.25 | 688,825,121 | 41.43h |
| 3 | Gpt-5.5 Xhigh | 94.2 | 70/112 | 112 | $652.93 | 831,903,815 | 40.25h |
| 4 | Sol Medium | 94.2 | 70/112 | 112 | $389.61 | 493,856,231 | 33.99h |
| 5 | Sol Xhigh | 93.7 | 69/111 | 111 | $755.10 | 1,001,745,163 | 51.67h |
| 6 | Luna Max | 87.4 | 65/112 | 112 | $283.68 | 1,954,599,939 | 71.56h |
| 7 | Gpt-5.5 High | 84.7 | 63/112 | 112 | $406.22 | 511,287,441 | 30.41h |
| 8 | Terra Xhigh | 84.7 | 63/112 | 112 | $278.89 | 680,211,588 | 36.06h |
| 9 | Sol Low | 80.1 | 59/111 | 111 | $227.98 | 261,045,068 | 23.37h |
| 10 | Terra High | 70 | 52/112 | 112 | $151.70 | 342,150,384 | 23.67h |
| 11 | Luna High | 67.3 | 50/112 | 112 | $121.13 | 793,042,455 | 35.68h |

## Interpretation

- The endpoint provides model-level `score`, pass counts, task counts, tokens, wall time, and estimated cost.
- It does not expose the ten task-level outcomes, so `Weighted /100` cannot be recomputed from this API summary alone.
- Task-weighted rankings remain based on the repository's task matrix and weight snapshots; this report monitors the latest API summary.
- When source data is unchanged, the automation still updates its heartbeat without presenting it as a new benchmark batch.
- The raw API response is not stored in the public repository; only required model-summary fields are archived.

Archived API snapshots: **39**.
