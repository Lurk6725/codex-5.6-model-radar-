# GPT‑5.6 Codex Model Radar

[简体中文](#简体中文) · [English](#english) · [最新双语报告](reports/latest.md) · [中文项目说明](docs/PROJECT_OVERVIEW_ZH_CN.md) · [English overview](docs/PROJECT_OVERVIEW_EN.md)

> **数据来源 / Data attribution:** 基准测试原始数据来自 **Codex Radar**（`codexradar.com`，原 `codex-reset-radar.pages.dev`）。本仓库是独立的二次分析项目，与 OpenAI、Codex Radar 或 DeepSWE 均无官方隶属关系。  
> Source benchmark data comes from **Codex Radar** (`codexradar.com`, formerly `codex-reset-radar.pages.dev`). This is an independent secondary-analysis project and is not affiliated with OpenAI, Codex Radar, or DeepSWE.

---

# 简体中文

## 项目简介

这是一个由社区维护、可复现的 GPT‑5.6 Codex 模型长期监控项目，关注 **Luna、Terra、Sol** 各模型家族及不同推理强度的实际工程任务表现。

项目在 Codex Radar 公开测试结果的基础上增加：

- 任务难度加权；
- 多轮稳定性和波动分析；
- 异常批次识别与降权；
- 订阅额度性价分析；
- 成本—能力 Pareto 前沿；
- 面向不同工作类型的模型推荐。

本项目只分析公开展示的信息，不使用私有 API，不绕过认证，也不访问受保护端点。未来如需完整历史同步、私有 API 或受保护数据集再分发，将先与 Codex Radar 维护者沟通。

完整中文说明见 [`docs/PROJECT_OVERVIEW_ZH_CN.md`](docs/PROJECT_OVERVIEW_ZH_CN.md)。

## 跟踪范围

- 模型家族：**Luna、Terra、Sol**；
- 推理强度：可用时记录 **low、medium、high、xhigh、max**；
- Codex Radar / DeepSWE 固定仓库级工程任务；
- 原始通过数、逐题结果、Token、执行时间和估算费用；
- 难度加权能力分；
- 单位额度效率；
- 最近三轮、五轮中位数与指数趋势；
- 异常批次、波动率和推荐变化。

## 当前工作结论

这些结论是阶段性的，必须和历史数据及异常标记一起阅读：

| 使用场景 | 当前默认建议 |
|---|---|
| 机械、低风险、允许重试 | Luna Medium 或 Terra Medium，先看近期稳定性 |
| 日常 Codex 开发 | **Sol Medium** |
| 高难、额度敏感、允许长时间运行 | **Luna Max** |
| 最高能力兜底 | 较低档失败后再使用 **Sol Max** |

High、XHigh、Max 并不在每个批次中呈现单调提升。单次十题结果噪声较大，推荐主要依据滚动统计，而不是只看最新一轮。

## 评分方法

来源网站的等权分给每道题相同分值。本项目额外使用“软逆通过率”权重：

```text
原始难度_i = 1 / sqrt(历史通过率_i)
题目权重_i = 100 × 原始难度_i / sum(原始难度)
难度加权分 = sum(题目权重_i × 是否通过_i)
```

主要指标：

1. **难度加权分（0–100）**：修正题目难度后的能力分；
2. **加权 IQ（0–150）**：难度加权分乘以 1.5，便于与来源网站展示尺度对照；
3. **额度效率**：难度加权分除以网站估算美元等价费用；
4. **滚动稳定性**：最近有效批次的中位数、均值与波动范围；
5. **异常修正趋势**：异常批次保留展示，但在长期趋势中降权。

完整公式见 [`docs/METHODOLOGY.md`](docs/METHODOLOGY.md)。

## 订阅额度口径

社区转述的 OpenAI 员工澄清指出，超过 272K 输入后的 API 长上下文阶梯价格不适用于 ChatGPT/Codex 订阅额度分析。因此本项目：

- 不给订阅分析额外叠加 API 的 2× 输入和 1.5× 输出倍率；
- 将 Codex Radar 的美元等价费用视为**相对额度代理**，而不是精确订阅账单；
- 将总 Token 和执行时间单独作为 Agent 膨胀与延迟指标。

详见 [`docs/COSTS.md`](docs/COSTS.md)。

## 双语发布规范

每次新增测试数据并完成分析后，仓库必须同时更新中文和英文内容：

- `reports/latest.zh-CN.md`：中文完整分析；
- `reports/latest.en.md`：英文完整分析；
- `reports/latest.md`：中英文合并入口；
- 自动生成的汇总表也同时输出中文、英文和双语版本。

方法、推荐或数据口径发生变化时，中英文文档应在同一次提交中同步更新。详见 [`docs/BILINGUAL_POLICY.md`](docs/BILINGUAL_POLICY.md)。

## 数据政策

当前维护可使用：

1. 人工核对的公开网页快照；
2. 来源网站公开提供的摘要数据；
3. 本仓库自行计算的衍生指标。

项目不使用私有凭证、不规避访问控制，也不冒充 Codex Radar 官方镜像。每个批次应保留原始时间、来源 URL、数据来源说明，以及因四舍五入、部分重跑或缺失逐题矩阵产生的不确定性。

## 局限

- 当前固定测试集只有十道题，单题会让原始通过率变化 10 个百分点；
- 每个模型/任务通常每批只运行一次，Agent 轨迹具有随机性；
- 历史通过率可能包含任务家族偏好；
- 估算费用是相对额度代理，不是官方账户扣费；
- 某模型在这十题上最优，不代表它在 UI、写作、代码审查或私人仓库上同样最优。

---

# English

## Project overview

This is a community-maintained, reproducible long-term monitor for GPT‑5.6 Codex models, covering the **Luna, Terra, and Sol** families and their available reasoning-effort tiers.

On top of publicly visible Codex Radar results, the repository adds:

- task-difficulty weighting;
- multi-run stability and volatility analysis;
- anomalous-batch detection and down-weighting;
- subscription-oriented quota-efficiency analysis;
- cost-quality Pareto frontiers; and
- practical model recommendations by workload type.

The project analyzes only publicly visible information. It does not use a private API, bypass authentication, or access protected endpoints. Before adding full-history synchronization, private API access, or redistribution of a protected dataset, the maintainer will coordinate with Codex Radar.

A longer English overview is available in [`docs/PROJECT_OVERVIEW_EN.md`](docs/PROJECT_OVERVIEW_EN.md).

## What this repository tracks

- Model families: **Luna, Terra, Sol**;
- Reasoning efforts: **low, medium, high, xhigh, max** when available;
- Fixed repository-level engineering tasks derived from the Codex Radar / DeepSWE test set;
- Raw pass count, task-level outcomes, tokens, wall time, and estimated cost;
- Difficulty-weighted capability scores;
- Quality per estimated quota cost;
- Three-run and five-run rolling statistics;
- Volatility, anomalous batches, and recommendation changes.

## Current working conclusions

These conclusions are provisional and must be read together with historical data and anomaly flags:

| Use case | Current default |
|---|---|
| Mechanical, low-risk, retryable work | Luna Medium or Terra Medium, depending on recent stability |
| General daily Codex work | **Sol Medium** |
| Difficult, quota-sensitive, long-running work | **Luna Max** |
| Maximum-capability fallback | **Sol Max**, only after cheaper tiers fail |

High, XHigh, and Max do **not** show monotonic gains in every batch. Single ten-task runs are noisy, so recommendations rely on rolling evidence rather than the latest score alone.

## Scoring overview

The source site's equal-weight score gives every task the same value. This project additionally calculates a soft inverse-pass-rate weight:

```text
raw_difficulty_i = 1 / sqrt(historical_pass_rate_i)
weight_i = 100 * raw_difficulty_i / sum(raw_difficulty)
weighted_score = sum(weight_i * passed_i)
```

Primary metrics:

1. **Weighted score (0–100)** — difficulty-adjusted capability;
2. **Weighted IQ (0–150)** — weighted score multiplied by 1.5 for comparison with the source display scale;
3. **Quota efficiency** — weighted score divided by the source site's estimated USD-equivalent cost;
4. **Rolling stability** — recent medians, means, and ranges from valid batches;
5. **Anomaly-adjusted trend** — suspicious batches remain visible but receive less trend weight.

See [`docs/METHODOLOGY.md`](docs/METHODOLOGY.md) for full formulas.

## Subscription-cost interpretation

Community-reported clarification from an OpenAI employee indicates that the API-only long-context price step above 272K input tokens does not apply to ChatGPT/Codex subscription quota analysis. Therefore this project:

- does not add the API 2× input / 1.5× output multiplier to subscription analysis;
- treats Codex Radar's estimated USD-equivalent cost as a **relative quota proxy**, not an exact subscriber bill; and
- keeps total tokens and wall time as separate expansion and latency indicators.

See [`docs/COSTS.md`](docs/COSTS.md).

## Bilingual publication policy

Every new benchmark analysis must be published in both Simplified Chinese and English:

- `reports/latest.zh-CN.md` — complete Chinese analysis;
- `reports/latest.en.md` — complete English analysis;
- `reports/latest.md` — combined bilingual entry point;
- generated summary tables are emitted in Chinese, English, and combined formats.

Methodology, recommendation, and data-policy changes should update both languages in the same commit. See [`docs/BILINGUAL_POLICY.md`](docs/BILINGUAL_POLICY.md).

## Repository layout

```text
.
├── data/
│   ├── history/runs.csv
│   ├── schema/task_results.example.csv
│   └── weights/task_weights.csv
├── docs/
│   ├── PROJECT_OVERVIEW_EN.md
│   ├── PROJECT_OVERVIEW_ZH_CN.md
│   ├── BILINGUAL_POLICY.md
│   ├── DATA_SOURCES.md
│   ├── METHODOLOGY.md
│   ├── COSTS.md
│   ├── ANOMALIES.md
│   └── RECOMMENDATIONS.md
├── radar/
├── scripts/build_report.py
├── reports/
│   ├── latest.md
│   ├── latest.en.md
│   └── latest.zh-CN.md
└── tests/
```

## Reproduce the analysis

```bash
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -e .
pytest
python scripts/build_report.py
```

## Data policy

Current maintenance may use manually verified public-page snapshots, public summary data exposed by the source, and original calculations from this repository. The project does not use private credentials, evade access controls, or present itself as an official mirror.

Each imported batch should retain its original timestamp, source URL, provenance note, and uncertainty caused by rounding, partial reruns, or missing task-level matrices.

## Limitations

- The active test set contains only ten tasks, so one task changes raw pass rate by ten percentage points;
- Each model/task is generally observed once per batch, and agent trajectories are stochastic;
- Historical pass-rate weights may encode task-family bias;
- Estimated cost is a relative quota proxy, not an official account-level debit;
- The best model on this task set may not be the best model for UI design, writing, review, or a private repository.

## License

Code and original analysis are released under the MIT License. Third-party benchmark data remains subject to its source terms and attribution requirements.