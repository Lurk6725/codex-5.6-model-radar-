# Codex Radar API Monitor / API 自动监控

[简体中文](#简体中文) · [English](#english)

<a id="简体中文"></a>
# Codex Radar API 自动监控 — 简体中文

[English](api-latest.en.md) · [项目首页](../README.md) · [API 历史 CSV](../data/api/model_iq_history.csv) · [监控状态](../data/api/monitor_status.json)

**最近成功检查：** `2026-08-26T16:05:32+00:00`  
**当前 API 快照：** `a98a0183d48f159c`  
**源站观测时间：** `2026-07-22T06:57:20.626603+08:00`  
**本次发现新快照：** 是  
**返回模型数：** 11

> “最近成功检查”表示自动任务已正常访问 API；“源站观测时间”由上游接口提供，两者可能不同。

> 这是 Codex Radar API 返回的模型级摘要，不是本项目根据逐题矩阵计算的难度加权分。

## 当前 API 模型摘要

| 排名 | 模型档位 | 源站分数 | 通过 | 任务数 | 费用 | 总 Token | 耗时 |
|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | Sol Xhigh | 103.6 | 77/112 | 112 | $698.07 | 804,010,483 | 44.34h |
| 2 | Luna Max | 100.9 | 75/112 | 112 | $54.05 | 1,744,681,820 | 63.68h |
| 3 | Sol Medium | 100.9 | 75/112 | 112 | $312.16 | 415,503,791 | 28.70h |
| 4 | Gpt-5.5 Xhigh | 99.5 | 74/112 | 112 | $645.91 | 778,729,908 | 40.42h |
| 5 | Terra Max | 99.5 | 74/112 | 112 | $425.87 | 1,184,283,626 | 55.89h |
| 6 | Sol High | 88.8 | 66/112 | 112 | $507.82 | 563,029,413 | 33.39h |
| 7 | Gpt-5.5 High | 87.4 | 65/112 | 112 | $400.63 | 489,737,007 | 31.52h |
| 8 | Terra Xhigh | 84.7 | 63/112 | 112 | $211.60 | 593,573,531 | 36.50h |
| 9 | Sol Low | 83.4 | 62/112 | 112 | $172.50 | 209,414,220 | 17.01h |
| 10 | Terra High | 76.7 | 57/112 | 112 | $122.99 | 342,671,220 | 25.33h |
| 11 | Luna High | 75.3 | 56/112 | 112 | $22.47 | 702,101,912 | 32.12h |

## 口径说明

- 当前接口提供模型级 `score`、通过数、任务数、Token、耗时和估算费用。
- 当前接口没有返回十道任务的逐题通过矩阵，因此不能仅凭 API 摘要重新计算 `加权分 /100`。
- 加权排名仍以仓库中的逐题数据和权重快照为准；本报告用于自动监控源站最新摘要。
- 源站数据未变化时，自动任务仍会更新监控心跳，但不会把它描述成新的模型测试批次。
- 原始 API 响应不写入公开仓库，只保存必要的模型摘要字段。

当前已归档 API 快照数：**366**。


---

<a id="english"></a>
# Codex Radar API Monitor — English

[简体中文](api-latest.zh-CN.md) · [Project home](../README.md) · [API history CSV](../data/api/model_iq_history.csv) · [Monitor status](../data/api/monitor_status.json)

**Last successful check:** `2026-08-26T16:05:32+00:00`  
**Current API snapshot:** `a98a0183d48f159c`  
**Source observation:** `2026-07-22T06:57:20.626603+08:00`  
**New snapshot detected:** yes  
**Models returned:** 11

> “Last successful check” confirms that the automation reached the API. “Source observation” is supplied by the upstream endpoint and may be older.

> This is a model-level summary from the Codex Radar API, not the project's task-level difficulty-weighted score.

## Current API model summary

| Rank | Model tier | Source score | Passed | Tasks | Cost | Total tokens | Wall time |
|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | Sol Xhigh | 103.6 | 77/112 | 112 | $698.07 | 804,010,483 | 44.34h |
| 2 | Luna Max | 100.9 | 75/112 | 112 | $54.05 | 1,744,681,820 | 63.68h |
| 3 | Sol Medium | 100.9 | 75/112 | 112 | $312.16 | 415,503,791 | 28.70h |
| 4 | Gpt-5.5 Xhigh | 99.5 | 74/112 | 112 | $645.91 | 778,729,908 | 40.42h |
| 5 | Terra Max | 99.5 | 74/112 | 112 | $425.87 | 1,184,283,626 | 55.89h |
| 6 | Sol High | 88.8 | 66/112 | 112 | $507.82 | 563,029,413 | 33.39h |
| 7 | Gpt-5.5 High | 87.4 | 65/112 | 112 | $400.63 | 489,737,007 | 31.52h |
| 8 | Terra Xhigh | 84.7 | 63/112 | 112 | $211.60 | 593,573,531 | 36.50h |
| 9 | Sol Low | 83.4 | 62/112 | 112 | $172.50 | 209,414,220 | 17.01h |
| 10 | Terra High | 76.7 | 57/112 | 112 | $122.99 | 342,671,220 | 25.33h |
| 11 | Luna High | 75.3 | 56/112 | 112 | $22.47 | 702,101,912 | 32.12h |

## Interpretation

- The endpoint provides model-level `score`, pass counts, task counts, tokens, wall time, and estimated cost.
- It does not expose the ten task-level outcomes, so `Weighted /100` cannot be recomputed from this API summary alone.
- Task-weighted rankings remain based on the repository's task matrix and weight snapshots; this report monitors the latest API summary.
- When source data is unchanged, the automation still updates its heartbeat without presenting it as a new benchmark batch.
- The raw API response is not stored in the public repository; only required model-summary fields are archived.

Archived API snapshots: **366**.

