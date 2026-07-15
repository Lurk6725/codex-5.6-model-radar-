# Codex Radar API Monitor — English

[简体中文](api-latest.zh-CN.md) · [Project home](../README.md) · [API history CSV](../data/api/model_iq_history.csv) · [Monitor status](../data/api/monitor_status.json)

**Last successful check:** `2026-07-15T19:58:03+00:00`  
**Current API snapshot:** `16cded5d24c0bda2`  
**Source observation:** `2026-07-13T22:08:07.261261+08:00`  
**New snapshot detected:** no; the source returned the same snapshot  
**Models returned:** 8

> “Last successful check” confirms that the automation reached the API. “Source observation” is supplied by the upstream endpoint and may be older.

> This is a model-level summary from the Codex Radar API, not the project's task-level difficulty-weighted score.

## Current API model summary

| Rank | Model tier | Source score | Passed | Tasks | Cost | Total tokens | Wall time |
|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | Luna Max | 135 | 9/10 | 10 | $16.31 | 90,986,992 | 0.86h |
| 2 | Sol Low | 120 | 8/10 | 10 | $10.73 | 9,859,047 | 0.42h |
| 3 | Sol High | 105 | 7/10 | 10 | $24.99 | 24,760,599 | 0.77h |
| 4 | Sol Xhigh | 105 | 7/10 | 10 | $32.60 | 33,292,820 | 0.91h |
| 5 | Terra Max | 105 | 7/10 | 10 | $34.01 | 73,507,940 | 2.00h |
| 6 | Sol Medium | 90 | 6/10 | 10 | $16.63 | 15,274,427 | 0.69h |
| 7 | Luna High | 75 | 5/10 | 10 | $6.68 | 37,373,527 | 0.65h |
| 8 | Terra High | 75 | 5/10 | 10 | $9.26 | 16,730,290 | 0.43h |

## Interpretation

- The endpoint provides model-level `score`, pass counts, task counts, tokens, wall time, and estimated cost.
- It does not expose the ten task-level outcomes, so `Weighted /100` cannot be recomputed from this API summary alone.
- Task-weighted rankings remain based on the repository's task matrix and weight snapshots; this report monitors the latest API summary.
- When source data is unchanged, the automation still updates its heartbeat without presenting it as a new benchmark batch.
- The raw API response is not stored in the public repository; only required model-summary fields are archived.

Archived API snapshots: **5**.
