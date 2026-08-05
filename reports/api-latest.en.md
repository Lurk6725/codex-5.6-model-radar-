# Codex Radar API Monitor — English

[简体中文](api-latest.zh-CN.md) · [Project home](../README.md) · [API history CSV](../data/api/model_iq_history.csv) · [Monitor status](../data/api/monitor_status.json)

**Last successful check:** `2026-08-05T21:58:36+00:00`  
**Current API snapshot:** `bbd1ae40b9e9ba49`  
**Source observation:** `2026-07-22T06:57:20.626603+08:00`  
**New snapshot detected:** yes  
**Models returned:** 11

> “Last successful check” confirms that the automation reached the API. “Source observation” is supplied by the upstream endpoint and may be older.

> This is a model-level summary from the Codex Radar API, not the project's task-level difficulty-weighted score.

## Current API model summary

| Rank | Model tier | Source score | Passed | Tasks | Cost | Total tokens | Wall time |
|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | Sol Xhigh | 113 | 84/112 | 112 | $762.56 | 952,659,137 | 47.99h |
| 2 | Gpt-5.5 Xhigh | 96.9 | 72/112 | 112 | $652.52 | 800,732,331 | 42.20h |
| 3 | Luna Max | 94.2 | 70/112 | 112 | $58.81 | 1,707,250,673 | 59.87h |
| 4 | Gpt-5.5 High | 92.8 | 69/112 | 112 | $406.43 | 496,273,801 | 31.71h |
| 5 | Sol Medium | 92.8 | 69/112 | 112 | $409.77 | 520,906,145 | 31.80h |
| 6 | Terra Max | 88.8 | 66/112 | 112 | $456.61 | 1,452,135,373 | 60.00h |
| 7 | Sol High | 84.7 | 63/112 | 112 | $587.90 | 696,965,690 | 40.27h |
| 8 | Terra Xhigh | 82.1 | 61/112 | 112 | $227.94 | 603,583,456 | 34.38h |
| 9 | Luna High | 75.3 | 56/112 | 112 | $27.57 | 731,045,614 | 30.04h |
| 10 | Terra High | 74 | 55/112 | 112 | $134.04 | 353,545,448 | 25.15h |
| 11 | Sol Low | 72.6 | 54/112 | 112 | $231.68 | 255,586,680 | 21.83h |

## Interpretation

- The endpoint provides model-level `score`, pass counts, task counts, tokens, wall time, and estimated cost.
- It does not expose the ten task-level outcomes, so `Weighted /100` cannot be recomputed from this API summary alone.
- Task-weighted rankings remain based on the repository's task matrix and weight snapshots; this report monitors the latest API summary.
- When source data is unchanged, the automation still updates its heartbeat without presenting it as a new benchmark batch.
- The raw API response is not stored in the public repository; only required model-summary fields are archived.

Archived API snapshots: **180**.
