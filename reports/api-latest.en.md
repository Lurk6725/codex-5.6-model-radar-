# Codex Radar API Monitor — English

[简体中文](api-latest.zh-CN.md) · [Project home](../README.md) · [API history CSV](../data/api/model_iq_history.csv) · [Monitor status](../data/api/monitor_status.json)

**Last successful check:** `2026-08-07T10:37:39+00:00`  
**Current API snapshot:** `b1979a6b534dc848`  
**Source observation:** `2026-07-22T06:57:20.626603+08:00`  
**New snapshot detected:** no; the source returned the same snapshot  
**Models returned:** 11

> “Last successful check” confirms that the automation reached the API. “Source observation” is supplied by the upstream endpoint and may be older.

> This is a model-level summary from the Codex Radar API, not the project's task-level difficulty-weighted score.

## Current API model summary

| Rank | Model tier | Source score | Passed | Tasks | Cost | Total tokens | Wall time |
|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | Sol Xhigh | 104.9 | 78/112 | 112 | $755.75 | 965,471,168 | 47.65h |
| 2 | Gpt-5.5 High | 95.5 | 71/112 | 112 | $407.77 | 496,645,945 | 33.19h |
| 3 | Gpt-5.5 Xhigh | 95.5 | 71/112 | 112 | $649.00 | 808,542,276 | 41.87h |
| 4 | Luna Max | 95.5 | 71/112 | 112 | $58.84 | 1,786,682,773 | 61.26h |
| 5 | Sol Medium | 92.8 | 69/112 | 112 | $409.96 | 532,180,693 | 31.87h |
| 6 | Terra Max | 92.8 | 69/112 | 112 | $454.35 | 1,497,775,506 | 62.55h |
| 7 | Sol High | 91.5 | 68/112 | 112 | $583.69 | 664,209,899 | 39.25h |
| 8 | Terra Xhigh | 86.1 | 64/112 | 112 | $226.91 | 628,558,065 | 36.52h |
| 9 | Sol Low | 80.7 | 60/112 | 112 | $232.21 | 255,078,280 | 22.44h |
| 10 | Terra High | 80.7 | 60/112 | 112 | $130.53 | 350,435,867 | 25.23h |
| 11 | Luna High | 79.4 | 59/112 | 112 | $26.79 | 737,169,502 | 31.42h |

## Interpretation

- The endpoint provides model-level `score`, pass counts, task counts, tokens, wall time, and estimated cost.
- It does not expose the ten task-level outcomes, so `Weighted /100` cannot be recomputed from this API summary alone.
- Task-weighted rankings remain based on the repository's task matrix and weight snapshots; this report monitors the latest API summary.
- When source data is unchanged, the automation still updates its heartbeat without presenting it as a new benchmark batch.
- The raw API response is not stored in the public repository; only required model-summary fields are archived.

Archived API snapshots: **190**.
