# Codex Radar API Monitor / API 自动监控

[简体中文](#简体中文) · [English](#english)

<a id="简体中文"></a>
# Codex Radar API 自动监控 — 简体中文

[English](api-latest.en.md) · [项目首页](../README.md) · [API 历史 CSV](../data/api/model_iq_history.csv) · [监控状态](../data/api/monitor_status.json)

**最近成功检查：** `2026-07-24T21:30:54+00:00`  
**当前 API 快照：** `f63df3208badfa7f`  
**源站观测时间：** `2026-07-22T06:57:20.626603+08:00`  
**本次发现新快照：** 是  
**返回模型数：** 11

> “最近成功检查”表示自动任务已正常访问 API；“源站观测时间”由上游接口提供，两者可能不同。

> 这是 Codex Radar API 返回的模型级摘要，不是本项目根据逐题矩阵计算的难度加权分。

## 当前 API 模型摘要

| 排名 | 模型档位 | 源站分数 | 通过 | 任务数 | 费用 | 总 Token | 耗时 |
|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | Sol High | 96.9 | 72/112 | 112 | $631.23 | 859,931,277 | 39.40h |
| 2 | Sol Xhigh | 96.9 | 72/112 | 112 | $768.94 | 1,042,279,528 | 46.36h |
| 3 | Sol Medium | 95.5 | 71/112 | 112 | $429.65 | 546,039,617 | 30.17h |
| 4 | Terra Xhigh | 91.5 | 68/112 | 112 | $273.78 | 653,888,810 | 35.38h |
| 5 | Terra Max | 90.1 | 67/112 | 112 | $540.80 | 1,426,921,632 | 56.12h |
| 6 | Luna Max | 84.7 | 63/112 | 112 | $286.84 | 1,983,665,516 | 62.38h |
| 7 | Gpt-5.5 Xhigh | 83.4 | 62/112 | 112 | $654.83 | 842,802,131 | 45.77h |
| 8 | Gpt-5.5 High | 79.4 | 59/112 | 112 | $422.86 | 528,627,627 | 32.29h |
| 9 | Sol Low | 76.7 | 57/112 | 112 | $231.06 | 265,438,380 | 19.78h |
| 10 | Luna High | 70 | 52/112 | 112 | $110.68 | 707,039,669 | 32.07h |
| 11 | Terra High | 70 | 52/112 | 112 | $158.42 | 360,835,147 | 23.09h |

## 口径说明

- 当前接口提供模型级 `score`、通过数、任务数、Token、耗时和估算费用。
- 当前接口没有返回十道任务的逐题通过矩阵，因此不能仅凭 API 摘要重新计算 `加权分 /100`。
- 加权排名仍以仓库中的逐题数据和权重快照为准；本报告用于自动监控源站最新摘要。
- 源站数据未变化时，自动任务仍会更新监控心跳，但不会把它描述成新的模型测试批次。
- 原始 API 响应不写入公开仓库，只保存必要的模型摘要字段。

当前已归档 API 快照数：**74**。


---

<a id="english"></a>
# Codex Radar API Monitor — English

[简体中文](api-latest.zh-CN.md) · [Project home](../README.md) · [API history CSV](../data/api/model_iq_history.csv) · [Monitor status](../data/api/monitor_status.json)

**Last successful check:** `2026-07-24T21:30:54+00:00`  
**Current API snapshot:** `f63df3208badfa7f`  
**Source observation:** `2026-07-22T06:57:20.626603+08:00`  
**New snapshot detected:** yes  
**Models returned:** 11

> “Last successful check” confirms that the automation reached the API. “Source observation” is supplied by the upstream endpoint and may be older.

> This is a model-level summary from the Codex Radar API, not the project's task-level difficulty-weighted score.

## Current API model summary

| Rank | Model tier | Source score | Passed | Tasks | Cost | Total tokens | Wall time |
|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | Sol High | 96.9 | 72/112 | 112 | $631.23 | 859,931,277 | 39.40h |
| 2 | Sol Xhigh | 96.9 | 72/112 | 112 | $768.94 | 1,042,279,528 | 46.36h |
| 3 | Sol Medium | 95.5 | 71/112 | 112 | $429.65 | 546,039,617 | 30.17h |
| 4 | Terra Xhigh | 91.5 | 68/112 | 112 | $273.78 | 653,888,810 | 35.38h |
| 5 | Terra Max | 90.1 | 67/112 | 112 | $540.80 | 1,426,921,632 | 56.12h |
| 6 | Luna Max | 84.7 | 63/112 | 112 | $286.84 | 1,983,665,516 | 62.38h |
| 7 | Gpt-5.5 Xhigh | 83.4 | 62/112 | 112 | $654.83 | 842,802,131 | 45.77h |
| 8 | Gpt-5.5 High | 79.4 | 59/112 | 112 | $422.86 | 528,627,627 | 32.29h |
| 9 | Sol Low | 76.7 | 57/112 | 112 | $231.06 | 265,438,380 | 19.78h |
| 10 | Luna High | 70 | 52/112 | 112 | $110.68 | 707,039,669 | 32.07h |
| 11 | Terra High | 70 | 52/112 | 112 | $158.42 | 360,835,147 | 23.09h |

## Interpretation

- The endpoint provides model-level `score`, pass counts, task counts, tokens, wall time, and estimated cost.
- It does not expose the ten task-level outcomes, so `Weighted /100` cannot be recomputed from this API summary alone.
- Task-weighted rankings remain based on the repository's task matrix and weight snapshots; this report monitors the latest API summary.
- When source data is unchanged, the automation still updates its heartbeat without presenting it as a new benchmark batch.
- The raw API response is not stored in the public repository; only required model-summary fields are archived.

Archived API snapshots: **74**.

