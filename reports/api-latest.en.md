# Codex Radar API Monitor — English

[简体中文](api-latest.zh-CN.md) · [Project home](../README.md) · [API history CSV](../data/api/model_iq_history.csv) · [Monitor status](../data/api/monitor_status.json)

**Last successful check:** `2026-07-14T04:13:25+00:00`  
**Current API snapshot:** `56b5641f66b1a557`  
**Source observation:** `2026-07-13T22:08:07.261261+08:00`  
**New snapshot detected:** no; the source returned the same snapshot  
**Models returned:** 8

> “Last successful check” confirms that the automation reached the API. “Source observation” is supplied by the upstream endpoint and may be older.

> This is a model-level summary from the Codex Radar API, not the project's task-level difficulty-weighted score.

## Current API model summary

| Rank | Model tier | Source score | Passed | Tasks | Cost | Total tokens | Wall time |
|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | Sol High | 135 | 9/10 | 10 | $24.62 | 23,496,190 | 0.54h |
| 2 | Sol Medium | 135 | 9/10 | 10 | $18.41 | 18,483,032 | 0.46h |
| 3 | Sol Low | 120 | 8/10 | 10 | $9.73 | 8,195,968 | 0.27h |
| 4 | Terra Max | 105 | 7/10 | 10 | $30.91 | 65,722,639 | 0.63h |
| 5 | Luna Max | 90 | 6/10 | 10 | $15.11 | 88,731,185 | 0.66h |
| 6 | Sol Xhigh | 90 | 6/10 | 10 | $37.97 | 40,667,099 | 0.75h |
| 7 | Terra Medium | 75 | 5/10 | 10 | $5.18 | 8,014,450 | 0.39h |
| 8 | Luna Medium | 15 | 1/10 | 10 | $2.44 | 10,811,042 | 0.41h |

## Interpretation

- The endpoint provides model-level `score`, pass counts, task counts, tokens, wall time, and estimated cost.
- It does not expose the ten task-level outcomes, so `Weighted /100` cannot be recomputed from this API summary alone.
- Task-weighted rankings remain based on the repository's task matrix and weight snapshots; this report monitors the latest API summary.
- When source data is unchanged, the automation still updates its heartbeat without presenting it as a new benchmark batch.
- The raw API response is not stored in the public repository; only required model-summary fields are archived.

Archived API snapshots: **2**.
