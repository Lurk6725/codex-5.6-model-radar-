# Codex Radar API Monitor / API 自动监控

[简体中文](#简体中文) · [English](#english)

<a id="简体中文"></a>
# Codex Radar API 自动监控 — 简体中文

[English](api-latest.en.md) · [项目首页](../README.md) · [API 历史 CSV](../data/api/model_iq_history.csv) · [监控状态](../data/api/monitor_status.json)

**最近成功检查：** `2026-07-27T08:48:48+00:00`  
**当前 API 快照：** `a4c63ee445a237b5`  
**源站观测时间：** `2026-07-22T06:57:20.626603+08:00`  
**本次发现新快照：** 是  
**返回模型数：** 11

> “最近成功检查”表示自动任务已正常访问 API；“源站观测时间”由上游接口提供，两者可能不同。

> 这是 Codex Radar API 返回的模型级摘要，不是本项目根据逐题矩阵计算的难度加权分。

## 当前 API 模型摘要

| 排名 | 模型档位 | 源站分数 | 通过 | 任务数 | 费用 | 总 Token | 耗时 |
|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | Luna Max | 95.5 | 71/112 | 112 | $275.65 | 1,884,214,074 | 59.64h |
| 2 | Terra Max | 95.5 | 71/112 | 112 | $533.95 | 1,419,454,073 | 56.09h |
| 3 | Sol Medium | 94.2 | 70/112 | 112 | $416.17 | 513,455,869 | 30.72h |
| 4 | Sol High | 92.8 | 69/112 | 112 | $585.46 | 745,467,121 | 40.16h |
| 5 | Sol Xhigh | 91.5 | 68/112 | 112 | $787.35 | 1,081,767,338 | 51.96h |
| 6 | Gpt-5.5 High | 90.1 | 67/112 | 112 | $409.74 | 511,267,942 | 29.36h |
| 7 | Gpt-5.5 Xhigh | 83.4 | 62/112 | 112 | $661.20 | 850,710,916 | 42.74h |
| 8 | Terra Xhigh | 79.4 | 59/112 | 112 | $290.83 | 722,453,522 | 34.86h |
| 9 | Sol Low | 76.7 | 57/112 | 112 | $221.04 | 249,895,557 | 18.80h |
| 10 | Luna High | 72.6 | 54/112 | 112 | $113.85 | 728,898,728 | 29.94h |
| 11 | Terra High | 65.9 | 49/112 | 112 | $146.21 | 319,988,843 | 20.52h |

## 口径说明

- 当前接口提供模型级 `score`、通过数、任务数、Token、耗时和估算费用。
- 当前接口没有返回十道任务的逐题通过矩阵，因此不能仅凭 API 摘要重新计算 `加权分 /100`。
- 加权排名仍以仓库中的逐题数据和权重快照为准；本报告用于自动监控源站最新摘要。
- 源站数据未变化时，自动任务仍会更新监控心跳，但不会把它描述成新的模型测试批次。
- 原始 API 响应不写入公开仓库，只保存必要的模型摘要字段。

当前已归档 API 快照数：**94**。


---

<a id="english"></a>
# Codex Radar API Monitor — English

[简体中文](api-latest.zh-CN.md) · [Project home](../README.md) · [API history CSV](../data/api/model_iq_history.csv) · [Monitor status](../data/api/monitor_status.json)

**Last successful check:** `2026-07-27T08:48:48+00:00`  
**Current API snapshot:** `a4c63ee445a237b5`  
**Source observation:** `2026-07-22T06:57:20.626603+08:00`  
**New snapshot detected:** yes  
**Models returned:** 11

> “Last successful check” confirms that the automation reached the API. “Source observation” is supplied by the upstream endpoint and may be older.

> This is a model-level summary from the Codex Radar API, not the project's task-level difficulty-weighted score.

## Current API model summary

| Rank | Model tier | Source score | Passed | Tasks | Cost | Total tokens | Wall time |
|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | Luna Max | 95.5 | 71/112 | 112 | $275.65 | 1,884,214,074 | 59.64h |
| 2 | Terra Max | 95.5 | 71/112 | 112 | $533.95 | 1,419,454,073 | 56.09h |
| 3 | Sol Medium | 94.2 | 70/112 | 112 | $416.17 | 513,455,869 | 30.72h |
| 4 | Sol High | 92.8 | 69/112 | 112 | $585.46 | 745,467,121 | 40.16h |
| 5 | Sol Xhigh | 91.5 | 68/112 | 112 | $787.35 | 1,081,767,338 | 51.96h |
| 6 | Gpt-5.5 High | 90.1 | 67/112 | 112 | $409.74 | 511,267,942 | 29.36h |
| 7 | Gpt-5.5 Xhigh | 83.4 | 62/112 | 112 | $661.20 | 850,710,916 | 42.74h |
| 8 | Terra Xhigh | 79.4 | 59/112 | 112 | $290.83 | 722,453,522 | 34.86h |
| 9 | Sol Low | 76.7 | 57/112 | 112 | $221.04 | 249,895,557 | 18.80h |
| 10 | Luna High | 72.6 | 54/112 | 112 | $113.85 | 728,898,728 | 29.94h |
| 11 | Terra High | 65.9 | 49/112 | 112 | $146.21 | 319,988,843 | 20.52h |

## Interpretation

- The endpoint provides model-level `score`, pass counts, task counts, tokens, wall time, and estimated cost.
- It does not expose the ten task-level outcomes, so `Weighted /100` cannot be recomputed from this API summary alone.
- Task-weighted rankings remain based on the repository's task matrix and weight snapshots; this report monitors the latest API summary.
- When source data is unchanged, the automation still updates its heartbeat without presenting it as a new benchmark batch.
- The raw API response is not stored in the public repository; only required model-summary fields are archived.

Archived API snapshots: **94**.

