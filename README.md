# GPT‑5.6 Codex Model Radar

[简体中文](#简体中文) · [English](#english) · [最新分析 / Latest report](reports/latest.md) · [API 自动监控 / API monitor](reports/api-latest.md) · [历史数据 / History](reports/history/README.md)

> **数据来源 / Data attribution:** 原始基准测试数据来自 **Codex Radar**（`codexradar.com`，原 `codex-reset-radar.pages.dev`）。本仓库是独立的二次分析项目，与 OpenAI、Codex Radar 或 DeepSWE 均无官方隶属关系。  
> Source benchmark data comes from **Codex Radar** (`codexradar.com`, formerly `codex-reset-radar.pages.dev`). This is an independent secondary-analysis project and is not affiliated with OpenAI, Codex Radar, or DeepSWE.

---

# 简体中文

## 项目简介

本项目长期记录 GPT‑5.6 Codex 的 **Luna、Terra、Sol** 各模型家族及不同推理强度，并提供：

- 逐题难度加权分与加权分/$；
- API 模型级总分、费用、Token 和耗时趋势；
- 多轮稳定性、异常状态和推荐变化；
- 面向真实开发场景的模型选择建议。

已获授权的 Codex Radar API 自动更新模型级摘要，见 [API 自动监控](reports/api-latest.md)。API 不提供逐题矩阵、每模型 run ID 或完整/部分重跑标记，因此模型级 API 汇总与逐题加权榜分开维护。

## 当前模型推荐

**最新 API 数据日期：** `2026-07-14-am`  
**最新逐题矩阵：** `2026-07-13-1405`

| 使用场景 | 当前建议 | 说明 |
|---|---|---|
| 机械、低风险、允许重试 | **Terra Medium**；Sol Low 待复测 | Luna Medium 最新只有 1/10；Sol Low 的 8/10 仍需重复验证 |
| 日常开发与小项目 Bug 审查 | **Sol Medium** | 最新 9/10，与 High 同分但更便宜、更快 |
| 高难、额度敏感、允许后台长跑 | **先用 Sol Medium；Luna Max 作为观察候选** | Luna Max 最新降至 6/10，暂不再列为明确首选 |
| 最高能力兜底 | **Sol Max（历史结论）** | 最新 API 未返回 Sol Max，当前状态无法确认 |

## 最新 API 汇总趋势

> 下面是模型级等权总分，不是逐题难度加权排名。

| 排名 | 模型档位 | 通过 | 源站分数 | 费用 | 原始分/$ | Token | 耗时 |
|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | Sol High | 9/10 | 135 | $24.62 | 5.48 | 23.50M | 0.54h |
| 1 | **Sol Medium** | 9/10 | 135 | **$18.41** | **7.33** | **18.48M** | **0.46h** |
| 3 | Sol Low | 8/10 | 120 | $9.73 | 12.33 | 8.20M | 0.27h |
| 4 | Terra Max | 7/10 | 105 | $30.91 | 3.40 | 65.72M | 0.63h |
| 5 | Luna Max | 6/10 | 90 | $15.11 | 5.96 | 88.73M | 0.66h |
| 5 | Sol XHigh | 6/10 | 90 | $37.97 | 2.37 | 40.67M | 0.75h |
| 7 | Terra Medium | 5/10 | 75 | $5.18 | **14.48** | 8.01M | 0.39h |
| 8 | Luna Medium | 1/10 | 15 | $2.44 | 6.15 | 10.81M | 0.41h |

与上一 API 快照相比，八个返回档位的通过数总和从 44 增加到 51，费用基本持平，Token 下降约 11%，耗时下降约 28%。这说明整体状态从 7 月 13 日异常快照中明显恢复，但最新接口没有 Sol Max，也无法确认是否为完整重跑。

## 最近可计算的任务难度权重

**权重快照：** `2026-07-13-1405`  
**计算方法：** `weight_i ∝ 1 / sqrt(historical_pass_rate_i)`，归一化总分为 100。

| 题号 | 任务摘要 | 历史通过率 | 权重 /100 |
|---:|---|---:|---:|
| 01 | Ordered-map JSONPath API | 79% | 7.76 |
| 02 | Module loading and cache behavior | 80% | 7.71 |
| 03 | HTTPX multipart response parsing | 95% | 7.09 |
| 04 | Bandit incremental cache controls | 38% | 11.15 |
| 05 | IPython session replay behavior | 34% | 11.81 |
| 06 | ofetch origin-aware circuit breaker | 94% | 7.14 |
| 07 | Wiki and Markdown link conversion | 16% | **17.11** |
| 08 | CSS lexer abbreviation conversion | 49% | 9.91 |
| 09 | fd deterministic multi-key sorting | 35% | 11.70 |
| 10 | Stylesheet selector structure | 64% | 8.62 |
|  | **合计** |  | **100.00** |

## 最近可计算的模型加权排名

**逐题矩阵：** `2026-07-13-pm-anomaly`（14:05，异常批次，长期趋势权重 `0.35`）

| 排名 | 模型档位 | 通过 | 加权分 /100 | 估算费用 | 加权分/$ |
|---:|---|---:|---:|---:|---:|
| 1 | Luna Max | 7/10 | **70.31** | $18.90 | 3.72 |
| 2 | Sol XHigh | 7/10 | 66.56 | $33.60 | 1.98 |
| 3 | Sol High | 6/10 | 59.47 | $26.80 | 2.22 |
| 4 | Terra Max | 6/10 | 56.60 | $32.20 | 1.76 |
| 5 | Sol Low | 6/10 | 53.21 | $9.40 | 5.66 |
| 6 | Terra Medium | 5/10 | 50.38 | $6.00 | **8.40** |
| 7 | Sol Max | 5/10 | 48.32 | $59.80 | 0.81 |
| 8 | Sol Medium | 5/10 | 45.50 | $16.10 | 2.83 |
| 9 | Luna Medium | 2/10 | 18.24 | $2.40 | 7.60 |

此表不会随模型级 API 摘要自动重算。只有获得新的逐题矩阵后，才会更新加权分与加权分/$。

## 历史数据与方法

- [最新中英文分析](reports/latest.md)
- [API 自动监控报告](reports/api-latest.md)
- [API 历史 CSV](data/api/model_iq_history.csv)
- [逐批次历史索引](reports/history/README.md)
- [评分方法](docs/METHODOLOGY.md)
- [API 接入与限制](docs/API_INTEGRATION.md)

---

# English

## Project overview

This repository monitors GPT‑5.6 Codex **Luna, Terra, and Sol** families and their reasoning-effort tiers. It maintains two separate evidence tracks:

- task-matrix difficulty-weighted scores and weighted score per dollar;
- authorized API aggregate trends for score, pass count, cost, tokens, and wall time.

The API does not expose task outcomes, per-model run IDs, or full-versus-partial rerun markers. Aggregate API snapshots are therefore not mislabeled as task-weighted rankings.

## Current model recommendations

**Latest API source date:** `2026-07-14-am`  
**Latest task matrix:** `2026-07-13-1405`

| Work type | Current recommendation | Rationale |
|---|---|---|
| Mechanical, low-risk, retryable | **Terra Medium**; Sol Low pending repetition | Luna Medium fell to 1/10; Sol Low's 8/10 needs confirmation |
| Daily development and small-project bug review | **Sol Medium** | Latest result is 9/10, tying High while cheaper and faster |
| Difficult, quota-sensitive, long-running | **Try Sol Medium first; Luna Max remains a watchlist option** | Luna Max fell to 6/10 and is no longer the clear default |
| Maximum-capability fallback | **Sol Max, based on historical evidence** | Sol Max is absent from the latest API snapshot |

## Latest API aggregate trend

> This is an equal-weight model-level summary, not a task-weighted ranking.

| Rank | Model tier | Passed | Source score | Cost | Raw score/$ | Tokens | Time |
|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | Sol High | 9/10 | 135 | $24.62 | 5.48 | 23.50M | 0.54h |
| 1 | **Sol Medium** | 9/10 | 135 | **$18.41** | **7.33** | **18.48M** | **0.46h** |
| 3 | Sol Low | 8/10 | 120 | $9.73 | 12.33 | 8.20M | 0.27h |
| 4 | Terra Max | 7/10 | 105 | $30.91 | 3.40 | 65.72M | 0.63h |
| 5 | Luna Max | 6/10 | 90 | $15.11 | 5.96 | 88.73M | 0.66h |
| 5 | Sol XHigh | 6/10 | 90 | $37.97 | 2.37 | 40.67M | 0.75h |
| 7 | Terra Medium | 5/10 | 75 | $5.18 | **14.48** | 8.01M | 0.39h |
| 8 | Luna Medium | 1/10 | 15 | $2.44 | 6.15 | 10.81M | 0.41h |

Across the eight returned tiers, total passes rose from 44 to 51 while aggregate cost was nearly flat, tokens fell about 11%, and wall time fell about 28%. This is a broad recovery signal from the July 13 anomalous snapshot. However, Sol Max is missing and the API cannot confirm a complete rerun.

## Latest computable task weights

**Weight snapshot:** `2026-07-13-1405`  
**Formula:** `weight_i ∝ 1 / sqrt(historical_pass_rate_i)`, normalized to 100.

| Task | Historical pass rate | Weight /100 |
|---:|---:|---:|
| 01 | 79% | 7.76 |
| 02 | 80% | 7.71 |
| 03 | 95% | 7.09 |
| 04 | 38% | 11.15 |
| 05 | 34% | 11.81 |
| 06 | 94% | 7.14 |
| 07 | 16% | **17.11** |
| 08 | 49% | 9.91 |
| 09 | 35% | 11.70 |
| 10 | 64% | 8.62 |
|  | **Total** | **100.00** |

## Latest computable weighted ranking

**Task matrix:** `2026-07-13-pm-anomaly` (14:05, trend reliability `0.35`)

| Rank | Model tier | Passed | Weighted /100 | Estimated cost | Weighted/$ |
|---:|---|---:|---:|---:|---:|
| 1 | Luna Max | 7/10 | **70.31** | $18.90 | 3.72 |
| 2 | Sol XHigh | 7/10 | 66.56 | $33.60 | 1.98 |
| 3 | Sol High | 6/10 | 59.47 | $26.80 | 2.22 |
| 4 | Terra Max | 6/10 | 56.60 | $32.20 | 1.76 |
| 5 | Sol Low | 6/10 | 53.21 | $9.40 | 5.66 |
| 6 | Terra Medium | 5/10 | 50.38 | $6.00 | **8.40** |
| 7 | Sol Max | 5/10 | 48.32 | $59.80 | 0.81 |
| 8 | Sol Medium | 5/10 | 45.50 | $16.10 | 2.83 |
| 9 | Luna Medium | 2/10 | 18.24 | $2.40 | 7.60 |

This table is not automatically recomputed from aggregate API data. It changes only when a new task-level matrix is available.

## Data and methodology

- [Latest bilingual analysis](reports/latest.md)
- [API monitor](reports/api-latest.md)
- [API history CSV](data/api/model_iq_history.csv)
- [Historical batch index](reports/history/README.md)
- [Scoring methodology](docs/METHODOLOGY.md)
- [API integration and limitations](docs/API_INTEGRATION.md)

## License

Code and original analysis are released under the MIT License. Third-party benchmark data remains subject to its source terms and attribution requirements.
