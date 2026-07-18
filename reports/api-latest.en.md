# Codex Radar API Monitor — English

[简体中文](api-latest.zh-CN.md) · [Project home](../README.md) · [API history CSV](../data/api/model_iq_history.csv) · [Monitor status](../data/api/monitor_status.json)

**Last successful check:** `2026-07-18T00:12:15+00:00`  
**Current API snapshot:** `5121246ca8014f24`  
**Source observation:** `2026-07-13T22:08:07.261261+08:00`  
**New snapshot detected:** yes  
**Models returned:** 9

> “Last successful check” confirms that the automation reached the API. “Source observation” is supplied by the upstream endpoint and may be older.

> This is a model-level summary from the Codex Radar API, not the project's task-level difficulty-weighted score.

## Current API model summary

| Rank | Model tier | Source score | Passed | Tasks | Cost | Total tokens | Wall time |
|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | Terra Max | 98.6 | 72/110 | 110 | $499.21 | 1,289,069,769 | 55.37h |
| 2 | Sol High | 96.4 | 71/111 | 111 | $591.93 | 750,018,592 | 42.47h |
| 3 | Sol Xhigh | 94 | 68/109 | 109 | $748.94 | 1,020,032,500 | 49.61h |
| 4 | Sol Medium | 90.1 | 67/112 | 112 | $398.48 | 511,503,583 | 33.48h |
| 5 | Luna Max | 83.7 | 60/108 | 108 | $255.16 | 1,722,250,172 | 60.16h |
| 6 | Gpt-5.5 High | 81.4 | 60/111 | 111 | $393.52 | 497,740,107 | 33.40h |
| 7 | Sol Low | 81.4 | 60/111 | 111 | $219.93 | 268,500,664 | 21.83h |
| 8 | Terra High | 71.9 | 53/111 | 111 | $148.40 | 331,871,134 | 23.90h |
| 9 | Luna High | 60.3 | 44/110 | 110 | $121.92 | 792,217,570 | 32.63h |

## Interpretation

- The endpoint provides model-level `score`, pass counts, task counts, tokens, wall time, and estimated cost.
- It does not expose the ten task-level outcomes, so `Weighted /100` cannot be recomputed from this API summary alone.
- Task-weighted rankings remain based on the repository's task matrix and weight snapshots; this report monitors the latest API summary.
- When source data is unchanged, the automation still updates its heartbeat without presenting it as a new benchmark batch.
- The raw API response is not stored in the public repository; only required model-summary fields are archived.

Archived API snapshots: **17**.
