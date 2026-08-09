# Codex Radar API Monitor — English

[简体中文](api-latest.zh-CN.md) · [Project home](../README.md) · [API history CSV](../data/api/model_iq_history.csv) · [Monitor status](../data/api/monitor_status.json)

**Last successful check:** `2026-08-09T15:14:35+00:00`  
**Current API snapshot:** `fdfe498b8711c027`  
**Source observation:** `2026-07-22T06:57:20.626603+08:00`  
**New snapshot detected:** no; the source returned the same snapshot  
**Models returned:** 11

> “Last successful check” confirms that the automation reached the API. “Source observation” is supplied by the upstream endpoint and may be older.

> This is a model-level summary from the Codex Radar API, not the project's task-level difficulty-weighted score.

## Current API model summary

| Rank | Model tier | Source score | Passed | Tasks | Cost | Total tokens | Wall time |
|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | Sol Xhigh | 110.3 | 82/112 | 112 | $744.60 | 929,042,216 | 50.15h |
| 2 | Sol High | 100.9 | 75/112 | 112 | $570.87 | 584,192,707 | 35.84h |
| 3 | Gpt-5.5 Xhigh | 94.2 | 70/112 | 112 | $658.03 | 815,748,355 | 41.60h |
| 4 | Sol Medium | 94.2 | 70/112 | 112 | $411.87 | 521,016,305 | 32.36h |
| 5 | Luna Max | 92.8 | 69/112 | 112 | $58.72 | 1,757,350,948 | 60.13h |
| 6 | Terra Max | 92.8 | 69/112 | 112 | $435.31 | 1,242,921,098 | 52.58h |
| 7 | Sol Low | 86.1 | 64/112 | 112 | $229.61 | 284,316,040 | 21.92h |
| 8 | Terra Xhigh | 86.1 | 64/112 | 112 | $220.84 | 592,105,213 | 32.34h |
| 9 | Gpt-5.5 High | 83.4 | 62/112 | 112 | $406.03 | 471,958,389 | 28.18h |
| 10 | Terra High | 80.7 | 60/112 | 112 | $126.98 | 334,036,400 | 22.17h |
| 11 | Luna High | 70 | 52/112 | 112 | $26.23 | 720,793,763 | 31.42h |

## Interpretation

- The endpoint provides model-level `score`, pass counts, task counts, tokens, wall time, and estimated cost.
- It does not expose the ten task-level outcomes, so `Weighted /100` cannot be recomputed from this API summary alone.
- Task-weighted rankings remain based on the repository's task matrix and weight snapshots; this report monitors the latest API summary.
- When source data is unchanged, the automation still updates its heartbeat without presenting it as a new benchmark batch.
- The raw API response is not stored in the public repository; only required model-summary fields are archived.

Archived API snapshots: **216**.
