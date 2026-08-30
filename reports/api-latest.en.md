# Codex Radar API Monitor — English

[简体中文](api-latest.zh-CN.md) · [Project home](../README.md) · [API history CSV](../data/api/model_iq_history.csv) · [Monitor status](../data/api/monitor_status.json)

**Last successful check:** `2026-08-30T05:53:50+00:00`  
**Current API snapshot:** `0fec19e69e7672e1`  
**Source observation:** `2026-08-30T13:13:10.383684+08:00`  
**New snapshot detected:** yes  
**Models returned:** 11

> “Last successful check” confirms that the automation reached the API. “Source observation” is supplied by the upstream endpoint and may be older.

> This is a model-level summary from the Codex Radar API, not the project's task-level difficulty-weighted score.

## Current API model summary

| Rank | Model tier | Source score | Passed | Tasks | Cost | Total tokens | Wall time |
|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | Luna Max | 104.9 | 78/112 | 112 | $54.01 | 1,950,350,619 | 70.26h |
| 2 | Terra Max | 103.6 | 77/112 | 112 | $425.47 | 1,202,890,007 | 57.05h |
| 3 | Sol Xhigh | 100.9 | 75/112 | 112 | $621.69 | 811,769,677 | 44.87h |
| 4 | Gpt-5.5 Xhigh | 98.2 | 73/112 | 112 | $641.03 | 858,306,038 | 43.55h |
| 5 | Sol High | 96.9 | 72/112 | 112 | $501.78 | 599,337,100 | 35.85h |
| 6 | Sol Medium | 95.5 | 71/112 | 112 | $312.58 | 418,271,102 | 27.93h |
| 7 | Gpt-5.5 High | 86.1 | 64/112 | 112 | $398.08 | 527,218,318 | 27.97h |
| 8 | Terra Xhigh | 86.1 | 64/112 | 112 | $212.31 | 621,726,740 | 37.87h |
| 9 | Terra High | 82.1 | 61/112 | 112 | $122.89 | 346,874,818 | 26.30h |
| 10 | Sol Low | 79.4 | 59/112 | 112 | $171.64 | 216,098,756 | 16.76h |
| 11 | Luna High | 70 | 52/112 | 112 | $22.49 | 759,013,816 | 34.17h |

## Interpretation

- The endpoint provides model-level `score`, pass counts, task counts, tokens, wall time, and estimated cost.
- It does not expose the ten task-level outcomes, so `Weighted /100` cannot be recomputed from this API summary alone.
- Task-weighted rankings remain based on the repository's task matrix and weight snapshots; this report monitors the latest API summary.
- When source data is unchanged, the automation still updates its heartbeat without presenting it as a new benchmark batch.
- The raw API response is not stored in the public repository; only required model-summary fields are archived.

Archived API snapshots: **379**.
