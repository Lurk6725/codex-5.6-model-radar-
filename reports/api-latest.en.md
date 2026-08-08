# Codex Radar API Monitor — English

[简体中文](api-latest.zh-CN.md) · [Project home](../README.md) · [API history CSV](../data/api/model_iq_history.csv) · [Monitor status](../data/api/monitor_status.json)

**Last successful check:** `2026-08-08T08:21:47+00:00`  
**Current API snapshot:** `68c6abc895e24c3a`  
**Source observation:** `2026-07-22T06:57:20.626603+08:00`  
**New snapshot detected:** yes  
**Models returned:** 11

> “Last successful check” confirms that the automation reached the API. “Source observation” is supplied by the upstream endpoint and may be older.

> This is a model-level summary from the Codex Radar API, not the project's task-level difficulty-weighted score.

## Current API model summary

| Rank | Model tier | Source score | Passed | Tasks | Cost | Total tokens | Wall time |
|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | Sol Xhigh | 107.6 | 80/112 | 112 | $751.51 | 949,957,021 | 47.72h |
| 2 | Luna Max | 96.9 | 72/112 | 112 | $58.69 | 1,799,371,525 | 62.30h |
| 3 | Gpt-5.5 Xhigh | 92.8 | 69/112 | 112 | $650.46 | 802,620,271 | 41.22h |
| 4 | Sol High | 92.8 | 69/112 | 112 | $583.68 | 626,247,210 | 37.05h |
| 5 | Gpt-5.5 High | 91.5 | 68/112 | 112 | $407.39 | 496,122,631 | 32.27h |
| 6 | Sol Medium | 91.5 | 68/112 | 112 | $410.95 | 545,663,099 | 32.00h |
| 7 | Terra Max | 90.1 | 67/112 | 112 | $456.14 | 1,407,855,857 | 59.48h |
| 8 | Sol Low | 86.1 | 64/112 | 112 | $230.98 | 272,120,562 | 23.29h |
| 9 | Terra Xhigh | 83.4 | 62/112 | 112 | $226.55 | 634,341,576 | 36.34h |
| 10 | Luna High | 80.7 | 60/112 | 112 | $26.08 | 719,213,609 | 31.15h |
| 11 | Terra High | 75.3 | 56/112 | 112 | $129.39 | 352,378,645 | 24.92h |

## Interpretation

- The endpoint provides model-level `score`, pass counts, task counts, tokens, wall time, and estimated cost.
- It does not expose the ten task-level outcomes, so `Weighted /100` cannot be recomputed from this API summary alone.
- Task-weighted rankings remain based on the repository's task matrix and weight snapshots; this report monitors the latest API summary.
- When source data is unchanged, the automation still updates its heartbeat without presenting it as a new benchmark batch.
- The raw API response is not stored in the public repository; only required model-summary fields are archived.

Archived API snapshots: **201**.
