# Codex Radar API Monitor / API 自动监控

[简体中文](#简体中文) · [English](#english)

<a id="简体中文"></a>
# Codex Radar API 自动监控 — 简体中文

[English](api-latest.en.md) · [项目首页](../README.md) · [API 历史 CSV](../data/api/model_iq_history.csv) · [监控状态](../data/api/monitor_status.json)

**最近成功检查：** `2026-07-30T07:22:29+00:00`  
**当前 API 快照：** `5df5d2d5a7cc8352`  
**源站观测时间：** `2026-07-22T06:57:20.626603+08:00`  
**本次发现新快照：** 是  
**返回模型数：** 11

> “最近成功检查”表示自动任务已正常访问 API；“源站观测时间”由上游接口提供，两者可能不同。

> 这是 Codex Radar API 返回的模型级摘要，不是本项目根据逐题矩阵计算的难度加权分。

## 当前 API 模型摘要

| 排名 | 模型档位 | 源站分数 | 通过 | 任务数 | 费用 | 总 Token | 耗时 |
|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | Sol Xhigh | 94.2 | 70/112 | 112 | $724.56 | 951,842,084 | 44.60h |
| 2 | Sol High | 92.8 | 69/112 | 112 | $574.11 | 744,939,894 | 39.60h |
| 3 | Terra Max | 92.8 | 69/112 | 112 | $544.79 | 1,437,279,264 | 55.55h |
| 4 | Gpt-5.5 Xhigh | 91.5 | 68/112 | 112 | $655.40 | 837,318,370 | 44.28h |
| 5 | Gpt-5.5 High | 90.1 | 67/112 | 112 | $435.07 | 543,243,441 | 31.16h |
| 6 | Sol Medium | 84.7 | 63/112 | 112 | $412.19 | 508,936,172 | 30.70h |
| 7 | Terra Xhigh | 83.4 | 62/112 | 112 | $271.43 | 648,408,416 | 33.78h |
| 8 | Luna Max | 80.7 | 60/112 | 112 | $276.53 | 1,887,152,871 | 63.55h |
| 9 | Sol Low | 79.4 | 59/112 | 112 | $240.90 | 279,839,169 | 21.79h |
| 10 | Terra High | 74 | 55/112 | 112 | $156.92 | 354,595,336 | 23.07h |
| 11 | Luna High | 63.2 | 47/112 | 112 | $123.14 | 810,277,878 | 36.06h |

## 口径说明

- 当前接口提供模型级 `score`、通过数、任务数、Token、耗时和估算费用。
- 当前接口没有返回十道任务的逐题通过矩阵，因此不能仅凭 API 摘要重新计算 `加权分 /100`。
- 加权排名仍以仓库中的逐题数据和权重快照为准；本报告用于自动监控源站最新摘要。
- 源站数据未变化时，自动任务仍会更新监控心跳，但不会把它描述成新的模型测试批次。
- 原始 API 响应不写入公开仓库，只保存必要的模型摘要字段。

当前已归档 API 快照数：**119**。


---

<a id="english"></a>
# Codex Radar API Monitor — English

[简体中文](api-latest.zh-CN.md) · [Project home](../README.md) · [API history CSV](../data/api/model_iq_history.csv) · [Monitor status](../data/api/monitor_status.json)

**Last successful check:** `2026-07-30T07:22:29+00:00`  
**Current API snapshot:** `5df5d2d5a7cc8352`  
**Source observation:** `2026-07-22T06:57:20.626603+08:00`  
**New snapshot detected:** yes  
**Models returned:** 11

> “Last successful check” confirms that the automation reached the API. “Source observation” is supplied by the upstream endpoint and may be older.

> This is a model-level summary from the Codex Radar API, not the project's task-level difficulty-weighted score.

## Current API model summary

| Rank | Model tier | Source score | Passed | Tasks | Cost | Total tokens | Wall time |
|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | Sol Xhigh | 94.2 | 70/112 | 112 | $724.56 | 951,842,084 | 44.60h |
| 2 | Sol High | 92.8 | 69/112 | 112 | $574.11 | 744,939,894 | 39.60h |
| 3 | Terra Max | 92.8 | 69/112 | 112 | $544.79 | 1,437,279,264 | 55.55h |
| 4 | Gpt-5.5 Xhigh | 91.5 | 68/112 | 112 | $655.40 | 837,318,370 | 44.28h |
| 5 | Gpt-5.5 High | 90.1 | 67/112 | 112 | $435.07 | 543,243,441 | 31.16h |
| 6 | Sol Medium | 84.7 | 63/112 | 112 | $412.19 | 508,936,172 | 30.70h |
| 7 | Terra Xhigh | 83.4 | 62/112 | 112 | $271.43 | 648,408,416 | 33.78h |
| 8 | Luna Max | 80.7 | 60/112 | 112 | $276.53 | 1,887,152,871 | 63.55h |
| 9 | Sol Low | 79.4 | 59/112 | 112 | $240.90 | 279,839,169 | 21.79h |
| 10 | Terra High | 74 | 55/112 | 112 | $156.92 | 354,595,336 | 23.07h |
| 11 | Luna High | 63.2 | 47/112 | 112 | $123.14 | 810,277,878 | 36.06h |

## Interpretation

- The endpoint provides model-level `score`, pass counts, task counts, tokens, wall time, and estimated cost.
- It does not expose the ten task-level outcomes, so `Weighted /100` cannot be recomputed from this API summary alone.
- Task-weighted rankings remain based on the repository's task matrix and weight snapshots; this report monitors the latest API summary.
- When source data is unchanged, the automation still updates its heartbeat without presenting it as a new benchmark batch.
- The raw API response is not stored in the public repository; only required model-summary fields are archived.

Archived API snapshots: **119**.

