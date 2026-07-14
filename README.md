# GPT‑5.6 Codex Model Radar

[简体中文](#简体中文) · [English](#english) · [最新分析 / Latest report](reports/latest.md) · [API 自动监控 / API monitor](reports/api-latest.md) · [历史数据 / History](reports/history/README.md)

> **数据来源 / Data attribution:** 原始基准测试数据来自 **Codex Radar**（`codexradar.com`）。本仓库是独立二次分析项目，与 OpenAI、Codex Radar 或 DeepSWE 无官方隶属关系。  
> Source benchmark data comes from **Codex Radar** (`codexradar.com`). This is an independent secondary-analysis project and is not affiliated with OpenAI, Codex Radar, or DeepSWE.

---

# 简体中文

## 项目简介

本项目长期记录 GPT‑5.6 Codex 的 **Luna、Terra、Sol** 各模型家族与推理强度，并同时维护：

- 授权 API 提供的模型级总分、通过数、费用、Token 和耗时趋势；
- 公开网页提供的逐题矩阵、任务难度权重和加权分；
- 多轮稳定性、异常批次和模型推荐。

API 不提供逐题结果、每模型 run ID 或完整/部分重跑标记。因此自动 API 汇总与逐题加权榜分开保存；缺失数据由公开网页人工核对补齐。

## 当前模型推荐

**最新数据：** `2026-07-14-pm`，网页更新时间 14:34  
**最新逐题权重快照：** `2026-07-14-1434`

| 使用场景 | 当前建议 | 说明 |
|---|---|---|
| 机械、低风险、允许重试 | **Sol Low** | 连续两轮 8/10，本轮精确加权分/$ 为 8.46；历史仍有明显波动 |
| 日常开发与小项目 Bug 审查 | **Sol Medium** | 本轮汇总 7/10，与 High、XHigh 同分但更便宜；逐题列表存在一题不一致，置信度暂为中等 |
| 高难任务与最终兜底 | **Sol Max** | 本轮加权分最高 83.33，并通过最难第 07 题；费用 $49.90，只应在较低档失败后使用 |
| 暂不建议作为默认 | Terra High、Luna High、Luna Max、Sol XHigh | 当前绝对质量、成本或稳定性不占优 |

## 最新任务难度权重

`weight_i ∝ 1 / sqrt(historical_pass_rate_i)`，归一化总分为 100。

| 题号 | 历史通过率 | 权重 /100 |
|---:|---:|---:|
| 01 | 78.92% | 7.85 |
| 02 | 79.22% | 7.83 |
| 03 | 94.58% | 7.17 |
| 04 | 39.16% | 11.14 |
| 05 | 36.45% | 11.55 |
| 06 | 93.67% | 7.20 |
| 07 | 16.57% | **17.13** |
| 08 | 49.40% | 9.92 |
| 09 | 37.65% | 11.36 |
| 10 | 62.24% | 8.84 |
|  | **合计** | **100.00** |

## 最新模型加权排名

| 排名 | 模型档位 | 通过 | 加权分 /100 | 费用 | 加权分/$ |
|---:|---|---:|---:|---:|---:|
| 1 | **Sol Max** | 8/10 | **83.33** | $49.90 | 1.67 |
| 2 | **Sol Low** | 8/10 | **78.94** | $9.33 | **8.46** |
| 3–5* | **Sol Medium** | 7/10 | **66.18–75.48** | $16.85 | 3.93–4.48 |
| 3–5 | Sol High | 7/10 | 66.20 | $27.03 | 2.45 |
| 3–5 | Sol XHigh | 7/10 | 66.20 | $37.05 | 1.79 |
| 6 | Terra Max | 7/10 | 62.48 | $34.91 | 1.79 |
| 7 | Luna Max | 6/10 | 52.97 | $16.33 | 3.24 |
| 8 | Luna High | 5/10 | 41.42 | $5.88 | 7.05 |
| 9 | Terra High | 3/10 | 22.21 | $9.14 | 2.43 |

\* 源站汇总/API 将 Sol Medium 标为 7/10，但公开逐题列表只显示 6 个明确通过项，因此无法唯一确定精确加权分。仓库保留两份源信息，并显示 mathematically possible range，而不擅自猜测缺失题目。

`加权分/$` 会偏爱便宜模型，不能脱离绝对加权分和长期稳定性单独使用。

## 最新批次判断

本轮九个档位合计 **58/90**，总费用约 **$206.40**，总 Token 约 **363.7M**。相较上午批次，质量增加约 1.8%，费用增加约 0.9%，Token 增加约 8.2%。它不满足异常批次条件，因此记为**有效批次，附高消耗与来源不一致警告**。

## 数据入口

- [最新中英文分析](reports/latest.md)
- [API 自动监控](reports/api-latest.md)
- [逐批次历史索引](reports/history/README.md)
- [模型汇总历史 CSV](data/history/runs.csv)
- [逐题矩阵历史 CSV](data/history/task_matrices.csv)
- [最新任务权重 CSV](data/weights/task_weights.csv)
- [评分方法](docs/METHODOLOGY.md)
- [API 接入与限制](docs/API_INTEGRATION.md)

---

# English

## Project overview

This repository tracks GPT‑5.6 Codex **Luna, Terra, and Sol** families and reasoning-effort tiers using two evidence streams:

- authorized API aggregates for score, passes, cost, tokens, and wall time;
- public-page task matrices for difficulty-weighted scores and weighted score per dollar.

The API does not expose task outcomes, per-model run IDs, or full-versus-partial rerun markers. Missing task-level information is therefore verified from the public page rather than inferred from aggregate totals.

## Current model recommendations

**Latest data:** `2026-07-14-pm`, public-page update 14:34  
**Latest weight snapshot:** `2026-07-14-1434`

| Work type | Recommendation | Rationale |
|---|---|---|
| Mechanical, low-risk, retryable | **Sol Low** | Two consecutive 8/10 runs and an exact weighted/$ of 8.46, though its older history remains volatile |
| Daily development and small-project bug review | **Sol Medium** | Aggregate 7/10, tying High and XHigh at lower cost; confidence is medium because the source task list has a one-task mismatch |
| Difficult work and final fallback | **Sol Max** | Highest weighted score at 83.33 and passed task 07, but costs $49.90 |
| Not recommended as defaults | Terra High, Luna High, Luna Max, Sol XHigh | Current quality, cost, or stability is not competitive |

## Latest task weights

| Task | Historical pass rate | Weight /100 |
|---:|---:|---:|
| 01 | 78.92% | 7.85 |
| 02 | 79.22% | 7.83 |
| 03 | 94.58% | 7.17 |
| 04 | 39.16% | 11.14 |
| 05 | 36.45% | 11.55 |
| 06 | 93.67% | 7.20 |
| 07 | 16.57% | **17.13** |
| 08 | 49.40% | 9.92 |
| 09 | 37.65% | 11.36 |
| 10 | 62.24% | 8.84 |
|  | **Total** | **100.00** |

## Latest weighted ranking

| Rank | Model tier | Passed | Weighted /100 | Cost | Weighted/$ |
|---:|---|---:|---:|---:|---:|
| 1 | **Sol Max** | 8/10 | **83.33** | $49.90 | 1.67 |
| 2 | **Sol Low** | 8/10 | **78.94** | $9.33 | **8.46** |
| 3–5* | **Sol Medium** | 7/10 | **66.18–75.48** | $16.85 | 3.93–4.48 |
| 3–5 | Sol High | 7/10 | 66.20 | $27.03 | 2.45 |
| 3–5 | Sol XHigh | 7/10 | 66.20 | $37.05 | 1.79 |
| 6 | Terra Max | 7/10 | 62.48 | $34.91 | 1.79 |
| 7 | Luna Max | 6/10 | 52.97 | $16.33 | 3.24 |
| 8 | Luna High | 5/10 | 41.42 | $5.88 | 7.05 |
| 9 | Terra High | 3/10 | 22.21 | $9.14 | 2.43 |

\* The aggregate/API result reports Sol Medium as 7/10, while the public per-task list contains only six explicit passes. The repository preserves both source statements and reports the mathematically possible weighted-score range rather than guessing the missing task.

## Batch status

The nine tiers produced **58/90**, about **$206.40**, and **363.7M tokens**. Versus the morning batch, quality rose about 1.8%, cost rose about 0.9%, and tokens rose about 8.2%. The batch is recorded as **valid with high-consumption and source-consistency warnings**.

## Data links

- [Latest bilingual analysis](reports/latest.md)
- [API monitor](reports/api-latest.md)
- [Historical index](reports/history/README.md)
- [Aggregate run history](data/history/runs.csv)
- [Task-matrix history](data/history/task_matrices.csv)
- [Current weights](data/weights/task_weights.csv)

## License

Code and original analysis are released under the MIT License. Third-party benchmark data remains subject to its source terms and attribution requirements.
