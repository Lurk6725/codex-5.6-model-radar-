# Codex Radar API Monitor — English

[简体中文](api-latest.zh-CN.md) · [Project home](../README.md) · [API history CSV](../data/api/model_iq_history.csv) · [Monitor status](../data/api/monitor_status.json)

**Last successful check:** `2026-07-21T17:47:46+00:00`  
**Current API snapshot:** `eafe5db847e12f6e`  
**Source observation:** `2026-07-18T11:35:05.153982+08:00`  
**New snapshot detected:** yes  
**Models returned:** 11

> “Last successful check” confirms that the automation reached the API. “Source observation” is supplied by the upstream endpoint and may be older.

> This is a model-level summary from the Codex Radar API, not the project's task-level difficulty-weighted score.

## Current API model summary

| Rank | Model tier | Source score | Passed | Tasks | Cost | Total tokens | Wall time |
|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | Terra Max | 99.5 | 74/112 | 112 | $523.29 | 1,358,750,492 | 63.30h |
| 2 | Gpt-5.5 Xhigh | 96.9 | 72/112 | 112 | $653.55 | 840,714,298 | 42.34h |
| 3 | Luna Max | 96.9 | 72/112 | 112 | $281.66 | 1,932,982,867 | 67.54h |
| 4 | Sol Xhigh | 95 | 70/111 | 111 | $770.34 | 1,039,494,029 | 53.73h |
| 5 | Sol High | 94.2 | 70/112 | 112 | $569.24 | 727,466,351 | 42.50h |
| 6 | Sol Medium | 92.8 | 69/112 | 112 | $399.46 | 495,539,173 | 34.02h |
| 7 | Terra Xhigh | 92.8 | 69/112 | 112 | $283.58 | 696,455,008 | 37.71h |
| 8 | Gpt-5.5 High | 80.7 | 60/112 | 112 | $405.20 | 507,555,923 | 30.46h |
| 9 | Sol Low | 74.7 | 55/111 | 111 | $228.61 | 264,985,642 | 23.74h |
| 10 | Luna High | 71.3 | 53/112 | 112 | $121.22 | 793,140,827 | 36.45h |
| 11 | Terra High | 67.3 | 50/112 | 112 | $147.54 | 332,525,937 | 25.74h |

## Interpretation

- The endpoint provides model-level `score`, pass counts, task counts, tokens, wall time, and estimated cost.
- It does not expose the ten task-level outcomes, so `Weighted /100` cannot be recomputed from this API summary alone.
- Task-weighted rankings remain based on the repository's task matrix and weight snapshots; this report monitors the latest API summary.
- When source data is unchanged, the automation still updates its heartbeat without presenting it as a new benchmark batch.
- The raw API response is not stored in the public repository; only required model-summary fields are archived.

Archived API snapshots: **45**.
