# Codex Radar API Monitor — English

[简体中文](api-latest.zh-CN.md) · [Project home](../README.md) · [API history CSV](../data/api/model_iq_history.csv) · [Monitor status](../data/api/monitor_status.json)

**Last successful check:** `2026-08-09T15:51:42+00:00`  
**Current API snapshot:** `fd40f20f00ab4033`  
**Source observation:** `2026-07-22T06:57:20.626603+08:00`  
**New snapshot detected:** yes  
**Models returned:** 11

> “Last successful check” confirms that the automation reached the API. “Source observation” is supplied by the upstream endpoint and may be older.

> This is a model-level summary from the Codex Radar API, not the project's task-level difficulty-weighted score.

## Current API model summary

| Rank | Model tier | Source score | Passed | Tasks | Cost | Total tokens | Wall time |
|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | Sol Xhigh | 110.3 | 82/112 | 112 | $745.88 | 923,224,633 | 50.81h |
| 2 | Sol High | 100.9 | 75/112 | 112 | $570.90 | 585,404,791 | 35.79h |
| 3 | Gpt-5.5 Xhigh | 95.5 | 71/112 | 112 | $657.98 | 811,774,721 | 42.12h |
| 4 | Sol Medium | 94.2 | 70/112 | 112 | $412.19 | 522,413,376 | 32.33h |
| 5 | Terra Max | 94.2 | 70/112 | 112 | $438.59 | 1,176,166,561 | 51.47h |
| 6 | Luna Max | 91.5 | 68/112 | 112 | $58.73 | 1,760,445,787 | 61.12h |
| 7 | Sol Low | 86.1 | 64/112 | 112 | $230.93 | 274,544,489 | 21.60h |
| 8 | Terra Xhigh | 84.7 | 63/112 | 112 | $220.37 | 594,382,392 | 32.85h |
| 9 | Gpt-5.5 High | 83.4 | 62/112 | 112 | $405.96 | 469,650,791 | 27.98h |
| 10 | Terra High | 79.4 | 59/112 | 112 | $126.98 | 335,327,704 | 22.30h |
| 11 | Luna High | 72.6 | 54/112 | 112 | $26.22 | 716,238,126 | 31.48h |

## Interpretation

- The endpoint provides model-level `score`, pass counts, task counts, tokens, wall time, and estimated cost.
- It does not expose the ten task-level outcomes, so `Weighted /100` cannot be recomputed from this API summary alone.
- Task-weighted rankings remain based on the repository's task matrix and weight snapshots; this report monitors the latest API summary.
- When source data is unchanged, the automation still updates its heartbeat without presenting it as a new benchmark batch.
- The raw API response is not stored in the public repository; only required model-summary fields are archived.

Archived API snapshots: **217**.
