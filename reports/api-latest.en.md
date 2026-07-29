# Codex Radar API Monitor — English

[简体中文](api-latest.zh-CN.md) · [Project home](../README.md) · [API history CSV](../data/api/model_iq_history.csv) · [Monitor status](../data/api/monitor_status.json)

**Last successful check:** `2026-07-29T17:58:32+00:00`  
**Current API snapshot:** `1ccf813cea8c56ae`  
**Source observation:** `2026-07-22T06:57:20.626603+08:00`  
**New snapshot detected:** yes  
**Models returned:** 11

> “Last successful check” confirms that the automation reached the API. “Source observation” is supplied by the upstream endpoint and may be older.

> This is a model-level summary from the Codex Radar API, not the project's task-level difficulty-weighted score.

## Current API model summary

| Rank | Model tier | Source score | Passed | Tasks | Cost | Total tokens | Wall time |
|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | Sol Xhigh | 100.9 | 75/112 | 112 | $746.03 | 989,757,829 | 45.56h |
| 2 | Gpt-5.5 Xhigh | 99.5 | 74/112 | 112 | $663.28 | 840,034,100 | 45.83h |
| 3 | Sol High | 96.9 | 72/112 | 112 | $561.86 | 722,612,071 | 40.18h |
| 4 | Terra Max | 95.5 | 71/112 | 112 | $545.32 | 1,441,972,604 | 54.01h |
| 5 | Gpt-5.5 High | 92.8 | 69/112 | 112 | $447.03 | 548,687,558 | 32.89h |
| 6 | Terra Xhigh | 84.7 | 63/112 | 112 | $294.87 | 726,252,964 | 35.71h |
| 7 | Luna Max | 83.4 | 62/112 | 112 | $272.56 | 1,860,652,706 | 63.59h |
| 8 | Sol Medium | 83.4 | 62/112 | 112 | $421.40 | 525,868,666 | 32.17h |
| 9 | Sol Low | 80.7 | 60/112 | 112 | $234.15 | 269,121,961 | 21.71h |
| 10 | Terra High | 71.3 | 53/112 | 112 | $158.30 | 358,214,281 | 24.39h |
| 11 | Luna High | 68.6 | 51/112 | 112 | $125.13 | 826,576,623 | 37.38h |

## Interpretation

- The endpoint provides model-level `score`, pass counts, task counts, tokens, wall time, and estimated cost.
- It does not expose the ten task-level outcomes, so `Weighted /100` cannot be recomputed from this API summary alone.
- Task-weighted rankings remain based on the repository's task matrix and weight snapshots; this report monitors the latest API summary.
- When source data is unchanged, the automation still updates its heartbeat without presenting it as a new benchmark batch.
- The raw API response is not stored in the public repository; only required model-summary fields are archived.

Archived API snapshots: **115**.
