# Codex Radar API Monitor — English

[简体中文](api-latest.zh-CN.md) · [Project home](../README.md) · [API history CSV](../data/api/model_iq_history.csv) · [Monitor status](../data/api/monitor_status.json)

**Last successful check:** `2026-07-25T08:26:20+00:00`  
**Current API snapshot:** `6d256d8c631a91b0`  
**Source observation:** `2026-07-22T06:57:20.626603+08:00`  
**New snapshot detected:** yes  
**Models returned:** 11

> “Last successful check” confirms that the automation reached the API. “Source observation” is supplied by the upstream endpoint and may be older.

> This is a model-level summary from the Codex Radar API, not the project's task-level difficulty-weighted score.

## Current API model summary

| Rank | Model tier | Source score | Passed | Tasks | Cost | Total tokens | Wall time |
|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | Sol Xhigh | 98.2 | 73/112 | 112 | $770.42 | 1,044,888,923 | 46.44h |
| 2 | Sol High | 96.9 | 72/112 | 112 | $631.47 | 860,288,439 | 39.55h |
| 3 | Sol Medium | 94.2 | 70/112 | 112 | $429.27 | 545,774,141 | 29.84h |
| 4 | Terra Xhigh | 92.8 | 69/112 | 112 | $279.11 | 673,572,184 | 36.43h |
| 5 | Terra Max | 90.1 | 67/112 | 112 | $541.55 | 1,421,958,384 | 56.29h |
| 6 | Luna Max | 86.1 | 64/112 | 112 | $286.12 | 1,979,519,999 | 61.60h |
| 7 | Gpt-5.5 Xhigh | 83.4 | 62/112 | 112 | $655.21 | 845,566,894 | 44.82h |
| 8 | Gpt-5.5 High | 78 | 58/112 | 112 | $422.74 | 528,578,602 | 32.36h |
| 9 | Sol Low | 76.7 | 57/112 | 112 | $232.35 | 268,266,447 | 20.49h |
| 10 | Terra High | 70 | 52/112 | 112 | $157.87 | 360,116,961 | 23.07h |
| 11 | Luna High | 68.6 | 51/112 | 112 | $110.97 | 709,076,574 | 32.08h |

## Interpretation

- The endpoint provides model-level `score`, pass counts, task counts, tokens, wall time, and estimated cost.
- It does not expose the ten task-level outcomes, so `Weighted /100` cannot be recomputed from this API summary alone.
- Task-weighted rankings remain based on the repository's task matrix and weight snapshots; this report monitors the latest API summary.
- When source data is unchanged, the automation still updates its heartbeat without presenting it as a new benchmark batch.
- The raw API response is not stored in the public repository; only required model-summary fields are archived.

Archived API snapshots: **77**.
