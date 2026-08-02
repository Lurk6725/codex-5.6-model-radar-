# Codex Radar API Monitor — English

[简体中文](api-latest.zh-CN.md) · [Project home](../README.md) · [API history CSV](../data/api/model_iq_history.csv) · [Monitor status](../data/api/monitor_status.json)

**Last successful check:** `2026-08-02T04:03:15+00:00`  
**Current API snapshot:** `9ae378b81bfda633`  
**Source observation:** `2026-07-22T06:57:20.626603+08:00`  
**New snapshot detected:** yes  
**Models returned:** 11

> “Last successful check” confirms that the automation reached the API. “Source observation” is supplied by the upstream endpoint and may be older.

> This is a model-level summary from the Codex Radar API, not the project's task-level difficulty-weighted score.

## Current API model summary

| Rank | Model tier | Source score | Passed | Tasks | Cost | Total tokens | Wall time |
|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | Sol Xhigh | 99.5 | 74/112 | 112 | $773.88 | 987,682,668 | 47.43h |
| 2 | Gpt-5.5 Xhigh | 92.8 | 69/112 | 112 | $652.53 | 833,319,390 | 44.07h |
| 3 | Sol Medium | 87.4 | 65/112 | 112 | $422.10 | 584,254,678 | 33.69h |
| 4 | Terra Max | 87.4 | 65/112 | 112 | $526.31 | 1,524,683,439 | 57.63h |
| 5 | Sol High | 86.1 | 64/112 | 112 | $601.80 | 789,058,145 | 41.69h |
| 6 | Luna Max | 79.4 | 59/112 | 112 | $117.42 | 1,830,772,578 | 57.34h |
| 7 | Gpt-5.5 High | 78 | 58/112 | 112 | $416.38 | 532,117,430 | 32.36h |
| 8 | Terra Xhigh | 75.3 | 56/112 | 112 | $269.58 | 730,760,029 | 35.07h |
| 9 | Terra High | 74 | 55/112 | 112 | $151.20 | 402,737,742 | 26.03h |
| 10 | Luna High | 72.6 | 54/112 | 112 | $66.03 | 799,737,919 | 33.66h |
| 11 | Sol Low | 72.6 | 54/112 | 112 | $249.21 | 286,547,836 | 21.09h |

## Interpretation

- The endpoint provides model-level `score`, pass counts, task counts, tokens, wall time, and estimated cost.
- It does not expose the ten task-level outcomes, so `Weighted /100` cannot be recomputed from this API summary alone.
- Task-weighted rankings remain based on the repository's task matrix and weight snapshots; this report monitors the latest API summary.
- When source data is unchanged, the automation still updates its heartbeat without presenting it as a new benchmark batch.
- The raw API response is not stored in the public repository; only required model-summary fields are archived.

Archived API snapshots: **150**.
