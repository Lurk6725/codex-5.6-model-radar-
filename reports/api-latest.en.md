# Codex Radar API Monitor — English

[简体中文](api-latest.zh-CN.md) · [Project home](../README.md) · [API history CSV](../data/api/model_iq_history.csv) · [Monitor status](../data/api/monitor_status.json)

**Last successful check:** `2026-08-22T09:45:18+00:00`  
**Current API snapshot:** `a16fa534c691f49b`  
**Source observation:** `2026-07-22T06:57:20.626603+08:00`  
**New snapshot detected:** yes  
**Models returned:** 11

> “Last successful check” confirms that the automation reached the API. “Source observation” is supplied by the upstream endpoint and may be older.

> This is a model-level summary from the Codex Radar API, not the project's task-level difficulty-weighted score.

## Current API model summary

| Rank | Model tier | Source score | Passed | Tasks | Cost | Total tokens | Wall time |
|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | Sol Xhigh | 102.2 | 76/112 | 112 | $723.03 | 852,115,690 | 43.65h |
| 2 | Gpt-5.5 Xhigh | 98.2 | 73/112 | 112 | $652.21 | 777,214,772 | 42.16h |
| 3 | Terra Max | 95.5 | 71/112 | 112 | $432.57 | 1,193,173,342 | 56.78h |
| 4 | Gpt-5.5 High | 94.2 | 70/112 | 112 | $401.09 | 531,860,027 | 34.53h |
| 5 | Luna Max | 86.1 | 64/112 | 112 | $54.41 | 1,671,342,969 | 59.67h |
| 6 | Sol High | 86.1 | 64/112 | 112 | $535.03 | 633,086,093 | 35.95h |
| 7 | Terra Xhigh | 84.7 | 63/112 | 112 | $213.82 | 577,802,223 | 37.00h |
| 8 | Sol Medium | 82.1 | 61/112 | 112 | $404.57 | 464,681,467 | 34.28h |
| 9 | Luna High | 76.7 | 57/112 | 112 | $22.62 | 683,225,386 | 29.76h |
| 10 | Terra High | 74 | 55/112 | 112 | $125.16 | 335,405,095 | 24.83h |
| 11 | Sol Low | 72.6 | 54/112 | 112 | $223.62 | 261,917,630 | 24.15h |

## Interpretation

- The endpoint provides model-level `score`, pass counts, task counts, tokens, wall time, and estimated cost.
- It does not expose the ten task-level outcomes, so `Weighted /100` cannot be recomputed from this API summary alone.
- Task-weighted rankings remain based on the repository's task matrix and weight snapshots; this report monitors the latest API summary.
- When source data is unchanged, the automation still updates its heartbeat without presenting it as a new benchmark batch.
- The raw API response is not stored in the public repository; only required model-summary fields are archived.

Archived API snapshots: **323**.
