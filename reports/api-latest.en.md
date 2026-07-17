# Codex Radar API Monitor — English

[简体中文](api-latest.zh-CN.md) · [Project home](../README.md) · [API history CSV](../data/api/model_iq_history.csv) · [Monitor status](../data/api/monitor_status.json)

**Last successful check:** `2026-07-17T08:30:23+00:00`  
**Current API snapshot:** `4ecd10ee9c029a65`  
**Source observation:** `2026-07-13T22:08:07.261261+08:00`  
**New snapshot detected:** yes  
**Models returned:** 9

> “Last successful check” confirms that the automation reached the API. “Source observation” is supplied by the upstream endpoint and may be older.

> This is a model-level summary from the Codex Radar API, not the project's task-level difficulty-weighted score.

## Current API model summary

| Rank | Model tier | Source score | Passed | Tasks | Cost | Total tokens | Wall time |
|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | Terra Max | 95.7 | 54/85 | 85 | $411.59 | 1,070,244,298 | 43.92h |
| 2 | Sol Xhigh | 93.6 | 64/103 | 103 | $702.23 | 942,352,637 | 47.15h |
| 3 | Luna Max | 93 | 58/94 | 94 | $218.84 | 1,480,530,254 | 51.51h |
| 4 | Sol High | 89.8 | 62/104 | 104 | $541.11 | 706,849,039 | 40.78h |
| 5 | Gpt-5.5 High | 84.9 | 62/110 | 110 | $387.37 | 486,362,154 | 50.30h |
| 6 | Sol Medium | 84.5 | 60/107 | 107 | $349.04 | 416,802,979 | 29.35h |
| 7 | Terra High | 77.9 | 46/89 | 89 | $117.53 | 269,890,085 | 20.42h |
| 8 | Sol Low | 73.1 | 49/101 | 101 | $192.79 | 214,750,123 | 17.89h |
| 9 | Luna High | 62.5 | 34/82 | 82 | $92.14 | 595,325,067 | 24.61h |

## Interpretation

- The endpoint provides model-level `score`, pass counts, task counts, tokens, wall time, and estimated cost.
- It does not expose the ten task-level outcomes, so `Weighted /100` cannot be recomputed from this API summary alone.
- Task-weighted rankings remain based on the repository's task matrix and weight snapshots; this report monitors the latest API summary.
- When source data is unchanged, the automation still updates its heartbeat without presenting it as a new benchmark batch.
- The raw API response is not stored in the public repository; only required model-summary fields are archived.

Archived API snapshots: **9**.
