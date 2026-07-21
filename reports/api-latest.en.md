# Codex Radar API Monitor — English

[简体中文](api-latest.zh-CN.md) · [Project home](../README.md) · [API history CSV](../data/api/model_iq_history.csv) · [Monitor status](../data/api/monitor_status.json)

**Last successful check:** `2026-07-21T22:38:42+00:00`  
**Current API snapshot:** `a8c81a52711689be`  
**Source observation:** `2026-07-18T11:35:05.153982+08:00`  
**New snapshot detected:** yes  
**Models returned:** 11

> “Last successful check” confirms that the automation reached the API. “Source observation” is supplied by the upstream endpoint and may be older.

> This is a model-level summary from the Codex Radar API, not the project's task-level difficulty-weighted score.

## Current API model summary

| Rank | Model tier | Source score | Passed | Tasks | Cost | Total tokens | Wall time |
|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | Terra Max | 102.2 | 76/112 | 112 | $525.91 | 1,365,377,297 | 63.14h |
| 2 | Luna Max | 96.9 | 72/112 | 112 | $278.22 | 1,914,123,207 | 66.09h |
| 3 | Gpt-5.5 Xhigh | 95.5 | 71/112 | 112 | $653.00 | 839,273,334 | 42.15h |
| 4 | Sol High | 94.2 | 70/112 | 112 | $566.30 | 726,045,964 | 42.04h |
| 5 | Sol Xhigh | 93.7 | 69/111 | 111 | $772.22 | 1,042,307,763 | 53.10h |
| 6 | Terra Xhigh | 92.8 | 69/112 | 112 | $276.98 | 670,589,152 | 37.14h |
| 7 | Sol Medium | 91.5 | 68/112 | 112 | $398.14 | 494,709,664 | 33.46h |
| 8 | Gpt-5.5 High | 78 | 58/112 | 112 | $402.44 | 502,621,502 | 30.02h |
| 9 | Sol Low | 77.4 | 57/111 | 111 | $228.40 | 264,732,858 | 23.72h |
| 10 | Luna High | 70 | 52/112 | 112 | $120.63 | 787,262,695 | 36.37h |
| 11 | Terra High | 68.6 | 51/112 | 112 | $143.84 | 323,722,247 | 25.31h |

## Interpretation

- The endpoint provides model-level `score`, pass counts, task counts, tokens, wall time, and estimated cost.
- It does not expose the ten task-level outcomes, so `Weighted /100` cannot be recomputed from this API summary alone.
- Task-weighted rankings remain based on the repository's task matrix and weight snapshots; this report monitors the latest API summary.
- When source data is unchanged, the automation still updates its heartbeat without presenting it as a new benchmark batch.
- The raw API response is not stored in the public repository; only required model-summary fields are archived.

Archived API snapshots: **48**.
