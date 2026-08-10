# Codex Radar API Monitor — English

[简体中文](api-latest.zh-CN.md) · [Project home](../README.md) · [API history CSV](../data/api/model_iq_history.csv) · [Monitor status](../data/api/monitor_status.json)

**Last successful check:** `2026-08-10T12:33:51+00:00`  
**Current API snapshot:** `7fd177ceb44d832b`  
**Source observation:** `2026-07-22T06:57:20.626603+08:00`  
**New snapshot detected:** yes  
**Models returned:** 11

> “Last successful check” confirms that the automation reached the API. “Source observation” is supplied by the upstream endpoint and may be older.

> This is a model-level summary from the Codex Radar API, not the project's task-level difficulty-weighted score.

## Current API model summary

| Rank | Model tier | Source score | Passed | Tasks | Cost | Total tokens | Wall time |
|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | Sol Xhigh | 107.6 | 80/112 | 112 | $737.91 | 902,106,035 | 50.57h |
| 2 | Sol High | 100.9 | 75/112 | 112 | $568.19 | 620,042,392 | 40.10h |
| 3 | Terra Max | 99.5 | 74/112 | 112 | $439.26 | 1,162,321,028 | 51.70h |
| 4 | Gpt-5.5 Xhigh | 96.9 | 72/112 | 112 | $657.37 | 815,323,847 | 41.86h |
| 5 | Luna Max | 92.8 | 69/112 | 112 | $58.68 | 1,812,876,011 | 60.97h |
| 6 | Sol Medium | 88.8 | 66/112 | 112 | $410.06 | 459,161,702 | 31.48h |
| 7 | Sol Low | 87.4 | 65/112 | 112 | $230.71 | 274,690,066 | 22.83h |
| 8 | Gpt-5.5 High | 86.1 | 64/112 | 112 | $405.29 | 472,556,002 | 29.31h |
| 9 | Terra Xhigh | 86.1 | 64/112 | 112 | $220.16 | 577,051,659 | 32.83h |
| 10 | Terra High | 72.6 | 54/112 | 112 | $127.02 | 333,563,397 | 22.70h |
| 11 | Luna High | 71.3 | 53/112 | 112 | $26.21 | 724,432,375 | 33.59h |

## Interpretation

- The endpoint provides model-level `score`, pass counts, task counts, tokens, wall time, and estimated cost.
- It does not expose the ten task-level outcomes, so `Weighted /100` cannot be recomputed from this API summary alone.
- Task-weighted rankings remain based on the repository's task matrix and weight snapshots; this report monitors the latest API summary.
- When source data is unchanged, the automation still updates its heartbeat without presenting it as a new benchmark batch.
- The raw API response is not stored in the public repository; only required model-summary fields are archived.

Archived API snapshots: **227**.
