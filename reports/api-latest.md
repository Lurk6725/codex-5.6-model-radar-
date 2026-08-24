# Codex Radar API Monitor / API 自动监控

[简体中文](#简体中文) · [English](#english)

<a id="简体中文"></a>
# Codex Radar API 自动监控 — 简体中文

[English](api-latest.en.md) · [项目首页](../README.md) · [API 历史 CSV](../data/api/model_iq_history.csv) · [监控状态](../data/api/monitor_status.json)

**最近成功检查：** `2026-08-24T21:46:28+00:00`  
**当前 API 快照：** `941c09a8307d8a00`  
**源站观测时间：** `2026-07-22T06:57:20.626603+08:00`  
**本次发现新快照：** 是  
**返回模型数：** 11

> “最近成功检查”表示自动任务已正常访问 API；“源站观测时间”由上游接口提供，两者可能不同。

> 这是 Codex Radar API 返回的模型级摘要，不是本项目根据逐题矩阵计算的难度加权分。

## 当前 API 模型摘要

| 排名 | 模型档位 | 源站分数 | 通过 | 任务数 | 费用 | 总 Token | 耗时 |
|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | Sol Xhigh | 104.9 | 78/112 | 112 | $713.06 | 806,295,391 | 45.22h |
| 2 | Luna Max | 102.2 | 76/112 | 112 | $54.09 | 1,695,662,174 | 58.27h |
| 3 | Gpt-5.5 Xhigh | 100.9 | 75/112 | 112 | $647.85 | 774,677,760 | 40.53h |
| 4 | Terra Max | 95.5 | 71/112 | 112 | $425.52 | 1,161,065,574 | 54.82h |
| 5 | Gpt-5.5 High | 88.8 | 66/112 | 112 | $400.49 | 496,314,317 | 31.82h |
| 6 | Sol High | 86.1 | 64/112 | 112 | $530.43 | 572,020,545 | 34.65h |
| 7 | Terra Xhigh | 86.1 | 64/112 | 112 | $212.46 | 599,269,710 | 37.30h |
| 8 | Sol Medium | 82.1 | 61/112 | 112 | $402.39 | 445,166,718 | 31.58h |
| 9 | Terra High | 75.3 | 56/112 | 112 | $124.31 | 327,419,508 | 24.55h |
| 10 | Luna High | 74 | 55/112 | 112 | $22.48 | 702,020,476 | 31.93h |
| 11 | Sol Low | 72.6 | 54/112 | 112 | $222.41 | 254,308,848 | 22.27h |

## 口径说明

- 当前接口提供模型级 `score`、通过数、任务数、Token、耗时和估算费用。
- 当前接口没有返回十道任务的逐题通过矩阵，因此不能仅凭 API 摘要重新计算 `加权分 /100`。
- 加权排名仍以仓库中的逐题数据和权重快照为准；本报告用于自动监控源站最新摘要。
- 源站数据未变化时，自动任务仍会更新监控心跳，但不会把它描述成新的模型测试批次。
- 原始 API 响应不写入公开仓库，只保存必要的模型摘要字段。

当前已归档 API 快照数：**348**。


---

<a id="english"></a>
# Codex Radar API Monitor — English

[简体中文](api-latest.zh-CN.md) · [Project home](../README.md) · [API history CSV](../data/api/model_iq_history.csv) · [Monitor status](../data/api/monitor_status.json)

**Last successful check:** `2026-08-24T21:46:28+00:00`  
**Current API snapshot:** `941c09a8307d8a00`  
**Source observation:** `2026-07-22T06:57:20.626603+08:00`  
**New snapshot detected:** yes  
**Models returned:** 11

> “Last successful check” confirms that the automation reached the API. “Source observation” is supplied by the upstream endpoint and may be older.

> This is a model-level summary from the Codex Radar API, not the project's task-level difficulty-weighted score.

## Current API model summary

| Rank | Model tier | Source score | Passed | Tasks | Cost | Total tokens | Wall time |
|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | Sol Xhigh | 104.9 | 78/112 | 112 | $713.06 | 806,295,391 | 45.22h |
| 2 | Luna Max | 102.2 | 76/112 | 112 | $54.09 | 1,695,662,174 | 58.27h |
| 3 | Gpt-5.5 Xhigh | 100.9 | 75/112 | 112 | $647.85 | 774,677,760 | 40.53h |
| 4 | Terra Max | 95.5 | 71/112 | 112 | $425.52 | 1,161,065,574 | 54.82h |
| 5 | Gpt-5.5 High | 88.8 | 66/112 | 112 | $400.49 | 496,314,317 | 31.82h |
| 6 | Sol High | 86.1 | 64/112 | 112 | $530.43 | 572,020,545 | 34.65h |
| 7 | Terra Xhigh | 86.1 | 64/112 | 112 | $212.46 | 599,269,710 | 37.30h |
| 8 | Sol Medium | 82.1 | 61/112 | 112 | $402.39 | 445,166,718 | 31.58h |
| 9 | Terra High | 75.3 | 56/112 | 112 | $124.31 | 327,419,508 | 24.55h |
| 10 | Luna High | 74 | 55/112 | 112 | $22.48 | 702,020,476 | 31.93h |
| 11 | Sol Low | 72.6 | 54/112 | 112 | $222.41 | 254,308,848 | 22.27h |

## Interpretation

- The endpoint provides model-level `score`, pass counts, task counts, tokens, wall time, and estimated cost.
- It does not expose the ten task-level outcomes, so `Weighted /100` cannot be recomputed from this API summary alone.
- Task-weighted rankings remain based on the repository's task matrix and weight snapshots; this report monitors the latest API summary.
- When source data is unchanged, the automation still updates its heartbeat without presenting it as a new benchmark batch.
- The raw API response is not stored in the public repository; only required model-summary fields are archived.

Archived API snapshots: **348**.

