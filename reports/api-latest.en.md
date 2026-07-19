# Codex Radar API Monitor — English

[简体中文](api-latest.zh-CN.md) · [Project home](../README.md) · [API history CSV](../data/api/model_iq_history.csv) · [Monitor status](../data/api/monitor_status.json)

**Last successful check:** `2026-07-19T03:59:14+00:00`  
**Current API snapshot:** `72e73f3d4ef40feb`  
**Source observation:** `2026-07-18T11:35:05.153982+08:00`  
**New snapshot detected:** yes  
**Models returned:** 9

> “Last successful check” confirms that the automation reached the API. “Source observation” is supplied by the upstream endpoint and may be older.

> This is a model-level summary from the Codex Radar API, not the project's task-level difficulty-weighted score.

## Current API model summary

| Rank | Model tier | Source score | Passed | Tasks | Cost | Total tokens | Wall time |
|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | Terra Max | 98.2 | 73/112 | 112 | $511.61 | 1,320,272,286 | 60.51h |
| 2 | Sol Xhigh | 94.5 | 69/110 | 110 | $754.39 | 1,051,164,643 | 52.51h |
| 3 | Sol High | 94.2 | 70/112 | 112 | $618.71 | 798,925,750 | 44.67h |
| 4 | Sol Medium | 90.1 | 67/112 | 112 | $392.82 | 494,690,851 | 34.19h |
| 5 | Gpt-5.5 High | 87.4 | 65/112 | 112 | $403.44 | 507,806,644 | 30.30h |
| 6 | Luna Max | 87.4 | 65/112 | 112 | $275.01 | 1,872,191,038 | 67.66h |
| 7 | Sol Low | 78.7 | 58/111 | 111 | $213.70 | 260,114,570 | 21.47h |
| 8 | Terra High | 65.9 | 49/112 | 112 | $145.32 | 323,424,747 | 23.32h |
| 9 | Luna High | 62.4 | 46/111 | 111 | $121.70 | 793,177,682 | 33.90h |

## Interpretation

- The endpoint provides model-level `score`, pass counts, task counts, tokens, wall time, and estimated cost.
- It does not expose the ten task-level outcomes, so `Weighted /100` cannot be recomputed from this API summary alone.
- Task-weighted rankings remain based on the repository's task matrix and weight snapshots; this report monitors the latest API summary.
- When source data is unchanged, the automation still updates its heartbeat without presenting it as a new benchmark batch.
- The raw API response is not stored in the public repository; only required model-summary fields are archived.

Archived API snapshots: **26**.
