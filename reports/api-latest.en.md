# Codex Radar API Monitor — English

[简体中文](api-latest.zh-CN.md) · [Project home](../README.md) · [API history CSV](../data/api/model_iq_history.csv) · [Monitor status](../data/api/monitor_status.json)

**Last successful check:** `2026-08-09T02:31:27+00:00`  
**Current API snapshot:** `5e6b0a79a36f43e6`  
**Source observation:** `2026-07-22T06:57:20.626603+08:00`  
**New snapshot detected:** yes  
**Models returned:** 11

> “Last successful check” confirms that the automation reached the API. “Source observation” is supplied by the upstream endpoint and may be older.

> This is a model-level summary from the Codex Radar API, not the project's task-level difficulty-weighted score.

## Current API model summary

| Rank | Model tier | Source score | Passed | Tasks | Cost | Total tokens | Wall time |
|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | Sol Xhigh | 106.3 | 79/112 | 112 | $751.03 | 914,108,838 | 47.41h |
| 2 | Sol High | 98.2 | 73/112 | 112 | $570.74 | 606,515,998 | 35.26h |
| 3 | Luna Max | 92.8 | 69/112 | 112 | $58.76 | 1,782,984,841 | 61.94h |
| 4 | Terra Max | 92.8 | 69/112 | 112 | $449.14 | 1,363,179,071 | 56.89h |
| 5 | Gpt-5.5 Xhigh | 91.5 | 68/112 | 112 | $657.08 | 780,090,813 | 40.85h |
| 6 | Sol Medium | 90.1 | 67/112 | 112 | $410.97 | 526,276,180 | 31.12h |
| 7 | Gpt-5.5 High | 88.8 | 66/112 | 112 | $408.00 | 488,991,949 | 31.84h |
| 8 | Sol Low | 82.1 | 61/112 | 112 | $228.47 | 264,575,655 | 21.84h |
| 9 | Terra Xhigh | 80.7 | 60/112 | 112 | $225.86 | 613,844,536 | 35.30h |
| 10 | Luna High | 76.7 | 57/112 | 112 | $26.06 | 723,478,923 | 31.80h |
| 11 | Terra High | 74 | 55/112 | 112 | $127.99 | 336,709,403 | 22.58h |

## Interpretation

- The endpoint provides model-level `score`, pass counts, task counts, tokens, wall time, and estimated cost.
- It does not expose the ten task-level outcomes, so `Weighted /100` cannot be recomputed from this API summary alone.
- Task-weighted rankings remain based on the repository's task matrix and weight snapshots; this report monitors the latest API summary.
- When source data is unchanged, the automation still updates its heartbeat without presenting it as a new benchmark batch.
- The raw API response is not stored in the public repository; only required model-summary fields are archived.

Archived API snapshots: **210**.
