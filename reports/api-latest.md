# Codex Radar API Monitor / API 自动监控

[简体中文](#简体中文) · [English](#english)

<a id="简体中文"></a>
# Codex Radar API 自动监控 — 简体中文

[English](api-latest.en.md) · [项目首页](../README.md) · [API 历史 CSV](../data/api/model_iq_history.csv) · [监控状态](../data/api/monitor_status.json)

**最近成功检查：** `2026-08-18T09:51:02+00:00`  
**当前 API 快照：** `a041b3ad072c33bb`  
**源站观测时间：** `2026-07-22T06:57:20.626603+08:00`  
**本次发现新快照：** 否；源站仍返回同一快照  
**返回模型数：** 11

> “最近成功检查”表示自动任务已正常访问 API；“源站观测时间”由上游接口提供，两者可能不同。

> 这是 Codex Radar API 返回的模型级摘要，不是本项目根据逐题矩阵计算的难度加权分。

## 当前 API 模型摘要

| 排名 | 模型档位 | 源站分数 | 通过 | 任务数 | 费用 | 总 Token | 耗时 |
|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | Terra Max | 99.5 | 74/112 | 112 | $436.14 | 1,271,216,961 | 60.31h |
| 2 | Sol Xhigh | 98.2 | 73/112 | 112 | $729.57 | 846,042,232 | 45.24h |
| 3 | Gpt-5.5 Xhigh | 94.2 | 70/112 | 112 | $654.66 | 768,592,836 | 42.11h |
| 4 | Luna Max | 92.8 | 69/112 | 112 | $58.81 | 1,781,414,081 | 63.71h |
| 5 | Sol High | 91.5 | 68/112 | 112 | $538.21 | 639,355,346 | 36.21h |
| 6 | Gpt-5.5 High | 90.1 | 67/112 | 112 | $403.46 | 495,804,840 | 33.23h |
| 7 | Terra Xhigh | 86.1 | 64/112 | 112 | $216.95 | 605,158,740 | 39.18h |
| 8 | Sol Medium | 84.7 | 63/112 | 112 | $392.17 | 488,309,629 | 33.95h |
| 9 | Luna High | 75.3 | 56/112 | 112 | $26.13 | 768,411,852 | 35.11h |
| 10 | Terra High | 74 | 55/112 | 112 | $126.37 | 348,564,925 | 26.65h |
| 11 | Sol Low | 68.6 | 51/112 | 112 | $225.77 | 276,296,616 | 24.23h |

## 口径说明

- 当前接口提供模型级 `score`、通过数、任务数、Token、耗时和估算费用。
- 当前接口没有返回十道任务的逐题通过矩阵，因此不能仅凭 API 摘要重新计算 `加权分 /100`。
- 加权排名仍以仓库中的逐题数据和权重快照为准；本报告用于自动监控源站最新摘要。
- 源站数据未变化时，自动任务仍会更新监控心跳，但不会把它描述成新的模型测试批次。
- 原始 API 响应不写入公开仓库，只保存必要的模型摘要字段。

当前已归档 API 快照数：**289**。


---

<a id="english"></a>
# Codex Radar API Monitor — English

[简体中文](api-latest.zh-CN.md) · [Project home](../README.md) · [API history CSV](../data/api/model_iq_history.csv) · [Monitor status](../data/api/monitor_status.json)

**Last successful check:** `2026-08-18T09:51:02+00:00`  
**Current API snapshot:** `a041b3ad072c33bb`  
**Source observation:** `2026-07-22T06:57:20.626603+08:00`  
**New snapshot detected:** no; the source returned the same snapshot  
**Models returned:** 11

> “Last successful check” confirms that the automation reached the API. “Source observation” is supplied by the upstream endpoint and may be older.

> This is a model-level summary from the Codex Radar API, not the project's task-level difficulty-weighted score.

## Current API model summary

| Rank | Model tier | Source score | Passed | Tasks | Cost | Total tokens | Wall time |
|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | Terra Max | 99.5 | 74/112 | 112 | $436.14 | 1,271,216,961 | 60.31h |
| 2 | Sol Xhigh | 98.2 | 73/112 | 112 | $729.57 | 846,042,232 | 45.24h |
| 3 | Gpt-5.5 Xhigh | 94.2 | 70/112 | 112 | $654.66 | 768,592,836 | 42.11h |
| 4 | Luna Max | 92.8 | 69/112 | 112 | $58.81 | 1,781,414,081 | 63.71h |
| 5 | Sol High | 91.5 | 68/112 | 112 | $538.21 | 639,355,346 | 36.21h |
| 6 | Gpt-5.5 High | 90.1 | 67/112 | 112 | $403.46 | 495,804,840 | 33.23h |
| 7 | Terra Xhigh | 86.1 | 64/112 | 112 | $216.95 | 605,158,740 | 39.18h |
| 8 | Sol Medium | 84.7 | 63/112 | 112 | $392.17 | 488,309,629 | 33.95h |
| 9 | Luna High | 75.3 | 56/112 | 112 | $26.13 | 768,411,852 | 35.11h |
| 10 | Terra High | 74 | 55/112 | 112 | $126.37 | 348,564,925 | 26.65h |
| 11 | Sol Low | 68.6 | 51/112 | 112 | $225.77 | 276,296,616 | 24.23h |

## Interpretation

- The endpoint provides model-level `score`, pass counts, task counts, tokens, wall time, and estimated cost.
- It does not expose the ten task-level outcomes, so `Weighted /100` cannot be recomputed from this API summary alone.
- Task-weighted rankings remain based on the repository's task matrix and weight snapshots; this report monitors the latest API summary.
- When source data is unchanged, the automation still updates its heartbeat without presenting it as a new benchmark batch.
- The raw API response is not stored in the public repository; only required model-summary fields are archived.

Archived API snapshots: **289**.

