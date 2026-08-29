# Codex Radar API Monitor — English

[简体中文](api-latest.zh-CN.md) · [Project home](../README.md) · [API history CSV](../data/api/model_iq_history.csv) · [Monitor status](../data/api/monitor_status.json)

**Last successful check:** `2026-08-29T21:47:08+00:00`  
**Current API snapshot:** `48f73639db84c91b`  
**Source observation:** `2026-07-22T06:57:20.626603+08:00`  
**New snapshot detected:** yes  
**Models returned:** 11

> “Last successful check” confirms that the automation reached the API. “Source observation” is supplied by the upstream endpoint and may be older.

> This is a model-level summary from the Codex Radar API, not the project's task-level difficulty-weighted score.

## Current API model summary

| Rank | Model tier | Source score | Passed | Tasks | Cost | Total tokens | Wall time |
|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | Luna Max | 104.9 | 78/112 | 112 | $54.01 | 1,946,316,476 | 70.14h |
| 2 | Terra Max | 103.6 | 77/112 | 112 | $426.27 | 1,216,077,354 | 57.37h |
| 3 | Sol Xhigh | 102.2 | 76/112 | 112 | $629.65 | 824,099,757 | 45.32h |
| 4 | Gpt-5.5 Xhigh | 100.9 | 75/112 | 112 | $642.24 | 828,367,016 | 43.02h |
| 5 | Sol High | 96.9 | 72/112 | 112 | $507.94 | 599,978,454 | 35.80h |
| 6 | Sol Medium | 95.5 | 71/112 | 112 | $312.37 | 423,060,717 | 27.97h |
| 7 | Gpt-5.5 High | 86.1 | 64/112 | 112 | $398.19 | 523,208,927 | 27.80h |
| 8 | Terra Xhigh | 86.1 | 64/112 | 112 | $212.33 | 617,068,003 | 38.16h |
| 9 | Terra High | 83.4 | 62/112 | 112 | $122.90 | 346,192,333 | 26.31h |
| 10 | Sol Low | 79.4 | 59/112 | 112 | $171.66 | 215,533,913 | 16.72h |
| 11 | Luna High | 72.6 | 54/112 | 112 | $22.50 | 741,544,440 | 33.80h |

## Interpretation

- The endpoint provides model-level `score`, pass counts, task counts, tokens, wall time, and estimated cost.
- It does not expose the ten task-level outcomes, so `Weighted /100` cannot be recomputed from this API summary alone.
- Task-weighted rankings remain based on the repository's task matrix and weight snapshots; this report monitors the latest API summary.
- When source data is unchanged, the automation still updates its heartbeat without presenting it as a new benchmark batch.
- The raw API response is not stored in the public repository; only required model-summary fields are archived.

Archived API snapshots: **377**.
