# Codex Radar API Monitor — English

[简体中文](api-latest.zh-CN.md) · [Project home](../README.md) · [API history CSV](../data/api/model_iq_history.csv) · [Monitor status](../data/api/monitor_status.json)

**Last successful check:** `2026-08-10T14:07:36+00:00`  
**Current API snapshot:** `4ff6bd806dfdc800`  
**Source observation:** `2026-07-22T06:57:20.626603+08:00`  
**New snapshot detected:** yes  
**Models returned:** 11

> “Last successful check” confirms that the automation reached the API. “Source observation” is supplied by the upstream endpoint and may be older.

> This is a model-level summary from the Codex Radar API, not the project's task-level difficulty-weighted score.

## Current API model summary

| Rank | Model tier | Source score | Passed | Tasks | Cost | Total tokens | Wall time |
|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | Sol Xhigh | 104.9 | 78/112 | 112 | $737.96 | 893,138,225 | 50.85h |
| 2 | Gpt-5.5 Xhigh | 99.5 | 74/112 | 112 | $657.16 | 815,394,316 | 41.92h |
| 3 | Sol High | 99.5 | 74/112 | 112 | $567.92 | 618,305,017 | 39.79h |
| 4 | Terra Max | 98.2 | 73/112 | 112 | $439.08 | 1,205,741,875 | 53.48h |
| 5 | Luna Max | 90.1 | 67/112 | 112 | $58.69 | 1,814,867,001 | 61.13h |
| 6 | Sol Medium | 90.1 | 67/112 | 112 | $410.11 | 461,562,961 | 31.58h |
| 7 | Gpt-5.5 High | 86.1 | 64/112 | 112 | $405.13 | 471,219,108 | 28.75h |
| 8 | Sol Low | 84.7 | 63/112 | 112 | $230.58 | 272,761,924 | 22.85h |
| 9 | Terra Xhigh | 84.7 | 63/112 | 112 | $220.06 | 569,748,185 | 32.82h |
| 10 | Luna High | 74 | 55/112 | 112 | $26.22 | 726,132,017 | 33.56h |
| 11 | Terra High | 72.6 | 54/112 | 112 | $126.96 | 335,643,058 | 23.17h |

## Interpretation

- The endpoint provides model-level `score`, pass counts, task counts, tokens, wall time, and estimated cost.
- It does not expose the ten task-level outcomes, so `Weighted /100` cannot be recomputed from this API summary alone.
- Task-weighted rankings remain based on the repository's task matrix and weight snapshots; this report monitors the latest API summary.
- When source data is unchanged, the automation still updates its heartbeat without presenting it as a new benchmark batch.
- The raw API response is not stored in the public repository; only required model-summary fields are archived.

Archived API snapshots: **228**.
