# Codex Radar API Monitor — English

[简体中文](api-latest.zh-CN.md) · [Project home](../README.md) · [API history CSV](../data/api/model_iq_history.csv) · [Monitor status](../data/api/monitor_status.json)

**Last successful check:** `2026-08-09T10:57:02+00:00`  
**Current API snapshot:** `e89cf5bc8e5ea082`  
**Source observation:** `2026-07-22T06:57:20.626603+08:00`  
**New snapshot detected:** no; the source returned the same snapshot  
**Models returned:** 11

> “Last successful check” confirms that the automation reached the API. “Source observation” is supplied by the upstream endpoint and may be older.

> This is a model-level summary from the Codex Radar API, not the project's task-level difficulty-weighted score.

## Current API model summary

| Rank | Model tier | Source score | Passed | Tasks | Cost | Total tokens | Wall time |
|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | Sol Xhigh | 111.7 | 83/112 | 112 | $743.74 | 956,600,600 | 49.98h |
| 2 | Sol High | 96.9 | 72/112 | 112 | $571.33 | 596,281,898 | 36.53h |
| 3 | Luna Max | 92.8 | 69/112 | 112 | $58.78 | 1,711,166,271 | 59.16h |
| 4 | Sol Low | 91.5 | 68/112 | 112 | $228.79 | 272,484,565 | 21.89h |
| 5 | Sol Medium | 91.5 | 68/112 | 112 | $408.31 | 522,031,404 | 31.65h |
| 6 | Terra Max | 91.5 | 68/112 | 112 | $443.44 | 1,294,305,450 | 55.13h |
| 7 | Gpt-5.5 High | 90.1 | 67/112 | 112 | $406.45 | 479,330,247 | 30.66h |
| 8 | Gpt-5.5 Xhigh | 90.1 | 67/112 | 112 | $659.38 | 812,779,847 | 42.28h |
| 9 | Terra Xhigh | 86.1 | 64/112 | 112 | $223.96 | 595,822,464 | 33.69h |
| 10 | Terra High | 78 | 58/112 | 112 | $126.81 | 335,608,785 | 22.33h |
| 11 | Luna High | 74 | 55/112 | 112 | $26.21 | 737,175,155 | 31.60h |

## Interpretation

- The endpoint provides model-level `score`, pass counts, task counts, tokens, wall time, and estimated cost.
- It does not expose the ten task-level outcomes, so `Weighted /100` cannot be recomputed from this API summary alone.
- Task-weighted rankings remain based on the repository's task matrix and weight snapshots; this report monitors the latest API summary.
- When source data is unchanged, the automation still updates its heartbeat without presenting it as a new benchmark batch.
- The raw API response is not stored in the public repository; only required model-summary fields are archived.

Archived API snapshots: **214**.
