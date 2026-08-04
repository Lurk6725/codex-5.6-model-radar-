# Codex Radar API Monitor — English

[简体中文](api-latest.zh-CN.md) · [Project home](../README.md) · [API history CSV](../data/api/model_iq_history.csv) · [Monitor status](../data/api/monitor_status.json)

**Last successful check:** `2026-08-04T12:30:22+00:00`  
**Current API snapshot:** `3a649f34c1bb8ace`  
**Source observation:** `2026-07-22T06:57:20.626603+08:00`  
**New snapshot detected:** yes  
**Models returned:** 11

> “Last successful check” confirms that the automation reached the API. “Source observation” is supplied by the upstream endpoint and may be older.

> This is a model-level summary from the Codex Radar API, not the project's task-level difficulty-weighted score.

## Current API model summary

| Rank | Model tier | Source score | Passed | Tasks | Cost | Total tokens | Wall time |
|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | Sol Xhigh | 107.6 | 80/112 | 112 | $761.30 | 944,294,774 | 47.20h |
| 2 | Gpt-5.5 Xhigh | 100.9 | 75/112 | 112 | $653.10 | 769,217,568 | 41.39h |
| 3 | Luna Max | 99.5 | 74/112 | 112 | $58.81 | 1,698,853,768 | 57.95h |
| 4 | Terra Max | 91.5 | 68/112 | 112 | $459.02 | 1,480,263,459 | 59.17h |
| 5 | Sol Medium | 88.8 | 66/112 | 112 | $410.73 | 535,475,002 | 31.15h |
| 6 | Gpt-5.5 High | 84.7 | 63/112 | 112 | $407.77 | 493,691,511 | 30.67h |
| 7 | Sol High | 84.7 | 63/112 | 112 | $590.03 | 668,768,341 | 38.94h |
| 8 | Terra High | 83.4 | 62/112 | 112 | $139.29 | 352,400,979 | 23.65h |
| 9 | Terra Xhigh | 82.1 | 61/112 | 112 | $231.16 | 605,029,919 | 33.26h |
| 10 | Sol Low | 71.3 | 53/112 | 112 | $231.72 | 241,889,880 | 20.35h |
| 11 | Luna High | 70 | 52/112 | 112 | $27.57 | 745,391,871 | 29.56h |

## Interpretation

- The endpoint provides model-level `score`, pass counts, task counts, tokens, wall time, and estimated cost.
- It does not expose the ten task-level outcomes, so `Weighted /100` cannot be recomputed from this API summary alone.
- Task-weighted rankings remain based on the repository's task matrix and weight snapshots; this report monitors the latest API summary.
- When source data is unchanged, the automation still updates its heartbeat without presenting it as a new benchmark batch.
- The raw API response is not stored in the public repository; only required model-summary fields are archived.

Archived API snapshots: **169**.
