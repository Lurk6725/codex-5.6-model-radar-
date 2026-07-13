# 最新分析报告 / Latest Analysis Report

[简体中文完整页](latest.zh-CN.md) · [Full English page](latest.en.md) · [历史数据 / History](history/README.md) · [项目首页 / Project home](../README.md)

**分析截止 / Cutoff:** 2026-07-13 14:05 Asia/Shanghai  
**数据来源 / Source:** Codex Radar  
**最新批次 / Latest batch:** `2026-07-13-pm-anomaly` — 异常批次 / anomalous, trend reliability `0.35`

---

## 模型推荐 / Model recommendations

| 场景 / Work type | 推荐 / Recommendation | 说明 / Rationale |
|---|---|---|
| 机械、低风险、允许重试 / Mechanical, low-risk, retryable | Luna Medium 或 / or Terra Medium | 先看近期稳定性 / check recent stability |
| 日常开发 / General daily development | **Sol Medium** | 正常批次中最均衡 / best balance across normal runs |
| 高难、额度敏感、可长跑 / Difficult, quota-sensitive, long-running | **Luna Max** | 多轮较强，但慢且 Token 高 / strong multi-run results, but slow and token-heavy |
| 最高能力兜底 / Maximum-capability fallback | **Sol Max** | 上限最高，但费用和波动也最大 / highest ceiling, but highest cost and volatility |

14:05 批次整体质量下降、费用和 Token 同时上升，因此不会以完整权重改变长期推荐。  
The 14:05 batch combines lower aggregate quality with higher cost and token activity, so it does not receive full weight when changing the long-term recommendation.

## 最新任务难度权重 / Latest task-difficulty weights

**权重快照 / Weight snapshot:** `2026-07-13-1405`  
**公式 / Formula:** `weight_i ∝ 1 / sqrt(historical_pass_rate_i)`, normalized to 100.

| 题号 / Task | 任务摘要 / Short description | 历史通过率 / Pass rate | 权重 /100 |
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
|  | **合计 / Total** |  | **100.00** |

[权重 CSV / Weight CSV](../data/weights/task_weights.csv)

## 最新观测排名 / Latest observed weighted ranking

> 最新观测值属于异常批次，不应直接视为长期模型层级。  
> The latest observation is anomalous and should not be treated as the long-term model hierarchy.

| 排名 / Rank | 模型 / Tier | 通过 / Passed | 加权分 /100 | 费用 / Cost | 加权分/$ / Weighted/$ |
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

## 最近正常完整批次 / Latest complete non-anomalous ranking

**批次 / Batch:** `2026-07-13-am`（约 / about 09:16）

| 排名 / Rank | 模型 / Tier | 通过 / Passed | 加权分 /100 | 费用 / Cost | 加权分/$ / Weighted/$ |
|---:|---|---:|---:|---:|---:|
| 1 | Sol Max | 10/10 | **100.00** | $34.94 | 2.86 |
| 2 | Sol Medium | 9/10 | **82.81** | $8.23 | **10.06** |
| 3 | Luna Max | 8/10 | 74.35 | $14.35 | 5.18 |
| 4 | Sol High | 7/10 | 72.79 | $15.01 | 4.85 |
| 5 | Sol XHigh | 7/10 | 66.75 | $26.39 | 2.53 |
| 6 | Terra Max | 7/10 | 62.38 | $30.19 | 2.07 |
| 7 | Sol Low | 5/10 | 46.28 | $5.96 | 7.77 |
| 8 | Terra Medium | 4/10 | 33.71 | $6.17 | 5.46 |
| 8 | Luna Medium | 4/10 | 33.71 | $2.42 | **13.95** |

“加权分/$”天然偏爱便宜模型，不能脱离绝对加权分和多轮稳定性单独使用。  
Weighted score per dollar naturally favors cheap models and must be read together with absolute quality and rolling stability.

## 异常批次判断 / Anomaly assessment

与上午正常批次相比，14:05 批次的总通过数下降约五分之一，而总估算费用和 Token 活动量均上升超过 40%。多个互不相关档位同时出现“更贵但更差”的结果，因此保留原始数据，但长期趋势仅计 `0.35` 权重。

Relative to the valid morning batch, aggregate passes fell by roughly one fifth while total estimated cost and token activity each rose by more than 40%. Several unrelated tiers became both more expensive and less successful, so the raw data is retained but receives only `0.35` trend weight.

## 稳定结论 / Stable interpretation

- **Sol Medium** 仍是日常默认 / remains the daily default.
- **Luna Max** 仍是高难、额度敏感的长时间后台路线 / remains the quota-sensitive difficult-work route for long background runs.
- **Sol Max** 是最高上限兜底，而不是常驻默认 / is a maximum-ceiling fallback, not a standing default.
- High、XHigh、Max 并不稳定地单调提升 / High, XHigh, and Max do not reliably improve monotonically.

## 历史数据 / Historical data

[查看全部批次及跳转索引 / Browse every recorded batch](history/README.md)  
[原始汇总 CSV / Raw aggregate CSV](../data/history/runs.csv)
