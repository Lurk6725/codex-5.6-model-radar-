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

**最新数据：** `2026-07-14-am`，网页更新时间 07:46  
**最新逐题权重快照：** `2026-07-14-0746`

| 使用场景 | 当前建议 | 说明 |
|---|---|---|
| 机械、低风险、允许重试 | **Terra Medium**；Sol Low 为更强但波动较大的候选 | Terra Medium 成本低；Sol Low 本轮 8/10，但历史波动明显 |
| 日常开发与小项目 Bug 审查 | **Sol Medium** | 与 Sol High 同为 9/10、逐题完全相同，但更便宜 |
| 高难、额度敏感、允许后台长跑 | **先用 Sol Medium；Luna Max 仅作专项候选** | Luna Max 本轮 6/10，唯一通过第 07 题，但通用质量不如 Medium |
| 最高能力兜底 | **Sol Max 仅保留历史上限含义** | 本轮 6/10 且费用最高，Max 不等于稳定更强 |

## 最新任务难度权重

`weight_i ∝ 1 / sqrt(historical_pass_rate_i)`，归一化总分为 100。

| 题号 | 历史通过率 | 权重 /100 |
|---:|---:|---:|
| 01 | 78.88% | 7.80 |
| 02 | 79.81% | 7.76 |
| 03 | 94.41% | 7.13 |
| 04 | 38.82% | 11.12 |
| 05 | 35.40% | 11.65 |
| 06 | 93.48% | 7.17 |
| 07 | 16.15% | **17.25** |
| 08 | 49.38% | 9.86 |
| 09 | 36.02% | 11.55 |
| 10 | 63.24% | 8.71 |
|  | **合计** | **100.00** |

## 最新模型加权排名

| 排名 | 模型档位 | 通过 | 加权分 /100 | 费用 | 加权分/$ |
|---:|---|---:|---:|---:|---:|
| 1 | **Sol Medium** | 9/10 | **82.75** | $18.41 | **4.49** |
| 2 | Sol High | 9/10 | **82.75** | $24.62 | 3.36 |
| 3 | Sol Low | 8/10 | 71.63 | $9.73 | 7.36 |
| 4 | Terra Max | 7/10 | 62.92 | $30.91 | 2.04 |
| 5 | Luna Max | 6/10 | 60.29 | $15.11 | 3.99 |
| 6 | Sol Max | 6/10 | 59.15 | $60.20 | 0.98 |
| 7 | Sol XHigh | 6/10 | 54.64 | $37.97 | 1.44 |
| 8 | **Terra Medium** | 5/10 | 45.25 | **$5.18** | **8.73** |
| 9 | Luna Medium | 1/10 | 11.65 | $2.44 | 4.78 |

`加权分/$` 会偏爱便宜模型，不能脱离绝对加权分和长期稳定性单独使用。

## 最新批次判断

本轮九个档位合计 57/90，总费用约 $204.59，总 Token 约 336.1M。质量较 7 月 13 日异常批次明显恢复，但消耗仍高。由于质量相较最近正常批次只下降约 6.6%，未达到项目异常规则要求的 15%，因此记为**有效批次，附高消耗警告**。

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

**Latest data:** `2026-07-14-am`, public-page update 07:46  
**Latest weight snapshot:** `2026-07-14-0746`

| Work type | Recommendation | Rationale |
|---|---|---|
| Mechanical, low-risk, retryable | **Terra Medium**; Sol Low as a stronger but volatile candidate | Terra Medium is cheap; Sol Low reached 8/10 but remains unstable historically |
| Daily development and small-project bug review | **Sol Medium** | It tied Sol High at 9/10 with identical task outcomes at lower cost |
| Difficult, quota-sensitive, long-running | **Try Sol Medium first; Luna Max only as a specialized candidate** | Luna Max reached 6/10 and uniquely passed task 07, but broad quality was lower |
| Maximum-capability fallback | **Sol Max only as a historical-ceiling fallback** | It reached 6/10 at the highest cost |

## Latest task weights

| Task | Historical pass rate | Weight /100 |
|---:|---:|---:|
| 01 | 78.88% | 7.80 |
| 02 | 79.81% | 7.76 |
| 03 | 94.41% | 7.13 |
| 04 | 38.82% | 11.12 |
| 05 | 35.40% | 11.65 |
| 06 | 93.48% | 7.17 |
| 07 | 16.15% | **17.25** |
| 08 | 49.38% | 9.86 |
| 09 | 36.02% | 11.55 |
| 10 | 63.24% | 8.71 |
|  | **Total** | **100.00** |

## Latest weighted ranking

| Rank | Model tier | Passed | Weighted /100 | Cost | Weighted/$ |
|---:|---|---:|---:|---:|---:|
| 1 | **Sol Medium** | 9/10 | **82.75** | $18.41 | **4.49** |
| 2 | Sol High | 9/10 | **82.75** | $24.62 | 3.36 |
| 3 | Sol Low | 8/10 | 71.63 | $9.73 | 7.36 |
| 4 | Terra Max | 7/10 | 62.92 | $30.91 | 2.04 |
| 5 | Luna Max | 6/10 | 60.29 | $15.11 | 3.99 |
| 6 | Sol Max | 6/10 | 59.15 | $60.20 | 0.98 |
| 7 | Sol XHigh | 6/10 | 54.64 | $37.97 | 1.44 |
| 8 | **Terra Medium** | 5/10 | 45.25 | **$5.18** | **8.73** |
| 9 | Luna Medium | 1/10 | 11.65 | $2.44 | 4.78 |

## Batch status

The nine tiers produced 57/90 at about $204.59 and 336.1M tokens. Quality recovered substantially from the July 13 anomalous batch, while consumption remained elevated. Because the quality decline versus the latest valid morning batch was only about 6.6%, the batch is recorded as **valid with a high-consumption warning**.

## Data links

- [Latest bilingual analysis](reports/latest.md)
- [API monitor](reports/api-latest.md)
- [Historical index](reports/history/README.md)
- [Aggregate run history](data/history/runs.csv)
- [Task-matrix history](data/history/task_matrices.csv)
- [Current weights](data/weights/task_weights.csv)

## License

Code and original analysis are released under the MIT License. Third-party benchmark data remains subject to its source terms and attribution requirements.