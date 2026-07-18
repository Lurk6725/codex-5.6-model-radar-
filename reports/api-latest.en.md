# Codex Radar API Monitor — English

[简体中文](api-latest.zh-CN.md) · [Project home](../README.md) · [API history CSV](../data/api/model_iq_history.csv) · [Monitor status](../data/api/monitor_status.json)

**Last successful check:** `2026-07-18T19:54:27+00:00`  
**Current API snapshot:** `91f960004130fc66`  
**Source observation:** `2026-07-18T11:35:05.153982+08:00`  
**New snapshot detected:** yes  
**Models returned:** 9

> “Last successful check” confirms that the automation reached the API. “Source observation” is supplied by the upstream endpoint and may be older.

> This is a model-level summary from the Codex Radar API, not the project's task-level difficulty-weighted score.

## Current API model summary

| Rank | Model tier | Source score | Passed | Tasks | Cost | Total tokens | Wall time |
|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | Terra Max | 99.5 | 74/112 | 112 | $510.65 | 1,314,248,964 | 59.42h |
| 2 | Sol High | 94.2 | 70/112 | 112 | $624.09 | 813,069,841 | 44.76h |
| 3 | Sol Xhigh | 91.8 | 67/110 | 110 | $715.63 | 974,978,045 | 50.67h |
| 4 | Sol Medium | 90.1 | 67/112 | 112 | $391.81 | 492,993,337 | 34.08h |
| 5 | Gpt-5.5 High | 87.4 | 65/112 | 112 | $400.71 | 503,160,427 | 30.39h |
| 6 | Luna Max | 84.2 | 62/111 | 111 | $263.58 | 1,787,859,326 | 61.98h |
| 7 | Sol Low | 77.4 | 57/111 | 111 | $213.51 | 260,183,112 | 21.47h |
| 8 | Terra High | 67.3 | 50/112 | 112 | $144.94 | 322,432,936 | 23.12h |
| 9 | Luna High | 61.1 | 45/111 | 111 | $121.04 | 793,091,968 | 34.19h |

## Interpretation

- The endpoint provides model-level `score`, pass counts, task counts, tokens, wall time, and estimated cost.
- It does not expose the ten task-level outcomes, so `Weighted /100` cannot be recomputed from this API summary alone.
- Task-weighted rankings remain based on the repository's task matrix and weight snapshots; this report monitors the latest API summary.
- When source data is unchanged, the automation still updates its heartbeat without presenting it as a new benchmark batch.
- The raw API response is not stored in the public repository; only required model-summary fields are archived.

Archived API snapshots: **23**.
