# Codex Radar API Monitor — English

[简体中文](api-latest.zh-CN.md) · [Project home](../README.md) · [API history CSV](../data/api/model_iq_history.csv) · [Monitor status](../data/api/monitor_status.json)

**Last successful check:** `2026-07-22T14:26:58+00:00`  
**Current API snapshot:** `402696d0a81a34a1`  
**Source observation:** `2026-07-22T06:57:20.626603+08:00`  
**New snapshot detected:** yes  
**Models returned:** 11

> “Last successful check” confirms that the automation reached the API. “Source observation” is supplied by the upstream endpoint and may be older.

> This is a model-level summary from the Codex Radar API, not the project's task-level difficulty-weighted score.

## Current API model summary

| Rank | Model tier | Source score | Passed | Tasks | Cost | Total tokens | Wall time |
|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | Terra Max | 102.2 | 76/112 | 112 | $509.38 | 1,301,366,193 | 61.91h |
| 2 | Gpt-5.5 Xhigh | 96.9 | 72/112 | 112 | $654.89 | 846,900,337 | 44.71h |
| 3 | Luna Max | 94.2 | 70/112 | 112 | $284.55 | 1,964,016,269 | 66.58h |
| 4 | Sol Xhigh | 94.2 | 70/112 | 112 | $749.21 | 993,371,248 | 49.06h |
| 5 | Sol High | 92.8 | 69/112 | 112 | $601.90 | 797,243,406 | 44.63h |
| 6 | Sol Medium | 91.5 | 68/112 | 112 | $417.32 | 529,508,969 | 32.34h |
| 7 | Terra Xhigh | 91.5 | 68/112 | 112 | $272.20 | 654,326,116 | 37.95h |
| 8 | Gpt-5.5 High | 82.1 | 61/112 | 112 | $402.31 | 501,322,451 | 30.41h |
| 9 | Sol Low | 80.1 | 59/111 | 111 | $238.60 | 278,013,400 | 23.58h |
| 10 | Luna High | 71.3 | 53/112 | 112 | $109.85 | 689,020,179 | 34.16h |
| 11 | Terra High | 65.9 | 49/112 | 112 | $146.64 | 329,707,606 | 25.21h |

## Interpretation

- The endpoint provides model-level `score`, pass counts, task counts, tokens, wall time, and estimated cost.
- It does not expose the ten task-level outcomes, so `Weighted /100` cannot be recomputed from this API summary alone.
- Task-weighted rankings remain based on the repository's task matrix and weight snapshots; this report monitors the latest API summary.
- When source data is unchanged, the automation still updates its heartbeat without presenting it as a new benchmark batch.
- The raw API response is not stored in the public repository; only required model-summary fields are archived.

Archived API snapshots: **51**.
