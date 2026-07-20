# Codex Radar API Monitor — English

[简体中文](api-latest.zh-CN.md) · [Project home](../README.md) · [API history CSV](../data/api/model_iq_history.csv) · [Monitor status](../data/api/monitor_status.json)

**Last successful check:** `2026-07-20T10:32:37+00:00`  
**Current API snapshot:** `a61d13bc4e402f91`  
**Source observation:** `2026-07-18T11:35:05.153982+08:00`  
**New snapshot detected:** yes  
**Models returned:** 11

> “Last successful check” confirms that the automation reached the API. “Source observation” is supplied by the upstream endpoint and may be older.

> This is a model-level summary from the Codex Radar API, not the project's task-level difficulty-weighted score.

## Current API model summary

| Rank | Model tier | Source score | Passed | Tasks | Cost | Total tokens | Wall time |
|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | Terra Max | 103.6 | 77/112 | 112 | $507.20 | 1,311,342,722 | 59.68h |
| 2 | Gpt-5.5 Xhigh | 96.9 | 72/112 | 112 | $651.93 | 831,163,798 | 40.10h |
| 3 | Sol High | 95.5 | 71/112 | 112 | $556.20 | 700,602,287 | 42.35h |
| 4 | Sol Medium | 91.5 | 68/112 | 112 | $385.23 | 488,464,258 | 34.16h |
| 5 | Sol Xhigh | 90.9 | 67/111 | 111 | $732.93 | 975,783,501 | 50.48h |
| 6 | Luna Max | 86.1 | 64/112 | 112 | $284.87 | 1,963,931,960 | 71.83h |
| 7 | Terra Xhigh | 86.1 | 64/112 | 112 | $275.42 | 668,175,517 | 35.06h |
| 8 | Gpt-5.5 High | 84.7 | 63/112 | 112 | $409.63 | 516,680,431 | 31.09h |
| 9 | Sol Low | 80.1 | 59/111 | 111 | $227.72 | 260,296,984 | 22.56h |
| 10 | Terra High | 68.6 | 51/112 | 112 | $147.90 | 330,027,159 | 23.26h |
| 11 | Luna High | 67.3 | 50/112 | 112 | $122.45 | 803,544,849 | 35.55h |

## Interpretation

- The endpoint provides model-level `score`, pass counts, task counts, tokens, wall time, and estimated cost.
- It does not expose the ten task-level outcomes, so `Weighted /100` cannot be recomputed from this API summary alone.
- Task-weighted rankings remain based on the repository's task matrix and weight snapshots; this report monitors the latest API summary.
- When source data is unchanged, the automation still updates its heartbeat without presenting it as a new benchmark batch.
- The raw API response is not stored in the public repository; only required model-summary fields are archived.

Archived API snapshots: **38**.
