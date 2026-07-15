# GPT‑5.6 Codex Model Radar

[简体中文](#简体中文) · [English](#english) · [最新分析 / Latest report](reports/latest.md) · [API 自动监控 / API monitor](reports/api-latest.md) · [历史数据 / History](reports/history/README.md)

> **数据来源 / Data attribution:** 原始基准测试数据来自 **Codex Radar**（`codexradar.com`）。本仓库是独立二次分析项目，与 OpenAI、Codex Radar 或 DeepSWE 无官方隶属关系。  
> Source benchmark data comes from **Codex Radar** (`codexradar.com`). This is an independent secondary-analysis project and is not affiliated with OpenAI, Codex Radar, or DeepSWE.

---

# 简体中文

## 项目简介

本项目长期记录 GPT‑5.6 Codex 的 **Luna、Terra、Sol** 模型家族和推理强度，并分别维护：

- 授权 API 提供的模型级分数、通过数、费用、Token 和耗时；
- 公开网页提供的逐题矩阵、历史通过率和难度加权分；
- 多轮稳定性、异常批次和实际模型推荐。

API 不提供逐题结果、每模型 run ID 或完整/部分重跑标记，因此 API 汇总和逐题加权榜分开保存，缺失信息由公开网页核对补齐。

## 当前模型推荐

**最新数据：** `2026-07-15-pm`，网页更新时间 17:22  
**最新权重快照：** `2026-07-15-1722`

| 使用场景 | 当前建议 | 说明 |
|---|---|---|
| 低成本、允许重试 | **Sol Low** | 本轮 8/10、加权分 71.69；历史仍有波动，不适合不可重试的重要任务 |
| 日常开发与小项目 Bug 审查 | **Sol Medium** | 本轮回落到 6/10，但长期中位数和成本仍优于 High/XHigh；默认结论保留、置信度下降 |
| 高难、额度敏感、允许后台长跑 | **Luna Max** | 本轮 9/10、加权分 90.08，并通过最难第 07 题；费用仅 $16.30 |
| Sol 系失败后的升级 | **优先 Sol High，而不是 XHigh/Max** | High 与 XHigh 同为 7/10，但 High 更便宜且加权分略高；Max 仅 6/10、费用最高 |
| 暂不建议默认 | Terra High、Luna High、Sol Max | 当前绝对质量、稳定性或成本不占优 |

## 最新任务难度权重

`weight_i ∝ 1 / sqrt(historical_pass_rate_i)`，归一化总分为 100。

| 题号 | 历史通过率 | 权重 /100 |
|---:|---:|---:|
| 01 | 78.86% | 7.93 |
| 02 | 79.71% | 7.88 |
| 03 | 94.29% | 7.25 |
| 04 | 39.71% | 11.17 |
| 05 | 38.29% | 11.37 |
| 06 | 94.00% | 7.26 |
| 07 | 16.86% | **17.14** |
| 08 | 50.29% | 9.92 |
| 09 | 40.29% | 11.09 |
| 10 | 61.32% | 8.99 |
|  | **合计** | **100.00** |

## 最新模型加权排名

| 排名 | 模型档位 | 通过 | 加权分 /100 | 费用 | 加权分/$ |
|---:|---|---:|---:|---:|---:|
| 1 | **Luna Max** | 9/10 | **90.08** | $16.30 | **5.53** |
| 2 | **Sol Low** | 8/10 | **71.69** | $10.70 | **6.70** |
| 3 | Sol High | 7/10 | 64.44 | $25.00 | 2.58 |
| 4 | Terra Max | 7/10 | 62.78 | $34.00 | 1.85 |
| 5 | Sol XHigh | 7/10 | 62.50 | $32.60 | 1.92 |
| 6 | Sol Medium | 6/10 | 54.82 | $16.60 | 3.30 |
| 7 | Sol Max | 6/10 | 54.61 | $51.40 | 1.06 |
| 8 | Terra High | 5/10 | 44.85 | $9.30 | 4.82 |
| 9 | Luna High | 5/10 | 41.40 | $6.70 | 6.18 |

`加权分/$` 会偏爱便宜但绝对成功率较低的档位，不能脱离加权分和多轮稳定性单独使用。

## 最新批次判断

本轮九个档位合计 **60/90**，总费用约 **$202.58**，总 Token 约 **360.7M**。相较上午批次，质量下降约 9.1%，费用和 Token 均小幅下降约 1.6%，未触发项目的异常批次规则，因此记为**有效批次**。

## 数据入口

- [最新中英文分析](reports/latest.md)
- [API 自动监控](reports/api-latest.md)
- [逐批次历史索引](reports/history/README.md)
- [基础模型汇总历史](data/history/runs.csv)
- [按批次新增的模型汇总](data/history/batches/)
- [逐题矩阵历史](data/history/task_matrices.csv)
- [最新任务权重](data/weights/task_weights.csv)
- [评分方法](docs/METHODOLOGY.md)
- [推荐框架](docs/RECOMMENDATIONS.md)

---

# English

## Project overview

This repository tracks GPT‑5.6 Codex **Luna, Terra, and Sol** families and reasoning-effort tiers using two evidence streams:

- authorized API aggregates for score, passes, cost, tokens, and wall time;
- public-page task matrices for difficulty-weighted scores and weighted score per dollar.

The API does not expose task outcomes, per-model run IDs, or full-versus-partial rerun markers, so aggregate monitoring and task-weighted rankings remain separate.

## Current model recommendations

**Latest data:** `2026-07-15-pm`, public-page update 17:22  
**Latest weight snapshot:** `2026-07-15-1722`

| Work type | Recommendation | Rationale |
|---|---|---|
| Low-cost and retryable | **Sol Low** | 8/10 and 71.69 weighted points, but historical volatility still makes it unsuitable for important non-retryable work |
| Daily development and small-project bug review | **Sol Medium** | It fell to 6/10, but its multi-run median and cost still support the default position; confidence is lower |
| Difficult, quota-sensitive, background execution | **Luna Max** | 9/10, 90.08 weighted points, task 07 passed, and only $16.30 |
| Escalation after a Sol-tier failure | **Prefer Sol High over XHigh or Max** | High tied XHigh at 7/10 while costing less and scoring slightly higher; Max reached only 6/10 |
| Not recommended as defaults | Terra High, Luna High, Sol Max | Current absolute quality, stability, or cost is not competitive |

## Latest weighted ranking

| Rank | Model tier | Passed | Weighted /100 | Cost | Weighted/$ |
|---:|---|---:|---:|---:|---:|
| 1 | **Luna Max** | 9/10 | **90.08** | $16.30 | **5.53** |
| 2 | **Sol Low** | 8/10 | **71.69** | $10.70 | **6.70** |
| 3 | Sol High | 7/10 | 64.44 | $25.00 | 2.58 |
| 4 | Terra Max | 7/10 | 62.78 | $34.00 | 1.85 |
| 5 | Sol XHigh | 7/10 | 62.50 | $32.60 | 1.92 |
| 6 | Sol Medium | 6/10 | 54.82 | $16.60 | 3.30 |
| 7 | Sol Max | 6/10 | 54.61 | $51.40 | 1.06 |
| 8 | Terra High | 5/10 | 44.85 | $9.30 | 4.82 |
| 9 | Luna High | 5/10 | 41.40 | $6.70 | 6.18 |

The nine tiers produced **60/90** at about **$202.58** and **360.7M tokens**. Quality declined 9.1% from the morning batch while cost and tokens also declined slightly, so this remains a valid batch.

## Data links

- [Latest bilingual analysis](reports/latest.md)
- [API monitor](reports/api-latest.md)
- [Historical index](reports/history/README.md)
- [Legacy aggregate history](data/history/runs.csv)
- [Per-batch aggregate files](data/history/batches/)
- [Task-matrix history](data/history/task_matrices.csv)
- [Current weights](data/weights/task_weights.csv)

## License

Code and original analysis are released under the MIT License. Third-party benchmark data remains subject to its source terms and attribution requirements.
