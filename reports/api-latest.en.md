# Codex Radar API Monitor — English

[简体中文](api-latest.zh-CN.md) · [Project home](../README.md) · [API history CSV](../data/api/model_iq_history.csv) · [Monitor status](../data/api/monitor_status.json)

**Last successful check:** `2026-07-31T18:47:21+00:00`  
**Current API snapshot:** `1810c20e0b2a4e08`  
**Source observation:** `2026-07-22T06:57:20.626603+08:00`  
**New snapshot detected:** yes  
**Models returned:** 11

> “Last successful check” confirms that the automation reached the API. “Source observation” is supplied by the upstream endpoint and may be older.

> This is a model-level summary from the Codex Radar API, not the project's task-level difficulty-weighted score.

## Current API model summary

| Rank | Model tier | Source score | Passed | Tasks | Cost | Total tokens | Wall time |
|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | Sol Xhigh | 94.2 | 70/112 | 112 | $774.22 | 1,015,154,792 | 46.81h |
| 2 | Sol High | 86.1 | 64/112 | 112 | $611.53 | 824,953,211 | 41.70h |
| 3 | Gpt-5.5 Xhigh | 84.7 | 63/112 | 112 | $647.68 | 822,468,628 | 42.65h |
| 4 | Luna Max | 82.1 | 61/112 | 112 | $151.08 | 1,787,997,485 | 56.01h |
| 5 | Sol Medium | 82.1 | 61/112 | 112 | $431.52 | 556,358,573 | 32.06h |
| 6 | Terra High | 82.1 | 61/112 | 112 | $161.61 | 382,610,587 | 24.63h |
| 7 | Terra Max | 82.1 | 61/112 | 112 | $563.78 | 1,547,791,094 | 56.77h |
| 8 | Terra Xhigh | 72.6 | 54/112 | 112 | $283.39 | 730,823,164 | 34.30h |
| 9 | Gpt-5.5 High | 70 | 52/112 | 112 | $422.08 | 536,660,971 | 33.11h |
| 10 | Sol Low | 70 | 52/112 | 112 | $252.47 | 290,713,010 | 22.33h |
| 11 | Luna High | 67.3 | 50/112 | 112 | $73.64 | 782,978,865 | 32.33h |

## Interpretation

- The endpoint provides model-level `score`, pass counts, task counts, tokens, wall time, and estimated cost.
- It does not expose the ten task-level outcomes, so `Weighted /100` cannot be recomputed from this API summary alone.
- Task-weighted rankings remain based on the repository's task matrix and weight snapshots; this report monitors the latest API summary.
- When source data is unchanged, the automation still updates its heartbeat without presenting it as a new benchmark batch.
- The raw API response is not stored in the public repository; only required model-summary fields are archived.

Archived API snapshots: **135**.
