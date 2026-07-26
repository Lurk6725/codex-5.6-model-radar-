# Codex Radar API Monitor — English

[简体中文](api-latest.zh-CN.md) · [Project home](../README.md) · [API history CSV](../data/api/model_iq_history.csv) · [Monitor status](../data/api/monitor_status.json)

**Last successful check:** `2026-07-26T04:46:22+00:00`  
**Current API snapshot:** `6d2889cec5383a8e`  
**Source observation:** `2026-07-22T06:57:20.626603+08:00`  
**New snapshot detected:** yes  
**Models returned:** 11

> “Last successful check” confirms that the automation reached the API. “Source observation” is supplied by the upstream endpoint and may be older.

> This is a model-level summary from the Codex Radar API, not the project's task-level difficulty-weighted score.

## Current API model summary

| Rank | Model tier | Source score | Passed | Tasks | Cost | Total tokens | Wall time |
|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | Terra Max | 95.5 | 71/112 | 112 | $554.86 | 1,453,468,245 | 57.31h |
| 2 | Sol High | 94.2 | 70/112 | 112 | $580.76 | 766,382,368 | 34.25h |
| 3 | Sol Medium | 94.2 | 70/112 | 112 | $438.73 | 561,741,062 | 29.77h |
| 4 | Sol Xhigh | 94.2 | 70/112 | 112 | $777.69 | 1,058,499,668 | 46.88h |
| 5 | Terra Xhigh | 88.8 | 66/112 | 112 | $283.50 | 688,611,151 | 36.27h |
| 6 | Gpt-5.5 Xhigh | 86.1 | 64/112 | 112 | $645.06 | 826,071,920 | 42.46h |
| 7 | Luna Max | 86.1 | 64/112 | 112 | $287.73 | 1,993,657,808 | 61.07h |
| 8 | Gpt-5.5 High | 79.4 | 59/112 | 112 | $416.98 | 521,618,109 | 31.62h |
| 9 | Terra High | 74 | 55/112 | 112 | $156.07 | 353,419,071 | 23.19h |
| 10 | Sol Low | 71.3 | 53/112 | 112 | $226.04 | 255,270,913 | 19.20h |
| 11 | Luna High | 65.9 | 49/112 | 112 | $112.05 | 716,407,692 | 30.58h |

## Interpretation

- The endpoint provides model-level `score`, pass counts, task counts, tokens, wall time, and estimated cost.
- It does not expose the ten task-level outcomes, so `Weighted /100` cannot be recomputed from this API summary alone.
- Task-weighted rankings remain based on the repository's task matrix and weight snapshots; this report monitors the latest API summary.
- When source data is unchanged, the automation still updates its heartbeat without presenting it as a new benchmark batch.
- The raw API response is not stored in the public repository; only required model-summary fields are archived.

Archived API snapshots: **86**.
