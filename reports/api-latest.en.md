# Codex Radar API Monitor — English

[简体中文](api-latest.zh-CN.md) · [Project home](../README.md) · [API history CSV](../data/api/model_iq_history.csv) · [Monitor status](../data/api/monitor_status.json)

**Last successful check:** `2026-08-12T09:33:25+00:00`  
**Current API snapshot:** `bc0996485a5ba5b5`  
**Source observation:** `2026-07-22T06:57:20.626603+08:00`  
**New snapshot detected:** yes  
**Models returned:** 11

> “Last successful check” confirms that the automation reached the API. “Source observation” is supplied by the upstream endpoint and may be older.

> This is a model-level summary from the Codex Radar API, not the project's task-level difficulty-weighted score.

## Current API model summary

| Rank | Model tier | Source score | Passed | Tasks | Cost | Total tokens | Wall time |
|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | Sol Xhigh | 104.9 | 78/112 | 112 | $736.92 | 905,867,039 | 48.42h |
| 2 | Terra Max | 103.6 | 77/112 | 112 | $437.35 | 1,212,190,412 | 55.94h |
| 3 | Sol High | 100.9 | 75/112 | 112 | $562.01 | 683,327,263 | 37.84h |
| 4 | Luna Max | 99.5 | 74/112 | 112 | $58.55 | 1,869,883,803 | 67.03h |
| 5 | Sol Medium | 96.9 | 72/112 | 112 | $407.72 | 473,465,440 | 31.34h |
| 6 | Gpt-5.5 Xhigh | 90.1 | 67/112 | 112 | $657.28 | 724,484,838 | 40.07h |
| 7 | Gpt-5.5 High | 88.8 | 66/112 | 112 | $404.18 | 491,615,660 | 32.30h |
| 8 | Terra Xhigh | 84.7 | 63/112 | 112 | $218.28 | 581,213,830 | 35.52h |
| 9 | Terra High | 79.4 | 59/112 | 112 | $126.93 | 348,379,142 | 24.38h |
| 10 | Sol Low | 74 | 55/112 | 112 | $228.88 | 271,523,134 | 22.21h |
| 11 | Luna High | 68.6 | 51/112 | 112 | $26.19 | 764,421,971 | 34.56h |

## Interpretation

- The endpoint provides model-level `score`, pass counts, task counts, tokens, wall time, and estimated cost.
- It does not expose the ten task-level outcomes, so `Weighted /100` cannot be recomputed from this API summary alone.
- Task-weighted rankings remain based on the repository's task matrix and weight snapshots; this report monitors the latest API summary.
- When source data is unchanged, the automation still updates its heartbeat without presenting it as a new benchmark batch.
- The raw API response is not stored in the public repository; only required model-summary fields are archived.

Archived API snapshots: **241**.
