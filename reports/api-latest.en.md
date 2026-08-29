# Codex Radar API Monitor — English

[简体中文](api-latest.zh-CN.md) · [Project home](../README.md) · [API history CSV](../data/api/model_iq_history.csv) · [Monitor status](../data/api/monitor_status.json)

**Last successful check:** `2026-08-29T04:10:55+00:00`  
**Current API snapshot:** `920069297e7d360e`  
**Source observation:** `2026-07-22T06:57:20.626603+08:00`  
**New snapshot detected:** yes  
**Models returned:** 11

> “Last successful check” confirms that the automation reached the API. “Source observation” is supplied by the upstream endpoint and may be older.

> This is a model-level summary from the Codex Radar API, not the project's task-level difficulty-weighted score.

## Current API model summary

| Rank | Model tier | Source score | Passed | Tasks | Cost | Total tokens | Wall time |
|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | Luna Max | 104.9 | 78/112 | 112 | $54.04 | 1,839,833,021 | 66.91h |
| 2 | Terra Max | 104.9 | 78/112 | 112 | $425.98 | 1,225,199,062 | 57.78h |
| 3 | Sol Xhigh | 103.6 | 77/112 | 112 | $642.27 | 802,214,928 | 45.61h |
| 4 | Sol Medium | 102.2 | 76/112 | 112 | $313.24 | 425,113,325 | 29.40h |
| 5 | Gpt-5.5 Xhigh | 100.9 | 75/112 | 112 | $646.04 | 783,799,449 | 41.83h |
| 6 | Sol High | 96.9 | 72/112 | 112 | $523.67 | 581,636,957 | 35.10h |
| 7 | Terra Xhigh | 87.4 | 65/112 | 112 | $212.45 | 630,154,770 | 38.84h |
| 8 | Gpt-5.5 High | 84.7 | 63/112 | 112 | $399.90 | 505,222,334 | 32.06h |
| 9 | Terra High | 82.1 | 61/112 | 112 | $122.98 | 343,668,811 | 25.84h |
| 10 | Sol Low | 80.7 | 60/112 | 112 | $172.62 | 208,547,401 | 17.47h |
| 11 | Luna High | 71.3 | 53/112 | 112 | $22.50 | 728,051,301 | 33.33h |

## Interpretation

- The endpoint provides model-level `score`, pass counts, task counts, tokens, wall time, and estimated cost.
- It does not expose the ten task-level outcomes, so `Weighted /100` cannot be recomputed from this API summary alone.
- Task-weighted rankings remain based on the repository's task matrix and weight snapshots; this report monitors the latest API summary.
- When source data is unchanged, the automation still updates its heartbeat without presenting it as a new benchmark batch.
- The raw API response is not stored in the public repository; only required model-summary fields are archived.

Archived API snapshots: **373**.
