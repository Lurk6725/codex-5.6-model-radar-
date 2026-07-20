# Codex Radar API Monitor — English

[简体中文](api-latest.zh-CN.md) · [Project home](../README.md) · [API history CSV](../data/api/model_iq_history.csv) · [Monitor status](../data/api/monitor_status.json)

**Last successful check:** `2026-07-20T07:33:27+00:00`  
**Current API snapshot:** `068ff35a551f0233`  
**Source observation:** `2026-07-18T11:35:05.153982+08:00`  
**New snapshot detected:** yes  
**Models returned:** 11

> “Last successful check” confirms that the automation reached the API. “Source observation” is supplied by the upstream endpoint and may be older.

> This is a model-level summary from the Codex Radar API, not the project's task-level difficulty-weighted score.

## Current API model summary

| Rank | Model tier | Source score | Passed | Tasks | Cost | Total tokens | Wall time |
|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | Terra Max | 99.5 | 74/112 | 112 | $507.18 | 1,311,882,221 | 59.61h |
| 2 | Sol High | 98.2 | 73/112 | 112 | $546.83 | 685,066,439 | 41.43h |
| 3 | Gpt-5.5 Xhigh | 95.5 | 71/112 | 112 | $652.40 | 831,874,557 | 40.08h |
| 4 | Sol Medium | 91.5 | 68/112 | 112 | $383.22 | 485,867,650 | 33.35h |
| 5 | Sol Xhigh | 90.9 | 67/111 | 111 | $734.59 | 975,730,096 | 50.47h |
| 6 | Luna Max | 86.1 | 64/112 | 112 | $284.68 | 1,962,759,027 | 71.62h |
| 7 | Gpt-5.5 High | 83.4 | 62/112 | 112 | $410.28 | 517,904,720 | 30.93h |
| 8 | Terra Xhigh | 83.4 | 62/112 | 112 | $272.82 | 661,078,767 | 34.54h |
| 9 | Sol Low | 80.1 | 59/111 | 111 | $227.72 | 260,296,984 | 22.56h |
| 10 | Terra High | 68.6 | 51/112 | 112 | $147.90 | 330,027,159 | 23.26h |
| 11 | Luna High | 67.3 | 50/112 | 112 | $122.69 | 805,911,642 | 35.55h |

## Interpretation

- The endpoint provides model-level `score`, pass counts, task counts, tokens, wall time, and estimated cost.
- It does not expose the ten task-level outcomes, so `Weighted /100` cannot be recomputed from this API summary alone.
- Task-weighted rankings remain based on the repository's task matrix and weight snapshots; this report monitors the latest API summary.
- When source data is unchanged, the automation still updates its heartbeat without presenting it as a new benchmark batch.
- The raw API response is not stored in the public repository; only required model-summary fields are archived.

Archived API snapshots: **37**.
