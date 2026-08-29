# Codex Radar API Monitor / API 自动监控

[简体中文](#简体中文) · [English](#english)

<a id="简体中文"></a>
# Codex Radar API 自动监控 — 简体中文

[English](api-latest.en.md) · [项目首页](../README.md) · [API 历史 CSV](../data/api/model_iq_history.csv) · [监控状态](../data/api/monitor_status.json)

**最近成功检查：** `2026-08-29T18:54:40+00:00`  
**当前 API 快照：** `72ff55339680c9e0`  
**源站观测时间：** `2026-07-22T06:57:20.626603+08:00`  
**本次发现新快照：** 是  
**返回模型数：** 11

> “最近成功检查”表示自动任务已正常访问 API；“源站观测时间”由上游接口提供，两者可能不同。

> 这是 Codex Radar API 返回的模型级摘要，不是本项目根据逐题矩阵计算的难度加权分。

## 当前 API 模型摘要

| 排名 | 模型档位 | 源站分数 | 通过 | 任务数 | 费用 | 总 Token | 耗时 |
|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | Luna Max | 104.9 | 78/112 | 112 | $54.03 | 1,889,522,331 | 68.39h |
| 2 | Sol Medium | 103.6 | 77/112 | 112 | $313.24 | 420,862,084 | 29.06h |
| 3 | Terra Max | 103.6 | 77/112 | 112 | $426.13 | 1,218,908,604 | 57.70h |
| 4 | Sol Xhigh | 102.2 | 76/112 | 112 | $629.57 | 820,170,487 | 45.86h |
| 5 | Gpt-5.5 Xhigh | 100.9 | 75/112 | 112 | $642.63 | 823,204,950 | 43.31h |
| 6 | Sol High | 95.5 | 71/112 | 112 | $508.38 | 606,485,699 | 36.23h |
| 7 | Gpt-5.5 High | 87.4 | 65/112 | 112 | $400.13 | 507,954,066 | 31.17h |
| 8 | Terra Xhigh | 87.4 | 65/112 | 112 | $212.39 | 617,466,514 | 38.05h |
| 9 | Terra High | 82.1 | 61/112 | 112 | $122.93 | 345,200,718 | 26.01h |
| 10 | Sol Low | 79.4 | 59/112 | 112 | $172.35 | 211,148,475 | 17.12h |
| 11 | Luna High | 72.6 | 54/112 | 112 | $22.51 | 728,334,900 | 33.41h |

## 口径说明

- 当前接口提供模型级 `score`、通过数、任务数、Token、耗时和估算费用。
- 当前接口没有返回十道任务的逐题通过矩阵，因此不能仅凭 API 摘要重新计算 `加权分 /100`。
- 加权排名仍以仓库中的逐题数据和权重快照为准；本报告用于自动监控源站最新摘要。
- 源站数据未变化时，自动任务仍会更新监控心跳，但不会把它描述成新的模型测试批次。
- 原始 API 响应不写入公开仓库，只保存必要的模型摘要字段。

当前已归档 API 快照数：**376**。


---

<a id="english"></a>
# Codex Radar API Monitor — English

[简体中文](api-latest.zh-CN.md) · [Project home](../README.md) · [API history CSV](../data/api/model_iq_history.csv) · [Monitor status](../data/api/monitor_status.json)

**Last successful check:** `2026-08-29T18:54:40+00:00`  
**Current API snapshot:** `72ff55339680c9e0`  
**Source observation:** `2026-07-22T06:57:20.626603+08:00`  
**New snapshot detected:** yes  
**Models returned:** 11

> “Last successful check” confirms that the automation reached the API. “Source observation” is supplied by the upstream endpoint and may be older.

> This is a model-level summary from the Codex Radar API, not the project's task-level difficulty-weighted score.

## Current API model summary

| Rank | Model tier | Source score | Passed | Tasks | Cost | Total tokens | Wall time |
|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | Luna Max | 104.9 | 78/112 | 112 | $54.03 | 1,889,522,331 | 68.39h |
| 2 | Sol Medium | 103.6 | 77/112 | 112 | $313.24 | 420,862,084 | 29.06h |
| 3 | Terra Max | 103.6 | 77/112 | 112 | $426.13 | 1,218,908,604 | 57.70h |
| 4 | Sol Xhigh | 102.2 | 76/112 | 112 | $629.57 | 820,170,487 | 45.86h |
| 5 | Gpt-5.5 Xhigh | 100.9 | 75/112 | 112 | $642.63 | 823,204,950 | 43.31h |
| 6 | Sol High | 95.5 | 71/112 | 112 | $508.38 | 606,485,699 | 36.23h |
| 7 | Gpt-5.5 High | 87.4 | 65/112 | 112 | $400.13 | 507,954,066 | 31.17h |
| 8 | Terra Xhigh | 87.4 | 65/112 | 112 | $212.39 | 617,466,514 | 38.05h |
| 9 | Terra High | 82.1 | 61/112 | 112 | $122.93 | 345,200,718 | 26.01h |
| 10 | Sol Low | 79.4 | 59/112 | 112 | $172.35 | 211,148,475 | 17.12h |
| 11 | Luna High | 72.6 | 54/112 | 112 | $22.51 | 728,334,900 | 33.41h |

## Interpretation

- The endpoint provides model-level `score`, pass counts, task counts, tokens, wall time, and estimated cost.
- It does not expose the ten task-level outcomes, so `Weighted /100` cannot be recomputed from this API summary alone.
- Task-weighted rankings remain based on the repository's task matrix and weight snapshots; this report monitors the latest API summary.
- When source data is unchanged, the automation still updates its heartbeat without presenting it as a new benchmark batch.
- The raw API response is not stored in the public repository; only required model-summary fields are archived.

Archived API snapshots: **376**.

