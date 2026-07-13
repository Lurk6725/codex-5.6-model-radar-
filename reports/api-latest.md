# Codex Radar API Monitor / API 自动监控

[简体中文](#简体中文) · [English](#english)

<a id="简体中文"></a>
# Codex Radar API 自动监控 — 简体中文

[English](api-latest.en.md) · [项目首页](../README.md) · [API 历史 CSV](../data/api/model_iq_history.csv)

**API 快照：** `a74e838c747f14bc`  
**源站观测时间：** `2026-07-13T22:08:07.261261+08:00`  
**本次抓取时间：** `2026-07-13T14:11:34+00:00`

> 这是 Codex Radar API 返回的模型级摘要，不是本项目根据逐题矩阵计算的难度加权分。

## 当前 API 模型摘要

| 排名 | 模型档位 | 源站分数 | 通过 | 任务数 | 费用 | 总 Token | 耗时 |
|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | Luna Max | 105 | 7/10 | 10 | $18.94 | 118,365,538 | 1.42h |
| 2 | Sol Xhigh | 105 | 7/10 | 10 | $33.63 | 36,684,441 | 0.85h |
| 3 | Sol High | 90 | 6/10 | 10 | $26.78 | 26,956,544 | 0.63h |
| 4 | Sol Low | 90 | 6/10 | 10 | $9.37 | 7,213,131 | 0.39h |
| 5 | Terra Max | 90 | 6/10 | 10 | $32.21 | 72,580,591 | 0.72h |
| 6 | Sol Medium | 75 | 5/10 | 10 | $16.14 | 15,100,079 | 0.59h |
| 7 | Terra Medium | 75 | 5/10 | 10 | $5.96 | 9,364,303 | 0.56h |
| 8 | Luna Medium | 30 | 2/10 | 10 | $2.43 | 10,458,978 | 0.54h |

## 口径说明

- 当前接口提供模型级 `score`、通过数、任务数、Token、耗时和估算费用。
- 当前接口没有返回十道任务的逐题通过矩阵，因此不能仅凭 API 摘要重新计算 `加权分 /100`。
- 加权排名仍以仓库中的逐题数据和权重快照为准；本报告用于自动监控源站最新摘要。
- 原始 API 响应不写入公开仓库，只保存必要的模型摘要字段。

当前已归档 API 快照数：**1**。


---

<a id="english"></a>
# Codex Radar API Monitor — English

[简体中文](api-latest.zh-CN.md) · [Project home](../README.md) · [API history CSV](../data/api/model_iq_history.csv)

**API snapshot:** `a74e838c747f14bc`  
**Source observation:** `2026-07-13T22:08:07.261261+08:00`  
**Retrieved:** `2026-07-13T14:11:34+00:00`

> This is a model-level summary from the Codex Radar API, not the project's task-level difficulty-weighted score.

## Current API model summary

| Rank | Model tier | Source score | Passed | Tasks | Cost | Total tokens | Wall time |
|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | Luna Max | 105 | 7/10 | 10 | $18.94 | 118,365,538 | 1.42h |
| 2 | Sol Xhigh | 105 | 7/10 | 10 | $33.63 | 36,684,441 | 0.85h |
| 3 | Sol High | 90 | 6/10 | 10 | $26.78 | 26,956,544 | 0.63h |
| 4 | Sol Low | 90 | 6/10 | 10 | $9.37 | 7,213,131 | 0.39h |
| 5 | Terra Max | 90 | 6/10 | 10 | $32.21 | 72,580,591 | 0.72h |
| 6 | Sol Medium | 75 | 5/10 | 10 | $16.14 | 15,100,079 | 0.59h |
| 7 | Terra Medium | 75 | 5/10 | 10 | $5.96 | 9,364,303 | 0.56h |
| 8 | Luna Medium | 30 | 2/10 | 10 | $2.43 | 10,458,978 | 0.54h |

## Interpretation

- The endpoint provides model-level `score`, pass counts, task counts, tokens, wall time, and estimated cost.
- It does not expose the ten task-level outcomes, so `Weighted /100` cannot be recomputed from this API summary alone.
- Task-weighted rankings remain based on the repository's task matrix and weight snapshots; this report monitors the latest API summary.
- The raw API response is not stored in the public repository; only required model-summary fields are archived.

Archived API snapshots: **1**.

