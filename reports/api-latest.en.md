# Codex Radar API Monitor — English

[简体中文](api-latest.zh-CN.md) · [Project home](../README.md) · [API history CSV](../data/api/model_iq_history.csv) · [Monitor status](../data/api/monitor_status.json)

**Last successful check:** `2026-08-12T20:25:01+00:00`  
**Current API snapshot:** `009c79ef82c3f6a5`  
**Source observation:** `2026-07-22T06:57:20.626603+08:00`  
**New snapshot detected:** yes  
**Models returned:** 11

> “Last successful check” confirms that the automation reached the API. “Source observation” is supplied by the upstream endpoint and may be older.

> This is a model-level summary from the Codex Radar API, not the project's task-level difficulty-weighted score.

## Current API model summary

| Rank | Model tier | Source score | Passed | Tasks | Cost | Total tokens | Wall time |
|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | Terra Max | 102.2 | 76/112 | 112 | $436.33 | 1,303,196,350 | 59.70h |
| 2 | Luna Max | 100.9 | 75/112 | 112 | $58.48 | 1,898,783,946 | 68.76h |
| 3 | Sol Xhigh | 100.9 | 75/112 | 112 | $731.06 | 868,766,087 | 46.98h |
| 4 | Gpt-5.5 Xhigh | 98.2 | 73/112 | 112 | $657.18 | 721,276,469 | 40.80h |
| 5 | Sol High | 98.2 | 73/112 | 112 | $561.16 | 685,697,376 | 38.55h |
| 6 | Sol Medium | 92.8 | 69/112 | 112 | $407.21 | 467,745,217 | 32.17h |
| 7 | Gpt-5.5 High | 84.7 | 63/112 | 112 | $403.77 | 491,109,168 | 33.95h |
| 8 | Terra Xhigh | 84.7 | 63/112 | 112 | $218.14 | 578,763,073 | 35.78h |
| 9 | Terra High | 75.3 | 56/112 | 112 | $126.88 | 337,610,432 | 25.06h |
| 10 | Luna High | 74 | 55/112 | 112 | $26.18 | 786,527,187 | 35.60h |
| 11 | Sol Low | 74 | 55/112 | 112 | $228.57 | 262,214,716 | 22.69h |

## Interpretation

- The endpoint provides model-level `score`, pass counts, task counts, tokens, wall time, and estimated cost.
- It does not expose the ten task-level outcomes, so `Weighted /100` cannot be recomputed from this API summary alone.
- Task-weighted rankings remain based on the repository's task matrix and weight snapshots; this report monitors the latest API summary.
- When source data is unchanged, the automation still updates its heartbeat without presenting it as a new benchmark batch.
- The raw API response is not stored in the public repository; only required model-summary fields are archived.

Archived API snapshots: **246**.
