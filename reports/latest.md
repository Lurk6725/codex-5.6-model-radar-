# 最新分析报告 / Latest Analysis Report

[中文完整分析](latest.zh-CN.md) · [Full English analysis](latest.en.md) · [API 自动监控 / API monitor](api-latest.md) · [历史数据 / History](history/README.md) · [项目首页 / Project home](../README.md)

**分析截止 / Cutoff:** 2026-07-14 09:00 Asia/Shanghai  
**最新 API 快照 / Latest API snapshot:** `56b5641f66b1a557`  
**API 数据日期 / Source date:** `2026-07-14-am`  
**逐题矩阵最后可用时间 / Latest task matrix:** 2026-07-13 14:05

> 本次只有模型级 API 汇总，没有逐题矩阵、每模型 run ID 或完整/部分重跑标记。以下更新实时趋势与推荐，不重新计算难度加权分。  
> This refresh contains aggregate API data only. There is no task matrix, per-model run ID, or full-versus-partial rerun marker, so real-time trends and recommendations are updated without fabricating new task-weighted scores.

## 模型推荐 / Model recommendations

| 场景 / Work type | 当前建议 / Recommendation | 说明 / Rationale |
|---|---|---|
| 机械、低风险、允许重试 / Mechanical, low-risk, retryable | **Terra Medium**；Sol Low 待复测 / Sol Low pending repetition | Luna Medium 最新仅 1/10 / Luna Medium fell to 1/10 |
| 日常开发与小项目 Bug 审查 / Daily development and small-project bug review | **Sol Medium** | 与 High 同为 9/10，但更便宜、更快 / ties High at 9/10 while cheaper and faster |
| 高难、额度敏感、可长跑 / Difficult, quota-sensitive, long-running | **先用 Sol Medium；Luna Max 降为观察候选 / Try Sol Medium first; Luna Max on watchlist** | Luna Max 最新为 6/10 / Luna Max fell to 6/10 |
| 最高能力兜底 / Maximum-capability fallback | **Sol Max（历史结论 / historical evidence）** | 最新 API 未返回 Sol Max / absent from the latest API snapshot |

## 最新 API 汇总 / Latest API aggregate view

`原始分/$ / Raw score/$` 使用源站等权分除以费用，并非逐题难度加权效率。

| 排名 / Rank | 模型 / Tier | 通过 / Passed | 源站分数 / Score | 费用 / Cost | 原始分/$ / Raw score/$ | Token | 耗时 / Time |
|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | Sol High | 9/10 | 135 | $24.62 | 5.48 | 23.50M | 0.54h |
| 1 | **Sol Medium** | 9/10 | 135 | **$18.41** | **7.33** | **18.48M** | **0.46h** |
| 3 | Sol Low | 8/10 | 120 | $9.73 | 12.33 | 8.20M | 0.27h |
| 4 | Terra Max | 7/10 | 105 | $30.91 | 3.40 | 65.72M | 0.63h |
| 5 | Luna Max | 6/10 | 90 | $15.11 | 5.96 | 88.73M | 0.66h |
| 5 | Sol XHigh | 6/10 | 90 | $37.97 | 2.37 | 40.67M | 0.75h |
| 7 | Terra Medium | 5/10 | 75 | $5.18 | **14.48** | 8.01M | 0.39h |
| 8 | Luna Medium | 1/10 | 15 | $2.44 | 6.15 | 10.81M | 0.41h |

## 变化摘要 / Change summary

- 八个返回档位总通过数由 44 升至 51（约 +15.9%）；总费用基本持平，Token 下降约 11%，总耗时下降约 28%。  
  Across the eight returned tiers, passes rose from 44 to 51 (+15.9%); aggregate cost was nearly flat, tokens fell about 11%, and wall time fell about 28%.
- Sol Medium 从 5/10 回升至 9/10；Sol High 同为 9/10，但成本与资源消耗更高。  
  Sol Medium recovered from 5/10 to 9/10; Sol High also reached 9/10 but at higher cost and resource use.
- Sol Low 从 6/10 升至 8/10，但没有逐题结构，暂不根据单轮改为默认。  
  Sol Low rose from 6/10 to 8/10, but the task mix is unknown and one aggregate snapshot is insufficient for default status.
- Luna Max 降至 6/10，Luna Medium 降至 1/10；Sol XHigh 降至 6/10且费用上升。  
  Luna Max fell to 6/10, Luna Medium to 1/10, and Sol XHigh fell to 6/10 while becoming more expensive.

## 数据限制 / Data limitations

- 最新 API 只返回八个档位，没有 Sol Max。  
  The latest API returns eight tiers and omits Sol Max.
- 没有逐题矩阵，所以无法更新 `加权分 /100` 与 `加权分/$`。  
  Without task outcomes, `Weighted /100` and task-weighted `Weighted/$` cannot be updated.
- 没有 per-model run ID 或部分重跑标记，只能确认汇总值变化。  
  There are no per-model run IDs or partial-rerun markers; only aggregate value changes can be confirmed.
- `source_date` 已变为 `2026-07-14-am`，但 API `observed_at` 仍保留旧时间，存在时间元数据不一致。  
  `source_date` is `2026-07-14-am`, while API `observed_at` remains stale, creating a timestamp inconsistency.

## 最近可计算的逐题加权结果 / Latest computable task-weighted result

逐题权重和加权榜仍以 `2026-07-13-1405` 矩阵为准。最新 API 汇总不会被冒充为新加权榜。  
Task weights and the weighted ranking remain based on the `2026-07-13-1405` matrix. The aggregate API refresh is not mislabeled as a new weighted ranking.

[查看中文详细分析](latest.zh-CN.md) · [Read the full English analysis](latest.en.md) · [查看 API 历史 CSV / API history CSV](../data/api/model_iq_history.csv)
