# Codex Radar API Monitor / API 自动监控

[简体中文](#简体中文) · [English](#english)

<a id="简体中文"></a>
# Codex Radar API 自动监控 — 简体中文

[English](api-latest.en.md) · [项目首页](../README.md) · [API 历史 CSV](../data/api/model_iq_history.csv) · [监控状态](../data/api/monitor_status.json)

**最近成功检查：** `2026-07-30T04:23:28+00:00`  
**当前 API 快照：** `0c96e271de3a1e5c`  
**源站观测时间：** `2026-07-22T06:57:20.626603+08:00`  
**本次发现新快照：** 是  
**返回模型数：** 11

> “最近成功检查”表示自动任务已正常访问 API；“源站观测时间”由上游接口提供，两者可能不同。

> 这是 Codex Radar API 返回的模型级摘要，不是本项目根据逐题矩阵计算的难度加权分。

## 当前 API 模型摘要

| 排名 | 模型档位 | 源站分数 | 通过 | 任务数 | 费用 | 总 Token | 耗时 |
|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | Gpt-5.5 Xhigh | 96.9 | 72/112 | 112 | $663.49 | 849,296,889 | 45.12h |
| 2 | Terra Max | 95.5 | 71/112 | 112 | $545.30 | 1,438,412,583 | 55.27h |
| 3 | Sol Xhigh | 94.2 | 70/112 | 112 | $725.59 | 951,491,509 | 44.88h |
| 4 | Sol High | 92.8 | 69/112 | 112 | $573.87 | 744,519,473 | 39.67h |
| 5 | Gpt-5.5 High | 88.8 | 66/112 | 112 | $433.00 | 540,360,222 | 31.22h |
| 6 | Sol Medium | 84.7 | 63/112 | 112 | $410.82 | 508,801,056 | 30.74h |
| 7 | Terra Xhigh | 82.1 | 61/112 | 112 | $274.09 | 658,186,777 | 33.83h |
| 8 | Luna Max | 80.7 | 60/112 | 112 | $277.79 | 1,899,713,158 | 63.66h |
| 9 | Sol Low | 80.7 | 60/112 | 112 | $234.31 | 269,737,683 | 20.96h |
| 10 | Terra High | 72.6 | 54/112 | 112 | $156.67 | 354,655,158 | 23.17h |
| 11 | Luna High | 63.2 | 47/112 | 112 | $123.02 | 809,087,206 | 36.31h |

## 口径说明

- 当前接口提供模型级 `score`、通过数、任务数、Token、耗时和估算费用。
- 当前接口没有返回十道任务的逐题通过矩阵，因此不能仅凭 API 摘要重新计算 `加权分 /100`。
- 加权排名仍以仓库中的逐题数据和权重快照为准；本报告用于自动监控源站最新摘要。
- 源站数据未变化时，自动任务仍会更新监控心跳，但不会把它描述成新的模型测试批次。
- 原始 API 响应不写入公开仓库，只保存必要的模型摘要字段。

当前已归档 API 快照数：**118**。


---

<a id="english"></a>
# Codex Radar API Monitor — English

[简体中文](api-latest.zh-CN.md) · [Project home](../README.md) · [API history CSV](../data/api/model_iq_history.csv) · [Monitor status](../data/api/monitor_status.json)

**Last successful check:** `2026-07-30T04:23:28+00:00`  
**Current API snapshot:** `0c96e271de3a1e5c`  
**Source observation:** `2026-07-22T06:57:20.626603+08:00`  
**New snapshot detected:** yes  
**Models returned:** 11

> “Last successful check” confirms that the automation reached the API. “Source observation” is supplied by the upstream endpoint and may be older.

> This is a model-level summary from the Codex Radar API, not the project's task-level difficulty-weighted score.

## Current API model summary

| Rank | Model tier | Source score | Passed | Tasks | Cost | Total tokens | Wall time |
|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | Gpt-5.5 Xhigh | 96.9 | 72/112 | 112 | $663.49 | 849,296,889 | 45.12h |
| 2 | Terra Max | 95.5 | 71/112 | 112 | $545.30 | 1,438,412,583 | 55.27h |
| 3 | Sol Xhigh | 94.2 | 70/112 | 112 | $725.59 | 951,491,509 | 44.88h |
| 4 | Sol High | 92.8 | 69/112 | 112 | $573.87 | 744,519,473 | 39.67h |
| 5 | Gpt-5.5 High | 88.8 | 66/112 | 112 | $433.00 | 540,360,222 | 31.22h |
| 6 | Sol Medium | 84.7 | 63/112 | 112 | $410.82 | 508,801,056 | 30.74h |
| 7 | Terra Xhigh | 82.1 | 61/112 | 112 | $274.09 | 658,186,777 | 33.83h |
| 8 | Luna Max | 80.7 | 60/112 | 112 | $277.79 | 1,899,713,158 | 63.66h |
| 9 | Sol Low | 80.7 | 60/112 | 112 | $234.31 | 269,737,683 | 20.96h |
| 10 | Terra High | 72.6 | 54/112 | 112 | $156.67 | 354,655,158 | 23.17h |
| 11 | Luna High | 63.2 | 47/112 | 112 | $123.02 | 809,087,206 | 36.31h |

## Interpretation

- The endpoint provides model-level `score`, pass counts, task counts, tokens, wall time, and estimated cost.
- It does not expose the ten task-level outcomes, so `Weighted /100` cannot be recomputed from this API summary alone.
- Task-weighted rankings remain based on the repository's task matrix and weight snapshots; this report monitors the latest API summary.
- When source data is unchanged, the automation still updates its heartbeat without presenting it as a new benchmark batch.
- The raw API response is not stored in the public repository; only required model-summary fields are archived.

Archived API snapshots: **118**.

