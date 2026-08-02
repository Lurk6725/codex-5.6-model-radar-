# Codex Radar API Monitor — English

[简体中文](api-latest.zh-CN.md) · [Project home](../README.md) · [API history CSV](../data/api/model_iq_history.csv) · [Monitor status](../data/api/monitor_status.json)

**Last successful check:** `2026-08-02T09:24:46+00:00`  
**Current API snapshot:** `f69146c1612fae0f`  
**Source observation:** `2026-07-22T06:57:20.626603+08:00`  
**New snapshot detected:** yes  
**Models returned:** 11

> “Last successful check” confirms that the automation reached the API. “Source observation” is supplied by the upstream endpoint and may be older.

> This is a model-level summary from the Codex Radar API, not the project's task-level difficulty-weighted score.

## Current API model summary

| Rank | Model tier | Source score | Passed | Tasks | Cost | Total tokens | Wall time |
|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | Sol Xhigh | 99.5 | 74/112 | 112 | $771.80 | 980,560,538 | 47.26h |
| 2 | Gpt-5.5 Xhigh | 95.5 | 71/112 | 112 | $652.09 | 832,613,363 | 44.02h |
| 3 | Terra Max | 90.1 | 67/112 | 112 | $525.33 | 1,526,665,107 | 57.79h |
| 4 | Sol Medium | 88.8 | 66/112 | 112 | $420.82 | 570,743,040 | 33.40h |
| 5 | Sol High | 87.4 | 65/112 | 112 | $601.92 | 778,994,525 | 41.80h |
| 6 | Luna Max | 86.1 | 64/112 | 112 | $100.56 | 1,802,437,285 | 59.20h |
| 7 | Gpt-5.5 High | 78 | 58/112 | 112 | $415.66 | 517,232,141 | 31.96h |
| 8 | Terra Xhigh | 74 | 55/112 | 112 | $268.79 | 725,231,760 | 35.15h |
| 9 | Luna High | 72.6 | 54/112 | 112 | $65.32 | 798,902,056 | 33.72h |
| 10 | Sol Low | 71.3 | 53/112 | 112 | $248.25 | 286,088,794 | 21.14h |
| 11 | Terra High | 71.3 | 53/112 | 112 | $149.17 | 397,413,546 | 25.95h |

## Interpretation

- The endpoint provides model-level `score`, pass counts, task counts, tokens, wall time, and estimated cost.
- It does not expose the ten task-level outcomes, so `Weighted /100` cannot be recomputed from this API summary alone.
- Task-weighted rankings remain based on the repository's task matrix and weight snapshots; this report monitors the latest API summary.
- When source data is unchanged, the automation still updates its heartbeat without presenting it as a new benchmark batch.
- The raw API response is not stored in the public repository; only required model-summary fields are archived.

Archived API snapshots: **152**.
