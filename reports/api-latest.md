# Codex Radar API Monitor / API 自动监控

[简体中文](#简体中文) · [English](#english)

<a id="简体中文"></a>
# Codex Radar API 自动监控 — 简体中文

[English](api-latest.en.md) · [项目首页](../README.md) · [API 历史 CSV](../data/api/model_iq_history.csv) · [监控状态](../data/api/monitor_status.json)

**最近成功检查：** `2026-08-09T20:54:04+00:00`  
**当前 API 快照：** `eb03f1216a5bc8fa`  
**源站观测时间：** `2026-07-22T06:57:20.626603+08:00`  
**本次发现新快照：** 否；源站仍返回同一快照  
**返回模型数：** 11

> “最近成功检查”表示自动任务已正常访问 API；“源站观测时间”由上游接口提供，两者可能不同。

> 这是 Codex Radar API 返回的模型级摘要，不是本项目根据逐题矩阵计算的难度加权分。

## 当前 API 模型摘要

| 排名 | 模型档位 | 源站分数 | 通过 | 任务数 | 费用 | 总 Token | 耗时 |
|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | Sol Xhigh | 109 | 81/112 | 112 | $745.60 | 921,839,541 | 53.06h |
| 2 | Sol High | 99.5 | 74/112 | 112 | $569.21 | 592,274,890 | 35.95h |
| 3 | Terra Max | 96.9 | 72/112 | 112 | $438.71 | 1,185,200,821 | 52.07h |
| 4 | Gpt-5.5 Xhigh | 92.8 | 69/112 | 112 | $658.15 | 804,896,595 | 41.79h |
| 5 | Luna Max | 90.1 | 67/112 | 112 | $58.69 | 1,786,126,152 | 62.18h |
| 6 | Sol Low | 88.8 | 66/112 | 112 | $230.79 | 277,928,979 | 22.70h |
| 7 | Sol Medium | 87.4 | 65/112 | 112 | $410.15 | 457,753,326 | 30.52h |
| 8 | Gpt-5.5 High | 83.4 | 62/112 | 112 | $405.81 | 476,823,971 | 27.70h |
| 9 | Terra Xhigh | 82.1 | 61/112 | 112 | $220.24 | 595,491,811 | 33.27h |
| 10 | Luna High | 78 | 58/112 | 112 | $26.21 | 713,331,282 | 31.17h |
| 11 | Terra High | 78 | 58/112 | 112 | $127.08 | 331,866,916 | 22.59h |

## 口径说明

- 当前接口提供模型级 `score`、通过数、任务数、Token、耗时和估算费用。
- 当前接口没有返回十道任务的逐题通过矩阵，因此不能仅凭 API 摘要重新计算 `加权分 /100`。
- 加权排名仍以仓库中的逐题数据和权重快照为准；本报告用于自动监控源站最新摘要。
- 源站数据未变化时，自动任务仍会更新监控心跳，但不会把它描述成新的模型测试批次。
- 原始 API 响应不写入公开仓库，只保存必要的模型摘要字段。

当前已归档 API 快照数：**219**。


---

<a id="english"></a>
# Codex Radar API Monitor — English

[简体中文](api-latest.zh-CN.md) · [Project home](../README.md) · [API history CSV](../data/api/model_iq_history.csv) · [Monitor status](../data/api/monitor_status.json)

**Last successful check:** `2026-08-09T20:54:04+00:00`  
**Current API snapshot:** `eb03f1216a5bc8fa`  
**Source observation:** `2026-07-22T06:57:20.626603+08:00`  
**New snapshot detected:** no; the source returned the same snapshot  
**Models returned:** 11

> “Last successful check” confirms that the automation reached the API. “Source observation” is supplied by the upstream endpoint and may be older.

> This is a model-level summary from the Codex Radar API, not the project's task-level difficulty-weighted score.

## Current API model summary

| Rank | Model tier | Source score | Passed | Tasks | Cost | Total tokens | Wall time |
|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | Sol Xhigh | 109 | 81/112 | 112 | $745.60 | 921,839,541 | 53.06h |
| 2 | Sol High | 99.5 | 74/112 | 112 | $569.21 | 592,274,890 | 35.95h |
| 3 | Terra Max | 96.9 | 72/112 | 112 | $438.71 | 1,185,200,821 | 52.07h |
| 4 | Gpt-5.5 Xhigh | 92.8 | 69/112 | 112 | $658.15 | 804,896,595 | 41.79h |
| 5 | Luna Max | 90.1 | 67/112 | 112 | $58.69 | 1,786,126,152 | 62.18h |
| 6 | Sol Low | 88.8 | 66/112 | 112 | $230.79 | 277,928,979 | 22.70h |
| 7 | Sol Medium | 87.4 | 65/112 | 112 | $410.15 | 457,753,326 | 30.52h |
| 8 | Gpt-5.5 High | 83.4 | 62/112 | 112 | $405.81 | 476,823,971 | 27.70h |
| 9 | Terra Xhigh | 82.1 | 61/112 | 112 | $220.24 | 595,491,811 | 33.27h |
| 10 | Luna High | 78 | 58/112 | 112 | $26.21 | 713,331,282 | 31.17h |
| 11 | Terra High | 78 | 58/112 | 112 | $127.08 | 331,866,916 | 22.59h |

## Interpretation

- The endpoint provides model-level `score`, pass counts, task counts, tokens, wall time, and estimated cost.
- It does not expose the ten task-level outcomes, so `Weighted /100` cannot be recomputed from this API summary alone.
- Task-weighted rankings remain based on the repository's task matrix and weight snapshots; this report monitors the latest API summary.
- When source data is unchanged, the automation still updates its heartbeat without presenting it as a new benchmark batch.
- The raw API response is not stored in the public repository; only required model-summary fields are archived.

Archived API snapshots: **219**.

