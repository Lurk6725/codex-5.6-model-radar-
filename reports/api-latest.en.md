# Codex Radar API Monitor — English

[简体中文](api-latest.zh-CN.md) · [Project home](../README.md) · [API history CSV](../data/api/model_iq_history.csv) · [Monitor status](../data/api/monitor_status.json)

**Last successful check:** `2026-08-19T08:56:54+00:00`  
**Current API snapshot:** `f1c4bcd5d629be94`  
**Source observation:** `2026-07-22T06:57:20.626603+08:00`  
**New snapshot detected:** yes  
**Models returned:** 11

> “Last successful check” confirms that the automation reached the API. “Source observation” is supplied by the upstream endpoint and may be older.

> This is a model-level summary from the Codex Radar API, not the project's task-level difficulty-weighted score.

## Current API model summary

| Rank | Model tier | Source score | Passed | Tasks | Cost | Total tokens | Wall time |
|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | Terra Max | 99.5 | 74/112 | 112 | $434.66 | 1,266,644,120 | 60.10h |
| 2 | Sol Xhigh | 95.5 | 71/112 | 112 | $727.83 | 842,766,856 | 44.67h |
| 3 | Gpt-5.5 Xhigh | 94.2 | 70/112 | 112 | $654.08 | 767,886,849 | 41.67h |
| 4 | Luna Max | 94.2 | 70/112 | 112 | $55.21 | 1,824,030,574 | 64.85h |
| 5 | Gpt-5.5 High | 92.8 | 69/112 | 112 | $402.35 | 504,434,937 | 33.55h |
| 6 | Terra Xhigh | 88.8 | 66/112 | 112 | $215.32 | 609,861,700 | 38.83h |
| 7 | Sol High | 87.4 | 65/112 | 112 | $537.37 | 626,376,859 | 35.65h |
| 8 | Sol Medium | 86.1 | 64/112 | 112 | $399.03 | 504,916,038 | 34.61h |
| 9 | Terra High | 76.7 | 57/112 | 112 | $125.24 | 349,055,740 | 26.29h |
| 10 | Luna High | 75.3 | 56/112 | 112 | $23.58 | 771,621,821 | 34.86h |
| 11 | Sol Low | 70 | 52/112 | 112 | $225.28 | 273,370,091 | 24.68h |

## Interpretation

- The endpoint provides model-level `score`, pass counts, task counts, tokens, wall time, and estimated cost.
- It does not expose the ten task-level outcomes, so `Weighted /100` cannot be recomputed from this API summary alone.
- Task-weighted rankings remain based on the repository's task matrix and weight snapshots; this report monitors the latest API summary.
- When source data is unchanged, the automation still updates its heartbeat without presenting it as a new benchmark batch.
- The raw API response is not stored in the public repository; only required model-summary fields are archived.

Archived API snapshots: **295**.
