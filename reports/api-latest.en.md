# Codex Radar API Monitor — English

[简体中文](api-latest.zh-CN.md) · [Project home](../README.md) · [API history CSV](../data/api/model_iq_history.csv) · [Monitor status](../data/api/monitor_status.json)

**Last successful check:** `2026-07-24T07:20:45+00:00`  
**Current API snapshot:** `4f5c91eabc85b4c9`  
**Source observation:** `2026-07-22T06:57:20.626603+08:00`  
**New snapshot detected:** yes  
**Models returned:** 11

> “Last successful check” confirms that the automation reached the API. “Source observation” is supplied by the upstream endpoint and may be older.

> This is a model-level summary from the Codex Radar API, not the project's task-level difficulty-weighted score.

## Current API model summary

| Rank | Model tier | Source score | Passed | Tasks | Cost | Total tokens | Wall time |
|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | Sol High | 96.9 | 72/112 | 112 | $627.83 | 847,499,301 | 39.68h |
| 2 | Sol Medium | 96.9 | 72/112 | 112 | $423.38 | 534,861,708 | 29.65h |
| 3 | Sol Xhigh | 96.9 | 72/112 | 112 | $768.65 | 1,041,906,936 | 46.88h |
| 4 | Terra Max | 92.8 | 69/112 | 112 | $527.87 | 1,384,796,531 | 56.26h |
| 5 | Terra Xhigh | 91.5 | 68/112 | 112 | $269.36 | 647,246,046 | 35.00h |
| 6 | Gpt-5.5 Xhigh | 87.4 | 65/112 | 112 | $655.73 | 846,791,894 | 46.31h |
| 7 | Gpt-5.5 High | 86.1 | 64/112 | 112 | $431.04 | 541,901,130 | 34.43h |
| 8 | Luna Max | 86.1 | 64/112 | 112 | $284.85 | 1,957,883,372 | 61.91h |
| 9 | Sol Low | 80.7 | 60/112 | 112 | $230.57 | 264,300,969 | 20.09h |
| 10 | Luna High | 68.6 | 51/112 | 112 | $108.98 | 689,293,052 | 32.56h |
| 11 | Terra High | 68.6 | 51/112 | 112 | $156.14 | 352,702,612 | 23.06h |

## Interpretation

- The endpoint provides model-level `score`, pass counts, task counts, tokens, wall time, and estimated cost.
- It does not expose the ten task-level outcomes, so `Weighted /100` cannot be recomputed from this API summary alone.
- Task-weighted rankings remain based on the repository's task matrix and weight snapshots; this report monitors the latest API summary.
- When source data is unchanged, the automation still updates its heartbeat without presenting it as a new benchmark batch.
- The raw API response is not stored in the public repository; only required model-summary fields are archived.

Archived API snapshots: **67**.
