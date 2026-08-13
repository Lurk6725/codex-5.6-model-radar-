# Codex Radar API Monitor — English

[简体中文](api-latest.zh-CN.md) · [Project home](../README.md) · [API history CSV](../data/api/model_iq_history.csv) · [Monitor status](../data/api/monitor_status.json)

**Last successful check:** `2026-08-13T07:03:32+00:00`  
**Current API snapshot:** `2c604c73a4e34083`  
**Source observation:** `2026-07-22T06:57:20.626603+08:00`  
**New snapshot detected:** yes  
**Models returned:** 11

> “Last successful check” confirms that the automation reached the API. “Source observation” is supplied by the upstream endpoint and may be older.

> This is a model-level summary from the Codex Radar API, not the project's task-level difficulty-weighted score.

## Current API model summary

| Rank | Model tier | Source score | Passed | Tasks | Cost | Total tokens | Wall time |
|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | Terra Max | 102.2 | 76/112 | 112 | $435.10 | 1,228,473,316 | 58.39h |
| 2 | Sol Xhigh | 99.5 | 74/112 | 112 | $726.52 | 840,755,853 | 44.87h |
| 3 | Luna Max | 98.2 | 73/112 | 112 | $58.58 | 1,885,399,291 | 68.05h |
| 4 | Gpt-5.5 Xhigh | 94.2 | 70/112 | 112 | $656.97 | 710,507,977 | 41.26h |
| 5 | Sol High | 88.8 | 66/112 | 112 | $538.07 | 648,444,328 | 36.78h |
| 6 | Gpt-5.5 High | 87.4 | 65/112 | 112 | $403.69 | 497,316,596 | 33.82h |
| 7 | Sol Medium | 87.4 | 65/112 | 112 | $382.86 | 446,483,241 | 31.54h |
| 8 | Terra Xhigh | 83.4 | 62/112 | 112 | $217.49 | 597,357,404 | 36.93h |
| 9 | Terra High | 75.3 | 56/112 | 112 | $126.56 | 336,749,333 | 25.35h |
| 10 | Luna High | 74 | 55/112 | 112 | $26.17 | 787,593,553 | 35.78h |
| 11 | Sol Low | 70 | 52/112 | 112 | $225.52 | 281,920,773 | 23.52h |

## Interpretation

- The endpoint provides model-level `score`, pass counts, task counts, tokens, wall time, and estimated cost.
- It does not expose the ten task-level outcomes, so `Weighted /100` cannot be recomputed from this API summary alone.
- Task-weighted rankings remain based on the repository's task matrix and weight snapshots; this report monitors the latest API summary.
- When source data is unchanged, the automation still updates its heartbeat without presenting it as a new benchmark batch.
- The raw API response is not stored in the public repository; only required model-summary fields are archived.

Archived API snapshots: **251**.
