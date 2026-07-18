# Codex Radar API Monitor — English

[简体中文](api-latest.zh-CN.md) · [Project home](../README.md) · [API history CSV](../data/api/model_iq_history.csv) · [Monitor status](../data/api/monitor_status.json)

**Last successful check:** `2026-07-18T11:25:27+00:00`  
**Current API snapshot:** `740b88b9298b2711`  
**Source observation:** `2026-07-18T11:35:05.153982+08:00`  
**New snapshot detected:** yes  
**Models returned:** 9

> “Last successful check” confirms that the automation reached the API. “Source observation” is supplied by the upstream endpoint and may be older.

> This is a model-level summary from the Codex Radar API, not the project's task-level difficulty-weighted score.

## Current API model summary

| Rank | Model tier | Source score | Passed | Tasks | Cost | Total tokens | Wall time |
|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | Terra Max | 99.5 | 74/112 | 112 | $512.82 | 1,326,362,879 | 57.80h |
| 2 | Sol High | 95.5 | 71/112 | 112 | $610.06 | 791,186,500 | 43.53h |
| 3 | Sol Xhigh | 92.6 | 67/109 | 109 | $709.41 | 941,812,278 | 48.85h |
| 4 | Sol Medium | 90.1 | 67/112 | 112 | $386.83 | 502,562,931 | 33.64h |
| 5 | Gpt-5.5 High | 86.1 | 64/112 | 112 | $395.78 | 496,350,562 | 30.43h |
| 6 | Luna Max | 84.2 | 62/111 | 111 | $262.58 | 1,771,742,314 | 61.84h |
| 7 | Sol Low | 77.4 | 57/111 | 111 | $216.71 | 264,537,555 | 21.63h |
| 8 | Terra High | 68.6 | 51/112 | 112 | $149.17 | 334,578,071 | 23.88h |
| 9 | Luna High | 63.8 | 47/111 | 111 | $120.58 | 788,342,464 | 33.09h |

## Interpretation

- The endpoint provides model-level `score`, pass counts, task counts, tokens, wall time, and estimated cost.
- It does not expose the ten task-level outcomes, so `Weighted /100` cannot be recomputed from this API summary alone.
- Task-weighted rankings remain based on the repository's task matrix and weight snapshots; this report monitors the latest API summary.
- When source data is unchanged, the automation still updates its heartbeat without presenting it as a new benchmark batch.
- The raw API response is not stored in the public repository; only required model-summary fields are archived.

Archived API snapshots: **19**.
