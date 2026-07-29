# Codex Radar API Monitor — English

[简体中文](api-latest.zh-CN.md) · [Project home](../README.md) · [API history CSV](../data/api/model_iq_history.csv) · [Monitor status](../data/api/monitor_status.json)

**Last successful check:** `2026-07-29T16:39:46+00:00`  
**Current API snapshot:** `e7f18dcff2419c6d`  
**Source observation:** `2026-07-22T06:57:20.626603+08:00`  
**New snapshot detected:** yes  
**Models returned:** 11

> “Last successful check” confirms that the automation reached the API. “Source observation” is supplied by the upstream endpoint and may be older.

> This is a model-level summary from the Codex Radar API, not the project's task-level difficulty-weighted score.

## Current API model summary

| Rank | Model tier | Source score | Passed | Tasks | Cost | Total tokens | Wall time |
|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | Sol Xhigh | 103.6 | 77/112 | 112 | $737.18 | 978,435,092 | 44.69h |
| 2 | Gpt-5.5 Xhigh | 98.2 | 73/112 | 112 | $660.75 | 836,324,944 | 45.66h |
| 3 | Sol High | 96.9 | 72/112 | 112 | $558.87 | 717,520,662 | 40.84h |
| 4 | Terra Max | 94.2 | 70/112 | 112 | $543.90 | 1,433,779,488 | 54.22h |
| 5 | Luna Max | 87.4 | 65/112 | 112 | $271.82 | 1,861,204,184 | 62.36h |
| 6 | Terra Xhigh | 86.1 | 64/112 | 112 | $294.55 | 725,991,256 | 35.35h |
| 7 | Gpt-5.5 High | 83.4 | 62/112 | 112 | $433.02 | 523,791,129 | 33.90h |
| 8 | Sol Low | 83.4 | 62/112 | 112 | $233.30 | 267,173,315 | 21.29h |
| 9 | Sol Medium | 82.1 | 61/112 | 112 | $415.85 | 514,714,517 | 32.51h |
| 10 | Luna High | 70 | 52/112 | 112 | $127.52 | 846,480,615 | 37.93h |
| 11 | Terra High | 67.3 | 50/112 | 112 | $159.15 | 360,453,380 | 24.18h |

## Interpretation

- The endpoint provides model-level `score`, pass counts, task counts, tokens, wall time, and estimated cost.
- It does not expose the ten task-level outcomes, so `Weighted /100` cannot be recomputed from this API summary alone.
- Task-weighted rankings remain based on the repository's task matrix and weight snapshots; this report monitors the latest API summary.
- When source data is unchanged, the automation still updates its heartbeat without presenting it as a new benchmark batch.
- The raw API response is not stored in the public repository; only required model-summary fields are archived.

Archived API snapshots: **114**.
