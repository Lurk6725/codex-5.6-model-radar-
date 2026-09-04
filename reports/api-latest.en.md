# Codex Radar API Monitor — English

[简体中文](api-latest.zh-CN.md) · [Project home](../README.md) · [API history CSV](../data/api/model_iq_history.csv) · [Monitor status](../data/api/monitor_status.json)

**Last successful check:** `2026-09-04T06:33:01+00:00`  
**Current API snapshot:** `b136ef496a4cd931`  
**Source observation:** `2026-09-02T20:11:35.648389+08:00`  
**New snapshot detected:** yes  
**Models returned:** 11

> “Last successful check” confirms that the automation reached the API. “Source observation” is supplied by the upstream endpoint and may be older.

> This is a model-level summary from the Codex Radar API, not the project's task-level difficulty-weighted score.

## Current API model summary

| Rank | Model tier | Source score | Passed | Tasks | Cost | Total tokens | Wall time |
|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | Luna Max | 109 | 81/112 | 112 | $54.22 | 2,165,365,346 | 76.27h |
| 2 | Terra Max | 106.3 | 79/112 | 112 | $420.43 | 1,244,001,980 | 58.89h |
| 3 | Gpt-5.5 Xhigh | 103.6 | 77/112 | 112 | $638.71 | 901,829,830 | 44.54h |
| 4 | Sol Xhigh | 99.5 | 74/112 | 112 | $580.94 | 823,180,926 | 44.87h |
| 5 | Sol High | 98.2 | 73/112 | 112 | $471.35 | 585,880,021 | 37.02h |
| 6 | Sol Medium | 96.9 | 72/112 | 112 | $312.42 | 415,822,645 | 27.28h |
| 7 | Gpt-5.5 High | 86.1 | 64/112 | 112 | $397.48 | 532,111,490 | 28.28h |
| 8 | Terra Xhigh | 86.1 | 64/112 | 112 | $210.67 | 588,164,809 | 36.44h |
| 9 | Terra High | 80.7 | 60/112 | 112 | $122.11 | 331,842,855 | 25.97h |
| 10 | Sol Low | 79.4 | 59/112 | 112 | $170.73 | 209,791,528 | 18.71h |
| 11 | Luna High | 68.6 | 51/112 | 112 | $22.49 | 809,612,612 | 34.52h |

## Interpretation

- The endpoint provides model-level `score`, pass counts, task counts, tokens, wall time, and estimated cost.
- It does not expose the ten task-level outcomes, so `Weighted /100` cannot be recomputed from this API summary alone.
- Task-weighted rankings remain based on the repository's task matrix and weight snapshots; this report monitors the latest API summary.
- When source data is unchanged, the automation still updates its heartbeat without presenting it as a new benchmark batch.
- The raw API response is not stored in the public repository; only required model-summary fields are archived.

Archived API snapshots: **401**.
