# Codex Radar API Monitor — English

[简体中文](api-latest.zh-CN.md) · [Project home](../README.md) · [API history CSV](../data/api/model_iq_history.csv) · [Monitor status](../data/api/monitor_status.json)

**Last successful check:** `2026-07-21T19:54:46+00:00`  
**Current API snapshot:** `a7da0a6b8cb08e4f`  
**Source observation:** `2026-07-18T11:35:05.153982+08:00`  
**New snapshot detected:** yes  
**Models returned:** 11

> “Last successful check” confirms that the automation reached the API. “Source observation” is supplied by the upstream endpoint and may be older.

> This is a model-level summary from the Codex Radar API, not the project's task-level difficulty-weighted score.

## Current API model summary

| Rank | Model tier | Source score | Passed | Tasks | Cost | Total tokens | Wall time |
|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | Terra Max | 100.9 | 75/112 | 112 | $524.85 | 1,362,685,529 | 63.29h |
| 2 | Luna Max | 98.2 | 73/112 | 112 | $282.01 | 1,933,572,707 | 67.40h |
| 3 | Gpt-5.5 Xhigh | 96.9 | 72/112 | 112 | $653.43 | 839,972,933 | 42.30h |
| 4 | Sol Xhigh | 95 | 70/111 | 111 | $770.94 | 1,041,094,307 | 53.66h |
| 5 | Sol Medium | 94.2 | 70/112 | 112 | $398.63 | 494,289,111 | 33.91h |
| 6 | Terra Xhigh | 94.2 | 70/112 | 112 | $282.47 | 693,022,882 | 37.66h |
| 7 | Sol High | 92.8 | 69/112 | 112 | $566.93 | 724,148,279 | 42.14h |
| 8 | Gpt-5.5 High | 79.4 | 59/112 | 112 | $405.58 | 507,597,218 | 30.25h |
| 9 | Sol Low | 76 | 56/111 | 111 | $228.69 | 265,154,316 | 23.61h |
| 10 | Luna High | 72.6 | 54/112 | 112 | $121.36 | 793,973,346 | 36.51h |
| 11 | Terra High | 65.9 | 49/112 | 112 | $147.43 | 334,940,812 | 25.81h |

## Interpretation

- The endpoint provides model-level `score`, pass counts, task counts, tokens, wall time, and estimated cost.
- It does not expose the ten task-level outcomes, so `Weighted /100` cannot be recomputed from this API summary alone.
- Task-weighted rankings remain based on the repository's task matrix and weight snapshots; this report monitors the latest API summary.
- When source data is unchanged, the automation still updates its heartbeat without presenting it as a new benchmark batch.
- The raw API response is not stored in the public repository; only required model-summary fields are archived.

Archived API snapshots: **46**.
