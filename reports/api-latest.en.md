# Codex Radar API Monitor — English

[简体中文](api-latest.zh-CN.md) · [Project home](../README.md) · [API history CSV](../data/api/model_iq_history.csv) · [Monitor status](../data/api/monitor_status.json)

**Last successful check:** `2026-07-30T16:17:00+00:00`  
**Current API snapshot:** `7ed6e136bd1d82ac`  
**Source observation:** `2026-07-22T06:57:20.626603+08:00`  
**New snapshot detected:** yes  
**Models returned:** 11

> “Last successful check” confirms that the automation reached the API. “Source observation” is supplied by the upstream endpoint and may be older.

> This is a model-level summary from the Codex Radar API, not the project's task-level difficulty-weighted score.

## Current API model summary

| Rank | Model tier | Source score | Passed | Tasks | Cost | Total tokens | Wall time |
|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | Gpt-5.5 Xhigh | 94.2 | 70/112 | 112 | $652.78 | 832,117,531 | 44.14h |
| 2 | Sol Xhigh | 94.2 | 70/112 | 112 | $729.55 | 964,831,825 | 45.99h |
| 3 | Luna Max | 87.4 | 65/112 | 112 | $268.23 | 1,828,183,720 | 60.76h |
| 4 | Sol High | 87.4 | 65/112 | 112 | $609.06 | 810,759,900 | 41.96h |
| 5 | Gpt-5.5 High | 83.4 | 62/112 | 112 | $438.02 | 551,636,518 | 31.76h |
| 6 | Terra Max | 82.1 | 61/112 | 112 | $571.43 | 1,496,972,548 | 55.72h |
| 7 | Sol Medium | 80.7 | 60/112 | 112 | $426.18 | 526,715,170 | 31.91h |
| 8 | Sol Low | 79.4 | 59/112 | 112 | $248.94 | 289,271,373 | 22.52h |
| 9 | Terra Xhigh | 76.7 | 57/112 | 112 | $290.34 | 707,395,139 | 34.90h |
| 10 | Terra High | 72.6 | 54/112 | 112 | $165.53 | 378,066,512 | 23.56h |
| 11 | Luna High | 64.6 | 48/112 | 112 | $124.53 | 827,352,277 | 34.32h |

## Interpretation

- The endpoint provides model-level `score`, pass counts, task counts, tokens, wall time, and estimated cost.
- It does not expose the ten task-level outcomes, so `Weighted /100` cannot be recomputed from this API summary alone.
- Task-weighted rankings remain based on the repository's task matrix and weight snapshots; this report monitors the latest API summary.
- When source data is unchanged, the automation still updates its heartbeat without presenting it as a new benchmark batch.
- The raw API response is not stored in the public repository; only required model-summary fields are archived.

Archived API snapshots: **123**.
