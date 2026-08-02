# Codex Radar API Monitor — English

[简体中文](api-latest.zh-CN.md) · [Project home](../README.md) · [API history CSV](../data/api/model_iq_history.csv) · [Monitor status](../data/api/monitor_status.json)

**Last successful check:** `2026-08-02T12:16:40+00:00`  
**Current API snapshot:** `7efc230085f4e58c`  
**Source observation:** `2026-07-22T06:57:20.626603+08:00`  
**New snapshot detected:** yes  
**Models returned:** 11

> “Last successful check” confirms that the automation reached the API. “Source observation” is supplied by the upstream endpoint and may be older.

> This is a model-level summary from the Codex Radar API, not the project's task-level difficulty-weighted score.

## Current API model summary

| Rank | Model tier | Source score | Passed | Tasks | Cost | Total tokens | Wall time |
|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | Gpt-5.5 Xhigh | 96.9 | 72/112 | 112 | $653.20 | 828,856,353 | 44.04h |
| 2 | Sol Xhigh | 96.9 | 72/112 | 112 | $773.44 | 969,680,143 | 47.39h |
| 3 | Terra Max | 92.8 | 69/112 | 112 | $518.69 | 1,523,523,562 | 58.38h |
| 4 | Luna Max | 88.8 | 66/112 | 112 | $66.16 | 1,740,320,911 | 59.94h |
| 5 | Sol Medium | 88.8 | 66/112 | 112 | $421.21 | 554,236,333 | 33.00h |
| 6 | Sol High | 84.7 | 63/112 | 112 | $599.83 | 767,569,080 | 42.54h |
| 7 | Gpt-5.5 High | 79.4 | 59/112 | 112 | $412.52 | 501,277,146 | 31.38h |
| 8 | Terra Xhigh | 79.4 | 59/112 | 112 | $268.51 | 700,710,452 | 34.66h |
| 9 | Terra High | 74 | 55/112 | 112 | $148.31 | 396,631,140 | 26.01h |
| 10 | Luna High | 71.3 | 53/112 | 112 | $63.01 | 780,906,104 | 32.56h |
| 11 | Sol Low | 71.3 | 53/112 | 112 | $245.74 | 287,791,678 | 21.80h |

## Interpretation

- The endpoint provides model-level `score`, pass counts, task counts, tokens, wall time, and estimated cost.
- It does not expose the ten task-level outcomes, so `Weighted /100` cannot be recomputed from this API summary alone.
- Task-weighted rankings remain based on the repository's task matrix and weight snapshots; this report monitors the latest API summary.
- When source data is unchanged, the automation still updates its heartbeat without presenting it as a new benchmark batch.
- The raw API response is not stored in the public repository; only required model-summary fields are archived.

Archived API snapshots: **154**.
