# Codex Radar API Monitor — English

[简体中文](api-latest.zh-CN.md) · [Project home](../README.md) · [API history CSV](../data/api/model_iq_history.csv) · [Monitor status](../data/api/monitor_status.json)

**Last successful check:** `2026-07-21T10:08:45+00:00`  
**Current API snapshot:** `c63818abfdd3128f`  
**Source observation:** `2026-07-18T11:35:05.153982+08:00`  
**New snapshot detected:** yes  
**Models returned:** 11

> “Last successful check” confirms that the automation reached the API. “Source observation” is supplied by the upstream endpoint and may be older.

> This is a model-level summary from the Codex Radar API, not the project's task-level difficulty-weighted score.

## Current API model summary

| Rank | Model tier | Source score | Passed | Tasks | Cost | Total tokens | Wall time |
|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | Terra Max | 100.9 | 75/112 | 112 | $519.96 | 1,348,720,452 | 61.60h |
| 2 | Sol Xhigh | 97.7 | 72/111 | 111 | $778.80 | 1,049,564,123 | 54.16h |
| 3 | Gpt-5.5 Xhigh | 95.5 | 71/112 | 112 | $657.91 | 845,525,043 | 41.35h |
| 4 | Sol High | 94.2 | 70/112 | 112 | $570.11 | 728,632,417 | 42.95h |
| 5 | Sol Medium | 94.2 | 70/112 | 112 | $387.56 | 489,931,203 | 34.30h |
| 6 | Luna Max | 92.8 | 69/112 | 112 | $279.20 | 1,907,106,717 | 70.31h |
| 7 | Terra Xhigh | 87.4 | 65/112 | 112 | $282.54 | 693,046,150 | 36.70h |
| 8 | Gpt-5.5 High | 80.7 | 60/112 | 112 | $401.64 | 502,814,602 | 29.61h |
| 9 | Sol Low | 73.3 | 54/111 | 111 | $229.18 | 263,088,468 | 22.88h |
| 10 | Luna High | 72.6 | 54/112 | 112 | $121.92 | 801,212,739 | 35.24h |
| 11 | Terra High | 70 | 52/112 | 112 | $150.20 | 338,287,491 | 24.46h |

## Interpretation

- The endpoint provides model-level `score`, pass counts, task counts, tokens, wall time, and estimated cost.
- It does not expose the ten task-level outcomes, so `Weighted /100` cannot be recomputed from this API summary alone.
- Task-weighted rankings remain based on the repository's task matrix and weight snapshots; this report monitors the latest API summary.
- When source data is unchanged, the automation still updates its heartbeat without presenting it as a new benchmark batch.
- The raw API response is not stored in the public repository; only required model-summary fields are archived.

Archived API snapshots: **41**.
