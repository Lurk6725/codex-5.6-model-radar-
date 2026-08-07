# Codex Radar API Monitor — English

[简体中文](api-latest.zh-CN.md) · [Project home](../README.md) · [API history CSV](../data/api/model_iq_history.csv) · [Monitor status](../data/api/monitor_status.json)

**Last successful check:** `2026-08-07T03:40:16+00:00`  
**Current API snapshot:** `18026ee0481bbfc2`  
**Source observation:** `2026-07-22T06:57:20.626603+08:00`  
**New snapshot detected:** yes  
**Models returned:** 11

> “Last successful check” confirms that the automation reached the API. “Source observation” is supplied by the upstream endpoint and may be older.

> This is a model-level summary from the Codex Radar API, not the project's task-level difficulty-weighted score.

## Current API model summary

| Rank | Model tier | Source score | Passed | Tasks | Cost | Total tokens | Wall time |
|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | Sol Xhigh | 104.9 | 78/112 | 112 | $755.58 | 968,932,925 | 48.01h |
| 2 | Gpt-5.5 High | 96.9 | 72/112 | 112 | $407.55 | 506,921,755 | 32.88h |
| 3 | Sol Medium | 95.5 | 71/112 | 112 | $410.34 | 531,239,823 | 31.81h |
| 4 | Terra Max | 95.5 | 71/112 | 112 | $453.94 | 1,483,721,236 | 61.97h |
| 5 | Gpt-5.5 Xhigh | 94.2 | 70/112 | 112 | $647.80 | 812,555,013 | 41.77h |
| 6 | Luna Max | 90.1 | 67/112 | 112 | $58.74 | 1,777,326,232 | 61.13h |
| 7 | Sol High | 87.4 | 65/112 | 112 | $583.50 | 680,077,013 | 39.63h |
| 8 | Terra Xhigh | 86.1 | 64/112 | 112 | $226.51 | 629,931,643 | 36.55h |
| 9 | Luna High | 80.7 | 60/112 | 112 | $26.84 | 730,652,900 | 31.43h |
| 10 | Sol Low | 78 | 58/112 | 112 | $232.02 | 258,634,860 | 22.39h |
| 11 | Terra High | 78 | 58/112 | 112 | $131.04 | 343,704,720 | 24.59h |

## Interpretation

- The endpoint provides model-level `score`, pass counts, task counts, tokens, wall time, and estimated cost.
- It does not expose the ten task-level outcomes, so `Weighted /100` cannot be recomputed from this API summary alone.
- Task-weighted rankings remain based on the repository's task matrix and weight snapshots; this report monitors the latest API summary.
- When source data is unchanged, the automation still updates its heartbeat without presenting it as a new benchmark batch.
- The raw API response is not stored in the public repository; only required model-summary fields are archived.

Archived API snapshots: **187**.
