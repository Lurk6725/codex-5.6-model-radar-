# GPT‑5.6 Codex Model Radar

[简体中文](#简体中文) · [English](#english) · [最新分析 / Latest report](reports/latest.md) · [历史数据 / History](reports/history/README.md)

> **数据来源 / Data attribution:** 原始基准测试数据来自 **Codex Radar**（`codexradar.com`，原 `codex-reset-radar.pages.dev`）。本仓库是独立的二次分析项目，与 OpenAI、Codex Radar 或 DeepSWE 均无官方隶属关系。  
> Source benchmark data comes from **Codex Radar** (`codexradar.com`, formerly `codex-reset-radar.pages.dev`). This is an independent secondary-analysis project and is not affiliated with OpenAI, Codex Radar, or DeepSWE.

---

# 简体中文

## 项目简介

本项目长期记录 GPT‑5.6 Codex 的 **Luna、Terra、Sol** 各模型家族及不同推理强度，并在公开测试结果基础上计算：

- 任务难度加权分；
- 加权分 / 美元等价费用；
- 多轮稳定性与异常批次；
- 成本—能力 Pareto 前沿；
- 面向实际开发场景的模型推荐。

当前项目只使用公开页面和公开摘要中的数据，并保留来源、时间戳、异常状态和数据精度说明。

## 当前模型推荐

推荐依据长期记录，而不是只看最新一轮。最新的 14:05 批次被标记为异常批次，因此不会以完整权重改变长期推荐。

| 使用场景 | 当前建议 | 说明 |
|---|---|---|
| 机械、低风险、允许重试 | Luna Medium 或 Terra Medium | 先检查最近几轮稳定性 |
| 日常 Codex 开发 | **Sol Medium** | 当前最均衡的默认档 |
| 高难、额度敏感、可长时间运行 | **Luna Max** | 成本较低，但耗时和 Token 较高 |
| 最高能力兜底 | **Sol Max** | 仅在较低档失败或成功价值极高时使用 |

## 最新任务难度权重

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

## 最新模型加权排名

**最新观测批次：** `2026-07-13-pm-anomaly`（14:05，异常批次，长期趋势权重 `0.35`）

| 排名 | 模型档位 | 通过 | 加权分 /100 | 估算费用 | 加权分/$ |
|---:|---|---:|---:|---:|---:|
| 1 | Luna Max | 7/10 | **70.31** | $18.90 | **3.72** |
| 2 | Sol XHigh | 7/10 | 66.56 | $33.60 | 1.98 |
| 3 | Sol High | 6/10 | 59.47 | $26.80 | 2.22 |
| 4 | Terra Max | 6/10 | 56.60 | $32.20 | 1.76 |
| 5 | Sol Low | 6/10 | 53.21 | $9.40 | 5.66 |
| 6 | Terra Medium | 5/10 | 50.38 | $6.00 | **8.40** |
| 7 | Sol Max | 5/10 | 48.32 | $59.80 | 0.81 |
| 8 | Sol Medium | 5/10 | 45.50 | $16.10 | 2.83 |
| 9 | Luna Medium | 2/10 | 18.24 | $2.40 | 7.60 |

由于该批次整体质量下降、费用和 Token 同时上升，长期推荐主要参考最近正常批次与滚动历史。详细解释见[最新分析](reports/latest.zh-CN.md)。

## 历史数据

所有已记录批次均可从[历史数据索引](reports/history/README.md)跳转查看。原始汇总数据保存在 [`data/history/runs.csv`](data/history/runs.csv)，任务权重快照保存在 [`data/weights/task_weights.csv`](data/weights/task_weights.csv)。

## 评分方法

```text
原始难度_i = 1 / sqrt(历史通过率_i)
题目权重_i = 100 × 原始难度_i / sum(原始难度)
难度加权分 = sum(题目权重_i × 是否通过_i)
额度效率 = 难度加权分 / 网站估算美元等价费用
```

完整方法见 [`docs/METHODOLOGY.md`](docs/METHODOLOGY.md)，订阅额度口径见 [`docs/COSTS.md`](docs/COSTS.md)。

## 局限

- 固定测试集只有十道题，单题会让原始通过率变化 10 个百分点；
- 每个模型/任务通常每批只运行一次，Agent 轨迹具有随机性；
- 历史通过率可能包含任务家族偏好；
- 估算费用是相对额度代理，不是官方账户扣费；
- 某模型在这十题上最优，不代表它在所有私人项目中同样最优。

---

# English

## Project overview

This repository tracks GPT‑5.6 Codex **Luna, Terra, and Sol** model families and their reasoning-effort tiers. It adds reproducible analysis on top of publicly visible Codex Radar results:

- task-difficulty weighting;
- weighted score per estimated dollar-equivalent cost;
- rolling stability and anomalous-batch handling;
- cost-quality Pareto frontiers; and
- practical recommendations by workload type.

The project uses public-page and public-summary data and records provenance, timestamps, anomaly status, and data precision.

## Current model recommendations

Recommendations are based on the recorded history, not on one latest run. The 14:05 batch is flagged as anomalous and therefore does not receive full trend weight.

| Work type | Current recommendation | Rationale |
|---|---|---|
| Mechanical, low-risk, retryable | Luna Medium or Terra Medium | Check recent stability first |
| General daily Codex work | **Sol Medium** | Best current balance for default use |
| Difficult, quota-sensitive, long-running | **Luna Max** | Lower estimated cost, but high latency and token use |
| Maximum-capability fallback | **Sol Max** | Use after cheaper tiers fail or when success value is very high |

## Latest task weights

**Weight snapshot:** `2026-07-13-1405`  
**Formula:** `weight_i ∝ 1 / sqrt(historical_pass_rate_i)`, normalized to 100.

| Task | Short description | Historical pass rate | Weight /100 |
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
|  | **Total** |  | **100.00** |

## Latest weighted model ranking

**Latest observed batch:** `2026-07-13-pm-anomaly` (14:05, anomalous, trend reliability weight `0.35`)

| Rank | Model tier | Passed | Weighted /100 | Estimated cost | Weighted/$ |
|---:|---|---:|---:|---:|---:|
| 1 | Luna Max | 7/10 | **70.31** | $18.90 | **3.72** |
| 2 | Sol XHigh | 7/10 | 66.56 | $33.60 | 1.98 |
| 3 | Sol High | 6/10 | 59.47 | $26.80 | 2.22 |
| 4 | Terra Max | 6/10 | 56.60 | $32.20 | 1.76 |
| 5 | Sol Low | 6/10 | 53.21 | $9.40 | 5.66 |
| 6 | Terra Medium | 5/10 | 50.38 | $6.00 | **8.40** |
| 7 | Sol Max | 5/10 | 48.32 | $59.80 | 0.81 |
| 8 | Sol Medium | 5/10 | 45.50 | $16.10 | 2.83 |
| 9 | Luna Medium | 2/10 | 18.24 | $2.40 | 7.60 |

Because this batch combines lower aggregate quality with higher cost and token activity, long-term recommendations primarily use recent valid batches and rolling history. See the [latest English analysis](reports/latest.en.md).

## Historical data

Every recorded batch is linked from the [history index](reports/history/README.md). Raw aggregate data is stored in [`data/history/runs.csv`](data/history/runs.csv), and the latest task-weight snapshot is stored in [`data/weights/task_weights.csv`](data/weights/task_weights.csv).

## Scoring

```text
raw_difficulty_i = 1 / sqrt(historical_pass_rate_i)
weight_i = 100 * raw_difficulty_i / sum(raw_difficulty)
weighted_score = sum(weight_i * passed_i)
quota_efficiency = weighted_score / estimated_USD_equivalent_cost
```

See [`docs/METHODOLOGY.md`](docs/METHODOLOGY.md) and [`docs/COSTS.md`](docs/COSTS.md).

## Limitations

- The active set contains only ten tasks;
- each model/task is generally observed once per batch;
- historical difficulty may include task-family bias;
- estimated cost is a relative quota proxy, not an official account debit;
- performance on these tasks does not guarantee performance on every private repository.

## License

Code and original analysis are released under the MIT License. Third-party benchmark data remains subject to its source terms and attribution requirements.
