# Codex Radar API Monitor — English

[简体中文](api-latest.zh-CN.md) · [Project home](../README.md) · [API history CSV](../data/api/model_iq_history.csv) · [Monitor status](../data/api/monitor_status.json)

**Last successful check:** `2026-07-18T08:11:33+00:00`  
**Current API snapshot:** `8d426ef65d8e2199`  
**Source observation:** `2026-07-18T11:35:05.153982+08:00`  
**New snapshot detected:** no; the source returned the same snapshot  
**Models returned:** 9

> “Last successful check” confirms that the automation reached the API. “Source observation” is supplied by the upstream endpoint and may be older.

> This is a model-level summary from the Codex Radar API, not the project's task-level difficulty-weighted score.

## Current API model summary

| Rank | Model tier | Source score | Passed | Tasks | Cost | Total tokens | Wall time |
|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | Terra Max | 97.7 | 72/111 | 111 | $503.89 | 1,303,566,593 | 56.12h |
| 2 | Sol High | 96.4 | 71/111 | 111 | $592.10 | 749,295,592 | 42.16h |
| 3 | Sol Xhigh | 91.2 | 66/109 | 109 | $745.08 | 1,003,528,450 | 48.99h |
| 4 | Sol Medium | 88.8 | 66/112 | 112 | $386.67 | 505,787,150 | 33.29h |
| 5 | Gpt-5.5 High | 82.8 | 61/111 | 111 | $394.34 | 498,744,537 | 33.11h |
| 6 | Luna Max | 81.6 | 59/109 | 109 | $258.11 | 1,740,674,392 | 61.49h |
| 7 | Sol Low | 77.4 | 57/111 | 111 | $219.25 | 268,711,370 | 21.41h |
| 8 | Terra High | 73.3 | 54/111 | 111 | $148.28 | 332,263,722 | 23.68h |
| 9 | Luna High | 61.1 | 45/111 | 111 | $120.69 | 781,623,998 | 32.59h |

## Interpretation

- The endpoint provides model-level `score`, pass counts, task counts, tokens, wall time, and estimated cost.
- It does not expose the ten task-level outcomes, so `Weighted /100` cannot be recomputed from this API summary alone.
- Task-weighted rankings remain based on the repository's task matrix and weight snapshots; this report monitors the latest API summary.
- When source data is unchanged, the automation still updates its heartbeat without presenting it as a new benchmark batch.
- The raw API response is not stored in the public repository; only required model-summary fields are archived.

Archived API snapshots: **18**.
