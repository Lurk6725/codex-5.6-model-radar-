# 最新分析报告 / Latest Analysis Report

[中文完整分析](latest.zh-CN.md) · [Full English analysis](latest.en.md) · [API 自动监控 / API monitor](api-latest.md) · [历史数据 / History](history/README.md) · [项目首页 / Project home](../README.md)

**分析截止 / Cutoff:** 2026-07-14 07:46 Asia/Shanghai  
**批次 / Batch:** `2026-07-14-am`  
**数据 / Sources:** Codex Radar 授权 API + 公开网页逐题矩阵 / authorized API + public task matrix

> API 返回八个档位，公开网页补齐 Sol Max、九档逐题矩阵和最新历史通过率。  
> The API returned eight tiers; the public page supplied Sol Max, the nine-tier task matrix, and updated historical pass rates.

## 模型推荐 / Model recommendations

| 场景 / Work type | 当前建议 / Recommendation | 说明 / Rationale |
|---|---|---|
| 机械、低风险、允许重试 / Mechanical, low-risk, retryable | **Terra Medium**；Sol Low 作为波动候选 / Sol Low as a volatile candidate | Terra 更便宜；Low 本轮 8/10 但长期波动大 |
| 日常开发与小项目 Bug 审查 / Daily development and small-project bug review | **Sol Medium** | 与 High 同为 9/10 且逐题相同，但更便宜 / same 9/10 task pattern as High at lower cost |
| 高难、额度敏感、可长跑 / Difficult, quota-sensitive, long-running | **先用 Sol Medium；Luna Max 仅专项候选 / Try Medium first; Luna Max specialized only** | Luna Max 6/10，但唯一通过第 07 题 |
| 最高能力兜底 / Maximum-capability fallback | **Sol Max 仅保留历史上限含义 / historical-ceiling only** | 本轮 6/10 且费用最高 |

## 最新权重 / Latest task weights

**快照 / Snapshot:** `2026-07-14-0746`  
`weight_i ∝ 1 / sqrt(historical_pass_rate_i)`，总和 / normalized total = 100.

| 题号 / Task | 历史通过率 / Pass rate | 权重 /100 |
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
|  | **合计 / Total** | **100.00** |

## 最新逐题加权排名 / Latest task-weighted ranking

| 排名 / Rank | 模型 / Tier | 通过 / Passed | 加权分 /100 | 费用 / Cost | 加权分/$ / Weighted/$ |
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

## 核心结论 / Core findings

- **Sol Medium 继续是默认档 / remains the default.** Medium 与 High 逐题结果完全相同，但成本更低。
- **Sol Low 值得观察 / is worth watching**, but one 8/10 run does not erase its weak historical median.
- **Luna Max 是专项而非通用优势 / is specialized, not broadly superior.** It uniquely passed task 07.
- **Sol Max 和 XHigh 再次没有单调收益 / again show no monotonic gain.** Both scored 6/10 at much higher cost.
- **Luna Medium 不再推荐 / is no longer recommended** after a 1/10 result.

## 批次状态 / Batch status

本轮 57/90，总费用约 $204.59，总 Token 约 336.1M。质量较 7 月 13 日异常批次明显恢复，但消耗仍高。它不满足项目异常规则中的 15% 质量下降条件，因此记为**有效批次，附高消耗警告**。  
The batch reached 57/90 with about $204.59 cost and 336.1M tokens. Quality recovered, while consumption remained high. It is recorded as **valid with a high-consumption warning**.

[逐题矩阵 / Task matrix](../data/history/task_matrices.csv) · [汇总历史 / Aggregate history](../data/history/runs.csv)