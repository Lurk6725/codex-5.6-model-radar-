# Codex Radar API Monitor — English

[简体中文](api-latest.zh-CN.md) · [Project home](../README.md) · [API history CSV](../data/api/model_iq_history.csv) · [Monitor status](../data/api/monitor_status.json)

**Last successful check:** `2026-08-11T05:42:43+00:00`  
**Current API snapshot:** `118291cfb36911e1`  
**Source observation:** `2026-07-22T06:57:20.626603+08:00`  
**New snapshot detected:** yes  
**Models returned:** 11

> “Last successful check” confirms that the automation reached the API. “Source observation” is supplied by the upstream endpoint and may be older.

> This is a model-level summary from the Codex Radar API, not the project's task-level difficulty-weighted score.

## Current API model summary

| Rank | Model tier | Source score | Passed | Tasks | Cost | Total tokens | Wall time |
|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | Sol High | 103.6 | 77/112 | 112 | $565.51 | 636,644,839 | 38.18h |
| 2 | Sol Xhigh | 102.2 | 76/112 | 112 | $737.00 | 900,828,311 | 49.95h |
| 3 | Terra Max | 99.5 | 74/112 | 112 | $438.67 | 1,183,601,975 | 53.12h |
| 4 | Sol Medium | 96.9 | 72/112 | 112 | $410.28 | 454,898,494 | 30.79h |
| 5 | Gpt-5.5 Xhigh | 95.5 | 71/112 | 112 | $655.83 | 790,321,799 | 41.10h |
| 6 | Luna Max | 91.5 | 68/112 | 112 | $58.60 | 1,827,461,136 | 62.62h |
| 7 | Sol Low | 87.4 | 65/112 | 112 | $229.69 | 274,350,527 | 22.15h |
| 8 | Terra Xhigh | 86.1 | 64/112 | 112 | $219.69 | 545,249,166 | 30.98h |
| 9 | Gpt-5.5 High | 84.7 | 63/112 | 112 | $404.33 | 489,308,423 | 29.84h |
| 10 | Terra High | 78 | 58/112 | 112 | $126.87 | 334,060,291 | 23.27h |
| 11 | Luna High | 74 | 55/112 | 112 | $26.17 | 751,125,618 | 33.75h |

## Interpretation

- The endpoint provides model-level `score`, pass counts, task counts, tokens, wall time, and estimated cost.
- It does not expose the ten task-level outcomes, so `Weighted /100` cannot be recomputed from this API summary alone.
- Task-weighted rankings remain based on the repository's task matrix and weight snapshots; this report monitors the latest API summary.
- When source data is unchanged, the automation still updates its heartbeat without presenting it as a new benchmark batch.
- The raw API response is not stored in the public repository; only required model-summary fields are archived.

Archived API snapshots: **230**.
