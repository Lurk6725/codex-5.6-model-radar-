# Codex Radar API Monitor — English

[简体中文](api-latest.zh-CN.md) · [Project home](../README.md) · [API history CSV](../data/api/model_iq_history.csv) · [Monitor status](../data/api/monitor_status.json)

**Last successful check:** `2026-08-01T12:14:48+00:00`  
**Current API snapshot:** `8628c9a0f2776aea`  
**Source observation:** `2026-07-22T06:57:20.626603+08:00`  
**New snapshot detected:** yes  
**Models returned:** 11

> “Last successful check” confirms that the automation reached the API. “Source observation” is supplied by the upstream endpoint and may be older.

> This is a model-level summary from the Codex Radar API, not the project's task-level difficulty-weighted score.

## Current API model summary

| Rank | Model tier | Source score | Passed | Tasks | Cost | Total tokens | Wall time |
|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | Sol Xhigh | 99.5 | 74/112 | 112 | $770.21 | 1,004,237,049 | 47.09h |
| 2 | Gpt-5.5 Xhigh | 92.8 | 69/112 | 112 | $646.21 | 836,072,424 | 43.72h |
| 3 | Sol High | 88.8 | 66/112 | 112 | $609.32 | 798,204,093 | 40.98h |
| 4 | Terra Max | 87.4 | 65/112 | 112 | $539.06 | 1,552,295,001 | 57.67h |
| 5 | Sol Medium | 84.7 | 63/112 | 112 | $424.27 | 564,560,700 | 32.83h |
| 6 | Gpt-5.5 High | 79.4 | 59/112 | 112 | $415.21 | 533,551,635 | 32.58h |
| 7 | Luna Max | 79.4 | 59/112 | 112 | $137.53 | 1,772,398,306 | 55.97h |
| 8 | Terra High | 78 | 58/112 | 112 | $152.78 | 402,004,027 | 25.74h |
| 9 | Sol Low | 74 | 55/112 | 112 | $250.60 | 288,331,032 | 21.53h |
| 10 | Terra Xhigh | 74 | 55/112 | 112 | $271.04 | 735,473,939 | 34.58h |
| 11 | Luna High | 68.6 | 51/112 | 112 | $71.11 | 806,052,613 | 33.66h |

## Interpretation

- The endpoint provides model-level `score`, pass counts, task counts, tokens, wall time, and estimated cost.
- It does not expose the ten task-level outcomes, so `Weighted /100` cannot be recomputed from this API summary alone.
- Task-weighted rankings remain based on the repository's task matrix and weight snapshots; this report monitors the latest API summary.
- When source data is unchanged, the automation still updates its heartbeat without presenting it as a new benchmark batch.
- The raw API response is not stored in the public repository; only required model-summary fields are archived.

Archived API snapshots: **143**.
