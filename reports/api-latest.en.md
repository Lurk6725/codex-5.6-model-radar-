# Codex Radar API Monitor — English

[简体中文](api-latest.zh-CN.md) · [Project home](../README.md) · [API history CSV](../data/api/model_iq_history.csv) · [Monitor status](../data/api/monitor_status.json)

**Last successful check:** `2026-07-25T20:00:31+00:00`  
**Current API snapshot:** `020a13e01401bd73`  
**Source observation:** `2026-07-22T06:57:20.626603+08:00`  
**New snapshot detected:** yes  
**Models returned:** 11

> “Last successful check” confirms that the automation reached the API. “Source observation” is supplied by the upstream endpoint and may be older.

> This is a model-level summary from the Codex Radar API, not the project's task-level difficulty-weighted score.

## Current API model summary

| Rank | Model tier | Source score | Passed | Tasks | Cost | Total tokens | Wall time |
|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | Sol Xhigh | 96.9 | 72/112 | 112 | $791.11 | 1,080,504,146 | 47.74h |
| 2 | Sol Medium | 95.5 | 71/112 | 112 | $439.95 | 565,443,224 | 30.67h |
| 3 | Sol High | 92.8 | 69/112 | 112 | $581.41 | 770,817,987 | 34.83h |
| 4 | Terra Max | 90.1 | 67/112 | 112 | $567.76 | 1,494,948,012 | 58.60h |
| 5 | Terra Xhigh | 88.8 | 66/112 | 112 | $283.56 | 688,057,620 | 37.30h |
| 6 | Luna Max | 86.1 | 64/112 | 112 | $287.40 | 1,986,853,701 | 61.43h |
| 7 | Gpt-5.5 Xhigh | 82.1 | 61/112 | 112 | $650.28 | 835,217,984 | 44.46h |
| 8 | Gpt-5.5 High | 80.7 | 60/112 | 112 | $417.19 | 519,575,381 | 32.17h |
| 9 | Sol Low | 75.3 | 56/112 | 112 | $234.35 | 267,101,872 | 20.16h |
| 10 | Terra High | 72.6 | 54/112 | 112 | $156.68 | 355,890,940 | 23.41h |
| 11 | Luna High | 67.3 | 50/112 | 112 | $114.08 | 734,739,298 | 32.18h |

## Interpretation

- The endpoint provides model-level `score`, pass counts, task counts, tokens, wall time, and estimated cost.
- It does not expose the ten task-level outcomes, so `Weighted /100` cannot be recomputed from this API summary alone.
- Task-weighted rankings remain based on the repository's task matrix and weight snapshots; this report monitors the latest API summary.
- When source data is unchanged, the automation still updates its heartbeat without presenting it as a new benchmark batch.
- The raw API response is not stored in the public repository; only required model-summary fields are archived.

Archived API snapshots: **83**.
