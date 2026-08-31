# Codex Radar API Monitor — English

[简体中文](api-latest.zh-CN.md) · [Project home](../README.md) · [API history CSV](../data/api/model_iq_history.csv) · [Monitor status](../data/api/monitor_status.json)

**Last successful check:** `2026-08-31T06:16:05+00:00`  
**Current API snapshot:** `149ba4de7bbb1cc5`  
**Source observation:** `2026-08-31T12:10:31+08:00`  
**New snapshot detected:** yes  
**Models returned:** 11

> “Last successful check” confirms that the automation reached the API. “Source observation” is supplied by the upstream endpoint and may be older.

> This is a model-level summary from the Codex Radar API, not the project's task-level difficulty-weighted score.

## Current API model summary

| Rank | Model tier | Source score | Passed | Tasks | Cost | Total tokens | Wall time |
|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | Luna Max | 106.3 | 79/112 | 112 | $54.09 | 2,050,195,044 | 72.56h |
| 2 | Terra Max | 104.9 | 78/112 | 112 | $421.34 | 1,222,890,032 | 57.07h |
| 3 | Gpt-5.5 Xhigh | 102.2 | 76/112 | 112 | $638.48 | 891,467,450 | 42.87h |
| 4 | Sol Xhigh | 102.2 | 76/112 | 112 | $581.61 | 828,867,822 | 42.41h |
| 5 | Sol High | 100.9 | 75/112 | 112 | $478.75 | 579,314,598 | 35.15h |
| 6 | Sol Medium | 98.2 | 73/112 | 112 | $312.53 | 421,286,436 | 26.94h |
| 7 | Gpt-5.5 High | 87.4 | 65/112 | 112 | $397.54 | 526,345,981 | 27.91h |
| 8 | Terra Xhigh | 84.7 | 63/112 | 112 | $211.75 | 578,761,638 | 35.19h |
| 9 | Sol Low | 82.1 | 61/112 | 112 | $171.21 | 206,479,686 | 16.49h |
| 10 | Terra High | 78 | 58/112 | 112 | $122.35 | 342,128,093 | 25.07h |
| 11 | Luna High | 67.3 | 50/112 | 112 | $22.48 | 814,878,559 | 33.70h |

## Interpretation

- The endpoint provides model-level `score`, pass counts, task counts, tokens, wall time, and estimated cost.
- It does not expose the ten task-level outcomes, so `Weighted /100` cannot be recomputed from this API summary alone.
- Task-weighted rankings remain based on the repository's task matrix and weight snapshots; this report monitors the latest API summary.
- When source data is unchanged, the automation still updates its heartbeat without presenting it as a new benchmark batch.
- The raw API response is not stored in the public repository; only required model-summary fields are archived.

Archived API snapshots: **385**.
