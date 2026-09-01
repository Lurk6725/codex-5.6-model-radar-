# Codex Radar API Monitor — English

[简体中文](api-latest.zh-CN.md) · [Project home](../README.md) · [API history CSV](../data/api/model_iq_history.csv) · [Monitor status](../data/api/monitor_status.json)

**Last successful check:** `2026-09-01T10:14:01+00:00`  
**Current API snapshot:** `095804ea967c2ef5`  
**Source observation:** `2026-09-01T00:10:37.982059+08:00`  
**New snapshot detected:** yes  
**Models returned:** 11

> “Last successful check” confirms that the automation reached the API. “Source observation” is supplied by the upstream endpoint and may be older.

> This is a model-level summary from the Codex Radar API, not the project's task-level difficulty-weighted score.

## Current API model summary

| Rank | Model tier | Source score | Passed | Tasks | Cost | Total tokens | Wall time |
|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | Luna Max | 106.3 | 79/112 | 112 | $54.11 | 2,059,922,207 | 72.56h |
| 2 | Terra Max | 104.9 | 78/112 | 112 | $420.25 | 1,224,521,314 | 57.63h |
| 3 | Gpt-5.5 Xhigh | 103.6 | 77/112 | 112 | $638.67 | 900,400,993 | 44.19h |
| 4 | Sol Xhigh | 102.2 | 76/112 | 112 | $581.20 | 837,129,584 | 42.94h |
| 5 | Sol Medium | 99.5 | 74/112 | 112 | $312.55 | 419,606,372 | 28.03h |
| 6 | Sol High | 98.2 | 73/112 | 112 | $471.34 | 582,196,217 | 36.73h |
| 7 | Gpt-5.5 High | 86.1 | 64/112 | 112 | $397.43 | 531,233,945 | 27.65h |
| 8 | Terra Xhigh | 83.4 | 62/112 | 112 | $211.80 | 582,542,685 | 36.10h |
| 9 | Terra High | 79.4 | 59/112 | 112 | $122.12 | 339,665,026 | 25.64h |
| 10 | Sol Low | 78 | 58/112 | 112 | $170.65 | 207,380,814 | 17.98h |
| 11 | Luna High | 67.3 | 50/112 | 112 | $22.48 | 815,421,847 | 33.93h |

## Interpretation

- The endpoint provides model-level `score`, pass counts, task counts, tokens, wall time, and estimated cost.
- It does not expose the ten task-level outcomes, so `Weighted /100` cannot be recomputed from this API summary alone.
- Task-weighted rankings remain based on the repository's task matrix and weight snapshots; this report monitors the latest API summary.
- When source data is unchanged, the automation still updates its heartbeat without presenting it as a new benchmark batch.
- The raw API response is not stored in the public repository; only required model-summary fields are archived.

Archived API snapshots: **389**.
