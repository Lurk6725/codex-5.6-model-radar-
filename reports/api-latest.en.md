# Codex Radar API Monitor — English

[简体中文](api-latest.zh-CN.md) · [Project home](../README.md) · [API history CSV](../data/api/model_iq_history.csv) · [Monitor status](../data/api/monitor_status.json)

**Last successful check:** `2026-08-07T16:10:48+00:00`  
**Current API snapshot:** `d2a63420468d366d`  
**Source observation:** `2026-07-22T06:57:20.626603+08:00`  
**New snapshot detected:** yes  
**Models returned:** 11

> “Last successful check” confirms that the automation reached the API. “Source observation” is supplied by the upstream endpoint and may be older.

> This is a model-level summary from the Codex Radar API, not the project's task-level difficulty-weighted score.

## Current API model summary

| Rank | Model tier | Source score | Passed | Tasks | Cost | Total tokens | Wall time |
|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | Sol Xhigh | 106.3 | 79/112 | 112 | $755.64 | 961,336,862 | 48.23h |
| 2 | Gpt-5.5 High | 95.5 | 71/112 | 112 | $407.82 | 496,746,988 | 33.26h |
| 3 | Luna Max | 95.5 | 71/112 | 112 | $58.71 | 1,819,365,033 | 63.08h |
| 4 | Gpt-5.5 Xhigh | 94.2 | 70/112 | 112 | $648.86 | 811,688,896 | 41.93h |
| 5 | Sol High | 92.8 | 69/112 | 112 | $583.43 | 670,665,804 | 39.06h |
| 6 | Terra Max | 92.8 | 69/112 | 112 | $454.58 | 1,496,838,765 | 62.11h |
| 7 | Sol Medium | 91.5 | 68/112 | 112 | $409.37 | 536,437,209 | 32.00h |
| 8 | Terra Xhigh | 83.4 | 62/112 | 112 | $227.21 | 637,337,355 | 36.41h |
| 9 | Luna High | 82.1 | 61/112 | 112 | $26.75 | 743,060,188 | 31.37h |
| 10 | Sol Low | 82.1 | 61/112 | 112 | $231.41 | 263,652,728 | 22.94h |
| 11 | Terra High | 79.4 | 59/112 | 112 | $130.35 | 351,109,164 | 24.90h |

## Interpretation

- The endpoint provides model-level `score`, pass counts, task counts, tokens, wall time, and estimated cost.
- It does not expose the ten task-level outcomes, so `Weighted /100` cannot be recomputed from this API summary alone.
- Task-weighted rankings remain based on the repository's task matrix and weight snapshots; this report monitors the latest API summary.
- When source data is unchanged, the automation still updates its heartbeat without presenting it as a new benchmark batch.
- The raw API response is not stored in the public repository; only required model-summary fields are archived.

Archived API snapshots: **193**.
