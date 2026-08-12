# Codex Radar API Monitor — English

[简体中文](api-latest.zh-CN.md) · [Project home](../README.md) · [API history CSV](../data/api/model_iq_history.csv) · [Monitor status](../data/api/monitor_status.json)

**Last successful check:** `2026-08-12T02:47:25+00:00`  
**Current API snapshot:** `98b452d0152110e2`  
**Source observation:** `2026-07-22T06:57:20.626603+08:00`  
**New snapshot detected:** yes  
**Models returned:** 11

> “Last successful check” confirms that the automation reached the API. “Source observation” is supplied by the upstream endpoint and may be older.

> This is a model-level summary from the Codex Radar API, not the project's task-level difficulty-weighted score.

## Current API model summary

| Rank | Model tier | Source score | Passed | Tasks | Cost | Total tokens | Wall time |
|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | Sol Xhigh | 109 | 81/112 | 112 | $735.88 | 906,540,976 | 49.26h |
| 2 | Sol High | 103.6 | 77/112 | 112 | $562.85 | 646,763,460 | 37.81h |
| 3 | Luna Max | 102.2 | 76/112 | 112 | $58.69 | 1,833,551,143 | 62.88h |
| 4 | Terra Max | 100.9 | 75/112 | 112 | $437.68 | 1,187,685,816 | 53.74h |
| 5 | Gpt-5.5 High | 92.8 | 69/112 | 112 | $404.13 | 485,122,204 | 32.15h |
| 6 | Gpt-5.5 Xhigh | 92.8 | 69/112 | 112 | $656.80 | 737,780,499 | 40.30h |
| 7 | Sol Medium | 90.1 | 67/112 | 112 | $407.47 | 471,920,521 | 31.45h |
| 8 | Terra Xhigh | 84.7 | 63/112 | 112 | $218.36 | 565,384,292 | 33.98h |
| 9 | Terra High | 79.4 | 59/112 | 112 | $127.14 | 337,018,322 | 23.81h |
| 10 | Sol Low | 76.7 | 57/112 | 112 | $229.58 | 276,770,187 | 22.38h |
| 11 | Luna High | 67.3 | 50/112 | 112 | $26.20 | 771,959,148 | 34.48h |

## Interpretation

- The endpoint provides model-level `score`, pass counts, task counts, tokens, wall time, and estimated cost.
- It does not expose the ten task-level outcomes, so `Weighted /100` cannot be recomputed from this API summary alone.
- Task-weighted rankings remain based on the repository's task matrix and weight snapshots; this report monitors the latest API summary.
- When source data is unchanged, the automation still updates its heartbeat without presenting it as a new benchmark batch.
- The raw API response is not stored in the public repository; only required model-summary fields are archived.

Archived API snapshots: **238**.
