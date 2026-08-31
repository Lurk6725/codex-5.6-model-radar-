# Codex Radar API Monitor — English

[简体中文](api-latest.zh-CN.md) · [Project home](../README.md) · [API history CSV](../data/api/model_iq_history.csv) · [Monitor status](../data/api/monitor_status.json)

**Last successful check:** `2026-08-31T23:53:42+00:00`  
**Current API snapshot:** `8eeb176299bc50df`  
**Source observation:** `2026-09-01T00:10:37.982059+08:00`  
**New snapshot detected:** no; the source returned the same snapshot  
**Models returned:** 11

> “Last successful check” confirms that the automation reached the API. “Source observation” is supplied by the upstream endpoint and may be older.

> This is a model-level summary from the Codex Radar API, not the project's task-level difficulty-weighted score.

## Current API model summary

| Rank | Model tier | Source score | Passed | Tasks | Cost | Total tokens | Wall time |
|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | Luna Max | 106.3 | 79/112 | 112 | $54.12 | 2,054,861,949 | 72.49h |
| 2 | Terra Max | 104.9 | 78/112 | 112 | $421.34 | 1,222,890,032 | 57.07h |
| 3 | Gpt-5.5 Xhigh | 102.2 | 76/112 | 112 | $638.24 | 898,502,123 | 43.34h |
| 4 | Sol Xhigh | 102.2 | 76/112 | 112 | $581.61 | 828,867,822 | 42.41h |
| 5 | Sol Medium | 99.5 | 74/112 | 112 | $312.55 | 420,957,545 | 27.27h |
| 6 | Sol High | 98.2 | 73/112 | 112 | $473.03 | 571,906,817 | 36.59h |
| 7 | Gpt-5.5 High | 86.1 | 64/112 | 112 | $397.43 | 531,233,945 | 27.65h |
| 8 | Terra Xhigh | 84.7 | 63/112 | 112 | $211.69 | 581,089,499 | 35.82h |
| 9 | Sol Low | 79.4 | 59/112 | 112 | $170.65 | 208,069,294 | 17.17h |
| 10 | Terra High | 79.4 | 59/112 | 112 | $122.12 | 339,665,026 | 25.64h |
| 11 | Luna High | 67.3 | 50/112 | 112 | $22.48 | 814,585,965 | 33.77h |

## Interpretation

- The endpoint provides model-level `score`, pass counts, task counts, tokens, wall time, and estimated cost.
- It does not expose the ten task-level outcomes, so `Weighted /100` cannot be recomputed from this API summary alone.
- Task-weighted rankings remain based on the repository's task matrix and weight snapshots; this report monitors the latest API summary.
- When source data is unchanged, the automation still updates its heartbeat without presenting it as a new benchmark batch.
- The raw API response is not stored in the public repository; only required model-summary fields are archived.

Archived API snapshots: **387**.
