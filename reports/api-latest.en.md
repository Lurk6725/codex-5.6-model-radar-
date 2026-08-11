# Codex Radar API Monitor — English

[简体中文](api-latest.zh-CN.md) · [Project home](../README.md) · [API history CSV](../data/api/model_iq_history.csv) · [Monitor status](../data/api/monitor_status.json)

**Last successful check:** `2026-08-11T13:45:29+00:00`  
**Current API snapshot:** `e3052189831269ef`  
**Source observation:** `2026-07-22T06:57:20.626603+08:00`  
**New snapshot detected:** yes  
**Models returned:** 11

> “Last successful check” confirms that the automation reached the API. “Source observation” is supplied by the upstream endpoint and may be older.

> This is a model-level summary from the Codex Radar API, not the project's task-level difficulty-weighted score.

## Current API model summary

| Rank | Model tier | Source score | Passed | Tasks | Cost | Total tokens | Wall time |
|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | Sol Xhigh | 106.3 | 79/112 | 112 | $736.40 | 886,169,852 | 49.67h |
| 2 | Sol High | 103.6 | 77/112 | 112 | $565.47 | 638,971,791 | 38.36h |
| 3 | Terra Max | 100.9 | 75/112 | 112 | $438.32 | 1,180,579,291 | 53.42h |
| 4 | Luna Max | 95.5 | 71/112 | 112 | $58.61 | 1,817,779,511 | 63.46h |
| 5 | Sol Medium | 92.8 | 69/112 | 112 | $408.11 | 471,142,426 | 31.72h |
| 6 | Gpt-5.5 High | 91.5 | 68/112 | 112 | $404.03 | 486,945,107 | 32.74h |
| 7 | Gpt-5.5 Xhigh | 84.7 | 63/112 | 112 | $657.08 | 759,629,314 | 40.69h |
| 8 | Terra Xhigh | 83.4 | 62/112 | 112 | $219.59 | 552,277,259 | 32.38h |
| 9 | Sol Low | 79.4 | 59/112 | 112 | $229.67 | 282,114,317 | 22.75h |
| 10 | Terra High | 76.7 | 57/112 | 112 | $127.25 | 324,514,603 | 23.34h |
| 11 | Luna High | 65.9 | 49/112 | 112 | $26.24 | 745,491,511 | 34.78h |

## Interpretation

- The endpoint provides model-level `score`, pass counts, task counts, tokens, wall time, and estimated cost.
- It does not expose the ten task-level outcomes, so `Weighted /100` cannot be recomputed from this API summary alone.
- Task-weighted rankings remain based on the repository's task matrix and weight snapshots; this report monitors the latest API summary.
- When source data is unchanged, the automation still updates its heartbeat without presenting it as a new benchmark batch.
- The raw API response is not stored in the public repository; only required model-summary fields are archived.

Archived API snapshots: **232**.
