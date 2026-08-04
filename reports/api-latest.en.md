# Codex Radar API Monitor — English

[简体中文](api-latest.zh-CN.md) · [Project home](../README.md) · [API history CSV](../data/api/model_iq_history.csv) · [Monitor status](../data/api/monitor_status.json)

**Last successful check:** `2026-08-04T10:20:06+00:00`  
**Current API snapshot:** `e0580d0b68160918`  
**Source observation:** `2026-07-22T06:57:20.626603+08:00`  
**New snapshot detected:** yes  
**Models returned:** 11

> “Last successful check” confirms that the automation reached the API. “Source observation” is supplied by the upstream endpoint and may be older.

> This is a model-level summary from the Codex Radar API, not the project's task-level difficulty-weighted score.

## Current API model summary

| Rank | Model tier | Source score | Passed | Tasks | Cost | Total tokens | Wall time |
|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | Sol Xhigh | 109 | 81/112 | 112 | $761.36 | 940,352,658 | 47.26h |
| 2 | Luna Max | 99.5 | 74/112 | 112 | $58.81 | 1,698,853,768 | 57.95h |
| 3 | Gpt-5.5 Xhigh | 98.2 | 73/112 | 112 | $655.49 | 768,066,251 | 41.21h |
| 4 | Sol Medium | 91.5 | 68/112 | 112 | $411.08 | 535,712,535 | 30.85h |
| 5 | Terra Max | 91.5 | 68/112 | 112 | $459.19 | 1,479,623,593 | 59.13h |
| 6 | Gpt-5.5 High | 84.7 | 63/112 | 112 | $407.76 | 490,149,493 | 30.38h |
| 7 | Terra Xhigh | 83.4 | 62/112 | 112 | $231.17 | 606,712,770 | 33.23h |
| 8 | Sol High | 82.1 | 61/112 | 112 | $590.06 | 668,653,265 | 38.91h |
| 9 | Terra High | 80.7 | 60/112 | 112 | $139.90 | 358,109,558 | 23.58h |
| 10 | Sol Low | 72.6 | 54/112 | 112 | $230.00 | 239,752,251 | 20.26h |
| 11 | Luna High | 71.3 | 53/112 | 112 | $34.76 | 740,136,501 | 29.69h |

## Interpretation

- The endpoint provides model-level `score`, pass counts, task counts, tokens, wall time, and estimated cost.
- It does not expose the ten task-level outcomes, so `Weighted /100` cannot be recomputed from this API summary alone.
- Task-weighted rankings remain based on the repository's task matrix and weight snapshots; this report monitors the latest API summary.
- When source data is unchanged, the automation still updates its heartbeat without presenting it as a new benchmark batch.
- The raw API response is not stored in the public repository; only required model-summary fields are archived.

Archived API snapshots: **168**.
