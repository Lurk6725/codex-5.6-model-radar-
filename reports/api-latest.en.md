# Codex Radar API Monitor — English

[简体中文](api-latest.zh-CN.md) · [Project home](../README.md) · [API history CSV](../data/api/model_iq_history.csv) · [Monitor status](../data/api/monitor_status.json)

**Last successful check:** `2026-08-19T22:03:48+00:00`  
**Current API snapshot:** `2380e83a7f1266f7`  
**Source observation:** `2026-07-22T06:57:20.626603+08:00`  
**New snapshot detected:** no; the source returned the same snapshot  
**Models returned:** 11

> “Last successful check” confirms that the automation reached the API. “Source observation” is supplied by the upstream endpoint and may be older.

> This is a model-level summary from the Codex Radar API, not the project's task-level difficulty-weighted score.

## Current API model summary

| Rank | Model tier | Source score | Passed | Tasks | Cost | Total tokens | Wall time |
|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | Gpt-5.5 Xhigh | 98.2 | 73/112 | 112 | $653.29 | 778,732,004 | 41.65h |
| 2 | Sol Xhigh | 96.9 | 72/112 | 112 | $727.03 | 837,685,190 | 44.35h |
| 3 | Terra Max | 95.5 | 71/112 | 112 | $433.77 | 1,205,527,076 | 57.84h |
| 4 | Luna Max | 92.8 | 69/112 | 112 | $55.00 | 1,732,695,020 | 61.47h |
| 5 | Gpt-5.5 High | 90.1 | 67/112 | 112 | $401.06 | 531,752,320 | 34.26h |
| 6 | Sol High | 86.1 | 64/112 | 112 | $535.72 | 634,044,032 | 35.52h |
| 7 | Terra Xhigh | 84.7 | 63/112 | 112 | $213.50 | 582,652,902 | 37.39h |
| 8 | Sol Medium | 82.1 | 61/112 | 112 | $397.71 | 449,819,600 | 33.05h |
| 9 | Terra High | 75.3 | 56/112 | 112 | $124.97 | 346,072,733 | 25.70h |
| 10 | Luna High | 72.6 | 54/112 | 112 | $23.47 | 751,117,386 | 34.25h |
| 11 | Sol Low | 71.3 | 53/112 | 112 | $223.77 | 263,158,507 | 24.35h |

## Interpretation

- The endpoint provides model-level `score`, pass counts, task counts, tokens, wall time, and estimated cost.
- It does not expose the ten task-level outcomes, so `Weighted /100` cannot be recomputed from this API summary alone.
- Task-weighted rankings remain based on the repository's task matrix and weight snapshots; this report monitors the latest API summary.
- When source data is unchanged, the automation still updates its heartbeat without presenting it as a new benchmark batch.
- The raw API response is not stored in the public repository; only required model-summary fields are archived.

Archived API snapshots: **300**.
