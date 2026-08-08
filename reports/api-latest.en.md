# Codex Radar API Monitor — English

[简体中文](api-latest.zh-CN.md) · [Project home](../README.md) · [API history CSV](../data/api/model_iq_history.csv) · [Monitor status](../data/api/monitor_status.json)

**Last successful check:** `2026-08-08T07:17:54+00:00`  
**Current API snapshot:** `2ce16cde8756ed60`  
**Source observation:** `2026-07-22T06:57:20.626603+08:00`  
**New snapshot detected:** no; the source returned the same snapshot  
**Models returned:** 11

> “Last successful check” confirms that the automation reached the API. “Source observation” is supplied by the upstream endpoint and may be older.

> This is a model-level summary from the Codex Radar API, not the project's task-level difficulty-weighted score.

## Current API model summary

| Rank | Model tier | Source score | Passed | Tasks | Cost | Total tokens | Wall time |
|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | Sol Xhigh | 107.6 | 80/112 | 112 | $755.23 | 958,699,800 | 47.74h |
| 2 | Luna Max | 96.9 | 72/112 | 112 | $58.70 | 1,819,246,456 | 63.03h |
| 3 | Gpt-5.5 High | 92.8 | 69/112 | 112 | $407.62 | 496,766,773 | 33.22h |
| 4 | Gpt-5.5 Xhigh | 92.8 | 69/112 | 112 | $648.64 | 807,228,788 | 41.57h |
| 5 | Sol High | 91.5 | 68/112 | 112 | $583.64 | 642,932,239 | 37.91h |
| 6 | Sol Medium | 91.5 | 68/112 | 112 | $410.43 | 545,557,424 | 32.03h |
| 7 | Terra Max | 88.8 | 66/112 | 112 | $456.08 | 1,405,245,936 | 59.48h |
| 8 | Sol Low | 87.4 | 65/112 | 112 | $231.17 | 272,413,353 | 23.39h |
| 9 | Terra Xhigh | 83.4 | 62/112 | 112 | $227.82 | 640,437,210 | 36.48h |
| 10 | Luna High | 79.4 | 59/112 | 112 | $26.08 | 738,117,942 | 31.63h |
| 11 | Terra High | 76.7 | 57/112 | 112 | $129.45 | 349,517,437 | 24.95h |

## Interpretation

- The endpoint provides model-level `score`, pass counts, task counts, tokens, wall time, and estimated cost.
- It does not expose the ten task-level outcomes, so `Weighted /100` cannot be recomputed from this API summary alone.
- Task-weighted rankings remain based on the repository's task matrix and weight snapshots; this report monitors the latest API summary.
- When source data is unchanged, the automation still updates its heartbeat without presenting it as a new benchmark batch.
- The raw API response is not stored in the public repository; only required model-summary fields are archived.

Archived API snapshots: **200**.
