# Codex Radar API Monitor — English

[简体中文](api-latest.zh-CN.md) · [Project home](../README.md) · [API history CSV](../data/api/model_iq_history.csv) · [Monitor status](../data/api/monitor_status.json)

**Last successful check:** `2026-07-18T18:39:16+00:00`  
**Current API snapshot:** `8c55b75ee314c429`  
**Source observation:** `2026-07-18T11:35:05.153982+08:00`  
**New snapshot detected:** no; the source returned the same snapshot  
**Models returned:** 9

> “Last successful check” confirms that the automation reached the API. “Source observation” is supplied by the upstream endpoint and may be older.

> This is a model-level summary from the Codex Radar API, not the project's task-level difficulty-weighted score.

## Current API model summary

| Rank | Model tier | Source score | Passed | Tasks | Cost | Total tokens | Wall time |
|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | Terra Max | 99.5 | 74/112 | 112 | $512.48 | 1,326,057,730 | 59.54h |
| 2 | Sol High | 94.2 | 70/112 | 112 | $624.33 | 813,149,420 | 44.74h |
| 3 | Sol Xhigh | 93.1 | 68/110 | 110 | $717.44 | 957,047,784 | 49.72h |
| 4 | Sol Medium | 90.1 | 67/112 | 112 | $391.81 | 492,993,337 | 34.08h |
| 5 | Gpt-5.5 High | 88.8 | 66/112 | 112 | $399.14 | 500,912,388 | 30.16h |
| 6 | Luna Max | 84.2 | 62/111 | 111 | $262.30 | 1,778,687,174 | 61.86h |
| 7 | Sol Low | 74.7 | 55/111 | 111 | $214.42 | 261,755,281 | 21.50h |
| 8 | Terra High | 67.3 | 50/112 | 112 | $147.36 | 328,777,764 | 23.28h |
| 9 | Luna High | 62.4 | 46/111 | 111 | $120.58 | 787,569,487 | 33.55h |

## Interpretation

- The endpoint provides model-level `score`, pass counts, task counts, tokens, wall time, and estimated cost.
- It does not expose the ten task-level outcomes, so `Weighted /100` cannot be recomputed from this API summary alone.
- Task-weighted rankings remain based on the repository's task matrix and weight snapshots; this report monitors the latest API summary.
- When source data is unchanged, the automation still updates its heartbeat without presenting it as a new benchmark batch.
- The raw API response is not stored in the public repository; only required model-summary fields are archived.

Archived API snapshots: **22**.
