# Codex Radar API Monitor — English

[简体中文](api-latest.zh-CN.md) · [Project home](../README.md) · [API history CSV](../data/api/model_iq_history.csv) · [Monitor status](../data/api/monitor_status.json)

**Last successful check:** `2026-07-17T22:08:24+00:00`  
**Current API snapshot:** `4ed4b38c16bb6044`  
**Source observation:** `2026-07-13T22:08:07.261261+08:00`  
**New snapshot detected:** no; the source returned the same snapshot  
**Models returned:** 9

> “Last successful check” confirms that the automation reached the API. “Source observation” is supplied by the upstream endpoint and may be older.

> This is a model-level summary from the Codex Radar API, not the project's task-level difficulty-weighted score.

## Current API model summary

| Rank | Model tier | Source score | Passed | Tasks | Cost | Total tokens | Wall time |
|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | Terra Max | 96.8 | 70/109 | 109 | $493.61 | 1,265,413,278 | 54.73h |
| 2 | Sol High | 93.7 | 69/111 | 111 | $590.04 | 745,619,524 | 42.90h |
| 3 | Sol Xhigh | 92.9 | 66/107 | 107 | $741.66 | 1,014,108,781 | 49.36h |
| 4 | Sol Medium | 88.8 | 66/112 | 112 | $399.48 | 512,477,831 | 33.86h |
| 5 | Luna Max | 85.9 | 61/107 | 107 | $250.00 | 1,678,401,976 | 58.37h |
| 6 | Sol Low | 81.4 | 60/111 | 111 | $218.45 | 265,837,808 | 21.87h |
| 7 | Gpt-5.5 High | 78.7 | 58/111 | 111 | $392.91 | 496,296,519 | 33.92h |
| 8 | Terra High | 70.5 | 51/109 | 109 | $146.15 | 325,872,963 | 23.38h |
| 9 | Luna High | 62.2 | 45/109 | 109 | $122.18 | 793,918,182 | 32.81h |

## Interpretation

- The endpoint provides model-level `score`, pass counts, task counts, tokens, wall time, and estimated cost.
- It does not expose the ten task-level outcomes, so `Weighted /100` cannot be recomputed from this API summary alone.
- Task-weighted rankings remain based on the repository's task matrix and weight snapshots; this report monitors the latest API summary.
- When source data is unchanged, the automation still updates its heartbeat without presenting it as a new benchmark batch.
- The raw API response is not stored in the public repository; only required model-summary fields are archived.

Archived API snapshots: **16**.
