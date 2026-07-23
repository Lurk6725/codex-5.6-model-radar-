# Codex Radar API Monitor — English

[简体中文](api-latest.zh-CN.md) · [Project home](../README.md) · [API history CSV](../data/api/model_iq_history.csv) · [Monitor status](../data/api/monitor_status.json)

**Last successful check:** `2026-07-23T19:48:44+00:00`  
**Current API snapshot:** `65f390678d100923`  
**Source observation:** `2026-07-22T06:57:20.626603+08:00`  
**New snapshot detected:** yes  
**Models returned:** 11

> “Last successful check” confirms that the automation reached the API. “Source observation” is supplied by the upstream endpoint and may be older.

> This is a model-level summary from the Codex Radar API, not the project's task-level difficulty-weighted score.

## Current API model summary

| Rank | Model tier | Source score | Passed | Tasks | Cost | Total tokens | Wall time |
|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | Sol Xhigh | 100.9 | 75/112 | 112 | $790.12 | 1,081,098,044 | 48.04h |
| 2 | Sol High | 96.9 | 72/112 | 112 | $676.87 | 943,750,167 | 42.37h |
| 3 | Sol Medium | 96.9 | 72/112 | 112 | $423.30 | 533,975,527 | 30.67h |
| 4 | Terra Max | 92.8 | 69/112 | 112 | $529.22 | 1,389,074,400 | 56.46h |
| 5 | Terra Xhigh | 88.8 | 66/112 | 112 | $271.91 | 656,210,760 | 35.85h |
| 6 | Gpt-5.5 High | 87.4 | 65/112 | 112 | $431.49 | 544,856,184 | 35.13h |
| 7 | Gpt-5.5 Xhigh | 87.4 | 65/112 | 112 | $647.72 | 833,590,421 | 46.43h |
| 8 | Luna Max | 83.4 | 62/112 | 112 | $283.58 | 1,944,413,731 | 62.10h |
| 9 | Sol Low | 79.4 | 59/112 | 112 | $231.63 | 269,693,567 | 20.31h |
| 10 | Terra High | 71.3 | 53/112 | 112 | $153.91 | 346,782,862 | 22.99h |
| 11 | Luna High | 65.9 | 49/112 | 112 | $108.92 | 682,960,969 | 32.58h |

## Interpretation

- The endpoint provides model-level `score`, pass counts, task counts, tokens, wall time, and estimated cost.
- It does not expose the ten task-level outcomes, so `Weighted /100` cannot be recomputed from this API summary alone.
- Task-weighted rankings remain based on the repository's task matrix and weight snapshots; this report monitors the latest API summary.
- When source data is unchanged, the automation still updates its heartbeat without presenting it as a new benchmark batch.
- The raw API response is not stored in the public repository; only required model-summary fields are archived.

Archived API snapshots: **64**.
