# Codex Radar API Monitor — English

[简体中文](api-latest.zh-CN.md) · [Project home](../README.md) · [API history CSV](../data/api/model_iq_history.csv) · [Monitor status](../data/api/monitor_status.json)

**Last successful check:** `2026-07-21T21:34:54+00:00`  
**Current API snapshot:** `5098bcf8384abbbf`  
**Source observation:** `2026-07-18T11:35:05.153982+08:00`  
**New snapshot detected:** yes  
**Models returned:** 11

> “Last successful check” confirms that the automation reached the API. “Source observation” is supplied by the upstream endpoint and may be older.

> This is a model-level summary from the Codex Radar API, not the project's task-level difficulty-weighted score.

## Current API model summary

| Rank | Model tier | Source score | Passed | Tasks | Cost | Total tokens | Wall time |
|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | Terra Max | 102.2 | 76/112 | 112 | $524.81 | 1,360,465,083 | 63.22h |
| 2 | Luna Max | 96.9 | 72/112 | 112 | $281.27 | 1,935,130,197 | 66.96h |
| 3 | Gpt-5.5 Xhigh | 95.5 | 71/112 | 112 | $652.74 | 838,964,559 | 42.16h |
| 4 | Sol Xhigh | 95 | 70/111 | 111 | $771.11 | 1,040,456,202 | 53.36h |
| 5 | Sol High | 94.2 | 70/112 | 112 | $566.30 | 726,045,964 | 42.04h |
| 6 | Terra Xhigh | 94.2 | 70/112 | 112 | $276.22 | 668,081,867 | 37.18h |
| 7 | Sol Medium | 91.5 | 68/112 | 112 | $400.22 | 498,394,959 | 33.59h |
| 8 | Gpt-5.5 High | 78 | 58/112 | 112 | $405.70 | 508,373,778 | 30.18h |
| 9 | Sol Low | 76 | 56/111 | 111 | $228.78 | 265,014,892 | 23.72h |
| 10 | Luna High | 70 | 52/112 | 112 | $120.63 | 787,262,695 | 36.37h |
| 11 | Terra High | 65.9 | 49/112 | 112 | $144.76 | 325,922,203 | 25.68h |

## Interpretation

- The endpoint provides model-level `score`, pass counts, task counts, tokens, wall time, and estimated cost.
- It does not expose the ten task-level outcomes, so `Weighted /100` cannot be recomputed from this API summary alone.
- Task-weighted rankings remain based on the repository's task matrix and weight snapshots; this report monitors the latest API summary.
- When source data is unchanged, the automation still updates its heartbeat without presenting it as a new benchmark batch.
- The raw API response is not stored in the public repository; only required model-summary fields are archived.

Archived API snapshots: **47**.
