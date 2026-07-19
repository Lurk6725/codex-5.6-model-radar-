# Codex Radar API Monitor — English

[简体中文](api-latest.zh-CN.md) · [Project home](../README.md) · [API history CSV](../data/api/model_iq_history.csv) · [Monitor status](../data/api/monitor_status.json)

**Last successful check:** `2026-07-19T10:45:45+00:00`  
**Current API snapshot:** `148feb3313588063`  
**Source observation:** `2026-07-18T11:35:05.153982+08:00`  
**New snapshot detected:** no; the source returned the same snapshot  
**Models returned:** 9

> “Last successful check” confirms that the automation reached the API. “Source observation” is supplied by the upstream endpoint and may be older.

> This is a model-level summary from the Codex Radar API, not the project's task-level difficulty-weighted score.

## Current API model summary

| Rank | Model tier | Source score | Passed | Tasks | Cost | Total tokens | Wall time |
|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | Terra Max | 98.2 | 73/112 | 112 | $515.19 | 1,332,284,288 | 61.00h |
| 2 | Sol High | 96.9 | 72/112 | 112 | $608.54 | 777,424,936 | 44.35h |
| 3 | Sol Xhigh | 95 | 70/111 | 111 | $758.83 | 1,051,678,155 | 53.38h |
| 4 | Sol Medium | 88.8 | 66/112 | 112 | $390.64 | 497,783,619 | 34.24h |
| 5 | Luna Max | 87.4 | 65/112 | 112 | $276.48 | 1,888,705,386 | 67.98h |
| 6 | Gpt-5.5 High | 83.4 | 62/112 | 112 | $413.08 | 523,399,575 | 30.64h |
| 7 | Sol Low | 82.8 | 61/111 | 111 | $223.31 | 265,991,558 | 22.16h |
| 8 | Terra High | 65.9 | 49/112 | 112 | $146.53 | 327,087,510 | 23.50h |
| 9 | Luna High | 64.6 | 48/112 | 112 | $122.12 | 796,982,720 | 34.30h |

## Interpretation

- The endpoint provides model-level `score`, pass counts, task counts, tokens, wall time, and estimated cost.
- It does not expose the ten task-level outcomes, so `Weighted /100` cannot be recomputed from this API summary alone.
- Task-weighted rankings remain based on the repository's task matrix and weight snapshots; this report monitors the latest API summary.
- When source data is unchanged, the automation still updates its heartbeat without presenting it as a new benchmark batch.
- The raw API response is not stored in the public repository; only required model-summary fields are archived.

Archived API snapshots: **28**.
