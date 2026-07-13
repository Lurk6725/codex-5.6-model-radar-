# 最新分析报告 / Latest Analysis Report

[简体中文](#简体中文) · [English](#english) · [中文单独页面](latest.zh-CN.md) · [English-only page](latest.en.md)

---

<a id="简体中文"></a>

# 简体中文

**分析截止时间：** 2026-07-13 14:05 Asia/Shanghai  
**主要数据来源：** Codex Radar  
**批次状态：** 异常批次；保留原始结果，长期趋势可靠度权重为 `0.35`

> 数据来源：Codex Radar（`codexradar.com`）。

## 摘要

14:05 批次不应被删除，但也不应和正常批次拥有相同的长期趋势权重。与当天上午批次相比，多数模型的整体质量下降，而估算费用和 Token 活动量在多个档位上同时显著上升。这种表现更像批次级、Harness 级或服务状态异常，而不是一次干净的模型能力排序测试。

因此长期推荐暂时不变：

| 工作类型 | 推荐 |
|---|---|
| 机械、允许重试 | Luna Medium 或 Terra Medium，但应先检查近期稳定性 |
| 日常开发 | **Sol Medium** |
| 高难、额度敏感 | **Luna Max** |
| 最高能力兜底 | 较低档失败后再使用 **Sol Max** |

## 14:05 异常批次

| 模型档位 | 通过 | 难度加权分 | 估算费用 | 每美元得分 |
|---|---:|---:|---:|---:|
| Luna Max | 7/10 | 70.31 | $18.90 | 3.72 |
| Sol XHigh | 7/10 | 66.56 | $33.60 | 1.98 |
| Sol High | 6/10 | 59.47 | $26.80 | 2.22 |
| Terra Max | 6/10 | 56.60 | $32.20 | 1.76 |
| Sol Low | 6/10 | 53.21 | $9.40 | 5.66 |
| Terra Medium | 5/10 | 50.38 | $6.00 | 8.40 |
| Sol Max | 5/10 | 48.32 | $59.80 | 0.81 |
| Sol Medium | 5/10 | 45.50 | $16.10 | 2.83 |
| Luna Medium | 2/10 | 18.24 | $2.40 | 7.60 |

这些结果以 `2026-07-13-pm-anomaly` 批次 ID 保存在 `data/history/runs.csv` 中，数值来自公开页面的四舍五入快照。

## 为什么对该批次降权

与分析时记录的上午批次相比：

- 全体通过数下降约五分之一；
- 总估算费用上升超过 40%；
- 总 Token 活动量上升超过 40%；
- 多个互不相关的模型档位同时出现成功率下降、费用增加。

按照仓库默认规则，当总体质量下降至少 15%，并且费用或 Token 增加至少 30% 时，会触发异常批次标记。

## 稳定性解读

### Sol Medium 仍然是日常默认

在当前公开历史中，Sol Medium 拥有最有用、样本相对最多的连续记录。其近期中心大约为十题通过七题，虽然也会出现更强或更弱的单轮结果，但正常批次的费用明显低于 High、XHigh 和 Max。

### Luna Max 仍然是高难、额度敏感任务的候选

Luna Max 在多轮测试中取得了较高通过数，估算费用相对较低，但总 Token 和执行时间很高。它更适合后台长时间执行，而不一定适合频繁交互式调试。

### Sol Max 仍然是兜底，而不是默认

Sol Max 展示过最高单轮上限，包括公开摘要中的 10/10；但它也在这次异常批次中出现了低成功率和极高费用。Max 不等于稳定成功保证。

### 推理强度并非单调提升

High、XHigh、Max 多次没有形成清晰的阶梯式提升。只有当前档位已经失败，或私人项目中的可复现实验证明确显示收益时，才应升级推理强度。

## 结论置信度

| 结论 | 置信度 |
|---|---|
| Sol Medium 是最合适的通用默认档 | 中等偏高 |
| Luna Max 是高难、额度敏感任务的有力候选 | 中等 |
| Sol Max 拥有最高上限 | 中等 |
| 14:05 能代表正常模型能力 | 低 |
| 应根据单一最新批次改变默认模型阶梯 | 极低 |

## 下一步最需要的数据

- 每个批次的完整逐题矩阵；
- 部分重跑和完整重跑的精确时间；
- 来源侧 Harness 或配置变化说明；
- Max 档位更多独立重复测试；
- 与 API 账单分离的订阅额度直接校准。

---

<a id="english"></a>

# English

**Analysis cutoff:** 2026-07-13 14:05 Asia/Shanghai  
**Primary source:** Codex Radar  
**Batch status:** anomalous; retained with reliability weight `0.35`

> Source benchmark data comes from Codex Radar (`codexradar.com`).

## Executive summary

The 14:05 batch should not be ignored, but it should not receive the same trend weight as a normal batch. Relative to the preceding morning batch, aggregate quality fell while estimated cost and token activity rose sharply across several model tiers. This is more consistent with a batch-level or harness-level disturbance than with a clean measurement of model hierarchy.

The long-term recommendation is therefore unchanged:

| Work type | Recommendation |
|---|---|
| Mechanical and retryable | Luna Medium or Terra Medium, with recent stability checked first |
| Daily development | **Sol Medium** |
| Difficult and quota-sensitive | **Luna Max** |
| Maximum-capability fallback | **Sol Max** after cheaper tiers fail |

## 14:05 anomalous batch

| Model tier | Passed | Difficulty-weighted score | Estimated cost | Score / $ |
|---|---:|---:|---:|---:|
| Luna Max | 7/10 | 70.31 | $18.90 | 3.72 |
| Sol XHigh | 7/10 | 66.56 | $33.60 | 1.98 |
| Sol High | 6/10 | 59.47 | $26.80 | 2.22 |
| Terra Max | 6/10 | 56.60 | $32.20 | 1.76 |
| Sol Low | 6/10 | 53.21 | $9.40 | 5.66 |
| Terra Medium | 5/10 | 50.38 | $6.00 | 8.40 |
| Sol Max | 5/10 | 48.32 | $59.80 | 0.81 |
| Sol Medium | 5/10 | 45.50 | $16.10 | 2.83 |
| Luna Medium | 2/10 | 18.24 | $2.40 | 7.60 |

These results are preserved in `data/history/runs.csv` as `2026-07-13-pm-anomaly` with rounded snapshot values.

## Why the batch is down-weighted

Compared with the preceding morning batch recorded during analysis:

- aggregate passes fell by roughly one fifth;
- aggregate estimated cost rose by more than 40%;
- aggregate token activity rose by more than 40%;
- several unrelated tiers simultaneously became less successful and more expensive.

Under the repository's default rule, a quality drop of at least 15% combined with a cost or token increase of at least 30% triggers an anomaly flag.

## Stable interpretation

### Sol Medium remains the daily default

The public history contains the largest useful sample for Sol Medium and shows a recent sequence centered around seven passes out of ten, with occasional stronger and weaker runs. Its normal-batch cost is substantially below High, XHigh, and Max.

### Luna Max remains the quota-sensitive difficult-work candidate

Luna Max has produced strong multi-run pass counts at relatively low estimated cost, though with high total tokens and long wall time. It is attractive for background execution, not necessarily interactive debugging.

### Sol Max remains a fallback, not a default

Sol Max has demonstrated the highest single-batch ceiling, including a 10/10 public-summary run, but it also produced a weak and very expensive result in the anomalous batch. Maximum effort is not a reliability guarantee.

### Reasoning effort is not monotonic

High, XHigh, and Max have repeatedly failed to improve in a clean staircase. Recommendations should move upward only after the current tier fails or project-specific evidence shows a real advantage.

## Confidence

| Conclusion | Confidence |
|---|---|
| Sol Medium is the best general default | Moderate to high |
| Luna Max is a strong quota-sensitive difficult tier | Moderate |
| Sol Max has the highest ceiling | Moderate |
| 14:05 represents normal model capability | Low |
| One latest batch should change the default ladder | Very low |

## Next data needed

- complete task-level matrices for every batch;
- exact timestamps for partial versus full reruns;
- source-side harness/configuration change notes;
- additional independent repetitions of Max tiers;
- direct subscriber-quota calibration separated from API billing.
