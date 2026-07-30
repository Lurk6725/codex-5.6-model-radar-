# Codex Radar API Monitor — English

[简体中文](api-latest.zh-CN.md) · [Project home](../README.md) · [API history CSV](../data/api/model_iq_history.csv) · [Monitor status](../data/api/monitor_status.json)

**Last successful check:** `2026-07-30T21:34:32+00:00`  
**Current API snapshot:** `1eed120872c41a72`  
**Source observation:** `2026-07-22T06:57:20.626603+08:00`  
**New snapshot detected:** yes  
**Models returned:** 11

> “Last successful check” confirms that the automation reached the API. “Source observation” is supplied by the upstream endpoint and may be older.

> This is a model-level summary from the Codex Radar API, not the project's task-level difficulty-weighted score.

## Current API model summary

| Rank | Model tier | Source score | Passed | Tasks | Cost | Total tokens | Wall time |
|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | Sol Xhigh | 95.5 | 71/112 | 112 | $743.68 | 983,922,943 | 46.88h |
| 2 | Gpt-5.5 Xhigh | 92.8 | 69/112 | 112 | $654.25 | 834,768,995 | 44.52h |
| 3 | Luna Max | 92.8 | 69/112 | 112 | $264.13 | 1,796,854,845 | 60.54h |
| 4 | Sol High | 91.5 | 68/112 | 112 | $606.19 | 803,840,814 | 41.68h |
| 5 | Gpt-5.5 High | 82.1 | 61/112 | 112 | $429.84 | 536,984,154 | 33.10h |
| 6 | Terra Max | 82.1 | 61/112 | 112 | $571.22 | 1,498,758,361 | 54.91h |
| 7 | Sol Low | 80.7 | 60/112 | 112 | $248.50 | 287,391,239 | 22.50h |
| 8 | Sol Medium | 79.4 | 59/112 | 112 | $426.44 | 530,197,619 | 30.61h |
| 9 | Terra High | 78 | 58/112 | 112 | $165.66 | 375,357,222 | 23.84h |
| 10 | Terra Xhigh | 78 | 58/112 | 112 | $293.90 | 716,275,463 | 33.66h |
| 11 | Luna High | 60.5 | 45/112 | 112 | $123.81 | 816,796,435 | 34.93h |

## Interpretation

- The endpoint provides model-level `score`, pass counts, task counts, tokens, wall time, and estimated cost.
- It does not expose the ten task-level outcomes, so `Weighted /100` cannot be recomputed from this API summary alone.
- Task-weighted rankings remain based on the repository's task matrix and weight snapshots; this report monitors the latest API summary.
- When source data is unchanged, the automation still updates its heartbeat without presenting it as a new benchmark batch.
- The raw API response is not stored in the public repository; only required model-summary fields are archived.

Archived API snapshots: **126**.
