# Codex Radar API Monitor — English

[简体中文](api-latest.zh-CN.md) · [Project home](../README.md) · [API history CSV](../data/api/model_iq_history.csv) · [Monitor status](../data/api/monitor_status.json)

**Last successful check:** `2026-08-17T01:57:05+00:00`  
**Current API snapshot:** `cf71266cd0e44426`  
**Source observation:** `2026-07-22T06:57:20.626603+08:00`  
**New snapshot detected:** yes  
**Models returned:** 11

> “Last successful check” confirms that the automation reached the API. “Source observation” is supplied by the upstream endpoint and may be older.

> This is a model-level summary from the Codex Radar API, not the project's task-level difficulty-weighted score.

## Current API model summary

| Rank | Model tier | Source score | Passed | Tasks | Cost | Total tokens | Wall time |
|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | Sol Xhigh | 96.9 | 72/112 | 112 | $724.92 | 857,958,602 | 45.23h |
| 2 | Terra Max | 96.9 | 72/112 | 112 | $435.25 | 1,248,050,401 | 58.63h |
| 3 | Gpt-5.5 Xhigh | 95.5 | 71/112 | 112 | $655.46 | 750,344,086 | 42.20h |
| 4 | Gpt-5.5 High | 94.2 | 70/112 | 112 | $403.54 | 497,510,501 | 33.09h |
| 5 | Luna Max | 92.8 | 69/112 | 112 | $58.61 | 1,772,516,419 | 64.38h |
| 6 | Sol High | 90.1 | 67/112 | 112 | $538.00 | 646,484,673 | 36.19h |
| 7 | Sol Medium | 87.4 | 65/112 | 112 | $382.82 | 471,222,662 | 32.74h |
| 8 | Terra Xhigh | 83.4 | 62/112 | 112 | $216.98 | 591,993,033 | 37.55h |
| 9 | Luna High | 78 | 58/112 | 112 | $26.16 | 763,933,747 | 35.36h |
| 10 | Terra High | 72.6 | 54/112 | 112 | $126.51 | 340,169,507 | 26.16h |
| 11 | Sol Low | 63.2 | 47/112 | 112 | $226.05 | 278,399,057 | 24.30h |

## Interpretation

- The endpoint provides model-level `score`, pass counts, task counts, tokens, wall time, and estimated cost.
- It does not expose the ten task-level outcomes, so `Weighted /100` cannot be recomputed from this API summary alone.
- Task-weighted rankings remain based on the repository's task matrix and weight snapshots; this report monitors the latest API summary.
- When source data is unchanged, the automation still updates its heartbeat without presenting it as a new benchmark batch.
- The raw API response is not stored in the public repository; only required model-summary fields are archived.

Archived API snapshots: **274**.
