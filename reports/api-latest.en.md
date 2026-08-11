# Codex Radar API Monitor — English

[简体中文](api-latest.zh-CN.md) · [Project home](../README.md) · [API history CSV](../data/api/model_iq_history.csv) · [Monitor status](../data/api/monitor_status.json)

**Last successful check:** `2026-08-11T23:06:01+00:00`  
**Current API snapshot:** `917bd5ee02fa0f1f`  
**Source observation:** `2026-07-22T06:57:20.626603+08:00`  
**New snapshot detected:** no; the source returned the same snapshot  
**Models returned:** 11

> “Last successful check” confirms that the automation reached the API. “Source observation” is supplied by the upstream endpoint and may be older.

> This is a model-level summary from the Codex Radar API, not the project's task-level difficulty-weighted score.

## Current API model summary

| Rank | Model tier | Source score | Passed | Tasks | Cost | Total tokens | Wall time |
|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | Sol Xhigh | 107.6 | 80/112 | 112 | $735.93 | 892,785,647 | 49.75h |
| 2 | Sol High | 103.6 | 77/112 | 112 | $562.68 | 640,990,590 | 37.84h |
| 3 | Luna Max | 100.9 | 75/112 | 112 | $58.63 | 1,822,288,553 | 62.78h |
| 4 | Terra Max | 99.5 | 74/112 | 112 | $437.79 | 1,192,436,773 | 54.09h |
| 5 | Gpt-5.5 High | 95.5 | 71/112 | 112 | $404.14 | 485,075,095 | 32.22h |
| 6 | Gpt-5.5 Xhigh | 88.8 | 66/112 | 112 | $657.01 | 740,440,818 | 40.44h |
| 7 | Sol Medium | 88.8 | 66/112 | 112 | $407.70 | 469,237,031 | 31.40h |
| 8 | Terra Xhigh | 86.1 | 64/112 | 112 | $219.38 | 571,993,515 | 33.88h |
| 9 | Sol Low | 79.4 | 59/112 | 112 | $229.60 | 276,710,385 | 22.87h |
| 10 | Terra High | 79.4 | 59/112 | 112 | $127.22 | 330,588,748 | 23.55h |
| 11 | Luna High | 65.9 | 49/112 | 112 | $26.19 | 769,544,995 | 34.59h |

## Interpretation

- The endpoint provides model-level `score`, pass counts, task counts, tokens, wall time, and estimated cost.
- It does not expose the ten task-level outcomes, so `Weighted /100` cannot be recomputed from this API summary alone.
- Task-weighted rankings remain based on the repository's task matrix and weight snapshots; this report monitors the latest API summary.
- When source data is unchanged, the automation still updates its heartbeat without presenting it as a new benchmark batch.
- The raw API response is not stored in the public repository; only required model-summary fields are archived.

Archived API snapshots: **236**.
