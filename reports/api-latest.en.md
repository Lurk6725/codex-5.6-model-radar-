# Codex Radar API Monitor — English

[简体中文](api-latest.zh-CN.md) · [Project home](../README.md) · [API history CSV](../data/api/model_iq_history.csv) · [Monitor status](../data/api/monitor_status.json)

**Last successful check:** `2026-07-28T01:07:54+00:00`  
**Current API snapshot:** `8be17b661ad8c19f`  
**Source observation:** `2026-07-22T06:57:20.626603+08:00`  
**New snapshot detected:** no; the source returned the same snapshot  
**Models returned:** 11

> “Last successful check” confirms that the automation reached the API. “Source observation” is supplied by the upstream endpoint and may be older.

> This is a model-level summary from the Codex Radar API, not the project's task-level difficulty-weighted score.

## Current API model summary

| Rank | Model tier | Source score | Passed | Tasks | Cost | Total tokens | Wall time |
|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | Luna Max | 95.5 | 71/112 | 112 | $274.58 | 1,882,630,175 | 59.73h |
| 2 | Sol Medium | 95.5 | 71/112 | 112 | $416.09 | 513,401,186 | 31.34h |
| 3 | Sol High | 94.2 | 70/112 | 112 | $580.33 | 739,075,008 | 41.75h |
| 4 | Terra Max | 92.8 | 69/112 | 112 | $529.95 | 1,410,364,350 | 55.87h |
| 5 | Sol Xhigh | 88.8 | 66/112 | 112 | $815.49 | 1,130,596,633 | 53.41h |
| 6 | Gpt-5.5 Xhigh | 87.4 | 65/112 | 112 | $655.19 | 840,083,533 | 42.55h |
| 7 | Gpt-5.5 High | 83.4 | 62/112 | 112 | $413.55 | 512,760,588 | 31.00h |
| 8 | Terra Xhigh | 80.7 | 60/112 | 112 | $295.10 | 740,098,427 | 37.20h |
| 9 | Luna High | 74 | 55/112 | 112 | $117.88 | 763,403,444 | 31.97h |
| 10 | Sol Low | 72.6 | 54/112 | 112 | $219.30 | 246,111,949 | 19.20h |
| 11 | Terra High | 68.6 | 51/112 | 112 | $149.16 | 330,583,115 | 21.91h |

## Interpretation

- The endpoint provides model-level `score`, pass counts, task counts, tokens, wall time, and estimated cost.
- It does not expose the ten task-level outcomes, so `Weighted /100` cannot be recomputed from this API summary alone.
- Task-weighted rankings remain based on the repository's task matrix and weight snapshots; this report monitors the latest API summary.
- When source data is unchanged, the automation still updates its heartbeat without presenting it as a new benchmark batch.
- The raw API response is not stored in the public repository; only required model-summary fields are archived.

Archived API snapshots: **99**.
