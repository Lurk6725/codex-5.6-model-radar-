# Codex Radar API Monitor / API 自动监控

[简体中文](#简体中文) · [English](#english)

<a id="简体中文"></a>
# Codex Radar API 自动监控 — 简体中文

[English](api-latest.en.md) · [项目首页](../README.md) · [API 历史 CSV](../data/api/model_iq_history.csv) · [监控状态](../data/api/monitor_status.json)

**最近成功检查：** `2026-07-24T14:16:09+00:00`  
**当前 API 快照：** `5649c10f8ce9daf3`  
**源站观测时间：** `2026-07-22T06:57:20.626603+08:00`  
**本次发现新快照：** 是  
**返回模型数：** 11

> “最近成功检查”表示自动任务已正常访问 API；“源站观测时间”由上游接口提供，两者可能不同。

> 这是 Codex Radar API 返回的模型级摘要，不是本项目根据逐题矩阵计算的难度加权分。

## 当前 API 模型摘要

| 排名 | 模型档位 | 源站分数 | 通过 | 任务数 | 费用 | 总 Token | 耗时 |
|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | Sol High | 96.9 | 72/112 | 112 | $631.67 | 854,207,062 | 39.59h |
| 2 | Sol Medium | 96.9 | 72/112 | 112 | $429.19 | 545,272,251 | 30.23h |
| 3 | Sol Xhigh | 94.2 | 70/112 | 112 | $767.98 | 1,041,666,787 | 46.38h |
| 4 | Terra Max | 91.5 | 68/112 | 112 | $538.61 | 1,413,971,331 | 55.35h |
| 5 | Terra Xhigh | 91.5 | 68/112 | 112 | $273.60 | 653,595,445 | 35.39h |
| 6 | Gpt-5.5 Xhigh | 84.7 | 63/112 | 112 | $653.26 | 839,779,854 | 45.76h |
| 7 | Luna Max | 84.7 | 63/112 | 112 | $285.55 | 1,973,251,568 | 62.08h |
| 8 | Gpt-5.5 High | 79.4 | 59/112 | 112 | $428.50 | 538,763,054 | 32.92h |
| 9 | Sol Low | 76.7 | 57/112 | 112 | $231.85 | 266,219,727 | 19.67h |
| 10 | Luna High | 70 | 52/112 | 112 | $110.95 | 706,997,733 | 32.25h |
| 11 | Terra High | 67.3 | 50/112 | 112 | $155.66 | 351,441,083 | 22.79h |

## 口径说明

- 当前接口提供模型级 `score`、通过数、任务数、Token、耗时和估算费用。
- 当前接口没有返回十道任务的逐题通过矩阵，因此不能仅凭 API 摘要重新计算 `加权分 /100`。
- 加权排名仍以仓库中的逐题数据和权重快照为准；本报告用于自动监控源站最新摘要。
- 源站数据未变化时，自动任务仍会更新监控心跳，但不会把它描述成新的模型测试批次。
- 原始 API 响应不写入公开仓库，只保存必要的模型摘要字段。

当前已归档 API 快照数：**70**。


---

<a id="english"></a>
# Codex Radar API Monitor — English

[简体中文](api-latest.zh-CN.md) · [Project home](../README.md) · [API history CSV](../data/api/model_iq_history.csv) · [Monitor status](../data/api/monitor_status.json)

**Last successful check:** `2026-07-24T14:16:09+00:00`  
**Current API snapshot:** `5649c10f8ce9daf3`  
**Source observation:** `2026-07-22T06:57:20.626603+08:00`  
**New snapshot detected:** yes  
**Models returned:** 11

> “Last successful check” confirms that the automation reached the API. “Source observation” is supplied by the upstream endpoint and may be older.

> This is a model-level summary from the Codex Radar API, not the project's task-level difficulty-weighted score.

## Current API model summary

| Rank | Model tier | Source score | Passed | Tasks | Cost | Total tokens | Wall time |
|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | Sol High | 96.9 | 72/112 | 112 | $631.67 | 854,207,062 | 39.59h |
| 2 | Sol Medium | 96.9 | 72/112 | 112 | $429.19 | 545,272,251 | 30.23h |
| 3 | Sol Xhigh | 94.2 | 70/112 | 112 | $767.98 | 1,041,666,787 | 46.38h |
| 4 | Terra Max | 91.5 | 68/112 | 112 | $538.61 | 1,413,971,331 | 55.35h |
| 5 | Terra Xhigh | 91.5 | 68/112 | 112 | $273.60 | 653,595,445 | 35.39h |
| 6 | Gpt-5.5 Xhigh | 84.7 | 63/112 | 112 | $653.26 | 839,779,854 | 45.76h |
| 7 | Luna Max | 84.7 | 63/112 | 112 | $285.55 | 1,973,251,568 | 62.08h |
| 8 | Gpt-5.5 High | 79.4 | 59/112 | 112 | $428.50 | 538,763,054 | 32.92h |
| 9 | Sol Low | 76.7 | 57/112 | 112 | $231.85 | 266,219,727 | 19.67h |
| 10 | Luna High | 70 | 52/112 | 112 | $110.95 | 706,997,733 | 32.25h |
| 11 | Terra High | 67.3 | 50/112 | 112 | $155.66 | 351,441,083 | 22.79h |

## Interpretation

- The endpoint provides model-level `score`, pass counts, task counts, tokens, wall time, and estimated cost.
- It does not expose the ten task-level outcomes, so `Weighted /100` cannot be recomputed from this API summary alone.
- Task-weighted rankings remain based on the repository's task matrix and weight snapshots; this report monitors the latest API summary.
- When source data is unchanged, the automation still updates its heartbeat without presenting it as a new benchmark batch.
- The raw API response is not stored in the public repository; only required model-summary fields are archived.

Archived API snapshots: **70**.

