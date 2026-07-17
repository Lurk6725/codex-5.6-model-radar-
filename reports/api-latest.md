# Codex Radar API Monitor / API 自动监控

[简体中文](#简体中文) · [English](#english)

<a id="简体中文"></a>
# Codex Radar API 自动监控 — 简体中文

[English](api-latest.en.md) · [项目首页](../README.md) · [API 历史 CSV](../data/api/model_iq_history.csv) · [监控状态](../data/api/monitor_status.json)

**最近成功检查：** `2026-07-17T11:59:32+00:00`  
**当前 API 快照：** `9058c9a04116e626`  
**源站观测时间：** `2026-07-13T22:08:07.261261+08:00`  
**本次发现新快照：** 是  
**返回模型数：** 9

> “最近成功检查”表示自动任务已正常访问 API；“源站观测时间”由上游接口提供，两者可能不同。

> 这是 Codex Radar API 返回的模型级摘要，不是本项目根据逐题矩阵计算的难度加权分。

## 当前 API 模型摘要

| 排名 | 模型档位 | 源站分数 | 通过 | 任务数 | 费用 | 总 Token | 耗时 |
|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | Terra Max | 97.3 | 62/96 | 96 | $460.10 | 1,190,621,148 | 48.61h |
| 2 | Sol Xhigh | 95.8 | 68/107 | 107 | $743.55 | 1,013,556,726 | 49.94h |
| 3 | Sol High | 91.8 | 64/105 | 105 | $555.72 | 716,181,775 | 41.30h |
| 4 | Luna Max | 90.1 | 61/102 | 102 | $238.61 | 1,594,280,542 | 56.05h |
| 5 | Sol Medium | 86.3 | 63/110 | 110 | $374.58 | 454,524,256 | 31.51h |
| 6 | Gpt-5.5 High | 85.5 | 63/111 | 111 | $397.83 | 501,890,340 | 46.06h |
| 7 | Terra High | 75.3 | 48/96 | 96 | $124.03 | 284,939,459 | 21.32h |
| 8 | Sol Low | 73.2 | 52/107 | 107 | $198.72 | 236,740,602 | 19.94h |
| 9 | Luna High | 60.6 | 39/97 | 97 | $111.11 | 719,669,227 | 29.38h |

## 口径说明

- 当前接口提供模型级 `score`、通过数、任务数、Token、耗时和估算费用。
- 当前接口没有返回十道任务的逐题通过矩阵，因此不能仅凭 API 摘要重新计算 `加权分 /100`。
- 加权排名仍以仓库中的逐题数据和权重快照为准；本报告用于自动监控源站最新摘要。
- 源站数据未变化时，自动任务仍会更新监控心跳，但不会把它描述成新的模型测试批次。
- 原始 API 响应不写入公开仓库，只保存必要的模型摘要字段。

当前已归档 API 快照数：**11**。


---

<a id="english"></a>
# Codex Radar API Monitor — English

[简体中文](api-latest.zh-CN.md) · [Project home](../README.md) · [API history CSV](../data/api/model_iq_history.csv) · [Monitor status](../data/api/monitor_status.json)

**Last successful check:** `2026-07-17T11:59:32+00:00`  
**Current API snapshot:** `9058c9a04116e626`  
**Source observation:** `2026-07-13T22:08:07.261261+08:00`  
**New snapshot detected:** yes  
**Models returned:** 9

> “Last successful check” confirms that the automation reached the API. “Source observation” is supplied by the upstream endpoint and may be older.

> This is a model-level summary from the Codex Radar API, not the project's task-level difficulty-weighted score.

## Current API model summary

| Rank | Model tier | Source score | Passed | Tasks | Cost | Total tokens | Wall time |
|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | Terra Max | 97.3 | 62/96 | 96 | $460.10 | 1,190,621,148 | 48.61h |
| 2 | Sol Xhigh | 95.8 | 68/107 | 107 | $743.55 | 1,013,556,726 | 49.94h |
| 3 | Sol High | 91.8 | 64/105 | 105 | $555.72 | 716,181,775 | 41.30h |
| 4 | Luna Max | 90.1 | 61/102 | 102 | $238.61 | 1,594,280,542 | 56.05h |
| 5 | Sol Medium | 86.3 | 63/110 | 110 | $374.58 | 454,524,256 | 31.51h |
| 6 | Gpt-5.5 High | 85.5 | 63/111 | 111 | $397.83 | 501,890,340 | 46.06h |
| 7 | Terra High | 75.3 | 48/96 | 96 | $124.03 | 284,939,459 | 21.32h |
| 8 | Sol Low | 73.2 | 52/107 | 107 | $198.72 | 236,740,602 | 19.94h |
| 9 | Luna High | 60.6 | 39/97 | 97 | $111.11 | 719,669,227 | 29.38h |

## Interpretation

- The endpoint provides model-level `score`, pass counts, task counts, tokens, wall time, and estimated cost.
- It does not expose the ten task-level outcomes, so `Weighted /100` cannot be recomputed from this API summary alone.
- Task-weighted rankings remain based on the repository's task matrix and weight snapshots; this report monitors the latest API summary.
- When source data is unchanged, the automation still updates its heartbeat without presenting it as a new benchmark batch.
- The raw API response is not stored in the public repository; only required model-summary fields are archived.

Archived API snapshots: **11**.

