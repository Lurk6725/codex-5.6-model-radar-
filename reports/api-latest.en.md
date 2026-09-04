# Codex Radar API Monitor — English

[简体中文](api-latest.zh-CN.md) · [Project home](../README.md) · [API history CSV](../data/api/model_iq_history.csv) · [Monitor status](../data/api/monitor_status.json)

**Last successful check:** `2026-09-04T01:24:30+00:00`  
**Current API snapshot:** `ecef060851979c73`  
**Source observation:** `2026-09-02T20:11:35.648389+08:00`  
**New snapshot detected:** no; the source returned the same snapshot  
**Models returned:** 11

> “Last successful check” confirms that the automation reached the API. “Source observation” is supplied by the upstream endpoint and may be older.

> This is a model-level summary from the Codex Radar API, not the project's task-level difficulty-weighted score.

## Current API model summary

| Rank | Model tier | Source score | Passed | Tasks | Cost | Total tokens | Wall time |
|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | Luna Max | 109 | 81/112 | 112 | $54.11 | 2,156,725,582 | 76.31h |
| 2 | Terra Max | 106.3 | 79/112 | 112 | $420.43 | 1,244,001,980 | 58.89h |
| 3 | Gpt-5.5 Xhigh | 103.6 | 77/112 | 112 | $638.71 | 902,425,982 | 44.53h |
| 4 | Sol Medium | 99.5 | 74/112 | 112 | $312.52 | 419,024,511 | 28.16h |
| 5 | Sol Xhigh | 99.5 | 74/112 | 112 | $580.94 | 822,797,613 | 45.13h |
| 6 | Sol High | 98.2 | 73/112 | 112 | $471.34 | 584,640,550 | 37.03h |
| 7 | Gpt-5.5 High | 86.1 | 64/112 | 112 | $397.48 | 532,111,490 | 28.28h |
| 8 | Terra Xhigh | 86.1 | 64/112 | 112 | $210.83 | 588,326,818 | 36.34h |
| 9 | Terra High | 80.7 | 60/112 | 112 | $122.16 | 332,356,481 | 25.95h |
| 10 | Sol Low | 78 | 58/112 | 112 | $170.68 | 207,919,016 | 18.69h |
| 11 | Luna High | 68.6 | 51/112 | 112 | $22.49 | 809,612,612 | 34.52h |

## Interpretation

- The endpoint provides model-level `score`, pass counts, task counts, tokens, wall time, and estimated cost.
- It does not expose the ten task-level outcomes, so `Weighted /100` cannot be recomputed from this API summary alone.
- Task-weighted rankings remain based on the repository's task matrix and weight snapshots; this report monitors the latest API summary.
- When source data is unchanged, the automation still updates its heartbeat without presenting it as a new benchmark batch.
- The raw API response is not stored in the public repository; only required model-summary fields are archived.

Archived API snapshots: **400**.
