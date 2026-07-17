# Codex Radar API Monitor — English

[简体中文](api-latest.zh-CN.md) · [Project home](../README.md) · [API history CSV](../data/api/model_iq_history.csv) · [Monitor status](../data/api/monitor_status.json)

**Last successful check:** `2026-07-17T15:45:27+00:00`  
**Current API snapshot:** `ba4a8b85182c4dee`  
**Source observation:** `2026-07-13T22:08:07.261261+08:00`  
**New snapshot detected:** yes  
**Models returned:** 9

> “Last successful check” confirms that the automation reached the API. “Source observation” is supplied by the upstream endpoint and may be older.

> This is a model-level summary from the Codex Radar API, not the project's task-level difficulty-weighted score.

## Current API model summary

| Rank | Model tier | Source score | Passed | Tasks | Cost | Total tokens | Wall time |
|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | Terra Max | 96.1 | 67/105 | 105 | $485.67 | 1,252,333,023 | 51.40h |
| 2 | Sol Xhigh | 95.8 | 68/107 | 107 | $729.49 | 999,902,342 | 48.85h |
| 3 | Sol High | 94.5 | 69/110 | 110 | $585.46 | 751,123,445 | 42.58h |
| 4 | Luna Max | 89 | 62/105 | 105 | $246.46 | 1,652,390,901 | 57.50h |
| 5 | Sol Medium | 88.2 | 65/111 | 111 | $383.10 | 478,834,764 | 32.02h |
| 6 | Sol Low | 80.2 | 58/109 | 109 | $210.76 | 256,591,378 | 20.80h |
| 7 | Gpt-5.5 High | 78.7 | 58/111 | 111 | $392.69 | 495,386,374 | 38.87h |
| 8 | Terra High | 75.3 | 52/104 | 104 | $136.23 | 315,089,839 | 23.02h |
| 9 | Luna High | 61.4 | 44/108 | 108 | $122.70 | 799,896,566 | 32.38h |

## Interpretation

- The endpoint provides model-level `score`, pass counts, task counts, tokens, wall time, and estimated cost.
- It does not expose the ten task-level outcomes, so `Weighted /100` cannot be recomputed from this API summary alone.
- Task-weighted rankings remain based on the repository's task matrix and weight snapshots; this report monitors the latest API summary.
- When source data is unchanged, the automation still updates its heartbeat without presenting it as a new benchmark batch.
- The raw API response is not stored in the public repository; only required model-summary fields are archived.

Archived API snapshots: **13**.
