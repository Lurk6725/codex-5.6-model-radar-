# Codex Radar API Monitor — English

[简体中文](api-latest.zh-CN.md) · [Project home](../README.md) · [API history CSV](../data/api/model_iq_history.csv) · [Monitor status](../data/api/monitor_status.json)

**Last successful check:** `2026-07-18T21:08:03+00:00`  
**Current API snapshot:** `ee5f563886261602`  
**Source observation:** `2026-07-18T11:35:05.153982+08:00`  
**New snapshot detected:** yes  
**Models returned:** 9

> “Last successful check” confirms that the automation reached the API. “Source observation” is supplied by the upstream endpoint and may be older.

> This is a model-level summary from the Codex Radar API, not the project's task-level difficulty-weighted score.

## Current API model summary

| Rank | Model tier | Source score | Passed | Tasks | Cost | Total tokens | Wall time |
|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | Terra Max | 98.2 | 73/112 | 112 | $511.01 | 1,315,272,005 | 60.19h |
| 2 | Sol High | 95.5 | 71/112 | 112 | $621.65 | 802,023,032 | 44.65h |
| 3 | Sol Xhigh | 94.5 | 69/110 | 110 | $756.68 | 1,053,862,197 | 52.28h |
| 4 | Sol Medium | 90.1 | 67/112 | 112 | $393.63 | 495,918,975 | 34.17h |
| 5 | Gpt-5.5 High | 87.4 | 65/112 | 112 | $402.76 | 506,972,611 | 30.48h |
| 6 | Luna Max | 86.9 | 64/111 | 111 | $269.58 | 1,841,900,872 | 62.61h |
| 7 | Sol Low | 78.7 | 58/111 | 111 | $213.73 | 260,790,318 | 21.54h |
| 8 | Terra High | 67.3 | 50/112 | 112 | $144.94 | 322,432,936 | 23.12h |
| 9 | Luna High | 62.4 | 46/111 | 111 | $121.44 | 790,017,198 | 34.04h |

## Interpretation

- The endpoint provides model-level `score`, pass counts, task counts, tokens, wall time, and estimated cost.
- It does not expose the ten task-level outcomes, so `Weighted /100` cannot be recomputed from this API summary alone.
- Task-weighted rankings remain based on the repository's task matrix and weight snapshots; this report monitors the latest API summary.
- When source data is unchanged, the automation still updates its heartbeat without presenting it as a new benchmark batch.
- The raw API response is not stored in the public repository; only required model-summary fields are archived.

Archived API snapshots: **24**.
