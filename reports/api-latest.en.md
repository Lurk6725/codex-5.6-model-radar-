# Codex Radar API Monitor — English

[简体中文](api-latest.zh-CN.md) · [Project home](../README.md) · [API history CSV](../data/api/model_iq_history.csv) · [Monitor status](../data/api/monitor_status.json)

**Last successful check:** `2026-08-07T08:31:56+00:00`  
**Current API snapshot:** `8fac1767eb7bc57e`  
**Source observation:** `2026-07-22T06:57:20.626603+08:00`  
**New snapshot detected:** yes  
**Models returned:** 11

> “Last successful check” confirms that the automation reached the API. “Source observation” is supplied by the upstream endpoint and may be older.

> This is a model-level summary from the Codex Radar API, not the project's task-level difficulty-weighted score.

## Current API model summary

| Rank | Model tier | Source score | Passed | Tasks | Cost | Total tokens | Wall time |
|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | Sol Xhigh | 106.3 | 79/112 | 112 | $755.73 | 972,009,619 | 47.88h |
| 2 | Gpt-5.5 High | 95.5 | 71/112 | 112 | $407.53 | 498,107,316 | 32.59h |
| 3 | Luna Max | 95.5 | 71/112 | 112 | $58.84 | 1,786,682,773 | 61.26h |
| 4 | Gpt-5.5 Xhigh | 94.2 | 70/112 | 112 | $648.98 | 809,459,576 | 41.83h |
| 5 | Sol Medium | 94.2 | 70/112 | 112 | $409.04 | 532,668,738 | 31.98h |
| 6 | Terra Max | 94.2 | 70/112 | 112 | $454.46 | 1,485,078,822 | 62.19h |
| 7 | Sol High | 88.8 | 66/112 | 112 | $583.89 | 666,589,080 | 39.67h |
| 8 | Terra Xhigh | 86.1 | 64/112 | 112 | $226.90 | 628,883,903 | 36.58h |
| 9 | Luna High | 79.4 | 59/112 | 112 | $26.79 | 737,169,502 | 31.42h |
| 10 | Terra High | 79.4 | 59/112 | 112 | $130.55 | 348,713,486 | 24.66h |
| 11 | Sol Low | 78 | 58/112 | 112 | $232.08 | 257,467,042 | 22.67h |

## Interpretation

- The endpoint provides model-level `score`, pass counts, task counts, tokens, wall time, and estimated cost.
- It does not expose the ten task-level outcomes, so `Weighted /100` cannot be recomputed from this API summary alone.
- Task-weighted rankings remain based on the repository's task matrix and weight snapshots; this report monitors the latest API summary.
- When source data is unchanged, the automation still updates its heartbeat without presenting it as a new benchmark batch.
- The raw API response is not stored in the public repository; only required model-summary fields are archived.

Archived API snapshots: **189**.
