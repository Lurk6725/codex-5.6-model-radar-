# Codex Radar API Monitor — English

[简体中文](api-latest.zh-CN.md) · [Project home](../README.md) · [API history CSV](../data/api/model_iq_history.csv) · [Monitor status](../data/api/monitor_status.json)

**Last successful check:** `2026-08-12T06:44:56+00:00`  
**Current API snapshot:** `d3bef9636a20ff52`  
**Source observation:** `2026-07-22T06:57:20.626603+08:00`  
**New snapshot detected:** yes  
**Models returned:** 11

> “Last successful check” confirms that the automation reached the API. “Source observation” is supplied by the upstream endpoint and may be older.

> This is a model-level summary from the Codex Radar API, not the project's task-level difficulty-weighted score.

## Current API model summary

| Rank | Model tier | Source score | Passed | Tasks | Cost | Total tokens | Wall time |
|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | Sol Xhigh | 104.9 | 78/112 | 112 | $737.11 | 919,060,401 | 48.72h |
| 2 | Terra Max | 103.6 | 77/112 | 112 | $437.42 | 1,211,489,491 | 55.81h |
| 3 | Luna Max | 99.5 | 74/112 | 112 | $58.60 | 1,868,026,198 | 65.33h |
| 4 | Sol High | 99.5 | 74/112 | 112 | $562.07 | 683,057,988 | 37.72h |
| 5 | Sol Medium | 96.9 | 72/112 | 112 | $407.72 | 471,801,753 | 31.40h |
| 6 | Gpt-5.5 High | 88.8 | 66/112 | 112 | $404.19 | 491,550,568 | 32.29h |
| 7 | Gpt-5.5 Xhigh | 88.8 | 66/112 | 112 | $657.09 | 730,973,038 | 39.98h |
| 8 | Terra Xhigh | 84.7 | 63/112 | 112 | $218.40 | 579,468,736 | 34.73h |
| 9 | Terra High | 79.4 | 59/112 | 112 | $127.10 | 347,162,993 | 24.10h |
| 10 | Sol Low | 74 | 55/112 | 112 | $228.88 | 271,523,134 | 22.21h |
| 11 | Luna High | 67.3 | 50/112 | 112 | $26.20 | 766,409,197 | 34.54h |

## Interpretation

- The endpoint provides model-level `score`, pass counts, task counts, tokens, wall time, and estimated cost.
- It does not expose the ten task-level outcomes, so `Weighted /100` cannot be recomputed from this API summary alone.
- Task-weighted rankings remain based on the repository's task matrix and weight snapshots; this report monitors the latest API summary.
- When source data is unchanged, the automation still updates its heartbeat without presenting it as a new benchmark batch.
- The raw API response is not stored in the public repository; only required model-summary fields are archived.

Archived API snapshots: **240**.
