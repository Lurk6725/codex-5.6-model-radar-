# Codex Radar API Monitor — English

[简体中文](api-latest.zh-CN.md) · [Project home](../README.md) · [API history CSV](../data/api/model_iq_history.csv) · [Monitor status](../data/api/monitor_status.json)

**Last successful check:** `2026-08-08T05:10:42+00:00`  
**Current API snapshot:** `60f1aeace97e00d6`  
**Source observation:** `2026-07-22T06:57:20.626603+08:00`  
**New snapshot detected:** no; the source returned the same snapshot  
**Models returned:** 11

> “Last successful check” confirms that the automation reached the API. “Source observation” is supplied by the upstream endpoint and may be older.

> This is a model-level summary from the Codex Radar API, not the project's task-level difficulty-weighted score.

## Current API model summary

| Rank | Model tier | Source score | Passed | Tasks | Cost | Total tokens | Wall time |
|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | Sol Xhigh | 107.6 | 80/112 | 112 | $755.51 | 955,498,497 | 47.78h |
| 2 | Luna Max | 96.9 | 72/112 | 112 | $58.70 | 1,819,246,456 | 63.03h |
| 3 | Gpt-5.5 High | 92.8 | 69/112 | 112 | $407.64 | 493,870,782 | 33.10h |
| 4 | Gpt-5.5 Xhigh | 92.8 | 69/112 | 112 | $648.64 | 807,228,788 | 41.57h |
| 5 | Sol Medium | 92.8 | 69/112 | 112 | $410.45 | 549,187,965 | 32.39h |
| 6 | Sol High | 91.5 | 68/112 | 112 | $583.15 | 645,338,943 | 38.22h |
| 7 | Terra Max | 88.8 | 66/112 | 112 | $456.08 | 1,407,557,031 | 59.52h |
| 8 | Sol Low | 84.7 | 63/112 | 112 | $231.33 | 271,573,831 | 23.40h |
| 9 | Terra Xhigh | 83.4 | 62/112 | 112 | $227.82 | 640,437,210 | 36.48h |
| 10 | Luna High | 79.4 | 59/112 | 112 | $26.10 | 739,056,992 | 31.71h |
| 11 | Terra High | 78 | 58/112 | 112 | $129.41 | 352,709,901 | 25.00h |

## Interpretation

- The endpoint provides model-level `score`, pass counts, task counts, tokens, wall time, and estimated cost.
- It does not expose the ten task-level outcomes, so `Weighted /100` cannot be recomputed from this API summary alone.
- Task-weighted rankings remain based on the repository's task matrix and weight snapshots; this report monitors the latest API summary.
- When source data is unchanged, the automation still updates its heartbeat without presenting it as a new benchmark batch.
- The raw API response is not stored in the public repository; only required model-summary fields are archived.

Archived API snapshots: **199**.
