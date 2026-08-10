# Codex Radar API Monitor — English

[简体中文](api-latest.zh-CN.md) · [Project home](../README.md) · [API history CSV](../data/api/model_iq_history.csv) · [Monitor status](../data/api/monitor_status.json)

**Last successful check:** `2026-08-10T08:07:12+00:00`  
**Current API snapshot:** `a8a74c7436422c77`  
**Source observation:** `2026-07-22T06:57:20.626603+08:00`  
**New snapshot detected:** yes  
**Models returned:** 11

> “Last successful check” confirms that the automation reached the API. “Source observation” is supplied by the upstream endpoint and may be older.

> This is a model-level summary from the Codex Radar API, not the project's task-level difficulty-weighted score.

## Current API model summary

| Rank | Model tier | Source score | Passed | Tasks | Cost | Total tokens | Wall time |
|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | Sol Xhigh | 107.6 | 80/112 | 112 | $737.92 | 901,801,883 | 50.53h |
| 2 | Gpt-5.5 Xhigh | 96.9 | 72/112 | 112 | $657.76 | 803,886,878 | 41.09h |
| 3 | Sol High | 96.9 | 72/112 | 112 | $568.19 | 593,729,934 | 37.62h |
| 4 | Terra Max | 96.9 | 72/112 | 112 | $439.42 | 1,120,747,549 | 49.75h |
| 5 | Luna Max | 91.5 | 68/112 | 112 | $58.69 | 1,772,339,299 | 60.43h |
| 6 | Sol Medium | 90.1 | 67/112 | 112 | $410.08 | 460,170,122 | 31.20h |
| 7 | Sol Low | 88.8 | 66/112 | 112 | $230.66 | 274,194,305 | 23.85h |
| 8 | Terra Xhigh | 86.1 | 64/112 | 112 | $220.33 | 566,929,485 | 33.37h |
| 9 | Gpt-5.5 High | 80.7 | 60/112 | 112 | $405.33 | 473,979,794 | 29.03h |
| 10 | Terra High | 72.6 | 54/112 | 112 | $127.06 | 331,846,096 | 22.93h |
| 11 | Luna High | 70 | 52/112 | 112 | $26.23 | 723,082,235 | 33.13h |

## Interpretation

- The endpoint provides model-level `score`, pass counts, task counts, tokens, wall time, and estimated cost.
- It does not expose the ten task-level outcomes, so `Weighted /100` cannot be recomputed from this API summary alone.
- Task-weighted rankings remain based on the repository's task matrix and weight snapshots; this report monitors the latest API summary.
- When source data is unchanged, the automation still updates its heartbeat without presenting it as a new benchmark batch.
- The raw API response is not stored in the public repository; only required model-summary fields are archived.

Archived API snapshots: **225**.
