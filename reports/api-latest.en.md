# Codex Radar API Monitor — English

[简体中文](api-latest.zh-CN.md) · [Project home](../README.md) · [API history CSV](../data/api/model_iq_history.csv) · [Monitor status](../data/api/monitor_status.json)

**Last successful check:** `2026-07-26T09:46:53+00:00`  
**Current API snapshot:** `39b7d8715ee63914`  
**Source observation:** `2026-07-22T06:57:20.626603+08:00`  
**New snapshot detected:** yes  
**Models returned:** 11

> “Last successful check” confirms that the automation reached the API. “Source observation” is supplied by the upstream endpoint and may be older.

> This is a model-level summary from the Codex Radar API, not the project's task-level difficulty-weighted score.

## Current API model summary

| Rank | Model tier | Source score | Passed | Tasks | Cost | Total tokens | Wall time |
|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | Sol Xhigh | 96.9 | 72/112 | 112 | $798.58 | 1,101,422,572 | 49.63h |
| 2 | Sol Medium | 94.2 | 70/112 | 112 | $449.69 | 579,879,585 | 30.93h |
| 3 | Terra Max | 94.2 | 70/112 | 112 | $539.47 | 1,415,984,823 | 56.22h |
| 4 | Luna Max | 92.8 | 69/112 | 112 | $284.82 | 1,966,269,526 | 61.62h |
| 5 | Sol High | 92.8 | 69/112 | 112 | $583.39 | 773,076,353 | 35.03h |
| 6 | Gpt-5.5 High | 88.8 | 66/112 | 112 | $420.84 | 529,330,445 | 31.73h |
| 7 | Gpt-5.5 Xhigh | 83.4 | 62/112 | 112 | $636.53 | 812,651,877 | 40.70h |
| 8 | Terra Xhigh | 83.4 | 62/112 | 112 | $284.16 | 690,934,300 | 35.86h |
| 9 | Sol Low | 75.3 | 56/112 | 112 | $225.19 | 253,480,097 | 18.83h |
| 10 | Terra High | 70 | 52/112 | 112 | $152.32 | 344,071,422 | 22.72h |
| 11 | Luna High | 64.6 | 48/112 | 112 | $114.84 | 735,551,289 | 29.69h |

## Interpretation

- The endpoint provides model-level `score`, pass counts, task counts, tokens, wall time, and estimated cost.
- It does not expose the ten task-level outcomes, so `Weighted /100` cannot be recomputed from this API summary alone.
- Task-weighted rankings remain based on the repository's task matrix and weight snapshots; this report monitors the latest API summary.
- When source data is unchanged, the automation still updates its heartbeat without presenting it as a new benchmark batch.
- The raw API response is not stored in the public repository; only required model-summary fields are archived.

Archived API snapshots: **88**.
