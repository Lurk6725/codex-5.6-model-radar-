# Codex Radar API Monitor / API 自动监控

[简体中文](#简体中文) · [English](#english)

<a id="简体中文"></a>
# Codex Radar API 自动监控 — 简体中文

[English](api-latest.en.md) · [项目首页](../README.md) · [API 历史 CSV](../data/api/model_iq_history.csv)

**API 快照：** `56b5641f66b1a557`  
**源站观测时间：** `2026-07-13T22:08:07.261261+08:00`  
**本次抓取时间：** `2026-07-14T01:00:55+00:00`

> 这是 Codex Radar API 返回的模型级摘要，不是本项目根据逐题矩阵计算的难度加权分。

## 当前 API 模型摘要

| 排名 | 模型档位 | 源站分数 | 通过 | 任务数 | 费用 | 总 Token | 耗时 |
|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | Sol High | 135 | 9/10 | 10 | $24.62 | 23,496,190 | 0.54h |
| 2 | Sol Medium | 135 | 9/10 | 10 | $18.41 | 18,483,032 | 0.46h |
| 3 | Sol Low | 120 | 8/10 | 10 | $9.73 | 8,195,968 | 0.27h |
| 4 | Terra Max | 105 | 7/10 | 10 | $30.91 | 65,722,639 | 0.63h |
| 5 | Luna Max | 90 | 6/10 | 10 | $15.11 | 88,731,185 | 0.66h |
| 6 | Sol Xhigh | 90 | 6/10 | 10 | $37.97 | 40,667,099 | 0.75h |
| 7 | Terra Medium | 75 | 5/10 | 10 | $5.18 | 8,014,450 | 0.39h |
| 8 | Luna Medium | 15 | 1/10 | 10 | $2.44 | 10,811,042 | 0.41h |

## 口径说明

- 当前接口提供模型级 `score`、通过数、任务数、Token、耗时和估算费用。
- 当前接口没有返回十道任务的逐题通过矩阵，因此不能仅凭 API 摘要重新计算 `加权分 /100`。
- 加权排名仍以仓库中的逐题数据和权重快照为准；本报告用于自动监控源站最新摘要。
- 原始 API 响应不写入公开仓库，只保存必要的模型摘要字段。

当前已归档 API 快照数：**2**。


---

<a id="english"></a>
# Codex Radar API Monitor — English

[简体中文](api-latest.zh-CN.md) · [Project home](../README.md) · [API history CSV](../data/api/model_iq_history.csv)

**API snapshot:** `56b5641f66b1a557`  
**Source observation:** `2026-07-13T22:08:07.261261+08:00`  
**Retrieved:** `2026-07-14T01:00:55+00:00`

> This is a model-level summary from the Codex Radar API, not the project's task-level difficulty-weighted score.

## Current API model summary

| Rank | Model tier | Source score | Passed | Tasks | Cost | Total tokens | Wall time |
|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | Sol High | 135 | 9/10 | 10 | $24.62 | 23,496,190 | 0.54h |
| 2 | Sol Medium | 135 | 9/10 | 10 | $18.41 | 18,483,032 | 0.46h |
| 3 | Sol Low | 120 | 8/10 | 10 | $9.73 | 8,195,968 | 0.27h |
| 4 | Terra Max | 105 | 7/10 | 10 | $30.91 | 65,722,639 | 0.63h |
| 5 | Luna Max | 90 | 6/10 | 10 | $15.11 | 88,731,185 | 0.66h |
| 6 | Sol Xhigh | 90 | 6/10 | 10 | $37.97 | 40,667,099 | 0.75h |
| 7 | Terra Medium | 75 | 5/10 | 10 | $5.18 | 8,014,450 | 0.39h |
| 8 | Luna Medium | 15 | 1/10 | 10 | $2.44 | 10,811,042 | 0.41h |

## Interpretation

- The endpoint provides model-level `score`, pass counts, task counts, tokens, wall time, and estimated cost.
- It does not expose the ten task-level outcomes, so `Weighted /100` cannot be recomputed from this API summary alone.
- Task-weighted rankings remain based on the repository's task matrix and weight snapshots; this report monitors the latest API summary.
- The raw API response is not stored in the public repository; only required model-summary fields are archived.

Archived API snapshots: **2**.

