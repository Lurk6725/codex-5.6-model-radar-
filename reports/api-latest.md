# Codex Radar API Monitor / API 自动监控

[简体中文](#简体中文) · [English](#english)

<a id="简体中文"></a>
# Codex Radar API 自动监控 — 简体中文

[English](api-latest.en.md) · [项目首页](../README.md) · [API 历史 CSV](../data/api/model_iq_history.csv) · [监控状态](../data/api/monitor_status.json)

**最近成功检查：** `2026-08-11T10:15:01+00:00`  
**当前 API 快照：** `5f8662df6250a4f0`  
**源站观测时间：** `2026-07-22T06:57:20.626603+08:00`  
**本次发现新快照：** 否；源站仍返回同一快照  
**返回模型数：** 11

> “最近成功检查”表示自动任务已正常访问 API；“源站观测时间”由上游接口提供，两者可能不同。

> 这是 Codex Radar API 返回的模型级摘要，不是本项目根据逐题矩阵计算的难度加权分。

## 当前 API 模型摘要

| 排名 | 模型档位 | 源站分数 | 通过 | 任务数 | 费用 | 总 Token | 耗时 |
|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | Sol Xhigh | 104.9 | 78/112 | 112 | $736.77 | 890,708,364 | 50.34h |
| 2 | Sol High | 102.2 | 76/112 | 112 | $565.61 | 644,482,608 | 38.56h |
| 3 | Terra Max | 99.5 | 74/112 | 112 | $438.32 | 1,189,073,303 | 53.21h |
| 4 | Sol Medium | 98.2 | 73/112 | 112 | $408.21 | 467,827,150 | 31.03h |
| 5 | Luna Max | 94.2 | 70/112 | 112 | $58.66 | 1,831,830,045 | 62.61h |
| 6 | Gpt-5.5 Xhigh | 92.8 | 69/112 | 112 | $655.95 | 785,679,470 | 40.93h |
| 7 | Gpt-5.5 High | 87.4 | 65/112 | 112 | $404.22 | 486,338,451 | 30.18h |
| 8 | Terra Xhigh | 86.1 | 64/112 | 112 | $219.57 | 545,181,751 | 30.92h |
| 9 | Sol Low | 84.7 | 63/112 | 112 | $229.69 | 275,504,478 | 22.43h |
| 10 | Terra High | 79.4 | 59/112 | 112 | $126.90 | 336,658,938 | 23.24h |
| 11 | Luna High | 72.6 | 54/112 | 112 | $26.18 | 747,779,026 | 33.55h |

## 口径说明

- 当前接口提供模型级 `score`、通过数、任务数、Token、耗时和估算费用。
- 当前接口没有返回十道任务的逐题通过矩阵，因此不能仅凭 API 摘要重新计算 `加权分 /100`。
- 加权排名仍以仓库中的逐题数据和权重快照为准；本报告用于自动监控源站最新摘要。
- 源站数据未变化时，自动任务仍会更新监控心跳，但不会把它描述成新的模型测试批次。
- 原始 API 响应不写入公开仓库，只保存必要的模型摘要字段。

当前已归档 API 快照数：**231**。


---

<a id="english"></a>
# Codex Radar API Monitor — English

[简体中文](api-latest.zh-CN.md) · [Project home](../README.md) · [API history CSV](../data/api/model_iq_history.csv) · [Monitor status](../data/api/monitor_status.json)

**Last successful check:** `2026-08-11T10:15:01+00:00`  
**Current API snapshot:** `5f8662df6250a4f0`  
**Source observation:** `2026-07-22T06:57:20.626603+08:00`  
**New snapshot detected:** no; the source returned the same snapshot  
**Models returned:** 11

> “Last successful check” confirms that the automation reached the API. “Source observation” is supplied by the upstream endpoint and may be older.

> This is a model-level summary from the Codex Radar API, not the project's task-level difficulty-weighted score.

## Current API model summary

| Rank | Model tier | Source score | Passed | Tasks | Cost | Total tokens | Wall time |
|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | Sol Xhigh | 104.9 | 78/112 | 112 | $736.77 | 890,708,364 | 50.34h |
| 2 | Sol High | 102.2 | 76/112 | 112 | $565.61 | 644,482,608 | 38.56h |
| 3 | Terra Max | 99.5 | 74/112 | 112 | $438.32 | 1,189,073,303 | 53.21h |
| 4 | Sol Medium | 98.2 | 73/112 | 112 | $408.21 | 467,827,150 | 31.03h |
| 5 | Luna Max | 94.2 | 70/112 | 112 | $58.66 | 1,831,830,045 | 62.61h |
| 6 | Gpt-5.5 Xhigh | 92.8 | 69/112 | 112 | $655.95 | 785,679,470 | 40.93h |
| 7 | Gpt-5.5 High | 87.4 | 65/112 | 112 | $404.22 | 486,338,451 | 30.18h |
| 8 | Terra Xhigh | 86.1 | 64/112 | 112 | $219.57 | 545,181,751 | 30.92h |
| 9 | Sol Low | 84.7 | 63/112 | 112 | $229.69 | 275,504,478 | 22.43h |
| 10 | Terra High | 79.4 | 59/112 | 112 | $126.90 | 336,658,938 | 23.24h |
| 11 | Luna High | 72.6 | 54/112 | 112 | $26.18 | 747,779,026 | 33.55h |

## Interpretation

- The endpoint provides model-level `score`, pass counts, task counts, tokens, wall time, and estimated cost.
- It does not expose the ten task-level outcomes, so `Weighted /100` cannot be recomputed from this API summary alone.
- Task-weighted rankings remain based on the repository's task matrix and weight snapshots; this report monitors the latest API summary.
- When source data is unchanged, the automation still updates its heartbeat without presenting it as a new benchmark batch.
- The raw API response is not stored in the public repository; only required model-summary fields are archived.

Archived API snapshots: **231**.

