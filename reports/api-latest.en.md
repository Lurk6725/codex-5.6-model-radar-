# Codex Radar API Monitor — English

[简体中文](api-latest.zh-CN.md) · [Project home](../README.md) · [API history CSV](../data/api/model_iq_history.csv) · [Monitor status](../data/api/monitor_status.json)

**Last successful check:** `2026-07-23T23:42:46+00:00`  
**Current API snapshot:** `73d01caf09b052f4`  
**Source observation:** `2026-07-22T06:57:20.626603+08:00`  
**New snapshot detected:** no; the source returned the same snapshot  
**Models returned:** 11

> “Last successful check” confirms that the automation reached the API. “Source observation” is supplied by the upstream endpoint and may be older.

> This is a model-level summary from the Codex Radar API, not the project's task-level difficulty-weighted score.

## Current API model summary

| Rank | Model tier | Source score | Passed | Tasks | Cost | Total tokens | Wall time |
|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | Sol Xhigh | 100.9 | 75/112 | 112 | $795.90 | 1,091,137,850 | 47.84h |
| 2 | Sol Medium | 96.9 | 72/112 | 112 | $423.95 | 536,261,646 | 30.39h |
| 3 | Sol High | 95.5 | 71/112 | 112 | $628.33 | 848,349,780 | 39.95h |
| 4 | Terra Max | 94.2 | 70/112 | 112 | $529.47 | 1,388,151,579 | 56.69h |
| 5 | Terra Xhigh | 90.1 | 67/112 | 112 | $270.13 | 650,377,458 | 35.40h |
| 6 | Gpt-5.5 High | 87.4 | 65/112 | 112 | $430.75 | 541,593,544 | 34.53h |
| 7 | Gpt-5.5 Xhigh | 87.4 | 65/112 | 112 | $654.79 | 845,384,749 | 46.24h |
| 8 | Luna Max | 83.4 | 62/112 | 112 | $280.43 | 1,917,312,444 | 61.24h |
| 9 | Sol Low | 79.4 | 59/112 | 112 | $231.33 | 268,906,676 | 20.27h |
| 10 | Terra High | 68.6 | 51/112 | 112 | $156.61 | 354,273,706 | 23.07h |
| 11 | Luna High | 67.3 | 50/112 | 112 | $108.61 | 679,002,482 | 32.41h |

## Interpretation

- The endpoint provides model-level `score`, pass counts, task counts, tokens, wall time, and estimated cost.
- It does not expose the ten task-level outcomes, so `Weighted /100` cannot be recomputed from this API summary alone.
- Task-weighted rankings remain based on the repository's task matrix and weight snapshots; this report monitors the latest API summary.
- When source data is unchanged, the automation still updates its heartbeat without presenting it as a new benchmark batch.
- The raw API response is not stored in the public repository; only required model-summary fields are archived.

Archived API snapshots: **66**.
