# Codex Radar API Monitor — English

[简体中文](api-latest.zh-CN.md) · [Project home](../README.md) · [API history CSV](../data/api/model_iq_history.csv) · [Monitor status](../data/api/monitor_status.json)

**Last successful check:** `2026-07-26T14:18:05+00:00`  
**Current API snapshot:** `c793b8d7e1f96b11`  
**Source observation:** `2026-07-22T06:57:20.626603+08:00`  
**New snapshot detected:** yes  
**Models returned:** 11

> “Last successful check” confirms that the automation reached the API. “Source observation” is supplied by the upstream endpoint and may be older.

> This is a model-level summary from the Codex Radar API, not the project's task-level difficulty-weighted score.

## Current API model summary

| Rank | Model tier | Source score | Passed | Tasks | Cost | Total tokens | Wall time |
|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | Sol Xhigh | 94.2 | 70/112 | 112 | $791.80 | 1,088,805,687 | 49.56h |
| 2 | Sol High | 92.8 | 69/112 | 112 | $583.39 | 776,310,106 | 36.03h |
| 3 | Sol Medium | 92.8 | 69/112 | 112 | $435.35 | 555,558,017 | 30.59h |
| 4 | Terra Max | 91.5 | 68/112 | 112 | $537.07 | 1,411,401,975 | 56.02h |
| 5 | Luna Max | 90.1 | 67/112 | 112 | $275.87 | 1,881,228,720 | 59.50h |
| 6 | Gpt-5.5 High | 88.8 | 66/112 | 112 | $417.53 | 525,876,517 | 28.66h |
| 7 | Gpt-5.5 Xhigh | 87.4 | 65/112 | 112 | $655.33 | 847,208,393 | 41.44h |
| 8 | Sol Low | 78 | 58/112 | 112 | $223.55 | 253,290,643 | 18.72h |
| 9 | Terra Xhigh | 75.3 | 56/112 | 112 | $274.70 | 664,134,154 | 34.24h |
| 10 | Luna High | 70 | 52/112 | 112 | $117.09 | 757,248,904 | 30.46h |
| 11 | Terra High | 68.6 | 51/112 | 112 | $145.96 | 320,044,598 | 20.56h |

## Interpretation

- The endpoint provides model-level `score`, pass counts, task counts, tokens, wall time, and estimated cost.
- It does not expose the ten task-level outcomes, so `Weighted /100` cannot be recomputed from this API summary alone.
- Task-weighted rankings remain based on the repository's task matrix and weight snapshots; this report monitors the latest API summary.
- When source data is unchanged, the automation still updates its heartbeat without presenting it as a new benchmark batch.
- The raw API response is not stored in the public repository; only required model-summary fields are archived.

Archived API snapshots: **90**.
