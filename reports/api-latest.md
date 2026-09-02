# Codex Radar API Monitor / API 自动监控

[简体中文](#简体中文) · [English](#english)

<a id="简体中文"></a>
# Codex Radar API 自动监控 — 简体中文

[English](api-latest.en.md) · [项目首页](../README.md) · [API 历史 CSV](../data/api/model_iq_history.csv) · [监控状态](../data/api/monitor_status.json)

**最近成功检查：** `2026-09-02T21:51:43+00:00`  
**当前 API 快照：** `492c2a870176a915`  
**源站观测时间：** `2026-09-02T20:11:35.648389+08:00`  
**本次发现新快照：** 否；源站仍返回同一快照  
**返回模型数：** 11

> “最近成功检查”表示自动任务已正常访问 API；“源站观测时间”由上游接口提供，两者可能不同。

> 这是 Codex Radar API 返回的模型级摘要，不是本项目根据逐题矩阵计算的难度加权分。

## 当前 API 模型摘要

| 排名 | 模型档位 | 源站分数 | 通过 | 任务数 | 费用 | 总 Token | 耗时 |
|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | Luna Max | 106.3 | 79/112 | 112 | $54.08 | 2,107,445,306 | 74.30h |
| 2 | Terra Max | 106.3 | 79/112 | 112 | $420.43 | 1,245,688,429 | 59.02h |
| 3 | Gpt-5.5 Xhigh | 103.6 | 77/112 | 112 | $638.70 | 903,745,336 | 44.52h |
| 4 | Sol Medium | 99.5 | 74/112 | 112 | $312.52 | 419,024,511 | 28.16h |
| 5 | Sol Xhigh | 99.5 | 74/112 | 112 | $580.94 | 822,797,613 | 45.13h |
| 6 | Sol High | 98.2 | 73/112 | 112 | $471.33 | 586,340,202 | 37.08h |
| 7 | Gpt-5.5 High | 86.1 | 64/112 | 112 | $397.48 | 532,111,490 | 28.28h |
| 8 | Terra Xhigh | 86.1 | 64/112 | 112 | $210.82 | 585,969,885 | 36.16h |
| 9 | Terra High | 80.7 | 60/112 | 112 | $122.16 | 332,356,481 | 25.95h |
| 10 | Sol Low | 78 | 58/112 | 112 | $170.66 | 207,262,701 | 18.63h |
| 11 | Luna High | 68.6 | 51/112 | 112 | $22.49 | 809,612,612 | 34.52h |

## 口径说明

- 当前接口提供模型级 `score`、通过数、任务数、Token、耗时和估算费用。
- 当前接口没有返回十道任务的逐题通过矩阵，因此不能仅凭 API 摘要重新计算 `加权分 /100`。
- 加权排名仍以仓库中的逐题数据和权重快照为准；本报告用于自动监控源站最新摘要。
- 源站数据未变化时，自动任务仍会更新监控心跳，但不会把它描述成新的模型测试批次。
- 原始 API 响应不写入公开仓库，只保存必要的模型摘要字段。

当前已归档 API 快照数：**398**。


---

<a id="english"></a>
# Codex Radar API Monitor — English

[简体中文](api-latest.zh-CN.md) · [Project home](../README.md) · [API history CSV](../data/api/model_iq_history.csv) · [Monitor status](../data/api/monitor_status.json)

**Last successful check:** `2026-09-02T21:51:43+00:00`  
**Current API snapshot:** `492c2a870176a915`  
**Source observation:** `2026-09-02T20:11:35.648389+08:00`  
**New snapshot detected:** no; the source returned the same snapshot  
**Models returned:** 11

> “Last successful check” confirms that the automation reached the API. “Source observation” is supplied by the upstream endpoint and may be older.

> This is a model-level summary from the Codex Radar API, not the project's task-level difficulty-weighted score.

## Current API model summary

| Rank | Model tier | Source score | Passed | Tasks | Cost | Total tokens | Wall time |
|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | Luna Max | 106.3 | 79/112 | 112 | $54.08 | 2,107,445,306 | 74.30h |
| 2 | Terra Max | 106.3 | 79/112 | 112 | $420.43 | 1,245,688,429 | 59.02h |
| 3 | Gpt-5.5 Xhigh | 103.6 | 77/112 | 112 | $638.70 | 903,745,336 | 44.52h |
| 4 | Sol Medium | 99.5 | 74/112 | 112 | $312.52 | 419,024,511 | 28.16h |
| 5 | Sol Xhigh | 99.5 | 74/112 | 112 | $580.94 | 822,797,613 | 45.13h |
| 6 | Sol High | 98.2 | 73/112 | 112 | $471.33 | 586,340,202 | 37.08h |
| 7 | Gpt-5.5 High | 86.1 | 64/112 | 112 | $397.48 | 532,111,490 | 28.28h |
| 8 | Terra Xhigh | 86.1 | 64/112 | 112 | $210.82 | 585,969,885 | 36.16h |
| 9 | Terra High | 80.7 | 60/112 | 112 | $122.16 | 332,356,481 | 25.95h |
| 10 | Sol Low | 78 | 58/112 | 112 | $170.66 | 207,262,701 | 18.63h |
| 11 | Luna High | 68.6 | 51/112 | 112 | $22.49 | 809,612,612 | 34.52h |

## Interpretation

- The endpoint provides model-level `score`, pass counts, task counts, tokens, wall time, and estimated cost.
- It does not expose the ten task-level outcomes, so `Weighted /100` cannot be recomputed from this API summary alone.
- Task-weighted rankings remain based on the repository's task matrix and weight snapshots; this report monitors the latest API summary.
- When source data is unchanged, the automation still updates its heartbeat without presenting it as a new benchmark batch.
- The raw API response is not stored in the public repository; only required model-summary fields are archived.

Archived API snapshots: **398**.

