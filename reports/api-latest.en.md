# Codex Radar API Monitor — English

[简体中文](api-latest.zh-CN.md) · [Project home](../README.md) · [API history CSV](../data/api/model_iq_history.csv) · [Monitor status](../data/api/monitor_status.json)

**Last successful check:** `2026-08-15T03:56:38+00:00`  
**Current API snapshot:** `c38d4ad61953ac55`  
**Source observation:** `2026-07-22T06:57:20.626603+08:00`  
**New snapshot detected:** no; the source returned the same snapshot  
**Models returned:** 11

> “Last successful check” confirms that the automation reached the API. “Source observation” is supplied by the upstream endpoint and may be older.

> This is a model-level summary from the Codex Radar API, not the project's task-level difficulty-weighted score.

## Current API model summary

| Rank | Model tier | Source score | Passed | Tasks | Cost | Total tokens | Wall time |
|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | Sol Xhigh | 99.5 | 74/112 | 112 | $725.81 | 852,956,696 | 45.31h |
| 2 | Terra Max | 99.5 | 74/112 | 112 | $435.41 | 1,255,614,743 | 59.87h |
| 3 | Gpt-5.5 Xhigh | 96.9 | 72/112 | 112 | $655.98 | 743,096,131 | 42.31h |
| 4 | Luna Max | 95.5 | 71/112 | 112 | $58.57 | 1,811,800,870 | 65.44h |
| 5 | Gpt-5.5 High | 92.8 | 69/112 | 112 | $403.64 | 499,074,683 | 32.74h |
| 6 | Sol High | 90.1 | 67/112 | 112 | $538.11 | 648,947,723 | 36.10h |
| 7 | Sol Medium | 87.4 | 65/112 | 112 | $382.76 | 455,481,969 | 32.41h |
| 8 | Terra Xhigh | 84.7 | 63/112 | 112 | $217.14 | 590,991,961 | 37.45h |
| 9 | Luna High | 75.3 | 56/112 | 112 | $26.16 | 782,075,070 | 36.45h |
| 10 | Terra High | 75.3 | 56/112 | 112 | $126.50 | 342,617,664 | 26.20h |
| 11 | Sol Low | 64.6 | 48/112 | 112 | $225.43 | 272,754,663 | 24.40h |

## Interpretation

- The endpoint provides model-level `score`, pass counts, task counts, tokens, wall time, and estimated cost.
- It does not expose the ten task-level outcomes, so `Weighted /100` cannot be recomputed from this API summary alone.
- Task-weighted rankings remain based on the repository's task matrix and weight snapshots; this report monitors the latest API summary.
- When source data is unchanged, the automation still updates its heartbeat without presenting it as a new benchmark batch.
- The raw API response is not stored in the public repository; only required model-summary fields are archived.

Archived API snapshots: **262**.
