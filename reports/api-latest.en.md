# Codex Radar API Monitor — English

[简体中文](api-latest.zh-CN.md) · [Project home](../README.md) · [API history CSV](../data/api/model_iq_history.csv) · [Monitor status](../data/api/monitor_status.json)

**Last successful check:** `2026-08-03T08:43:05+00:00`  
**Current API snapshot:** `03c9d1a74ab7290d`  
**Source observation:** `2026-07-22T06:57:20.626603+08:00`  
**New snapshot detected:** yes  
**Models returned:** 11

> “Last successful check” confirms that the automation reached the API. “Source observation” is supplied by the upstream endpoint and may be older.

> This is a model-level summary from the Codex Radar API, not the project's task-level difficulty-weighted score.

## Current API model summary

| Rank | Model tier | Source score | Passed | Tasks | Cost | Total tokens | Wall time |
|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | Sol Xhigh | 102.2 | 76/112 | 112 | $768.64 | 945,523,792 | 47.55h |
| 2 | Gpt-5.5 Xhigh | 99.5 | 74/112 | 112 | $656.64 | 817,121,542 | 43.90h |
| 3 | Terra Max | 95.5 | 71/112 | 112 | $508.97 | 1,487,808,488 | 58.07h |
| 4 | Luna Max | 92.8 | 69/112 | 112 | $61.12 | 1,745,001,510 | 59.99h |
| 5 | Sol Medium | 87.4 | 65/112 | 112 | $410.21 | 515,180,446 | 32.06h |
| 6 | Gpt-5.5 High | 83.4 | 62/112 | 112 | $412.14 | 503,333,141 | 31.46h |
| 7 | Sol High | 83.4 | 62/112 | 112 | $591.28 | 749,987,973 | 42.27h |
| 8 | Terra Xhigh | 80.7 | 60/112 | 112 | $251.27 | 645,102,260 | 34.43h |
| 9 | Sol Low | 74 | 55/112 | 112 | $237.32 | 253,369,353 | 20.65h |
| 10 | Luna High | 70 | 52/112 | 112 | $41.65 | 750,298,748 | 31.14h |
| 11 | Terra High | 70 | 52/112 | 112 | $146.58 | 393,909,871 | 25.53h |

## Interpretation

- The endpoint provides model-level `score`, pass counts, task counts, tokens, wall time, and estimated cost.
- It does not expose the ten task-level outcomes, so `Weighted /100` cannot be recomputed from this API summary alone.
- Task-weighted rankings remain based on the repository's task matrix and weight snapshots; this report monitors the latest API summary.
- When source data is unchanged, the automation still updates its heartbeat without presenting it as a new benchmark batch.
- The raw API response is not stored in the public repository; only required model-summary fields are archived.

Archived API snapshots: **162**.
