# Codex Radar API Monitor / API 自动监控

[简体中文](#简体中文) · [English](#english)

<a id="简体中文"></a>
# Codex Radar API 自动监控 — 简体中文

[English](api-latest.en.md) · [项目首页](../README.md) · [API 历史 CSV](../data/api/model_iq_history.csv) · [监控状态](../data/api/monitor_status.json)

**最近成功检查：** `2026-07-21T23:42:55+00:00`  
**当前 API 快照：** `a8c81a52711689be`  
**源站观测时间：** `2026-07-22T06:57:20.626603+08:00`  
**本次发现新快照：** 否；源站仍返回同一快照  
**返回模型数：** 11

> “最近成功检查”表示自动任务已正常访问 API；“源站观测时间”由上游接口提供，两者可能不同。

> 这是 Codex Radar API 返回的模型级摘要，不是本项目根据逐题矩阵计算的难度加权分。

## 当前 API 模型摘要

| 排名 | 模型档位 | 源站分数 | 通过 | 任务数 | 费用 | 总 Token | 耗时 |
|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | Terra Max | 102.2 | 76/112 | 112 | $525.91 | 1,365,377,297 | 63.14h |
| 2 | Luna Max | 96.9 | 72/112 | 112 | $278.22 | 1,914,123,207 | 66.09h |
| 3 | Gpt-5.5 Xhigh | 95.5 | 71/112 | 112 | $653.00 | 839,273,334 | 42.15h |
| 4 | Sol High | 94.2 | 70/112 | 112 | $566.30 | 726,045,964 | 42.04h |
| 5 | Sol Xhigh | 93.7 | 69/111 | 111 | $772.22 | 1,042,307,763 | 53.10h |
| 6 | Terra Xhigh | 92.8 | 69/112 | 112 | $276.98 | 670,589,152 | 37.14h |
| 7 | Sol Medium | 91.5 | 68/112 | 112 | $398.14 | 494,709,664 | 33.46h |
| 8 | Gpt-5.5 High | 78 | 58/112 | 112 | $402.44 | 502,621,502 | 30.02h |
| 9 | Sol Low | 77.4 | 57/111 | 111 | $228.40 | 264,732,858 | 23.72h |
| 10 | Luna High | 70 | 52/112 | 112 | $120.63 | 787,262,695 | 36.37h |
| 11 | Terra High | 68.6 | 51/112 | 112 | $143.84 | 323,722,247 | 25.31h |

## 口径说明

- 当前接口提供模型级 `score`、通过数、任务数、Token、耗时和估算费用。
- 当前接口没有返回十道任务的逐题通过矩阵，因此不能仅凭 API 摘要重新计算 `加权分 /100`。
- 加权排名仍以仓库中的逐题数据和权重快照为准；本报告用于自动监控源站最新摘要。
- 源站数据未变化时，自动任务仍会更新监控心跳，但不会把它描述成新的模型测试批次。
- 原始 API 响应不写入公开仓库，只保存必要的模型摘要字段。

当前已归档 API 快照数：**48**。


---

<a id="english"></a>
# Codex Radar API Monitor — English

[简体中文](api-latest.zh-CN.md) · [Project home](../README.md) · [API history CSV](../data/api/model_iq_history.csv) · [Monitor status](../data/api/monitor_status.json)

**Last successful check:** `2026-07-21T23:42:55+00:00`  
**Current API snapshot:** `a8c81a52711689be`  
**Source observation:** `2026-07-22T06:57:20.626603+08:00`  
**New snapshot detected:** no; the source returned the same snapshot  
**Models returned:** 11

> “Last successful check” confirms that the automation reached the API. “Source observation” is supplied by the upstream endpoint and may be older.

> This is a model-level summary from the Codex Radar API, not the project's task-level difficulty-weighted score.

## Current API model summary

| Rank | Model tier | Source score | Passed | Tasks | Cost | Total tokens | Wall time |
|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | Terra Max | 102.2 | 76/112 | 112 | $525.91 | 1,365,377,297 | 63.14h |
| 2 | Luna Max | 96.9 | 72/112 | 112 | $278.22 | 1,914,123,207 | 66.09h |
| 3 | Gpt-5.5 Xhigh | 95.5 | 71/112 | 112 | $653.00 | 839,273,334 | 42.15h |
| 4 | Sol High | 94.2 | 70/112 | 112 | $566.30 | 726,045,964 | 42.04h |
| 5 | Sol Xhigh | 93.7 | 69/111 | 111 | $772.22 | 1,042,307,763 | 53.10h |
| 6 | Terra Xhigh | 92.8 | 69/112 | 112 | $276.98 | 670,589,152 | 37.14h |
| 7 | Sol Medium | 91.5 | 68/112 | 112 | $398.14 | 494,709,664 | 33.46h |
| 8 | Gpt-5.5 High | 78 | 58/112 | 112 | $402.44 | 502,621,502 | 30.02h |
| 9 | Sol Low | 77.4 | 57/111 | 111 | $228.40 | 264,732,858 | 23.72h |
| 10 | Luna High | 70 | 52/112 | 112 | $120.63 | 787,262,695 | 36.37h |
| 11 | Terra High | 68.6 | 51/112 | 112 | $143.84 | 323,722,247 | 25.31h |

## Interpretation

- The endpoint provides model-level `score`, pass counts, task counts, tokens, wall time, and estimated cost.
- It does not expose the ten task-level outcomes, so `Weighted /100` cannot be recomputed from this API summary alone.
- Task-weighted rankings remain based on the repository's task matrix and weight snapshots; this report monitors the latest API summary.
- When source data is unchanged, the automation still updates its heartbeat without presenting it as a new benchmark batch.
- The raw API response is not stored in the public repository; only required model-summary fields are archived.

Archived API snapshots: **48**.

