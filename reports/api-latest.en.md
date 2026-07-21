# Codex Radar API Monitor — English

[简体中文](api-latest.zh-CN.md) · [Project home](../README.md) · [API history CSV](../data/api/model_iq_history.csv) · [Monitor status](../data/api/monitor_status.json)

**Last successful check:** `2026-07-21T04:35:14+00:00`  
**Current API snapshot:** `3ba49cc6daefcad6`  
**Source observation:** `2026-07-18T11:35:05.153982+08:00`  
**New snapshot detected:** yes  
**Models returned:** 11

> “Last successful check” confirms that the automation reached the API. “Source observation” is supplied by the upstream endpoint and may be older.

> This is a model-level summary from the Codex Radar API, not the project's task-level difficulty-weighted score.

## Current API model summary

| Rank | Model tier | Source score | Passed | Tasks | Cost | Total tokens | Wall time |
|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | Terra Max | 99.5 | 74/112 | 112 | $515.74 | 1,337,852,126 | 60.52h |
| 2 | Sol Xhigh | 96.4 | 71/111 | 111 | $787.47 | 1,058,013,473 | 55.13h |
| 3 | Sol High | 95.5 | 71/112 | 112 | $561.07 | 710,612,991 | 42.14h |
| 4 | Sol Medium | 94.2 | 70/112 | 112 | $385.87 | 487,483,722 | 33.87h |
| 5 | Gpt-5.5 Xhigh | 92.8 | 69/112 | 112 | $653.21 | 837,713,413 | 40.28h |
| 6 | Luna Max | 88.8 | 66/112 | 112 | $277.06 | 1,891,908,000 | 70.02h |
| 7 | Terra Xhigh | 86.1 | 64/112 | 112 | $279.84 | 686,204,736 | 36.06h |
| 8 | Gpt-5.5 High | 82.1 | 61/112 | 112 | $400.54 | 501,508,525 | 29.74h |
| 9 | Sol Low | 77.4 | 57/111 | 111 | $226.47 | 254,587,993 | 22.99h |
| 10 | Luna High | 72.6 | 54/112 | 112 | $121.18 | 794,938,403 | 35.67h |
| 11 | Terra High | 70 | 52/112 | 112 | $151.01 | 339,984,306 | 24.20h |

## Interpretation

- The endpoint provides model-level `score`, pass counts, task counts, tokens, wall time, and estimated cost.
- It does not expose the ten task-level outcomes, so `Weighted /100` cannot be recomputed from this API summary alone.
- Task-weighted rankings remain based on the repository's task matrix and weight snapshots; this report monitors the latest API summary.
- When source data is unchanged, the automation still updates its heartbeat without presenting it as a new benchmark batch.
- The raw API response is not stored in the public repository; only required model-summary fields are archived.

Archived API snapshots: **40**.
