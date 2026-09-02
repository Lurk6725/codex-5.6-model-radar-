# Codex Radar API Monitor — English

[简体中文](api-latest.zh-CN.md) · [Project home](../README.md) · [API history CSV](../data/api/model_iq_history.csv) · [Monitor status](../data/api/monitor_status.json)

**Last successful check:** `2026-09-02T06:27:03+00:00`  
**Current API snapshot:** `5abdf036e22db611`  
**Source observation:** `2026-09-02T02:17:42.377759+08:00`  
**New snapshot detected:** yes  
**Models returned:** 11

> “Last successful check” confirms that the automation reached the API. “Source observation” is supplied by the upstream endpoint and may be older.

> This is a model-level summary from the Codex Radar API, not the project's task-level difficulty-weighted score.

## Current API model summary

| Rank | Model tier | Source score | Passed | Tasks | Cost | Total tokens | Wall time |
|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | Luna Max | 106.3 | 79/112 | 112 | $54.08 | 2,107,445,306 | 74.30h |
| 2 | Terra Max | 106.3 | 79/112 | 112 | $420.43 | 1,245,688,429 | 59.02h |
| 3 | Gpt-5.5 Xhigh | 103.6 | 77/112 | 112 | $638.70 | 903,745,336 | 44.52h |
| 4 | Sol Xhigh | 102.2 | 76/112 | 112 | $581.20 | 837,129,584 | 42.94h |
| 5 | Sol Medium | 99.5 | 74/112 | 112 | $312.52 | 419,024,511 | 28.16h |
| 6 | Sol High | 98.2 | 73/112 | 112 | $471.31 | 584,514,075 | 36.82h |
| 7 | Gpt-5.5 High | 86.1 | 64/112 | 112 | $397.48 | 532,194,104 | 28.23h |
| 8 | Terra Xhigh | 86.1 | 64/112 | 112 | $210.82 | 585,969,885 | 36.16h |
| 9 | Terra High | 79.4 | 59/112 | 112 | $122.18 | 332,446,400 | 26.21h |
| 10 | Sol Low | 78 | 58/112 | 112 | $170.59 | 209,457,087 | 18.41h |
| 11 | Luna High | 68.6 | 51/112 | 112 | $22.49 | 809,612,612 | 34.52h |

## Interpretation

- The endpoint provides model-level `score`, pass counts, task counts, tokens, wall time, and estimated cost.
- It does not expose the ten task-level outcomes, so `Weighted /100` cannot be recomputed from this API summary alone.
- Task-weighted rankings remain based on the repository's task matrix and weight snapshots; this report monitors the latest API summary.
- When source data is unchanged, the automation still updates its heartbeat without presenting it as a new benchmark batch.
- The raw API response is not stored in the public repository; only required model-summary fields are archived.

Archived API snapshots: **395**.
