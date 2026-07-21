# Codex Radar API Monitor — English

[简体中文](api-latest.zh-CN.md) · [Project home](../README.md) · [API history CSV](../data/api/model_iq_history.csv) · [Monitor status](../data/api/monitor_status.json)

**Last successful check:** `2026-07-21T14:26:29+00:00`  
**Current API snapshot:** `01e50d352a10064e`  
**Source observation:** `2026-07-18T11:35:05.153982+08:00`  
**New snapshot detected:** yes  
**Models returned:** 11

> “Last successful check” confirms that the automation reached the API. “Source observation” is supplied by the upstream endpoint and may be older.

> This is a model-level summary from the Codex Radar API, not the project's task-level difficulty-weighted score.

## Current API model summary

| Rank | Model tier | Source score | Passed | Tasks | Cost | Total tokens | Wall time |
|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | Terra Max | 99.5 | 74/112 | 112 | $519.26 | 1,344,439,659 | 62.44h |
| 2 | Sol Xhigh | 96.4 | 71/111 | 111 | $772.32 | 1,043,065,226 | 53.90h |
| 3 | Sol High | 95.5 | 71/112 | 112 | $566.57 | 722,786,672 | 42.83h |
| 4 | Luna Max | 94.2 | 70/112 | 112 | $280.56 | 1,914,846,020 | 70.44h |
| 5 | Gpt-5.5 Xhigh | 92.8 | 69/112 | 112 | $653.78 | 841,158,919 | 42.24h |
| 6 | Sol Medium | 92.8 | 69/112 | 112 | $391.61 | 492,847,674 | 34.67h |
| 7 | Terra Xhigh | 90.1 | 67/112 | 112 | $282.26 | 692,890,125 | 37.83h |
| 8 | Gpt-5.5 High | 83.4 | 62/112 | 112 | $402.52 | 503,902,198 | 30.12h |
| 9 | Sol Low | 74.7 | 55/111 | 111 | $228.60 | 264,417,960 | 23.73h |
| 10 | Luna High | 71.3 | 53/112 | 112 | $121.17 | 794,502,423 | 36.38h |
| 11 | Terra High | 65.9 | 49/112 | 112 | $149.10 | 336,842,598 | 25.13h |

## Interpretation

- The endpoint provides model-level `score`, pass counts, task counts, tokens, wall time, and estimated cost.
- It does not expose the ten task-level outcomes, so `Weighted /100` cannot be recomputed from this API summary alone.
- Task-weighted rankings remain based on the repository's task matrix and weight snapshots; this report monitors the latest API summary.
- When source data is unchanged, the automation still updates its heartbeat without presenting it as a new benchmark batch.
- The raw API response is not stored in the public repository; only required model-summary fields are archived.

Archived API snapshots: **43**.
