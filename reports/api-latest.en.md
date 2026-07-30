# Codex Radar API Monitor — English

[简体中文](api-latest.zh-CN.md) · [Project home](../README.md) · [API history CSV](../data/api/model_iq_history.csv) · [Monitor status](../data/api/monitor_status.json)

**Last successful check:** `2026-07-30T12:06:07+00:00`  
**Current API snapshot:** `4bc462625c6a886a`  
**Source observation:** `2026-07-22T06:57:20.626603+08:00`  
**New snapshot detected:** yes  
**Models returned:** 11

> “Last successful check” confirms that the automation reached the API. “Source observation” is supplied by the upstream endpoint and may be older.

> This is a model-level summary from the Codex Radar API, not the project's task-level difficulty-weighted score.

## Current API model summary

| Rank | Model tier | Source score | Passed | Tasks | Cost | Total tokens | Wall time |
|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | Gpt-5.5 Xhigh | 95.5 | 71/112 | 112 | $652.09 | 835,338,225 | 43.85h |
| 2 | Sol Xhigh | 95.5 | 71/112 | 112 | $727.16 | 961,217,741 | 45.38h |
| 3 | Sol High | 91.5 | 68/112 | 112 | $596.41 | 787,455,948 | 41.01h |
| 4 | Luna Max | 87.4 | 65/112 | 112 | $271.30 | 1,849,899,022 | 61.67h |
| 5 | Gpt-5.5 High | 86.1 | 64/112 | 112 | $440.97 | 553,031,547 | 31.82h |
| 6 | Sol Low | 83.4 | 62/112 | 112 | $249.79 | 290,210,544 | 22.17h |
| 7 | Sol Medium | 83.4 | 62/112 | 112 | $422.56 | 523,939,726 | 30.92h |
| 8 | Terra Xhigh | 83.4 | 62/112 | 112 | $277.07 | 662,832,914 | 34.57h |
| 9 | Terra Max | 82.1 | 61/112 | 112 | $561.20 | 1,465,715,187 | 54.95h |
| 10 | Terra High | 74 | 55/112 | 112 | $160.32 | 362,561,521 | 22.90h |
| 11 | Luna High | 65.9 | 49/112 | 112 | $125.25 | 832,518,326 | 34.48h |

## Interpretation

- The endpoint provides model-level `score`, pass counts, task counts, tokens, wall time, and estimated cost.
- It does not expose the ten task-level outcomes, so `Weighted /100` cannot be recomputed from this API summary alone.
- Task-weighted rankings remain based on the repository's task matrix and weight snapshots; this report monitors the latest API summary.
- When source data is unchanged, the automation still updates its heartbeat without presenting it as a new benchmark batch.
- The raw API response is not stored in the public repository; only required model-summary fields are archived.

Archived API snapshots: **121**.
