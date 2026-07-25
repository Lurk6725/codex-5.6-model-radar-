# Codex Radar API Monitor — English

[简体中文](api-latest.zh-CN.md) · [Project home](../README.md) · [API history CSV](../data/api/model_iq_history.csv) · [Monitor status](../data/api/monitor_status.json)

**Last successful check:** `2026-07-25T11:39:07+00:00`  
**Current API snapshot:** `cfd1c04cc811c53a`  
**Source observation:** `2026-07-22T06:57:20.626603+08:00`  
**New snapshot detected:** yes  
**Models returned:** 11

> “Last successful check” confirms that the automation reached the API. “Source observation” is supplied by the upstream endpoint and may be older.

> This is a model-level summary from the Codex Radar API, not the project's task-level difficulty-weighted score.

## Current API model summary

| Rank | Model tier | Source score | Passed | Tasks | Cost | Total tokens | Wall time |
|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | Sol High | 99.5 | 74/112 | 112 | $610.18 | 823,348,246 | 37.70h |
| 2 | Sol Xhigh | 98.2 | 73/112 | 112 | $770.42 | 1,044,888,923 | 46.44h |
| 3 | Sol Medium | 95.5 | 71/112 | 112 | $427.44 | 543,271,272 | 29.69h |
| 4 | Terra Xhigh | 91.5 | 68/112 | 112 | $280.86 | 679,418,785 | 36.90h |
| 5 | Terra Max | 90.1 | 67/112 | 112 | $563.94 | 1,483,624,485 | 58.43h |
| 6 | Luna Max | 84.7 | 63/112 | 112 | $286.01 | 1,975,984,173 | 61.64h |
| 7 | Gpt-5.5 Xhigh | 80.7 | 60/112 | 112 | $654.61 | 844,043,048 | 45.11h |
| 8 | Gpt-5.5 High | 78 | 58/112 | 112 | $422.38 | 527,816,606 | 32.41h |
| 9 | Sol Low | 76.7 | 57/112 | 112 | $231.60 | 267,936,776 | 20.60h |
| 10 | Luna High | 70 | 52/112 | 112 | $113.84 | 733,357,266 | 32.34h |
| 11 | Terra High | 70 | 52/112 | 112 | $157.44 | 359,617,539 | 23.11h |

## Interpretation

- The endpoint provides model-level `score`, pass counts, task counts, tokens, wall time, and estimated cost.
- It does not expose the ten task-level outcomes, so `Weighted /100` cannot be recomputed from this API summary alone.
- Task-weighted rankings remain based on the repository's task matrix and weight snapshots; this report monitors the latest API summary.
- When source data is unchanged, the automation still updates its heartbeat without presenting it as a new benchmark batch.
- The raw API response is not stored in the public repository; only required model-summary fields are archived.

Archived API snapshots: **79**.
