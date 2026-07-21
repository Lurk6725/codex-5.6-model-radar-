# Codex Radar API Monitor / API 自动监控

[简体中文](#简体中文) · [English](#english)

<a id="简体中文"></a>
# Codex Radar API 自动监控 — 简体中文

[English](api-latest.en.md) · [项目首页](../README.md) · [API 历史 CSV](../data/api/model_iq_history.csv) · [监控状态](../data/api/monitor_status.json)

**最近成功检查：** `2026-07-21T16:08:03+00:00`  
**当前 API 快照：** `6cb9413586f1f8ea`  
**源站观测时间：** `2026-07-18T11:35:05.153982+08:00`  
**本次发现新快照：** 是  
**返回模型数：** 11

> “最近成功检查”表示自动任务已正常访问 API；“源站观测时间”由上游接口提供，两者可能不同。

> 这是 Codex Radar API 返回的模型级摘要，不是本项目根据逐题矩阵计算的难度加权分。

## 当前 API 模型摘要

| 排名 | 模型档位 | 源站分数 | 通过 | 任务数 | 费用 | 总 Token | 耗时 |
|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | Terra Max | 99.5 | 74/112 | 112 | $519.26 | 1,344,439,659 | 62.44h |
| 2 | Sol Xhigh | 96.4 | 71/111 | 111 | $772.74 | 1,043,997,748 | 53.89h |
| 3 | Gpt-5.5 Xhigh | 95.5 | 71/112 | 112 | $651.63 | 837,637,971 | 42.07h |
| 4 | Luna Max | 94.2 | 70/112 | 112 | $281.16 | 1,928,059,480 | 66.53h |
| 5 | Sol High | 92.8 | 69/112 | 112 | $571.13 | 730,405,605 | 42.78h |
| 6 | Sol Medium | 92.8 | 69/112 | 112 | $397.59 | 491,674,340 | 34.02h |
| 7 | Terra Xhigh | 92.8 | 69/112 | 112 | $283.58 | 696,455,008 | 37.71h |
| 8 | Gpt-5.5 High | 80.7 | 60/112 | 112 | $403.31 | 505,166,061 | 30.41h |
| 9 | Sol Low | 74.7 | 55/111 | 111 | $228.61 | 264,985,642 | 23.74h |
| 10 | Luna High | 71.3 | 53/112 | 112 | $121.67 | 797,408,040 | 36.27h |
| 11 | Terra High | 68.6 | 51/112 | 112 | $147.17 | 330,950,087 | 25.12h |

## 口径说明

- 当前接口提供模型级 `score`、通过数、任务数、Token、耗时和估算费用。
- 当前接口没有返回十道任务的逐题通过矩阵，因此不能仅凭 API 摘要重新计算 `加权分 /100`。
- 加权排名仍以仓库中的逐题数据和权重快照为准；本报告用于自动监控源站最新摘要。
- 源站数据未变化时，自动任务仍会更新监控心跳，但不会把它描述成新的模型测试批次。
- 原始 API 响应不写入公开仓库，只保存必要的模型摘要字段。

当前已归档 API 快照数：**44**。


---

<a id="english"></a>
# Codex Radar API Monitor — English

[简体中文](api-latest.zh-CN.md) · [Project home](../README.md) · [API history CSV](../data/api/model_iq_history.csv) · [Monitor status](../data/api/monitor_status.json)

**Last successful check:** `2026-07-21T16:08:03+00:00`  
**Current API snapshot:** `6cb9413586f1f8ea`  
**Source observation:** `2026-07-18T11:35:05.153982+08:00`  
**New snapshot detected:** yes  
**Models returned:** 11

> “Last successful check” confirms that the automation reached the API. “Source observation” is supplied by the upstream endpoint and may be older.

> This is a model-level summary from the Codex Radar API, not the project's task-level difficulty-weighted score.

## Current API model summary

| Rank | Model tier | Source score | Passed | Tasks | Cost | Total tokens | Wall time |
|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | Terra Max | 99.5 | 74/112 | 112 | $519.26 | 1,344,439,659 | 62.44h |
| 2 | Sol Xhigh | 96.4 | 71/111 | 111 | $772.74 | 1,043,997,748 | 53.89h |
| 3 | Gpt-5.5 Xhigh | 95.5 | 71/112 | 112 | $651.63 | 837,637,971 | 42.07h |
| 4 | Luna Max | 94.2 | 70/112 | 112 | $281.16 | 1,928,059,480 | 66.53h |
| 5 | Sol High | 92.8 | 69/112 | 112 | $571.13 | 730,405,605 | 42.78h |
| 6 | Sol Medium | 92.8 | 69/112 | 112 | $397.59 | 491,674,340 | 34.02h |
| 7 | Terra Xhigh | 92.8 | 69/112 | 112 | $283.58 | 696,455,008 | 37.71h |
| 8 | Gpt-5.5 High | 80.7 | 60/112 | 112 | $403.31 | 505,166,061 | 30.41h |
| 9 | Sol Low | 74.7 | 55/111 | 111 | $228.61 | 264,985,642 | 23.74h |
| 10 | Luna High | 71.3 | 53/112 | 112 | $121.67 | 797,408,040 | 36.27h |
| 11 | Terra High | 68.6 | 51/112 | 112 | $147.17 | 330,950,087 | 25.12h |

## Interpretation

- The endpoint provides model-level `score`, pass counts, task counts, tokens, wall time, and estimated cost.
- It does not expose the ten task-level outcomes, so `Weighted /100` cannot be recomputed from this API summary alone.
- Task-weighted rankings remain based on the repository's task matrix and weight snapshots; this report monitors the latest API summary.
- When source data is unchanged, the automation still updates its heartbeat without presenting it as a new benchmark batch.
- The raw API response is not stored in the public repository; only required model-summary fields are archived.

Archived API snapshots: **44**.

