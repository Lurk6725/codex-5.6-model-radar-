# Codex Radar API Monitor — English

[简体中文](api-latest.zh-CN.md) · [Project home](../README.md) · [API history CSV](../data/api/model_iq_history.csv) · [Monitor status](../data/api/monitor_status.json)

**Last successful check:** `2026-07-22T18:50:05+00:00`  
**Current API snapshot:** `d2593cc7804055e3`  
**Source observation:** `2026-07-22T06:57:20.626603+08:00`  
**New snapshot detected:** yes  
**Models returned:** 11

> “Last successful check” confirms that the automation reached the API. “Source observation” is supplied by the upstream endpoint and may be older.

> This is a model-level summary from the Codex Radar API, not the project's task-level difficulty-weighted score.

## Current API model summary

| Rank | Model tier | Source score | Passed | Tasks | Cost | Total tokens | Wall time |
|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | Terra Max | 100.9 | 75/112 | 112 | $508.14 | 1,305,129,337 | 61.25h |
| 2 | Gpt-5.5 Xhigh | 95.5 | 71/112 | 112 | $654.51 | 843,857,742 | 46.59h |
| 3 | Luna Max | 94.2 | 70/112 | 112 | $285.10 | 1,967,205,983 | 65.50h |
| 4 | Sol Xhigh | 94.2 | 70/112 | 112 | $737.49 | 975,005,830 | 48.78h |
| 5 | Terra Xhigh | 92.8 | 69/112 | 112 | $271.91 | 655,503,029 | 37.05h |
| 6 | Sol High | 91.5 | 68/112 | 112 | $598.98 | 795,933,987 | 43.92h |
| 7 | Sol Medium | 91.5 | 68/112 | 112 | $417.48 | 532,142,342 | 32.39h |
| 8 | Gpt-5.5 High | 86.1 | 64/112 | 112 | $411.47 | 514,566,814 | 32.37h |
| 9 | Sol Low | 78 | 58/112 | 112 | $237.95 | 276,333,851 | 22.71h |
| 10 | Luna High | 68.6 | 51/112 | 112 | $112.30 | 709,647,097 | 34.40h |
| 11 | Terra High | 67.3 | 50/112 | 112 | $148.10 | 332,872,358 | 24.66h |

## Interpretation

- The endpoint provides model-level `score`, pass counts, task counts, tokens, wall time, and estimated cost.
- It does not expose the ten task-level outcomes, so `Weighted /100` cannot be recomputed from this API summary alone.
- Task-weighted rankings remain based on the repository's task matrix and weight snapshots; this report monitors the latest API summary.
- When source data is unchanged, the automation still updates its heartbeat without presenting it as a new benchmark batch.
- The raw API response is not stored in the public repository; only required model-summary fields are archived.

Archived API snapshots: **53**.
