# Codex Radar API Monitor — English

[简体中文](api-latest.zh-CN.md) · [Project home](../README.md) · [API history CSV](../data/api/model_iq_history.csv) · [Monitor status](../data/api/monitor_status.json)

**Last successful check:** `2026-07-15T01:02:25+00:00`  
**Current API snapshot:** `156dd40c56c1b3ab`  
**Source observation:** `2026-07-13T22:08:07.261261+08:00`  
**New snapshot detected:** yes  
**Models returned:** 8

> “Last successful check” confirms that the automation reached the API. “Source observation” is supplied by the upstream endpoint and may be older.

> This is a model-level summary from the Codex Radar API, not the project's task-level difficulty-weighted score.

## Current API model summary

| Rank | Model tier | Source score | Passed | Tasks | Cost | Total tokens | Wall time |
|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | Sol Xhigh | 150 | 10/10 | 10 | $34.78 | 37,853,653 | 0.73h |
| 2 | Sol Medium | 135 | 9/10 | 10 | $17.78 | 17,508,917 | 0.51h |
| 3 | Sol High | 120 | 8/10 | 10 | $23.50 | 27,047,460 | 0.79h |
| 4 | Terra Max | 120 | 8/10 | 10 | $28.28 | 58,386,881 | 0.66h |
| 5 | Luna Max | 90 | 6/10 | 10 | $17.10 | 101,431,174 | 0.79h |
| 6 | Sol Low | 90 | 6/10 | 10 | $8.82 | 7,497,736 | 0.31h |
| 7 | Terra High | 90 | 6/10 | 10 | $9.25 | 15,975,263 | 0.37h |
| 8 | Luna High | 75 | 5/10 | 10 | $6.28 | 31,051,103 | 0.57h |

## Interpretation

- The endpoint provides model-level `score`, pass counts, task counts, tokens, wall time, and estimated cost.
- It does not expose the ten task-level outcomes, so `Weighted /100` cannot be recomputed from this API summary alone.
- Task-weighted rankings remain based on the repository's task matrix and weight snapshots; this report monitors the latest API summary.
- When source data is unchanged, the automation still updates its heartbeat without presenting it as a new benchmark batch.
- The raw API response is not stored in the public repository; only required model-summary fields are archived.

Archived API snapshots: **4**.
