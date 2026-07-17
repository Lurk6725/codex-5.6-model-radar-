# Codex Radar API Monitor — English

[简体中文](api-latest.zh-CN.md) · [Project home](../README.md) · [API history CSV](../data/api/model_iq_history.csv) · [Monitor status](../data/api/monitor_status.json)

**Last successful check:** `2026-07-17T16:53:54+00:00`  
**Current API snapshot:** `98a6194ef0a933d1`  
**Source observation:** `2026-07-13T22:08:07.261261+08:00`  
**New snapshot detected:** yes  
**Models returned:** 9

> “Last successful check” confirms that the automation reached the API. “Source observation” is supplied by the upstream endpoint and may be older.

> This is a model-level summary from the Codex Radar API, not the project's task-level difficulty-weighted score.

## Current API model summary

| Rank | Model tier | Source score | Passed | Tasks | Cost | Total tokens | Wall time |
|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | Terra Max | 96.3 | 69/108 | 108 | $501.20 | 1,300,313,139 | 53.65h |
| 2 | Sol Xhigh | 95.8 | 68/107 | 107 | $732.35 | 1,009,370,275 | 48.55h |
| 3 | Sol High | 94.5 | 69/110 | 110 | $590.12 | 753,480,648 | 42.46h |
| 4 | Sol Medium | 87.4 | 65/112 | 112 | $395.37 | 503,939,214 | 33.18h |
| 5 | Luna Max | 86.7 | 61/106 | 106 | $246.18 | 1,645,380,638 | 57.67h |
| 6 | Sol Low | 80.2 | 58/109 | 109 | $211.60 | 257,943,875 | 20.92h |
| 7 | Gpt-5.5 High | 78.7 | 58/111 | 111 | $391.70 | 494,270,142 | 36.57h |
| 8 | Terra High | 73.9 | 52/106 | 106 | $141.91 | 314,831,299 | 22.84h |
| 9 | Luna High | 63.6 | 46/109 | 109 | $123.61 | 804,184,621 | 32.73h |

## Interpretation

- The endpoint provides model-level `score`, pass counts, task counts, tokens, wall time, and estimated cost.
- It does not expose the ten task-level outcomes, so `Weighted /100` cannot be recomputed from this API summary alone.
- Task-weighted rankings remain based on the repository's task matrix and weight snapshots; this report monitors the latest API summary.
- When source data is unchanged, the automation still updates its heartbeat without presenting it as a new benchmark batch.
- The raw API response is not stored in the public repository; only required model-summary fields are archived.

Archived API snapshots: **14**.
