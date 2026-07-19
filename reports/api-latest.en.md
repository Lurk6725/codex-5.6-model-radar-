# Codex Radar API Monitor — English

[简体中文](api-latest.zh-CN.md) · [Project home](../README.md) · [API history CSV](../data/api/model_iq_history.csv) · [Monitor status](../data/api/monitor_status.json)

**Last successful check:** `2026-07-19T17:43:42+00:00`  
**Current API snapshot:** `72ba0455772fae5a`  
**Source observation:** `2026-07-18T11:35:05.153982+08:00`  
**New snapshot detected:** yes  
**Models returned:** 11

> “Last successful check” confirms that the automation reached the API. “Source observation” is supplied by the upstream endpoint and may be older.

> This is a model-level summary from the Codex Radar API, not the project's task-level difficulty-weighted score.

## Current API model summary

| Rank | Model tier | Source score | Passed | Tasks | Cost | Total tokens | Wall time |
|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | Sol High | 98.2 | 73/112 | 112 | $600.93 | 774,153,726 | 43.99h |
| 2 | Terra Max | 98.2 | 73/112 | 112 | $515.42 | 1,334,483,734 | 60.74h |
| 3 | Sol Xhigh | 95 | 70/111 | 111 | $750.78 | 1,016,284,008 | 52.80h |
| 4 | Gpt-5.5 Xhigh | 91.5 | 68/112 | 112 | $649.63 | 829,801,342 | 41.66h |
| 5 | Sol Medium | 88.8 | 66/112 | 112 | $390.44 | 496,126,909 | 34.27h |
| 6 | Luna Max | 87.4 | 65/112 | 112 | $279.23 | 1,915,502,705 | 69.15h |
| 7 | Gpt-5.5 High | 83.4 | 62/112 | 112 | $413.51 | 524,064,170 | 30.94h |
| 8 | Sol Low | 81.4 | 60/111 | 111 | $223.64 | 262,964,004 | 22.60h |
| 9 | Terra Xhigh | 78 | 58/112 | 112 | $258.14 | 612,247,972 | 33.04h |
| 10 | Terra High | 67.3 | 50/112 | 112 | $146.06 | 326,128,420 | 23.39h |
| 11 | Luna High | 64.6 | 48/112 | 112 | $119.94 | 778,902,100 | 34.27h |

## Interpretation

- The endpoint provides model-level `score`, pass counts, task counts, tokens, wall time, and estimated cost.
- It does not expose the ten task-level outcomes, so `Weighted /100` cannot be recomputed from this API summary alone.
- Task-weighted rankings remain based on the repository's task matrix and weight snapshots; this report monitors the latest API summary.
- When source data is unchanged, the automation still updates its heartbeat without presenting it as a new benchmark batch.
- The raw API response is not stored in the public repository; only required model-summary fields are archived.

Archived API snapshots: **32**.
