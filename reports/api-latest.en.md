# Codex Radar API Monitor — English

[简体中文](api-latest.zh-CN.md) · [Project home](../README.md) · [API history CSV](../data/api/model_iq_history.csv) · [Monitor status](../data/api/monitor_status.json)

**Last successful check:** `2026-08-02T11:07:19+00:00`  
**Current API snapshot:** `80c6638e418af863`  
**Source observation:** `2026-07-22T06:57:20.626603+08:00`  
**New snapshot detected:** yes  
**Models returned:** 11

> “Last successful check” confirms that the automation reached the API. “Source observation” is supplied by the upstream endpoint and may be older.

> This is a model-level summary from the Codex Radar API, not the project's task-level difficulty-weighted score.

## Current API model summary

| Rank | Model tier | Source score | Passed | Tasks | Cost | Total tokens | Wall time |
|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | Sol Xhigh | 98.2 | 73/112 | 112 | $771.85 | 969,734,013 | 47.18h |
| 2 | Gpt-5.5 Xhigh | 95.5 | 71/112 | 112 | $653.60 | 832,260,548 | 44.19h |
| 3 | Terra Max | 92.8 | 69/112 | 112 | $518.69 | 1,523,523,562 | 58.38h |
| 4 | Sol Medium | 88.8 | 66/112 | 112 | $420.79 | 555,393,288 | 32.68h |
| 5 | Luna Max | 86.1 | 64/112 | 112 | $82.20 | 1,784,237,015 | 59.72h |
| 6 | Sol High | 86.1 | 64/112 | 112 | $602.34 | 775,416,386 | 42.09h |
| 7 | Gpt-5.5 High | 79.4 | 59/112 | 112 | $416.27 | 502,668,150 | 31.38h |
| 8 | Terra Xhigh | 78 | 58/112 | 112 | $268.15 | 723,088,519 | 35.15h |
| 9 | Luna High | 72.6 | 54/112 | 112 | $65.32 | 793,648,605 | 33.64h |
| 10 | Terra High | 72.6 | 54/112 | 112 | $148.56 | 398,170,181 | 25.99h |
| 11 | Sol Low | 71.3 | 53/112 | 112 | $248.24 | 286,095,338 | 21.11h |

## Interpretation

- The endpoint provides model-level `score`, pass counts, task counts, tokens, wall time, and estimated cost.
- It does not expose the ten task-level outcomes, so `Weighted /100` cannot be recomputed from this API summary alone.
- Task-weighted rankings remain based on the repository's task matrix and weight snapshots; this report monitors the latest API summary.
- When source data is unchanged, the automation still updates its heartbeat without presenting it as a new benchmark batch.
- The raw API response is not stored in the public repository; only required model-summary fields are archived.

Archived API snapshots: **153**.
