# Codex Radar API Monitor — English

[简体中文](api-latest.zh-CN.md) · [Project home](../README.md) · [API history CSV](../data/api/model_iq_history.csv) · [Monitor status](../data/api/monitor_status.json)

**Last successful check:** `2026-08-02T16:39:12+00:00`  
**Current API snapshot:** `ca7b3dcd196ad505`  
**Source observation:** `2026-07-22T06:57:20.626603+08:00`  
**New snapshot detected:** yes  
**Models returned:** 11

> “Last successful check” confirms that the automation reached the API. “Source observation” is supplied by the upstream endpoint and may be older.

> This is a model-level summary from the Codex Radar API, not the project's task-level difficulty-weighted score.

## Current API model summary

| Rank | Model tier | Source score | Passed | Tasks | Cost | Total tokens | Wall time |
|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | Gpt-5.5 Xhigh | 100.9 | 75/112 | 112 | $655.80 | 813,923,464 | 44.11h |
| 2 | Sol Xhigh | 98.2 | 73/112 | 112 | $773.06 | 968,599,164 | 47.78h |
| 3 | Terra Max | 94.2 | 70/112 | 112 | $517.44 | 1,484,884,105 | 57.69h |
| 4 | Luna Max | 90.1 | 67/112 | 112 | $61.02 | 1,753,724,124 | 60.16h |
| 5 | Sol Medium | 90.1 | 67/112 | 112 | $418.12 | 540,585,195 | 32.54h |
| 6 | Sol High | 83.4 | 62/112 | 112 | $599.96 | 765,015,178 | 42.60h |
| 7 | Terra Xhigh | 80.7 | 60/112 | 112 | $263.59 | 682,019,169 | 34.58h |
| 8 | Gpt-5.5 High | 79.4 | 59/112 | 112 | $412.10 | 500,843,540 | 31.39h |
| 9 | Terra High | 72.6 | 54/112 | 112 | $147.77 | 396,770,492 | 25.81h |
| 10 | Luna High | 71.3 | 53/112 | 112 | $44.72 | 769,315,637 | 31.91h |
| 11 | Sol Low | 71.3 | 53/112 | 112 | $244.40 | 281,566,166 | 21.56h |

## Interpretation

- The endpoint provides model-level `score`, pass counts, task counts, tokens, wall time, and estimated cost.
- It does not expose the ten task-level outcomes, so `Weighted /100` cannot be recomputed from this API summary alone.
- Task-weighted rankings remain based on the repository's task matrix and weight snapshots; this report monitors the latest API summary.
- When source data is unchanged, the automation still updates its heartbeat without presenting it as a new benchmark batch.
- The raw API response is not stored in the public repository; only required model-summary fields are archived.

Archived API snapshots: **156**.
