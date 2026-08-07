# Codex Radar API Monitor — English

[简体中文](api-latest.zh-CN.md) · [Project home](../README.md) · [API history CSV](../data/api/model_iq_history.csv) · [Monitor status](../data/api/monitor_status.json)

**Last successful check:** `2026-08-07T00:33:00+00:00`  
**Current API snapshot:** `3ded1ce90a0325eb`  
**Source observation:** `2026-07-22T06:57:20.626603+08:00`  
**New snapshot detected:** yes  
**Models returned:** 11

> “Last successful check” confirms that the automation reached the API. “Source observation” is supplied by the upstream endpoint and may be older.

> This is a model-level summary from the Codex Radar API, not the project's task-level difficulty-weighted score.

## Current API model summary

| Rank | Model tier | Source score | Passed | Tasks | Cost | Total tokens | Wall time |
|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | Sol Xhigh | 106.3 | 79/112 | 112 | $755.58 | 970,637,716 | 48.17h |
| 2 | Gpt-5.5 High | 96.9 | 72/112 | 112 | $407.55 | 506,921,755 | 32.88h |
| 3 | Sol Medium | 96.9 | 72/112 | 112 | $410.26 | 533,184,268 | 31.84h |
| 4 | Terra Max | 95.5 | 71/112 | 112 | $453.96 | 1,483,210,899 | 61.90h |
| 5 | Gpt-5.5 Xhigh | 94.2 | 70/112 | 112 | $647.97 | 811,925,408 | 41.77h |
| 6 | Luna Max | 90.1 | 67/112 | 112 | $58.71 | 1,767,507,424 | 60.76h |
| 7 | Sol High | 87.4 | 65/112 | 112 | $583.50 | 680,077,013 | 39.63h |
| 8 | Terra Xhigh | 86.1 | 64/112 | 112 | $226.50 | 629,390,956 | 36.57h |
| 9 | Luna High | 80.7 | 60/112 | 112 | $26.85 | 730,157,373 | 31.38h |
| 10 | Sol Low | 78 | 58/112 | 112 | $232.06 | 258,604,843 | 22.34h |
| 11 | Terra High | 78 | 58/112 | 112 | $131.04 | 343,704,720 | 24.59h |

## Interpretation

- The endpoint provides model-level `score`, pass counts, task counts, tokens, wall time, and estimated cost.
- It does not expose the ten task-level outcomes, so `Weighted /100` cannot be recomputed from this API summary alone.
- Task-weighted rankings remain based on the repository's task matrix and weight snapshots; this report monitors the latest API summary.
- When source data is unchanged, the automation still updates its heartbeat without presenting it as a new benchmark batch.
- The raw API response is not stored in the public repository; only required model-summary fields are archived.

Archived API snapshots: **186**.
