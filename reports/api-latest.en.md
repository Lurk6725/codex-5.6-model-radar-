# Codex Radar API Monitor — English

[简体中文](api-latest.zh-CN.md) · [Project home](../README.md) · [API history CSV](../data/api/model_iq_history.csv) · [Monitor status](../data/api/monitor_status.json)

**Last successful check:** `2026-08-04T04:32:55+00:00`  
**Current API snapshot:** `357031b4dc47f6b4`  
**Source observation:** `2026-07-22T06:57:20.626603+08:00`  
**New snapshot detected:** yes  
**Models returned:** 11

> “Last successful check” confirms that the automation reached the API. “Source observation” is supplied by the upstream endpoint and may be older.

> This is a model-level summary from the Codex Radar API, not the project's task-level difficulty-weighted score.

## Current API model summary

| Rank | Model tier | Source score | Passed | Tasks | Cost | Total tokens | Wall time |
|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | Sol Xhigh | 106.3 | 79/112 | 112 | $761.52 | 939,278,651 | 47.14h |
| 2 | Luna Max | 99.5 | 74/112 | 112 | $59.06 | 1,780,165,394 | 62.37h |
| 3 | Gpt-5.5 Xhigh | 96.9 | 72/112 | 112 | $655.81 | 773,246,031 | 41.22h |
| 4 | Sol Medium | 91.5 | 68/112 | 112 | $412.09 | 528,832,721 | 30.31h |
| 5 | Terra Max | 90.1 | 67/112 | 112 | $473.77 | 1,446,736,858 | 57.92h |
| 6 | Gpt-5.5 High | 86.1 | 64/112 | 112 | $407.24 | 486,299,827 | 29.59h |
| 7 | Terra Xhigh | 83.4 | 62/112 | 112 | $238.58 | 612,674,220 | 33.06h |
| 8 | Terra High | 80.7 | 60/112 | 112 | $140.50 | 361,688,460 | 23.60h |
| 9 | Sol High | 79.4 | 59/112 | 112 | $592.20 | 670,115,090 | 38.51h |
| 10 | Sol Low | 79.4 | 59/112 | 112 | $229.53 | 230,874,132 | 19.70h |
| 11 | Luna High | 67.3 | 50/112 | 112 | $35.38 | 718,086,594 | 29.18h |

## Interpretation

- The endpoint provides model-level `score`, pass counts, task counts, tokens, wall time, and estimated cost.
- It does not expose the ten task-level outcomes, so `Weighted /100` cannot be recomputed from this API summary alone.
- Task-weighted rankings remain based on the repository's task matrix and weight snapshots; this report monitors the latest API summary.
- When source data is unchanged, the automation still updates its heartbeat without presenting it as a new benchmark batch.
- The raw API response is not stored in the public repository; only required model-summary fields are archived.

Archived API snapshots: **166**.
