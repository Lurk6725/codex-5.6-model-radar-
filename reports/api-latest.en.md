# Codex Radar API Monitor — English

[简体中文](api-latest.zh-CN.md) · [Project home](../README.md) · [API history CSV](../data/api/model_iq_history.csv) · [Monitor status](../data/api/monitor_status.json)

**Last successful check:** `2026-07-24T10:00:36+00:00`  
**Current API snapshot:** `d62daa241072f05e`  
**Source observation:** `2026-07-22T06:57:20.626603+08:00`  
**New snapshot detected:** yes  
**Models returned:** 11

> “Last successful check” confirms that the automation reached the API. “Source observation” is supplied by the upstream endpoint and may be older.

> This is a model-level summary from the Codex Radar API, not the project's task-level difficulty-weighted score.

## Current API model summary

| Rank | Model tier | Source score | Passed | Tasks | Cost | Total tokens | Wall time |
|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | Sol High | 98.2 | 73/112 | 112 | $627.51 | 846,918,801 | 39.72h |
| 2 | Sol Medium | 96.9 | 72/112 | 112 | $423.51 | 535,045,006 | 29.64h |
| 3 | Sol Xhigh | 95.5 | 71/112 | 112 | $765.45 | 1,036,672,209 | 46.53h |
| 4 | Terra Max | 92.8 | 69/112 | 112 | $537.13 | 1,409,982,936 | 55.46h |
| 5 | Terra Xhigh | 92.8 | 69/112 | 112 | $271.02 | 650,940,135 | 35.07h |
| 6 | Gpt-5.5 Xhigh | 87.4 | 65/112 | 112 | $651.22 | 838,314,935 | 46.12h |
| 7 | Luna Max | 86.1 | 64/112 | 112 | $284.69 | 1,958,413,224 | 61.92h |
| 8 | Sol Low | 80.7 | 60/112 | 112 | $231.77 | 266,082,738 | 20.13h |
| 9 | Gpt-5.5 High | 79.4 | 59/112 | 112 | $428.08 | 537,257,536 | 33.57h |
| 10 | Luna High | 70 | 52/112 | 112 | $109.06 | 689,923,367 | 32.22h |
| 11 | Terra High | 67.3 | 50/112 | 112 | $155.57 | 350,362,838 | 22.89h |

## Interpretation

- The endpoint provides model-level `score`, pass counts, task counts, tokens, wall time, and estimated cost.
- It does not expose the ten task-level outcomes, so `Weighted /100` cannot be recomputed from this API summary alone.
- Task-weighted rankings remain based on the repository's task matrix and weight snapshots; this report monitors the latest API summary.
- When source data is unchanged, the automation still updates its heartbeat without presenting it as a new benchmark batch.
- The raw API response is not stored in the public repository; only required model-summary fields are archived.

Archived API snapshots: **68**.
