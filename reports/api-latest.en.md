# Codex Radar API Monitor — English

[简体中文](api-latest.zh-CN.md) · [Project home](../README.md) · [API history CSV](../data/api/model_iq_history.csv) · [Monitor status](../data/api/monitor_status.json)

**Last successful check:** `2026-07-16T16:45:46+00:00`  
**Current API snapshot:** `c087c15bbef8b19e`  
**Source observation:** `2026-07-13T22:08:07.261261+08:00`  
**New snapshot detected:** no; the source returned the same snapshot  
**Models returned:** 8

> “Last successful check” confirms that the automation reached the API. “Source observation” is supplied by the upstream endpoint and may be older.

> This is a model-level summary from the Codex Radar API, not the project's task-level difficulty-weighted score.

## Current API model summary

| Rank | Model tier | Source score | Passed | Tasks | Cost | Total tokens | Wall time |
|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | Luna Max | 120 | 8/10 | 10 | $14.80 | 82,741,017 | 0.76h |
| 2 | Sol Medium | 120 | 8/10 | 10 | $17.29 | 16,426,651 | 0.57h |
| 3 | Luna High | 105 | 7/10 | 10 | $6.27 | 34,716,077 | 0.64h |
| 4 | Sol High | 105 | 7/10 | 10 | $23.26 | 22,592,202 | 0.98h |
| 5 | Sol Xhigh | 105 | 7/10 | 10 | $35.62 | 39,255,229 | 0.89h |
| 6 | Terra High | 105 | 7/10 | 10 | $10.14 | 19,571,014 | 0.66h |
| 7 | Sol Low | 90 | 6/10 | 10 | $9.38 | 7,273,775 | 0.44h |
| 8 | Terra Max | 90 | 6/10 | 10 | $37.30 | 90,529,600 | 0.93h |

## Interpretation

- The endpoint provides model-level `score`, pass counts, task counts, tokens, wall time, and estimated cost.
- It does not expose the ten task-level outcomes, so `Weighted /100` cannot be recomputed from this API summary alone.
- Task-weighted rankings remain based on the repository's task matrix and weight snapshots; this report monitors the latest API summary.
- When source data is unchanged, the automation still updates its heartbeat without presenting it as a new benchmark batch.
- The raw API response is not stored in the public repository; only required model-summary fields are archived.

Archived API snapshots: **6**.
