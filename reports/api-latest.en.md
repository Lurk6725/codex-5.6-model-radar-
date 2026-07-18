# Codex Radar API Monitor — English

[简体中文](api-latest.zh-CN.md) · [Project home](../README.md) · [API history CSV](../data/api/model_iq_history.csv) · [Monitor status](../data/api/monitor_status.json)

**Last successful check:** `2026-07-18T16:38:46+00:00`  
**Current API snapshot:** `14d34344206c2cd5`  
**Source observation:** `2026-07-18T11:35:05.153982+08:00`  
**New snapshot detected:** no; the source returned the same snapshot  
**Models returned:** 9

> “Last successful check” confirms that the automation reached the API. “Source observation” is supplied by the upstream endpoint and may be older.

> This is a model-level summary from the Codex Radar API, not the project's task-level difficulty-weighted score.

## Current API model summary

| Rank | Model tier | Source score | Passed | Tasks | Cost | Total tokens | Wall time |
|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | Terra Max | 99.5 | 74/112 | 112 | $511.25 | 1,324,427,796 | 58.71h |
| 2 | Sol High | 95.5 | 71/112 | 112 | $625.35 | 814,854,923 | 44.86h |
| 3 | Sol Xhigh | 93.1 | 68/110 | 110 | $716.80 | 960,252,679 | 49.15h |
| 4 | Sol Medium | 90.1 | 67/112 | 112 | $394.13 | 506,812,733 | 33.89h |
| 5 | Gpt-5.5 High | 88.8 | 66/112 | 112 | $398.05 | 498,789,149 | 30.07h |
| 6 | Luna Max | 84.2 | 62/111 | 111 | $263.06 | 1,776,333,137 | 62.07h |
| 7 | Sol Low | 74.7 | 55/111 | 111 | $214.73 | 261,442,331 | 21.71h |
| 8 | Terra High | 67.3 | 50/112 | 112 | $147.51 | 328,878,757 | 23.23h |
| 9 | Luna High | 63.8 | 47/111 | 111 | $120.59 | 789,419,565 | 33.51h |

## Interpretation

- The endpoint provides model-level `score`, pass counts, task counts, tokens, wall time, and estimated cost.
- It does not expose the ten task-level outcomes, so `Weighted /100` cannot be recomputed from this API summary alone.
- Task-weighted rankings remain based on the repository's task matrix and weight snapshots; this report monitors the latest API summary.
- When source data is unchanged, the automation still updates its heartbeat without presenting it as a new benchmark batch.
- The raw API response is not stored in the public repository; only required model-summary fields are archived.

Archived API snapshots: **21**.
