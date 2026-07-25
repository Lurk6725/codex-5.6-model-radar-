# Codex Radar API Monitor — English

[简体中文](api-latest.zh-CN.md) · [Project home](../README.md) · [API history CSV](../data/api/model_iq_history.csv) · [Monitor status](../data/api/monitor_status.json)

**Last successful check:** `2026-07-25T15:49:01+00:00`  
**Current API snapshot:** `784f2814704e2537`  
**Source observation:** `2026-07-22T06:57:20.626603+08:00`  
**New snapshot detected:** yes  
**Models returned:** 11

> “Last successful check” confirms that the automation reached the API. “Source observation” is supplied by the upstream endpoint and may be older.

> This is a model-level summary from the Codex Radar API, not the project's task-level difficulty-weighted score.

## Current API model summary

| Rank | Model tier | Source score | Passed | Tasks | Cost | Total tokens | Wall time |
|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | Sol Xhigh | 99.5 | 74/112 | 112 | $774.53 | 1,050,873,274 | 46.49h |
| 2 | Sol Medium | 95.5 | 71/112 | 112 | $438.53 | 562,425,926 | 30.44h |
| 3 | Sol High | 92.8 | 69/112 | 112 | $576.79 | 763,444,137 | 34.97h |
| 4 | Terra Max | 90.1 | 67/112 | 112 | $568.04 | 1,496,296,086 | 58.84h |
| 5 | Terra Xhigh | 90.1 | 67/112 | 112 | $282.08 | 684,534,756 | 37.22h |
| 6 | Luna Max | 84.7 | 63/112 | 112 | $284.71 | 1,961,948,649 | 60.91h |
| 7 | Gpt-5.5 Xhigh | 82.1 | 61/112 | 112 | $651.56 | 839,003,056 | 44.98h |
| 8 | Gpt-5.5 High | 79.4 | 59/112 | 112 | $421.44 | 526,421,474 | 32.41h |
| 9 | Sol Low | 78 | 58/112 | 112 | $232.87 | 267,672,112 | 20.62h |
| 10 | Terra High | 72.6 | 54/112 | 112 | $157.44 | 358,453,840 | 23.19h |
| 11 | Luna High | 67.3 | 50/112 | 112 | $114.11 | 734,806,940 | 32.34h |

## Interpretation

- The endpoint provides model-level `score`, pass counts, task counts, tokens, wall time, and estimated cost.
- It does not expose the ten task-level outcomes, so `Weighted /100` cannot be recomputed from this API summary alone.
- Task-weighted rankings remain based on the repository's task matrix and weight snapshots; this report monitors the latest API summary.
- When source data is unchanged, the automation still updates its heartbeat without presenting it as a new benchmark batch.
- The raw API response is not stored in the public repository; only required model-summary fields are archived.

Archived API snapshots: **81**.
