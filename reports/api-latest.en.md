# Codex Radar API Monitor — English

[简体中文](api-latest.zh-CN.md) · [Project home](../README.md) · [API history CSV](../data/api/model_iq_history.csv) · [Monitor status](../data/api/monitor_status.json)

**Last successful check:** `2026-07-30T17:53:34+00:00`  
**Current API snapshot:** `248f8d6b648ce139`  
**Source observation:** `2026-07-22T06:57:20.626603+08:00`  
**New snapshot detected:** yes  
**Models returned:** 11

> “Last successful check” confirms that the automation reached the API. “Source observation” is supplied by the upstream endpoint and may be older.

> This is a model-level summary from the Codex Radar API, not the project's task-level difficulty-weighted score.

## Current API model summary

| Rank | Model tier | Source score | Passed | Tasks | Cost | Total tokens | Wall time |
|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | Sol Xhigh | 96.9 | 72/112 | 112 | $738.17 | 982,062,009 | 45.95h |
| 2 | Gpt-5.5 Xhigh | 95.5 | 71/112 | 112 | $654.48 | 834,195,768 | 44.34h |
| 3 | Sol High | 92.8 | 69/112 | 112 | $609.23 | 809,277,604 | 41.35h |
| 4 | Luna Max | 87.4 | 65/112 | 112 | $264.66 | 1,800,270,680 | 60.34h |
| 5 | Gpt-5.5 High | 83.4 | 62/112 | 112 | $425.75 | 529,267,135 | 32.53h |
| 6 | Sol Medium | 82.1 | 61/112 | 112 | $426.68 | 527,847,498 | 32.11h |
| 7 | Terra Max | 82.1 | 61/112 | 112 | $571.07 | 1,499,787,209 | 55.09h |
| 8 | Sol Low | 80.7 | 60/112 | 112 | $248.86 | 287,971,779 | 22.41h |
| 9 | Terra Xhigh | 78 | 58/112 | 112 | $294.09 | 715,376,049 | 34.25h |
| 10 | Terra High | 74 | 55/112 | 112 | $163.77 | 370,836,641 | 23.64h |
| 11 | Luna High | 63.2 | 47/112 | 112 | $121.81 | 800,143,571 | 34.37h |

## Interpretation

- The endpoint provides model-level `score`, pass counts, task counts, tokens, wall time, and estimated cost.
- It does not expose the ten task-level outcomes, so `Weighted /100` cannot be recomputed from this API summary alone.
- Task-weighted rankings remain based on the repository's task matrix and weight snapshots; this report monitors the latest API summary.
- When source data is unchanged, the automation still updates its heartbeat without presenting it as a new benchmark batch.
- The raw API response is not stored in the public repository; only required model-summary fields are archived.

Archived API snapshots: **124**.
