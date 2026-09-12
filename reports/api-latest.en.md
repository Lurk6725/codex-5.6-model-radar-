# Codex Radar API Monitor — English

[简体中文](api-latest.zh-CN.md) · [Project home](../README.md) · [API history CSV](../data/api/model_iq_history.csv) · [Monitor status](../data/api/monitor_status.json)

**Last successful check:** `2026-09-12T19:27:28+00:00`  
**Current API snapshot:** `17654e2967d66266`  
**Source observation:** `2026-09-13T03:07:42.379697+08:00`  
**New snapshot detected:** no; the source returned the same snapshot  
**Models returned:** 11

> “Last successful check” confirms that the automation reached the API. “Source observation” is supplied by the upstream endpoint and may be older.

> This is a model-level summary from the Codex Radar API, not the project's task-level difficulty-weighted score.

## Current API model summary

| Rank | Model tier | Source score | Passed | Tasks | Cost | Total tokens | Wall time |
|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | Luna Max | 107.6 | 80/112 | 112 | $54.35 | 2,115,093,717 | 74.57h |
| 2 | Terra Max | 107.6 | 80/112 | 112 | $420.22 | 1,241,920,179 | 58.63h |
| 3 | Gpt-5.5 Xhigh | 104.9 | 78/112 | 112 | $639.12 | 899,261,482 | 42.82h |
| 4 | Sol Xhigh | 99.5 | 74/112 | 112 | $574.53 | 829,082,668 | 47.02h |
| 5 | Sol High | 98.2 | 73/112 | 112 | $466.63 | 585,912,217 | 37.10h |
| 6 | Sol Medium | 98.2 | 73/112 | 112 | $312.48 | 418,398,463 | 27.65h |
| 7 | Gpt-5.5 High | 84.7 | 63/112 | 112 | $397.47 | 535,538,181 | 27.05h |
| 8 | Terra Xhigh | 84.7 | 63/112 | 112 | $210.82 | 580,325,695 | 36.02h |
| 9 | Sol Low | 82.1 | 61/112 | 112 | $170.77 | 214,144,961 | 19.31h |
| 10 | Terra High | 80.7 | 60/112 | 112 | $121.97 | 317,244,282 | 25.21h |
| 11 | Luna High | 70 | 52/112 | 112 | $22.48 | 796,152,615 | 33.88h |

## Interpretation

- The endpoint provides model-level `score`, pass counts, task counts, tokens, wall time, and estimated cost.
- It does not expose the ten task-level outcomes, so `Weighted /100` cannot be recomputed from this API summary alone.
- Task-weighted rankings remain based on the repository's task matrix and weight snapshots; this report monitors the latest API summary.
- When source data is unchanged, the automation still updates its heartbeat without presenting it as a new benchmark batch.
- The raw API response is not stored in the public repository; only required model-summary fields are archived.

Archived API snapshots: **422**.
