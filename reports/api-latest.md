# Codex Radar API Monitor / API 自动监控

[简体中文](#简体中文) · [English](#english)

<a id="简体中文"></a>
# Codex Radar API 自动监控 — 简体中文

[English](api-latest.en.md) · [项目首页](../README.md) · [API 历史 CSV](../data/api/model_iq_history.csv) · [监控状态](../data/api/monitor_status.json)

**最近成功检查：** `2026-08-11T04:42:36+00:00`  
**当前 API 快照：** `be5987b314b4481d`  
**源站观测时间：** `2026-07-22T06:57:20.626603+08:00`  
**本次发现新快照：** 否；源站仍返回同一快照  
**返回模型数：** 11

> “最近成功检查”表示自动任务已正常访问 API；“源站观测时间”由上游接口提供，两者可能不同。

> 这是 Codex Radar API 返回的模型级摘要，不是本项目根据逐题矩阵计算的难度加权分。

## 当前 API 模型摘要

| 排名 | 模型档位 | 源站分数 | 通过 | 任务数 | 费用 | 总 Token | 耗时 |
|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | Sol Xhigh | 103.6 | 77/112 | 112 | $737.05 | 885,058,202 | 49.66h |
| 2 | Gpt-5.5 Xhigh | 102.2 | 76/112 | 112 | $656.84 | 791,650,610 | 42.13h |
| 3 | Sol High | 100.9 | 75/112 | 112 | $566.71 | 638,710,693 | 39.02h |
| 4 | Terra Max | 96.9 | 72/112 | 112 | $438.67 | 1,214,724,211 | 53.43h |
| 5 | Sol Medium | 92.8 | 69/112 | 112 | $410.36 | 455,949,802 | 30.78h |
| 6 | Luna Max | 87.4 | 65/112 | 112 | $58.54 | 1,824,310,241 | 61.02h |
| 7 | Sol Low | 87.4 | 65/112 | 112 | $229.99 | 275,609,023 | 22.23h |
| 8 | Terra Xhigh | 87.4 | 65/112 | 112 | $219.63 | 561,644,890 | 31.72h |
| 9 | Gpt-5.5 High | 84.7 | 63/112 | 112 | $404.37 | 486,438,930 | 30.03h |
| 10 | Terra High | 76.7 | 57/112 | 112 | $126.99 | 333,978,903 | 23.37h |
| 11 | Luna High | 71.3 | 53/112 | 112 | $26.23 | 737,069,438 | 32.84h |

## 口径说明

- 当前接口提供模型级 `score`、通过数、任务数、Token、耗时和估算费用。
- 当前接口没有返回十道任务的逐题通过矩阵，因此不能仅凭 API 摘要重新计算 `加权分 /100`。
- 加权排名仍以仓库中的逐题数据和权重快照为准；本报告用于自动监控源站最新摘要。
- 源站数据未变化时，自动任务仍会更新监控心跳，但不会把它描述成新的模型测试批次。
- 原始 API 响应不写入公开仓库，只保存必要的模型摘要字段。

当前已归档 API 快照数：**229**。


---

<a id="english"></a>
# Codex Radar API Monitor — English

[简体中文](api-latest.zh-CN.md) · [Project home](../README.md) · [API history CSV](../data/api/model_iq_history.csv) · [Monitor status](../data/api/monitor_status.json)

**Last successful check:** `2026-08-11T04:42:36+00:00`  
**Current API snapshot:** `be5987b314b4481d`  
**Source observation:** `2026-07-22T06:57:20.626603+08:00`  
**New snapshot detected:** no; the source returned the same snapshot  
**Models returned:** 11

> “Last successful check” confirms that the automation reached the API. “Source observation” is supplied by the upstream endpoint and may be older.

> This is a model-level summary from the Codex Radar API, not the project's task-level difficulty-weighted score.

## Current API model summary

| Rank | Model tier | Source score | Passed | Tasks | Cost | Total tokens | Wall time |
|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | Sol Xhigh | 103.6 | 77/112 | 112 | $737.05 | 885,058,202 | 49.66h |
| 2 | Gpt-5.5 Xhigh | 102.2 | 76/112 | 112 | $656.84 | 791,650,610 | 42.13h |
| 3 | Sol High | 100.9 | 75/112 | 112 | $566.71 | 638,710,693 | 39.02h |
| 4 | Terra Max | 96.9 | 72/112 | 112 | $438.67 | 1,214,724,211 | 53.43h |
| 5 | Sol Medium | 92.8 | 69/112 | 112 | $410.36 | 455,949,802 | 30.78h |
| 6 | Luna Max | 87.4 | 65/112 | 112 | $58.54 | 1,824,310,241 | 61.02h |
| 7 | Sol Low | 87.4 | 65/112 | 112 | $229.99 | 275,609,023 | 22.23h |
| 8 | Terra Xhigh | 87.4 | 65/112 | 112 | $219.63 | 561,644,890 | 31.72h |
| 9 | Gpt-5.5 High | 84.7 | 63/112 | 112 | $404.37 | 486,438,930 | 30.03h |
| 10 | Terra High | 76.7 | 57/112 | 112 | $126.99 | 333,978,903 | 23.37h |
| 11 | Luna High | 71.3 | 53/112 | 112 | $26.23 | 737,069,438 | 32.84h |

## Interpretation

- The endpoint provides model-level `score`, pass counts, task counts, tokens, wall time, and estimated cost.
- It does not expose the ten task-level outcomes, so `Weighted /100` cannot be recomputed from this API summary alone.
- Task-weighted rankings remain based on the repository's task matrix and weight snapshots; this report monitors the latest API summary.
- When source data is unchanged, the automation still updates its heartbeat without presenting it as a new benchmark batch.
- The raw API response is not stored in the public repository; only required model-summary fields are archived.

Archived API snapshots: **229**.

