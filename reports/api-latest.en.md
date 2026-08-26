# Codex Radar API Monitor — English

[简体中文](api-latest.zh-CN.md) · [Project home](../README.md) · [API history CSV](../data/api/model_iq_history.csv) · [Monitor status](../data/api/monitor_status.json)

**Last successful check:** `2026-08-26T04:24:57+00:00`  
**Current API snapshot:** `bea4a7a65cbb0a1f`  
**Source observation:** `2026-07-22T06:57:20.626603+08:00`  
**New snapshot detected:** yes  
**Models returned:** 11

> “Last successful check” confirms that the automation reached the API. “Source observation” is supplied by the upstream endpoint and may be older.

> This is a model-level summary from the Codex Radar API, not the project's task-level difficulty-weighted score.

## Current API model summary

| Rank | Model tier | Source score | Passed | Tasks | Cost | Total tokens | Wall time |
|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | Sol Xhigh | 104.9 | 78/112 | 112 | $698.11 | 803,438,240 | 44.37h |
| 2 | Gpt-5.5 Xhigh | 100.9 | 75/112 | 112 | $646.64 | 774,754,216 | 40.33h |
| 3 | Luna Max | 100.9 | 75/112 | 112 | $54.06 | 1,694,370,246 | 59.26h |
| 4 | Sol Medium | 96.9 | 72/112 | 112 | $372.22 | 415,548,255 | 28.75h |
| 5 | Terra Max | 96.9 | 72/112 | 112 | $426.63 | 1,176,995,104 | 55.10h |
| 6 | Sol High | 90.1 | 67/112 | 112 | $513.11 | 564,589,961 | 33.57h |
| 7 | Gpt-5.5 High | 88.8 | 66/112 | 112 | $400.92 | 499,325,678 | 31.81h |
| 8 | Terra Xhigh | 84.7 | 63/112 | 112 | $211.61 | 588,315,219 | 36.34h |
| 9 | Sol Low | 82.1 | 61/112 | 112 | $190.97 | 234,885,957 | 18.56h |
| 10 | Terra High | 78 | 58/112 | 112 | $123.40 | 332,626,639 | 25.32h |
| 11 | Luna High | 75.3 | 56/112 | 112 | $22.47 | 699,897,163 | 32.07h |

## Interpretation

- The endpoint provides model-level `score`, pass counts, task counts, tokens, wall time, and estimated cost.
- It does not expose the ten task-level outcomes, so `Weighted /100` cannot be recomputed from this API summary alone.
- Task-weighted rankings remain based on the repository's task matrix and weight snapshots; this report monitors the latest API summary.
- When source data is unchanged, the automation still updates its heartbeat without presenting it as a new benchmark batch.
- The raw API response is not stored in the public repository; only required model-summary fields are archived.

Archived API snapshots: **360**.
