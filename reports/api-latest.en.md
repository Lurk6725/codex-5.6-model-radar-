# Codex Radar API Monitor — English

[简体中文](api-latest.zh-CN.md) · [Project home](../README.md) · [API history CSV](../data/api/model_iq_history.csv) · [Monitor status](../data/api/monitor_status.json)

**Last successful check:** `2026-08-11T19:49:03+00:00`  
**Current API snapshot:** `b4f86a6adf6e090a`  
**Source observation:** `2026-07-22T06:57:20.626603+08:00`  
**New snapshot detected:** yes  
**Models returned:** 11

> “Last successful check” confirms that the automation reached the API. “Source observation” is supplied by the upstream endpoint and may be older.

> This is a model-level summary from the Codex Radar API, not the project's task-level difficulty-weighted score.

## Current API model summary

| Rank | Model tier | Source score | Passed | Tasks | Cost | Total tokens | Wall time |
|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | Sol Xhigh | 109 | 81/112 | 112 | $736.17 | 896,244,482 | 50.19h |
| 2 | Sol High | 102.2 | 76/112 | 112 | $563.02 | 645,121,803 | 38.21h |
| 3 | Luna Max | 100.9 | 75/112 | 112 | $58.58 | 1,817,141,376 | 62.92h |
| 4 | Terra Max | 98.2 | 73/112 | 112 | $437.80 | 1,193,139,206 | 54.11h |
| 5 | Gpt-5.5 High | 94.2 | 70/112 | 112 | $404.10 | 486,871,531 | 32.27h |
| 6 | Gpt-5.5 Xhigh | 88.8 | 66/112 | 112 | $657.01 | 740,440,818 | 40.44h |
| 7 | Sol Medium | 88.8 | 66/112 | 112 | $407.70 | 469,237,031 | 31.40h |
| 8 | Terra Xhigh | 86.1 | 64/112 | 112 | $219.50 | 570,048,558 | 33.75h |
| 9 | Terra High | 79.4 | 59/112 | 112 | $127.21 | 331,103,036 | 23.56h |
| 10 | Sol Low | 78 | 58/112 | 112 | $229.63 | 276,098,442 | 22.93h |
| 11 | Luna High | 65.9 | 49/112 | 112 | $26.19 | 754,927,311 | 34.51h |

## Interpretation

- The endpoint provides model-level `score`, pass counts, task counts, tokens, wall time, and estimated cost.
- It does not expose the ten task-level outcomes, so `Weighted /100` cannot be recomputed from this API summary alone.
- Task-weighted rankings remain based on the repository's task matrix and weight snapshots; this report monitors the latest API summary.
- When source data is unchanged, the automation still updates its heartbeat without presenting it as a new benchmark batch.
- The raw API response is not stored in the public repository; only required model-summary fields are archived.

Archived API snapshots: **235**.
