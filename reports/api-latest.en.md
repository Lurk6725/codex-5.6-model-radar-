# Codex Radar API Monitor — English

[简体中文](api-latest.zh-CN.md) · [Project home](../README.md) · [API history CSV](../data/api/model_iq_history.csv) · [Monitor status](../data/api/monitor_status.json)

**Last successful check:** `2026-07-17T19:51:13+00:00`  
**Current API snapshot:** `e342ecf372f6c863`  
**Source observation:** `2026-07-13T22:08:07.261261+08:00`  
**New snapshot detected:** yes  
**Models returned:** 9

> “Last successful check” confirms that the automation reached the API. “Source observation” is supplied by the upstream endpoint and may be older.

> This is a model-level summary from the Codex Radar API, not the project's task-level difficulty-weighted score.

## Current API model summary

| Rank | Model tier | Source score | Passed | Tasks | Cost | Total tokens | Wall time |
|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | Terra Max | 96.8 | 70/109 | 109 | $503.07 | 1,302,290,828 | 54.65h |
| 2 | Sol High | 96.4 | 71/111 | 111 | $589.02 | 744,317,983 | 42.65h |
| 3 | Sol Xhigh | 92.9 | 66/107 | 107 | $740.72 | 1,014,131,819 | 49.05h |
| 4 | Sol Medium | 88.8 | 66/112 | 112 | $394.80 | 503,320,690 | 33.57h |
| 5 | Luna Max | 85.9 | 61/107 | 107 | $249.20 | 1,668,562,925 | 58.16h |
| 6 | Sol Low | 83.6 | 61/110 | 110 | $215.42 | 261,897,671 | 21.77h |
| 7 | Gpt-5.5 High | 78.7 | 58/111 | 111 | $392.21 | 495,259,747 | 34.25h |
| 8 | Terra High | 69.1 | 50/109 | 109 | $146.92 | 327,578,208 | 23.46h |
| 9 | Luna High | 62.2 | 45/109 | 109 | $123.01 | 800,465,790 | 32.73h |

## Interpretation

- The endpoint provides model-level `score`, pass counts, task counts, tokens, wall time, and estimated cost.
- It does not expose the ten task-level outcomes, so `Weighted /100` cannot be recomputed from this API summary alone.
- Task-weighted rankings remain based on the repository's task matrix and weight snapshots; this report monitors the latest API summary.
- When source data is unchanged, the automation still updates its heartbeat without presenting it as a new benchmark batch.
- The raw API response is not stored in the public repository; only required model-summary fields are archived.

Archived API snapshots: **15**.
