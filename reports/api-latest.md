# Codex Radar API Monitor / API 自动监控

[简体中文](#简体中文) · [English](#english)

<a id="简体中文"></a>
# Codex Radar API 自动监控 — 简体中文

[English](api-latest.en.md) · [项目首页](../README.md) · [API 历史 CSV](../data/api/model_iq_history.csv) · [监控状态](../data/api/monitor_status.json)

**最近成功检查：** `2026-07-23T04:41:29+00:00`  
**当前 API 快照：** `e6a18a82e898633d`  
**源站观测时间：** `2026-07-22T06:57:20.626603+08:00`  
**本次发现新快照：** 是  
**返回模型数：** 11

> “最近成功检查”表示自动任务已正常访问 API；“源站观测时间”由上游接口提供，两者可能不同。

> 这是 Codex Radar API 返回的模型级摘要，不是本项目根据逐题矩阵计算的难度加权分。

## 当前 API 模型摘要

| 排名 | 模型档位 | 源站分数 | 通过 | 任务数 | 费用 | 总 Token | 耗时 |
|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | Sol Xhigh | 100.9 | 75/112 | 112 | $776.65 | 1,052,887,988 | 48.98h |
| 2 | Gpt-5.5 Xhigh | 96.9 | 72/112 | 112 | $654.08 | 843,471,087 | 46.38h |
| 3 | Terra Max | 96.9 | 72/112 | 112 | $519.07 | 1,348,930,170 | 61.28h |
| 4 | Sol Medium | 92.8 | 69/112 | 112 | $431.84 | 550,033,877 | 32.67h |
| 5 | Luna Max | 91.5 | 68/112 | 112 | $278.07 | 1,902,419,844 | 64.56h |
| 6 | Terra Xhigh | 91.5 | 68/112 | 112 | $269.22 | 648,349,115 | 36.07h |
| 7 | Sol High | 90.1 | 67/112 | 112 | $641.04 | 878,549,545 | 44.16h |
| 8 | Gpt-5.5 High | 84.7 | 63/112 | 112 | $433.57 | 549,443,804 | 34.84h |
| 9 | Sol Low | 75.3 | 56/112 | 112 | $238.86 | 281,014,702 | 22.59h |
| 10 | Luna High | 70 | 52/112 | 112 | $113.02 | 714,465,763 | 35.08h |
| 11 | Terra High | 65.9 | 49/112 | 112 | $156.76 | 358,992,188 | 24.59h |

## 口径说明

- 当前接口提供模型级 `score`、通过数、任务数、Token、耗时和估算费用。
- 当前接口没有返回十道任务的逐题通过矩阵，因此不能仅凭 API 摘要重新计算 `加权分 /100`。
- 加权排名仍以仓库中的逐题数据和权重快照为准；本报告用于自动监控源站最新摘要。
- 源站数据未变化时，自动任务仍会更新监控心跳，但不会把它描述成新的模型测试批次。
- 原始 API 响应不写入公开仓库，只保存必要的模型摘要字段。

当前已归档 API 快照数：**58**。


---

<a id="english"></a>
# Codex Radar API Monitor — English

[简体中文](api-latest.zh-CN.md) · [Project home](../README.md) · [API history CSV](../data/api/model_iq_history.csv) · [Monitor status](../data/api/monitor_status.json)

**Last successful check:** `2026-07-23T04:41:29+00:00`  
**Current API snapshot:** `e6a18a82e898633d`  
**Source observation:** `2026-07-22T06:57:20.626603+08:00`  
**New snapshot detected:** yes  
**Models returned:** 11

> “Last successful check” confirms that the automation reached the API. “Source observation” is supplied by the upstream endpoint and may be older.

> This is a model-level summary from the Codex Radar API, not the project's task-level difficulty-weighted score.

## Current API model summary

| Rank | Model tier | Source score | Passed | Tasks | Cost | Total tokens | Wall time |
|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | Sol Xhigh | 100.9 | 75/112 | 112 | $776.65 | 1,052,887,988 | 48.98h |
| 2 | Gpt-5.5 Xhigh | 96.9 | 72/112 | 112 | $654.08 | 843,471,087 | 46.38h |
| 3 | Terra Max | 96.9 | 72/112 | 112 | $519.07 | 1,348,930,170 | 61.28h |
| 4 | Sol Medium | 92.8 | 69/112 | 112 | $431.84 | 550,033,877 | 32.67h |
| 5 | Luna Max | 91.5 | 68/112 | 112 | $278.07 | 1,902,419,844 | 64.56h |
| 6 | Terra Xhigh | 91.5 | 68/112 | 112 | $269.22 | 648,349,115 | 36.07h |
| 7 | Sol High | 90.1 | 67/112 | 112 | $641.04 | 878,549,545 | 44.16h |
| 8 | Gpt-5.5 High | 84.7 | 63/112 | 112 | $433.57 | 549,443,804 | 34.84h |
| 9 | Sol Low | 75.3 | 56/112 | 112 | $238.86 | 281,014,702 | 22.59h |
| 10 | Luna High | 70 | 52/112 | 112 | $113.02 | 714,465,763 | 35.08h |
| 11 | Terra High | 65.9 | 49/112 | 112 | $156.76 | 358,992,188 | 24.59h |

## Interpretation

- The endpoint provides model-level `score`, pass counts, task counts, tokens, wall time, and estimated cost.
- It does not expose the ten task-level outcomes, so `Weighted /100` cannot be recomputed from this API summary alone.
- Task-weighted rankings remain based on the repository's task matrix and weight snapshots; this report monitors the latest API summary.
- When source data is unchanged, the automation still updates its heartbeat without presenting it as a new benchmark batch.
- The raw API response is not stored in the public repository; only required model-summary fields are archived.

Archived API snapshots: **58**.

