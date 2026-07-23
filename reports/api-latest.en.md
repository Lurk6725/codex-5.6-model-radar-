# Codex Radar API Monitor — English

[简体中文](api-latest.zh-CN.md) · [Project home](../README.md) · [API history CSV](../data/api/model_iq_history.csv) · [Monitor status](../data/api/monitor_status.json)

**Last successful check:** `2026-07-23T14:35:47+00:00`  
**Current API snapshot:** `4508e73271f1c938`  
**Source observation:** `2026-07-22T06:57:20.626603+08:00`  
**New snapshot detected:** yes  
**Models returned:** 11

> “Last successful check” confirms that the automation reached the API. “Source observation” is supplied by the upstream endpoint and may be older.

> This is a model-level summary from the Codex Radar API, not the project's task-level difficulty-weighted score.

## Current API model summary

| Rank | Model tier | Source score | Passed | Tasks | Cost | Total tokens | Wall time |
|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | Sol Xhigh | 96.9 | 72/112 | 112 | $792.66 | 1,080,183,998 | 49.24h |
| 2 | Terra Max | 96.9 | 72/112 | 112 | $518.40 | 1,347,156,285 | 59.18h |
| 3 | Sol Medium | 95.5 | 71/112 | 112 | $431.10 | 549,671,489 | 31.95h |
| 4 | Sol High | 92.8 | 69/112 | 112 | $665.52 | 923,272,181 | 43.38h |
| 5 | Gpt-5.5 Xhigh | 91.5 | 68/112 | 112 | $646.31 | 832,566,389 | 46.76h |
| 6 | Terra Xhigh | 91.5 | 68/112 | 112 | $265.00 | 636,751,705 | 35.31h |
| 7 | Luna Max | 84.7 | 63/112 | 112 | $277.47 | 1,894,451,052 | 62.06h |
| 8 | Gpt-5.5 High | 83.4 | 62/112 | 112 | $430.77 | 545,431,547 | 34.65h |
| 9 | Sol Low | 75.3 | 56/112 | 112 | $231.99 | 267,220,523 | 21.35h |
| 10 | Luna High | 70 | 52/112 | 112 | $113.05 | 714,921,951 | 34.34h |
| 11 | Terra High | 67.3 | 50/112 | 112 | $158.50 | 364,818,574 | 24.51h |

## Interpretation

- The endpoint provides model-level `score`, pass counts, task counts, tokens, wall time, and estimated cost.
- It does not expose the ten task-level outcomes, so `Weighted /100` cannot be recomputed from this API summary alone.
- Task-weighted rankings remain based on the repository's task matrix and weight snapshots; this report monitors the latest API summary.
- When source data is unchanged, the automation still updates its heartbeat without presenting it as a new benchmark batch.
- The raw API response is not stored in the public repository; only required model-summary fields are archived.

Archived API snapshots: **61**.
