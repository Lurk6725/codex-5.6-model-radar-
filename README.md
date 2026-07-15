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

**最新数据：** `2026-07-15-am`，网页更新时间 08:03  
**最新权重快照：** `2026-07-15-0803`

| 使用场景 | 当前建议 | 说明 |
|---|---|---|
| 低成本、允许重试 | **Sol Low** | 本轮回落到 6/10，仍便宜，但不能用于不可重试的重要任务 |
| 日常开发与小项目 Bug 审查 | **Sol Medium** | 9/10、加权分 82.98，仍是能力、成本和稳定性的最佳平衡 |
| 高价值困难任务 | **先用 Sol Medium；失败后升级 Sol XHigh** | XHigh 本轮 10/10，但长期中位数仍低于本轮表现，升级结论置信度为中等 |
| 特定高难任务/第 07 类任务 | **Terra Max 可作为专项候选** | 本轮 8/10并通过最难第 07 题，费用低于 Sol XHigh 和 Sol Max |
| 不建议自动升级 | Sol Max、Sol High | 本轮二者逐题完全相同，High 费用约为 Max 的 39% |

## 最新任务难度权重

`weight_i ∝ 1 / sqrt(historical_pass_rate_i)`，归一化总分为 100。

| 题号 | 历史通过率 | 权重 /100 |
|---:|---:|---:|
| 01 | 78.59% | 7.92 |
| 02 | 79.77% | 7.86 |
| 03 | 94.43% | 7.23 |
| 04 | 39.59% | 11.16 |
| 05 | 37.54% | 11.46 |
| 06 | 93.84% | 7.25 |
| 07 | 17.01% | **17.02** |
| 08 | 49.85% | 9.94 |
| 09 | 39.00% | 11.24 |
| 10 | 62.06% | 8.91 |
|  | **合计** | **100.00** |

## 最新模型加权排名

| 排名 | 模型档位 | 通过 | 加权分 /100 | 费用 | 加权分/$ |
|---:|---|---:|---:|---:|---:|
| 1 | **Sol XHigh** | 10/10 | **100.00** | $34.80 | 2.87 |
| 2 | **Sol Medium** | 9/10 | **82.98** | $17.80 | **4.66** |
| 3 | Terra Max | 8/10 | 79.93 | $28.30 | 2.82 |
| 4 | Sol High | 8/10 | 74.06 | $23.50 | 3.15 |
| 5 | Sol Max | 8/10 | 74.06 | $60.10 | 1.23 |
| 6 | Sol Low | 6/10 | 59.73 | $8.80 | 6.79 |
| 7 | Luna Max | 6/10 | 54.98 | $17.10 | 3.22 |
| 8 | Terra High | 6/10 | 50.41 | $9.20 | 5.48 |
| 9 | Luna High | 5/10 | 46.42 | $6.30 | **7.37** |

`加权分/$` 会偏爱便宜但绝对成功率较低的档位，不能脱离加权分和多轮稳定性单独使用。

## 最新批次判断

本轮九个档位合计 **66/90**，总费用约 **$205.89**，总 Token 约 **366.7M**。相较 7 月 14 日下午，质量增加约 13.8%，费用基本持平，Token 增加约 0.8%。本轮记为**有效批次**，不触发异常降权。

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

**Latest data:** `2026-07-15-am`, public-page update 08:03  
**Latest weight snapshot:** `2026-07-15-0803`

| Work type | Recommendation | Rationale |
|---|---|---|
| Low-cost and retryable | **Sol Low** | It fell to 6/10 this round; still cheap, but unsuitable for important non-retryable work |
| Daily development and small-project bug review | **Sol Medium** | 9/10 and 82.98 weighted points remain the best balance of quality, cost, and stability |
| High-value difficult work | **Start with Sol Medium, then escalate to Sol XHigh** | XHigh reached 10/10, but its long-run median is below this single-round result |
| Task-07-like specialization | **Terra Max as a specialist candidate** | It reached 8/10 and passed the hardest task at lower cost than Sol XHigh and Sol Max |
| Do not upgrade automatically | Sol Max and Sol High | They had identical task outcomes, while High cost about 39% as much as Max |

## Latest weighted ranking

| Rank | Model tier | Passed | Weighted /100 | Cost | Weighted/$ |
|---:|---|---:|---:|---:|---:|
| 1 | **Sol XHigh** | 10/10 | **100.00** | $34.80 | 2.87 |
| 2 | **Sol Medium** | 9/10 | **82.98** | $17.80 | **4.66** |
| 3 | Terra Max | 8/10 | 79.93 | $28.30 | 2.82 |
| 4 | Sol High | 8/10 | 74.06 | $23.50 | 3.15 |
| 5 | Sol Max | 8/10 | 74.06 | $60.10 | 1.23 |
| 6 | Sol Low | 6/10 | 59.73 | $8.80 | 6.79 |
| 7 | Luna Max | 6/10 | 54.98 | $17.10 | 3.22 |
| 8 | Terra High | 6/10 | 50.41 | $9.20 | 5.48 |
| 9 | Luna High | 5/10 | 46.42 | $6.30 | **7.37** |

The nine tiers produced **66/90** at about **$205.89** and **366.7M tokens**. Quality improved 13.8% from the previous afternoon batch while cost was essentially unchanged, so this is recorded as a valid batch.

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
