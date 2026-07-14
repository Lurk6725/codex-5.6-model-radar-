# 最新分析报告 / Latest Analysis Report

[中文完整分析](latest.zh-CN.md) · [Full English analysis](latest.en.md) · [API 自动监控 / API monitor](api-latest.md) · [历史数据 / History](history/README.md) · [项目首页 / Project home](../README.md)

**分析截止 / Cutoff:** 2026-07-14 14:34 Asia/Shanghai  
**批次 / Batch:** `2026-07-14-pm`  
**API 快照 / API snapshot:** `e0ac3269c1279e22`  
**数据 / Sources:** Codex Radar 授权 API + 公开网页逐题矩阵 / authorized API + public task matrix

> 源站将 Sol Medium 汇总为 7/10，但公开逐题列表只显示六个明确通过项，因此本报告展示加权分范围，不猜测缺失题目。  
> The source reports Sol Medium as 7/10, while its public task list contains only six explicit passes. The report therefore shows a weighted-score range instead of guessing the missing task.

## 模型推荐 / Model recommendations

| 场景 / Work type | 当前建议 / Recommendation | 说明 / Rationale |
|---|---|---|
| 机械、低风险、允许重试 / Mechanical, low-risk, retryable | **Sol Low** | 连续两轮 8/10；本轮加权分/$ 8.46 / two consecutive 8/10 runs; weighted/$ 8.46 |
| 日常开发与小项目 Bug 审查 / Daily development and small-project bug review | **Sol Medium** | 与 High、XHigh 同为汇总 7/10，但明显更便宜 / same aggregate 7/10 as High and XHigh at much lower cost |
| 高难任务与最终兜底 / Difficult work and final fallback | **Sol Max** | 加权分最高 83.33，但费用 $49.90 / highest weighted score, but costs $49.90 |

## 最新权重 / Latest task weights

**快照 / Snapshot:** `2026-07-14-1434`

| 题号 / Task | 历史通过率 / Pass rate | 权重 /100 |
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
|  | **合计 / Total** | **100.00** |

## 最新逐题加权排名 / Latest task-weighted ranking

| 排名 / Rank | 模型 / Tier | 通过 / Passed | 加权分 /100 | 费用 / Cost | 加权分/$ / Weighted/$ |
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

\* Sol Medium 的逐题列表与汇总总数不一致；机器可读数据保留该矛盾。 / Sol Medium's task list conflicts with its aggregate pass count; the machine-readable data preserves the discrepancy.

## 核心结论 / Core findings

- **Sol Low 升级为低成本推荐 / becomes the low-cost recommendation.** 连续两轮 8/10，且本轮通过最难第 07 题。 / Two consecutive 8/10 runs, including task 07 this time.
- **Sol Medium 保持日常默认 / remains the daily default.** 同为汇总 7/10 时，它比 High 和 XHigh 明显更便宜。 / At the same aggregate 7/10, it is much cheaper than High and XHigh.
- **Sol Max 恢复最高能力兜底 / restores the maximum-capability fallback.** 本轮加权分第一，但单位成本效率低。 / Highest weighted score, but poor cost efficiency.
- **High/XHigh 没有升级价值 / offer no upgrade value.** 两者逐题结果相同，High 更便宜；Medium 总分相同且更便宜。 / High and XHigh share the same task bitmap; Medium has the same aggregate score at lower cost.
- **Terra High 与 Luna High 是新档位 / are new active tiers.** 不能与上午的 Medium 档直接做同档趋势比较。 / They cannot be directly compared with the morning Medium tiers.

## 批次状态 / Batch status

本轮 58/90，总费用约 $206.40，总 Token 约 363.7M。相较上午，质量 +1.8%、费用 +0.9%、Token +8.2%。记录为**有效批次，附高消耗和来源一致性警告**。  
The batch reached 58/90 at about $206.40 and 363.7M tokens. Versus the morning run, quality rose 1.8%, cost rose 0.9%, and tokens rose 8.2%. It is recorded as **valid with high-consumption and source-consistency warnings**.

[逐题矩阵 / Task matrix](../data/history/task_matrices.csv) · [汇总历史 / Aggregate history](../data/history/runs.csv)
