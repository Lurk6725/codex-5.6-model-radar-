# Codex Radar API Monitor — English

[简体中文](api-latest.zh-CN.md) · [Project home](../README.md) · [API history CSV](../data/api/model_iq_history.csv) · [Monitor status](../data/api/monitor_status.json)

**Last successful check:** `2026-07-21T16:08:03+00:00`  
**Current API snapshot:** `6cb9413586f1f8ea`  
**Source observation:** `2026-07-18T11:35:05.153982+08:00`  
**New snapshot detected:** yes  
**Models returned:** 11

> “Last successful check” confirms that the automation reached the API. “Source observation” is supplied by the upstream endpoint and may be older.

> This is a model-level summary from the Codex Radar API, not the project's task-level difficulty-weighted score.

## Current API model summary

| Rank | Model tier | Source score | Passed | Tasks | Cost | Total tokens | Wall time |
|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | Terra Max | 99.5 | 74/112 | 112 | $519.26 | 1,344,439,659 | 62.44h |
| 2 | Sol Xhigh | 96.4 | 71/111 | 111 | $772.74 | 1,043,997,748 | 53.89h |
| 3 | Gpt-5.5 Xhigh | 95.5 | 71/112 | 112 | $651.63 | 837,637,971 | 42.07h |
| 4 | Luna Max | 94.2 | 70/112 | 112 | $281.16 | 1,928,059,480 | 66.53h |
| 5 | Sol High | 92.8 | 69/112 | 112 | $571.13 | 730,405,605 | 42.78h |
| 6 | Sol Medium | 92.8 | 69/112 | 112 | $397.59 | 491,674,340 | 34.02h |
| 7 | Terra Xhigh | 92.8 | 69/112 | 112 | $283.58 | 696,455,008 | 37.71h |
| 8 | Gpt-5.5 High | 80.7 | 60/112 | 112 | $403.31 | 505,166,061 | 30.41h |
| 9 | Sol Low | 74.7 | 55/111 | 111 | $228.61 | 264,985,642 | 23.74h |
| 10 | Luna High | 71.3 | 53/112 | 112 | $121.67 | 797,408,040 | 36.27h |
| 11 | Terra High | 68.6 | 51/112 | 112 | $147.17 | 330,950,087 | 25.12h |

## Interpretation

- The endpoint provides model-level `score`, pass counts, task counts, tokens, wall time, and estimated cost.
- It does not expose the ten task-level outcomes, so `Weighted /100` cannot be recomputed from this API summary alone.
- Task-weighted rankings remain based on the repository's task matrix and weight snapshots; this report monitors the latest API summary.
- When source data is unchanged, the automation still updates its heartbeat without presenting it as a new benchmark batch.
- The raw API response is not stored in the public repository; only required model-summary fields are archived.

Archived API snapshots: **44**.
