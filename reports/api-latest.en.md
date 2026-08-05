# Codex Radar API Monitor — English

[简体中文](api-latest.zh-CN.md) · [Project home](../README.md) · [API history CSV](../data/api/model_iq_history.csv) · [Monitor status](../data/api/monitor_status.json)

**Last successful check:** `2026-08-05T20:40:28+00:00`  
**Current API snapshot:** `3d8f58aca3d875ff`  
**Source observation:** `2026-07-22T06:57:20.626603+08:00`  
**New snapshot detected:** yes  
**Models returned:** 11

> “Last successful check” confirms that the automation reached the API. “Source observation” is supplied by the upstream endpoint and may be older.

> This is a model-level summary from the Codex Radar API, not the project's task-level difficulty-weighted score.

## Current API model summary

| Rank | Model tier | Source score | Passed | Tasks | Cost | Total tokens | Wall time |
|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | Sol Xhigh | 111.7 | 83/112 | 112 | $762.59 | 951,373,798 | 48.04h |
| 2 | Gpt-5.5 Xhigh | 96.9 | 72/112 | 112 | $652.52 | 800,732,331 | 42.20h |
| 3 | Luna Max | 94.2 | 70/112 | 112 | $58.81 | 1,709,404,187 | 59.91h |
| 4 | Sol Medium | 92.8 | 69/112 | 112 | $409.77 | 520,906,145 | 31.80h |
| 5 | Gpt-5.5 High | 91.5 | 68/112 | 112 | $406.94 | 497,560,344 | 31.61h |
| 6 | Terra Max | 90.1 | 67/112 | 112 | $456.59 | 1,439,653,530 | 59.31h |
| 7 | Sol High | 86.1 | 64/112 | 112 | $587.87 | 698,619,457 | 40.09h |
| 8 | Terra Xhigh | 82.1 | 61/112 | 112 | $227.98 | 602,066,362 | 34.22h |
| 9 | Terra High | 79.4 | 59/112 | 112 | $135.05 | 348,319,852 | 24.76h |
| 10 | Luna High | 75.3 | 56/112 | 112 | $27.59 | 727,247,221 | 29.73h |
| 11 | Sol Low | 71.3 | 53/112 | 112 | $231.28 | 253,149,274 | 21.79h |

## Interpretation

- The endpoint provides model-level `score`, pass counts, task counts, tokens, wall time, and estimated cost.
- It does not expose the ten task-level outcomes, so `Weighted /100` cannot be recomputed from this API summary alone.
- Task-weighted rankings remain based on the repository's task matrix and weight snapshots; this report monitors the latest API summary.
- When source data is unchanged, the automation still updates its heartbeat without presenting it as a new benchmark batch.
- The raw API response is not stored in the public repository; only required model-summary fields are archived.

Archived API snapshots: **179**.
