# Codex Radar API Monitor — English

[简体中文](api-latest.zh-CN.md) · [Project home](../README.md) · [API history CSV](../data/api/model_iq_history.csv) · [Monitor status](../data/api/monitor_status.json)

**Last successful check:** `2026-08-24T10:22:46+00:00`  
**Current API snapshot:** `059ec25f460a7ecf`  
**Source observation:** `2026-07-22T06:57:20.626603+08:00`  
**New snapshot detected:** yes  
**Models returned:** 11

> “Last successful check” confirms that the automation reached the API. “Source observation” is supplied by the upstream endpoint and may be older.

> This is a model-level summary from the Codex Radar API, not the project's task-level difficulty-weighted score.

## Current API model summary

| Rank | Model tier | Source score | Passed | Tasks | Cost | Total tokens | Wall time |
|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | Sol Xhigh | 104.9 | 78/112 | 112 | $713.14 | 805,106,139 | 45.08h |
| 2 | Gpt-5.5 Xhigh | 99.5 | 74/112 | 112 | $648.82 | 773,233,958 | 40.17h |
| 3 | Terra Max | 95.5 | 71/112 | 112 | $425.52 | 1,161,065,574 | 54.82h |
| 4 | Luna Max | 90.1 | 67/112 | 112 | $54.38 | 1,722,023,212 | 58.43h |
| 5 | Gpt-5.5 High | 88.8 | 66/112 | 112 | $400.49 | 496,314,317 | 31.82h |
| 6 | Sol High | 86.1 | 64/112 | 112 | $530.43 | 572,020,545 | 34.65h |
| 7 | Terra Xhigh | 86.1 | 64/112 | 112 | $213.04 | 586,602,184 | 35.89h |
| 8 | Sol Medium | 80.7 | 60/112 | 112 | $403.10 | 445,252,928 | 31.33h |
| 9 | Luna High | 78 | 58/112 | 112 | $22.61 | 696,144,080 | 30.17h |
| 10 | Terra High | 76.7 | 57/112 | 112 | $124.39 | 328,427,130 | 24.51h |
| 11 | Sol Low | 72.6 | 54/112 | 112 | $222.43 | 253,968,576 | 22.22h |

## Interpretation

- The endpoint provides model-level `score`, pass counts, task counts, tokens, wall time, and estimated cost.
- It does not expose the ten task-level outcomes, so `Weighted /100` cannot be recomputed from this API summary alone.
- Task-weighted rankings remain based on the repository's task matrix and weight snapshots; this report monitors the latest API summary.
- When source data is unchanged, the automation still updates its heartbeat without presenting it as a new benchmark batch.
- The raw API response is not stored in the public repository; only required model-summary fields are archived.

Archived API snapshots: **342**.
