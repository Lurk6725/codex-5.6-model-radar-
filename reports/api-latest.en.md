# Codex Radar API Monitor — English

[简体中文](api-latest.zh-CN.md) · [Project home](../README.md) · [API history CSV](../data/api/model_iq_history.csv) · [Monitor status](../data/api/monitor_status.json)

**Last successful check:** `2026-08-09T07:41:12+00:00`  
**Current API snapshot:** `cbc64ea0e0e43885`  
**Source observation:** `2026-07-22T06:57:20.626603+08:00`  
**New snapshot detected:** yes  
**Models returned:** 11

> “Last successful check” confirms that the automation reached the API. “Source observation” is supplied by the upstream endpoint and may be older.

> This is a model-level summary from the Codex Radar API, not the project's task-level difficulty-weighted score.

## Current API model summary

| Rank | Model tier | Source score | Passed | Tasks | Cost | Total tokens | Wall time |
|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | Sol Xhigh | 111.7 | 83/112 | 112 | $747.74 | 923,312,721 | 48.49h |
| 2 | Sol High | 96.9 | 72/112 | 112 | $569.74 | 601,373,120 | 35.48h |
| 3 | Gpt-5.5 High | 92.8 | 69/112 | 112 | $406.93 | 482,941,650 | 31.39h |
| 4 | Terra Max | 92.8 | 69/112 | 112 | $443.29 | 1,317,242,550 | 56.12h |
| 5 | Gpt-5.5 Xhigh | 87.4 | 65/112 | 112 | $658.44 | 795,407,097 | 41.68h |
| 6 | Luna Max | 87.4 | 65/112 | 112 | $58.83 | 1,717,314,468 | 59.90h |
| 7 | Sol Medium | 84.7 | 63/112 | 112 | $408.47 | 519,599,838 | 31.63h |
| 8 | Terra Xhigh | 84.7 | 63/112 | 112 | $225.41 | 605,976,261 | 34.97h |
| 9 | Sol Low | 83.4 | 62/112 | 112 | $228.43 | 265,777,090 | 22.12h |
| 10 | Terra High | 78 | 58/112 | 112 | $127.34 | 341,618,169 | 22.88h |
| 11 | Luna High | 76.7 | 57/112 | 112 | $26.24 | 734,200,479 | 31.39h |

## Interpretation

- The endpoint provides model-level `score`, pass counts, task counts, tokens, wall time, and estimated cost.
- It does not expose the ten task-level outcomes, so `Weighted /100` cannot be recomputed from this API summary alone.
- Task-weighted rankings remain based on the repository's task matrix and weight snapshots; this report monitors the latest API summary.
- When source data is unchanged, the automation still updates its heartbeat without presenting it as a new benchmark batch.
- The raw API response is not stored in the public repository; only required model-summary fields are archived.

Archived API snapshots: **213**.
