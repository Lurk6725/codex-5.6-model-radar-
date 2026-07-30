# Codex Radar API Monitor — English

[简体中文](api-latest.zh-CN.md) · [Project home](../README.md) · [API history CSV](../data/api/model_iq_history.csv) · [Monitor status](../data/api/monitor_status.json)

**Last successful check:** `2026-07-30T10:05:35+00:00`  
**Current API snapshot:** `727f4f80b0a4196b`  
**Source observation:** `2026-07-22T06:57:20.626603+08:00`  
**New snapshot detected:** yes  
**Models returned:** 11

> “Last successful check” confirms that the automation reached the API. “Source observation” is supplied by the upstream endpoint and may be older.

> This is a model-level summary from the Codex Radar API, not the project's task-level difficulty-weighted score.

## Current API model summary

| Rank | Model tier | Source score | Passed | Tasks | Cost | Total tokens | Wall time |
|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | Sol Xhigh | 95.5 | 71/112 | 112 | $734.02 | 970,291,725 | 45.60h |
| 2 | Gpt-5.5 Xhigh | 92.8 | 69/112 | 112 | $654.30 | 837,048,236 | 44.20h |
| 3 | Sol High | 91.5 | 68/112 | 112 | $591.98 | 777,795,043 | 41.93h |
| 4 | Terra Max | 88.8 | 66/112 | 112 | $554.51 | 1,452,928,407 | 55.49h |
| 5 | Gpt-5.5 High | 86.1 | 64/112 | 112 | $432.92 | 537,261,882 | 30.99h |
| 6 | Terra Xhigh | 86.1 | 64/112 | 112 | $276.37 | 663,445,914 | 34.80h |
| 7 | Sol Medium | 83.4 | 62/112 | 112 | $418.79 | 518,011,104 | 31.09h |
| 8 | Luna Max | 82.1 | 61/112 | 112 | $279.90 | 1,911,012,866 | 63.17h |
| 9 | Sol Low | 78 | 58/112 | 112 | $250.58 | 290,833,850 | 22.25h |
| 10 | Terra High | 72.6 | 54/112 | 112 | $160.52 | 363,717,084 | 22.79h |
| 11 | Luna High | 61.9 | 46/112 | 112 | $124.78 | 827,123,891 | 34.43h |

## Interpretation

- The endpoint provides model-level `score`, pass counts, task counts, tokens, wall time, and estimated cost.
- It does not expose the ten task-level outcomes, so `Weighted /100` cannot be recomputed from this API summary alone.
- Task-weighted rankings remain based on the repository's task matrix and weight snapshots; this report monitors the latest API summary.
- When source data is unchanged, the automation still updates its heartbeat without presenting it as a new benchmark batch.
- The raw API response is not stored in the public repository; only required model-summary fields are archived.

Archived API snapshots: **120**.
