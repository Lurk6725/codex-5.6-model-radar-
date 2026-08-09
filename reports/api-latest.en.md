# Codex Radar API Monitor — English

[简体中文](api-latest.zh-CN.md) · [Project home](../README.md) · [API history CSV](../data/api/model_iq_history.csv) · [Monitor status](../data/api/monitor_status.json)

**Last successful check:** `2026-08-09T17:49:55+00:00`  
**Current API snapshot:** `93fe1140b02e1c22`  
**Source observation:** `2026-07-22T06:57:20.626603+08:00`  
**New snapshot detected:** yes  
**Models returned:** 11

> “Last successful check” confirms that the automation reached the API. “Source observation” is supplied by the upstream endpoint and may be older.

> This is a model-level summary from the Codex Radar API, not the project's task-level difficulty-weighted score.

## Current API model summary

| Rank | Model tier | Source score | Passed | Tasks | Cost | Total tokens | Wall time |
|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | Sol Xhigh | 109 | 81/112 | 112 | $745.91 | 920,766,487 | 51.58h |
| 2 | Sol High | 99.5 | 74/112 | 112 | $570.67 | 584,503,039 | 35.52h |
| 3 | Gpt-5.5 Xhigh | 95.5 | 71/112 | 112 | $657.99 | 808,271,685 | 41.92h |
| 4 | Terra Max | 95.5 | 71/112 | 112 | $438.51 | 1,172,734,604 | 51.29h |
| 5 | Sol Medium | 94.2 | 70/112 | 112 | $411.94 | 513,163,729 | 31.55h |
| 6 | Luna Max | 92.8 | 69/112 | 112 | $58.66 | 1,754,049,643 | 61.64h |
| 7 | Sol Low | 87.4 | 65/112 | 112 | $230.90 | 276,853,164 | 22.35h |
| 8 | Terra Xhigh | 83.4 | 62/112 | 112 | $220.23 | 594,703,992 | 32.95h |
| 9 | Gpt-5.5 High | 82.1 | 61/112 | 112 | $406.01 | 470,486,632 | 27.77h |
| 10 | Terra High | 80.7 | 60/112 | 112 | $127.01 | 332,758,636 | 22.28h |
| 11 | Luna High | 75.3 | 56/112 | 112 | $26.23 | 716,976,802 | 31.20h |

## Interpretation

- The endpoint provides model-level `score`, pass counts, task counts, tokens, wall time, and estimated cost.
- It does not expose the ten task-level outcomes, so `Weighted /100` cannot be recomputed from this API summary alone.
- Task-weighted rankings remain based on the repository's task matrix and weight snapshots; this report monitors the latest API summary.
- When source data is unchanged, the automation still updates its heartbeat without presenting it as a new benchmark batch.
- The raw API response is not stored in the public repository; only required model-summary fields are archived.

Archived API snapshots: **218**.
