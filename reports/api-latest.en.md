# Codex Radar API Monitor — English

[简体中文](api-latest.zh-CN.md) · [Project home](../README.md) · [API history CSV](../data/api/model_iq_history.csv) · [Monitor status](../data/api/monitor_status.json)

**Last successful check:** `2026-09-01T14:57:48+00:00`  
**Current API snapshot:** `1a3307f369d6c429`  
**Source observation:** `2026-09-01T00:10:37.982059+08:00`  
**New snapshot detected:** yes  
**Models returned:** 11

> “Last successful check” confirms that the automation reached the API. “Source observation” is supplied by the upstream endpoint and may be older.

> This is a model-level summary from the Codex Radar API, not the project's task-level difficulty-weighted score.

## Current API model summary

| Rank | Model tier | Source score | Passed | Tasks | Cost | Total tokens | Wall time |
|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | Luna Max | 106.3 | 79/112 | 112 | $54.10 | 2,074,148,621 | 73.23h |
| 2 | Terra Max | 106.3 | 79/112 | 112 | $420.16 | 1,223,662,682 | 58.24h |
| 3 | Gpt-5.5 Xhigh | 103.6 | 77/112 | 112 | $638.67 | 900,400,993 | 44.19h |
| 4 | Sol Xhigh | 102.2 | 76/112 | 112 | $581.20 | 837,129,584 | 42.94h |
| 5 | Sol Medium | 99.5 | 74/112 | 112 | $312.54 | 420,349,076 | 28.15h |
| 6 | Sol High | 98.2 | 73/112 | 112 | $471.34 | 582,196,217 | 36.73h |
| 7 | Gpt-5.5 High | 84.7 | 63/112 | 112 | $397.48 | 531,328,845 | 27.97h |
| 8 | Terra Xhigh | 83.4 | 62/112 | 112 | $211.81 | 581,658,492 | 36.04h |
| 9 | Sol Low | 78 | 58/112 | 112 | $170.65 | 207,380,814 | 17.98h |
| 10 | Terra High | 78 | 58/112 | 112 | $122.16 | 336,386,011 | 26.22h |
| 11 | Luna High | 68.6 | 51/112 | 112 | $22.48 | 818,903,608 | 34.41h |

## Interpretation

- The endpoint provides model-level `score`, pass counts, task counts, tokens, wall time, and estimated cost.
- It does not expose the ten task-level outcomes, so `Weighted /100` cannot be recomputed from this API summary alone.
- Task-weighted rankings remain based on the repository's task matrix and weight snapshots; this report monitors the latest API summary.
- When source data is unchanged, the automation still updates its heartbeat without presenting it as a new benchmark batch.
- The raw API response is not stored in the public repository; only required model-summary fields are archived.

Archived API snapshots: **390**.
