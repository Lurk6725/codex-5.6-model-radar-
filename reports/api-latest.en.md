# Codex Radar API Monitor — English

[简体中文](api-latest.zh-CN.md) · [Project home](../README.md) · [API history CSV](../data/api/model_iq_history.csv) · [Monitor status](../data/api/monitor_status.json)

**Last successful check:** `2026-07-20T04:10:52+00:00`  
**Current API snapshot:** `bb1641756730ddab`  
**Source observation:** `2026-07-18T11:35:05.153982+08:00`  
**New snapshot detected:** yes  
**Models returned:** 11

> “Last successful check” confirms that the automation reached the API. “Source observation” is supplied by the upstream endpoint and may be older.

> This is a model-level summary from the Codex Radar API, not the project's task-level difficulty-weighted score.

## Current API model summary

| Rank | Model tier | Source score | Passed | Tasks | Cost | Total tokens | Wall time |
|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | Terra Max | 98.2 | 73/112 | 112 | $512.43 | 1,325,805,276 | 60.65h |
| 2 | Sol High | 96.9 | 72/112 | 112 | $578.95 | 746,060,506 | 43.51h |
| 3 | Sol Xhigh | 95 | 70/111 | 111 | $711.19 | 939,839,117 | 50.94h |
| 4 | Gpt-5.5 Xhigh | 91.5 | 68/112 | 112 | $649.00 | 828,937,209 | 41.50h |
| 5 | Sol Medium | 87.4 | 65/112 | 112 | $386.23 | 492,037,778 | 33.86h |
| 6 | Luna Max | 86.1 | 64/112 | 112 | $279.43 | 1,914,108,937 | 69.43h |
| 7 | Gpt-5.5 High | 84.7 | 63/112 | 112 | $401.08 | 503,003,262 | 30.29h |
| 8 | Sol Low | 82.8 | 61/111 | 111 | $225.32 | 264,620,134 | 22.74h |
| 9 | Terra Xhigh | 79.4 | 59/112 | 112 | $269.79 | 652,887,140 | 33.92h |
| 10 | Terra High | 68.6 | 51/112 | 112 | $148.24 | 333,450,383 | 23.58h |
| 11 | Luna High | 61.9 | 46/112 | 112 | $120.78 | 787,687,692 | 34.74h |

## Interpretation

- The endpoint provides model-level `score`, pass counts, task counts, tokens, wall time, and estimated cost.
- It does not expose the ten task-level outcomes, so `Weighted /100` cannot be recomputed from this API summary alone.
- Task-weighted rankings remain based on the repository's task matrix and weight snapshots; this report monitors the latest API summary.
- When source data is unchanged, the automation still updates its heartbeat without presenting it as a new benchmark batch.
- The raw API response is not stored in the public repository; only required model-summary fields are archived.

Archived API snapshots: **36**.
