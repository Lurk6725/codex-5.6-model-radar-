# Codex Radar API Monitor / API 自动监控

[简体中文](#简体中文) · [English](#english)

<a id="简体中文"></a>
# Codex Radar API 自动监控 — 简体中文

[English](api-latest.en.md) · [项目首页](../README.md) · [API 历史 CSV](../data/api/model_iq_history.csv) · [监控状态](../data/api/monitor_status.json)

**最近成功检查：** `2026-09-05T01:02:06+00:00`  
**当前 API 快照：** `75d1cce37af97b7e`  
**源站观测时间：** `2026-09-02T20:11:35.648389+08:00`  
**本次发现新快照：** 否；源站仍返回同一快照  
**返回模型数：** 11

> “最近成功检查”表示自动任务已正常访问 API；“源站观测时间”由上游接口提供，两者可能不同。

> 这是 Codex Radar API 返回的模型级摘要，不是本项目根据逐题矩阵计算的难度加权分。

## 当前 API 模型摘要

| 排名 | 模型档位 | 源站分数 | 通过 | 任务数 | 费用 | 总 Token | 耗时 |
|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | Luna Max | 109 | 81/112 | 112 | $54.22 | 2,164,371,875 | 76.54h |
| 2 | Terra Max | 106.3 | 79/112 | 112 | $420.43 | 1,244,001,980 | 58.89h |
| 3 | Gpt-5.5 Xhigh | 103.6 | 77/112 | 112 | $638.71 | 901,829,830 | 44.54h |
| 4 | Sol Xhigh | 99.5 | 74/112 | 112 | $581.00 | 825,490,383 | 46.56h |
| 5 | Sol High | 98.2 | 73/112 | 112 | $470.71 | 584,493,333 | 37.01h |
| 6 | Sol Medium | 96.9 | 72/112 | 112 | $312.41 | 413,513,307 | 27.13h |
| 7 | Terra Xhigh | 86.1 | 64/112 | 112 | $210.68 | 587,416,643 | 36.41h |
| 8 | Gpt-5.5 High | 84.7 | 63/112 | 112 | $397.51 | 534,540,243 | 27.61h |
| 9 | Terra High | 80.7 | 60/112 | 112 | $122.04 | 333,171,526 | 26.03h |
| 10 | Sol Low | 79.4 | 59/112 | 112 | $170.72 | 208,522,660 | 18.68h |
| 11 | Luna High | 68.6 | 51/112 | 112 | $22.49 | 809,612,612 | 34.52h |

## 口径说明

- 当前接口提供模型级 `score`、通过数、任务数、Token、耗时和估算费用。
- 当前接口没有返回十道任务的逐题通过矩阵，因此不能仅凭 API 摘要重新计算 `加权分 /100`。
- 加权排名仍以仓库中的逐题数据和权重快照为准；本报告用于自动监控源站最新摘要。
- 源站数据未变化时，自动任务仍会更新监控心跳，但不会把它描述成新的模型测试批次。
- 原始 API 响应不写入公开仓库，只保存必要的模型摘要字段。

当前已归档 API 快照数：**403**。


---

<a id="english"></a>
# Codex Radar API Monitor — English

[简体中文](api-latest.zh-CN.md) · [Project home](../README.md) · [API history CSV](../data/api/model_iq_history.csv) · [Monitor status](../data/api/monitor_status.json)

**Last successful check:** `2026-09-05T01:02:06+00:00`  
**Current API snapshot:** `75d1cce37af97b7e`  
**Source observation:** `2026-09-02T20:11:35.648389+08:00`  
**New snapshot detected:** no; the source returned the same snapshot  
**Models returned:** 11

> “Last successful check” confirms that the automation reached the API. “Source observation” is supplied by the upstream endpoint and may be older.

> This is a model-level summary from the Codex Radar API, not the project's task-level difficulty-weighted score.

## Current API model summary

| Rank | Model tier | Source score | Passed | Tasks | Cost | Total tokens | Wall time |
|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | Luna Max | 109 | 81/112 | 112 | $54.22 | 2,164,371,875 | 76.54h |
| 2 | Terra Max | 106.3 | 79/112 | 112 | $420.43 | 1,244,001,980 | 58.89h |
| 3 | Gpt-5.5 Xhigh | 103.6 | 77/112 | 112 | $638.71 | 901,829,830 | 44.54h |
| 4 | Sol Xhigh | 99.5 | 74/112 | 112 | $581.00 | 825,490,383 | 46.56h |
| 5 | Sol High | 98.2 | 73/112 | 112 | $470.71 | 584,493,333 | 37.01h |
| 6 | Sol Medium | 96.9 | 72/112 | 112 | $312.41 | 413,513,307 | 27.13h |
| 7 | Terra Xhigh | 86.1 | 64/112 | 112 | $210.68 | 587,416,643 | 36.41h |
| 8 | Gpt-5.5 High | 84.7 | 63/112 | 112 | $397.51 | 534,540,243 | 27.61h |
| 9 | Terra High | 80.7 | 60/112 | 112 | $122.04 | 333,171,526 | 26.03h |
| 10 | Sol Low | 79.4 | 59/112 | 112 | $170.72 | 208,522,660 | 18.68h |
| 11 | Luna High | 68.6 | 51/112 | 112 | $22.49 | 809,612,612 | 34.52h |

## Interpretation

- The endpoint provides model-level `score`, pass counts, task counts, tokens, wall time, and estimated cost.
- It does not expose the ten task-level outcomes, so `Weighted /100` cannot be recomputed from this API summary alone.
- Task-weighted rankings remain based on the repository's task matrix and weight snapshots; this report monitors the latest API summary.
- When source data is unchanged, the automation still updates its heartbeat without presenting it as a new benchmark batch.
- The raw API response is not stored in the public repository; only required model-summary fields are archived.

Archived API snapshots: **403**.

