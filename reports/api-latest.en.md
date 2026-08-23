# Codex Radar API Monitor — English

[简体中文](api-latest.zh-CN.md) · [Project home](../README.md) · [API history CSV](../data/api/model_iq_history.csv) · [Monitor status](../data/api/monitor_status.json)

**Last successful check:** `2026-08-23T15:40:05+00:00`  
**Current API snapshot:** `0233100df15fd0c6`  
**Source observation:** `2026-07-22T06:57:20.626603+08:00`  
**New snapshot detected:** yes  
**Models returned:** 11

> “Last successful check” confirms that the automation reached the API. “Source observation” is supplied by the upstream endpoint and may be older.

> This is a model-level summary from the Codex Radar API, not the project's task-level difficulty-weighted score.

## Current API model summary

| Rank | Model tier | Source score | Passed | Tasks | Cost | Total tokens | Wall time |
|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | Sol Xhigh | 102.2 | 76/112 | 112 | $722.60 | 843,163,288 | 43.86h |
| 2 | Gpt-5.5 Xhigh | 98.2 | 73/112 | 112 | $651.33 | 781,822,253 | 42.04h |
| 3 | Gpt-5.5 High | 94.2 | 70/112 | 112 | $401.55 | 525,252,593 | 34.22h |
| 4 | Terra Max | 94.2 | 70/112 | 112 | $430.73 | 1,186,355,310 | 56.65h |
| 5 | Terra Xhigh | 87.4 | 65/112 | 112 | $213.69 | 581,309,512 | 37.01h |
| 6 | Luna Max | 86.1 | 64/112 | 112 | $54.40 | 1,700,892,861 | 59.67h |
| 7 | Sol High | 86.1 | 64/112 | 112 | $534.50 | 583,317,228 | 35.73h |
| 8 | Sol Medium | 83.4 | 62/112 | 112 | $404.68 | 458,081,443 | 33.21h |
| 9 | Luna High | 74 | 55/112 | 112 | $22.64 | 688,070,688 | 30.13h |
| 10 | Terra High | 74 | 55/112 | 112 | $124.81 | 335,449,664 | 24.85h |
| 11 | Sol Low | 72.6 | 54/112 | 112 | $223.16 | 262,208,236 | 23.88h |

## Interpretation

- The endpoint provides model-level `score`, pass counts, task counts, tokens, wall time, and estimated cost.
- It does not expose the ten task-level outcomes, so `Weighted /100` cannot be recomputed from this API summary alone.
- Task-weighted rankings remain based on the repository's task matrix and weight snapshots; this report monitors the latest API summary.
- When source data is unchanged, the automation still updates its heartbeat without presenting it as a new benchmark batch.
- The raw API response is not stored in the public repository; only required model-summary fields are archived.

Archived API snapshots: **333**.
