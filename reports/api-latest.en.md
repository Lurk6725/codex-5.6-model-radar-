# Codex Radar API Monitor — English

[简体中文](api-latest.zh-CN.md) · [Project home](../README.md) · [API history CSV](../data/api/model_iq_history.csv) · [Monitor status](../data/api/monitor_status.json)

**Last successful check:** `2026-08-19T14:54:43+00:00`  
**Current API snapshot:** `612e0f74e1a873dc`  
**Source observation:** `2026-07-22T06:57:20.626603+08:00`  
**New snapshot detected:** yes  
**Models returned:** 11

> “Last successful check” confirms that the automation reached the API. “Source observation” is supplied by the upstream endpoint and may be older.

> This is a model-level summary from the Codex Radar API, not the project's task-level difficulty-weighted score.

## Current API model summary

| Rank | Model tier | Source score | Passed | Tasks | Cost | Total tokens | Wall time |
|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | Terra Max | 99.5 | 74/112 | 112 | $434.66 | 1,251,190,862 | 59.35h |
| 2 | Sol Xhigh | 96.9 | 72/112 | 112 | $726.72 | 853,436,826 | 45.03h |
| 3 | Gpt-5.5 Xhigh | 95.5 | 71/112 | 112 | $653.60 | 776,793,482 | 41.68h |
| 4 | Luna Max | 92.8 | 69/112 | 112 | $55.20 | 1,820,675,445 | 64.76h |
| 5 | Gpt-5.5 High | 91.5 | 68/112 | 112 | $401.59 | 526,289,943 | 34.16h |
| 6 | Sol High | 88.8 | 66/112 | 112 | $535.96 | 636,747,676 | 35.86h |
| 7 | Terra Xhigh | 84.7 | 63/112 | 112 | $214.77 | 591,561,621 | 37.88h |
| 8 | Sol Medium | 83.4 | 62/112 | 112 | $398.37 | 484,446,533 | 34.03h |
| 9 | Terra High | 75.3 | 56/112 | 112 | $124.99 | 346,628,783 | 25.91h |
| 10 | Luna High | 74 | 55/112 | 112 | $23.49 | 758,693,080 | 34.50h |
| 11 | Sol Low | 74 | 55/112 | 112 | $223.93 | 267,746,916 | 24.74h |

## Interpretation

- The endpoint provides model-level `score`, pass counts, task counts, tokens, wall time, and estimated cost.
- It does not expose the ten task-level outcomes, so `Weighted /100` cannot be recomputed from this API summary alone.
- Task-weighted rankings remain based on the repository's task matrix and weight snapshots; this report monitors the latest API summary.
- When source data is unchanged, the automation still updates its heartbeat without presenting it as a new benchmark batch.
- The raw API response is not stored in the public repository; only required model-summary fields are archived.

Archived API snapshots: **297**.
