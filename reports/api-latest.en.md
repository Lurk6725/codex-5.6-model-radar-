# Codex Radar API Monitor — English

[简体中文](api-latest.zh-CN.md) · [Project home](../README.md) · [API history CSV](../data/api/model_iq_history.csv) · [Monitor status](../data/api/monitor_status.json)

**Last successful check:** `2026-08-06T01:07:53+00:00`  
**Current API snapshot:** `68164c1ef06c5197`  
**Source observation:** `2026-07-22T06:57:20.626603+08:00`  
**New snapshot detected:** no; the source returned the same snapshot  
**Models returned:** 11

> “Last successful check” confirms that the automation reached the API. “Source observation” is supplied by the upstream endpoint and may be older.

> This is a model-level summary from the Codex Radar API, not the project's task-level difficulty-weighted score.

## Current API model summary

| Rank | Model tier | Source score | Passed | Tasks | Cost | Total tokens | Wall time |
|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | Sol Xhigh | 113 | 84/112 | 112 | $761.10 | 948,800,760 | 47.81h |
| 2 | Gpt-5.5 Xhigh | 96.9 | 72/112 | 112 | $652.27 | 803,235,041 | 41.36h |
| 3 | Gpt-5.5 High | 92.8 | 69/112 | 112 | $406.58 | 497,750,762 | 31.52h |
| 4 | Luna Max | 92.8 | 69/112 | 112 | $58.74 | 1,708,363,691 | 59.97h |
| 5 | Sol Medium | 92.8 | 69/112 | 112 | $409.75 | 520,589,698 | 31.82h |
| 6 | Terra Max | 91.5 | 68/112 | 112 | $456.11 | 1,449,820,319 | 60.13h |
| 7 | Sol High | 87.4 | 65/112 | 112 | $588.01 | 694,540,149 | 40.13h |
| 8 | Terra Xhigh | 83.4 | 62/112 | 112 | $227.68 | 619,038,430 | 34.91h |
| 9 | Luna High | 75.3 | 56/112 | 112 | $27.57 | 731,045,614 | 30.04h |
| 10 | Terra High | 74 | 55/112 | 112 | $134.04 | 353,545,448 | 25.15h |
| 11 | Sol Low | 72.6 | 54/112 | 112 | $231.65 | 256,295,694 | 21.88h |

## Interpretation

- The endpoint provides model-level `score`, pass counts, task counts, tokens, wall time, and estimated cost.
- It does not expose the ten task-level outcomes, so `Weighted /100` cannot be recomputed from this API summary alone.
- Task-weighted rankings remain based on the repository's task matrix and weight snapshots; this report monitors the latest API summary.
- When source data is unchanged, the automation still updates its heartbeat without presenting it as a new benchmark batch.
- The raw API response is not stored in the public repository; only required model-summary fields are archived.

Archived API snapshots: **181**.
