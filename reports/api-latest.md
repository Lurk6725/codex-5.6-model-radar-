# Codex Radar API Monitor / API 自动监控

[简体中文](#简体中文) · [English](#english)

<a id="简体中文"></a>
# Codex Radar API 自动监控 — 简体中文

[English](api-latest.en.md) · [项目首页](../README.md) · [API 历史 CSV](../data/api/model_iq_history.csv) · [监控状态](../data/api/monitor_status.json)

**最近成功检查：** `2026-08-12T17:16:24+00:00`  
**当前 API 快照：** `50bd8e16ca59a87e`  
**源站观测时间：** `2026-07-22T06:57:20.626603+08:00`  
**本次发现新快照：** 否；源站仍返回同一快照  
**返回模型数：** 11

> “最近成功检查”表示自动任务已正常访问 API；“源站观测时间”由上游接口提供，两者可能不同。

> 这是 Codex Radar API 返回的模型级摘要，不是本项目根据逐题矩阵计算的难度加权分。

## 当前 API 模型摘要

| 排名 | 模型档位 | 源站分数 | 通过 | 任务数 | 费用 | 总 Token | 耗时 |
|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | Sol Xhigh | 103.6 | 77/112 | 112 | $733.13 | 898,617,449 | 48.62h |
| 2 | Terra Max | 103.6 | 77/112 | 112 | $436.90 | 1,250,144,854 | 57.08h |
| 3 | Sol High | 100.9 | 75/112 | 112 | $561.41 | 690,787,262 | 37.93h |
| 4 | Luna Max | 99.5 | 74/112 | 112 | $58.56 | 1,868,598,549 | 67.04h |
| 5 | Gpt-5.5 Xhigh | 94.2 | 70/112 | 112 | $657.06 | 722,589,708 | 40.18h |
| 6 | Sol Medium | 94.2 | 70/112 | 112 | $407.86 | 464,902,602 | 31.43h |
| 7 | Gpt-5.5 High | 88.8 | 66/112 | 112 | $404.19 | 493,375,036 | 32.54h |
| 8 | Terra Xhigh | 87.4 | 65/112 | 112 | $218.26 | 582,689,109 | 35.72h |
| 9 | Terra High | 82.1 | 61/112 | 112 | $126.90 | 344,933,448 | 24.34h |
| 10 | Sol Low | 75.3 | 56/112 | 112 | $228.70 | 271,479,771 | 22.38h |
| 11 | Luna High | 65.9 | 49/112 | 112 | $26.20 | 771,942,548 | 34.72h |

## 口径说明

- 当前接口提供模型级 `score`、通过数、任务数、Token、耗时和估算费用。
- 当前接口没有返回十道任务的逐题通过矩阵，因此不能仅凭 API 摘要重新计算 `加权分 /100`。
- 加权排名仍以仓库中的逐题数据和权重快照为准；本报告用于自动监控源站最新摘要。
- 源站数据未变化时，自动任务仍会更新监控心跳，但不会把它描述成新的模型测试批次。
- 原始 API 响应不写入公开仓库，只保存必要的模型摘要字段。

当前已归档 API 快照数：**244**。


---

<a id="english"></a>
# Codex Radar API Monitor — English

[简体中文](api-latest.zh-CN.md) · [Project home](../README.md) · [API history CSV](../data/api/model_iq_history.csv) · [Monitor status](../data/api/monitor_status.json)

**Last successful check:** `2026-08-12T17:16:24+00:00`  
**Current API snapshot:** `50bd8e16ca59a87e`  
**Source observation:** `2026-07-22T06:57:20.626603+08:00`  
**New snapshot detected:** no; the source returned the same snapshot  
**Models returned:** 11

> “Last successful check” confirms that the automation reached the API. “Source observation” is supplied by the upstream endpoint and may be older.

> This is a model-level summary from the Codex Radar API, not the project's task-level difficulty-weighted score.

## Current API model summary

| Rank | Model tier | Source score | Passed | Tasks | Cost | Total tokens | Wall time |
|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | Sol Xhigh | 103.6 | 77/112 | 112 | $733.13 | 898,617,449 | 48.62h |
| 2 | Terra Max | 103.6 | 77/112 | 112 | $436.90 | 1,250,144,854 | 57.08h |
| 3 | Sol High | 100.9 | 75/112 | 112 | $561.41 | 690,787,262 | 37.93h |
| 4 | Luna Max | 99.5 | 74/112 | 112 | $58.56 | 1,868,598,549 | 67.04h |
| 5 | Gpt-5.5 Xhigh | 94.2 | 70/112 | 112 | $657.06 | 722,589,708 | 40.18h |
| 6 | Sol Medium | 94.2 | 70/112 | 112 | $407.86 | 464,902,602 | 31.43h |
| 7 | Gpt-5.5 High | 88.8 | 66/112 | 112 | $404.19 | 493,375,036 | 32.54h |
| 8 | Terra Xhigh | 87.4 | 65/112 | 112 | $218.26 | 582,689,109 | 35.72h |
| 9 | Terra High | 82.1 | 61/112 | 112 | $126.90 | 344,933,448 | 24.34h |
| 10 | Sol Low | 75.3 | 56/112 | 112 | $228.70 | 271,479,771 | 22.38h |
| 11 | Luna High | 65.9 | 49/112 | 112 | $26.20 | 771,942,548 | 34.72h |

## Interpretation

- The endpoint provides model-level `score`, pass counts, task counts, tokens, wall time, and estimated cost.
- It does not expose the ten task-level outcomes, so `Weighted /100` cannot be recomputed from this API summary alone.
- Task-weighted rankings remain based on the repository's task matrix and weight snapshots; this report monitors the latest API summary.
- When source data is unchanged, the automation still updates its heartbeat without presenting it as a new benchmark batch.
- The raw API response is not stored in the public repository; only required model-summary fields are archived.

Archived API snapshots: **244**.

