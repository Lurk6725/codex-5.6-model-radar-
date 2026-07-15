# 历史测试数据 / Historical Benchmark Data

[返回项目首页 / Back to project home](../../README.md) · [最新分析 / Latest analysis](../latest.md) · [逐题矩阵 / Task matrices](../../data/history/task_matrices.csv)

本页提供所有已收录批次的快速跳转。早期批次缺少费用或逐题矩阵时保留空值，不使用后续权重倒推覆盖原始记录。

This page provides direct navigation to every recorded batch. Missing early cost or task-level fields remain blank rather than being reconstructed with later weights.

## 批次索引 / Batch index

| 批次 / Batch | 状态 / Status | 模型数 | 数据入口 / Data |
|---|---|---:|---|
| 2026-07-10-am | 正常 / valid | 4 | [基础历史 CSV](../../data/history/runs.csv) |
| 2026-07-10-pm_2 | 正常，部分档位 / valid, partial | 2 | [基础历史 CSV](../../data/history/runs.csv) |
| 2026-07-10-n | 正常 / valid | 4 | [基础历史 CSV](../../data/history/runs.csv) |
| 2026-07-11-pm | 正常 / valid | 8 | [基础历史 CSV](../../data/history/runs.csv) |
| 2026-07-12-am | 正常 / valid | 9 | [基础历史 CSV](../../data/history/runs.csv) |
| 2026-07-12-pm | 正常 / valid | 9 | [基础历史 CSV](../../data/history/runs.csv) |
| 2026-07-13-am | 正常 / valid | 9 | [基础历史 CSV](../../data/history/runs.csv) |
| 2026-07-13-pm-anomaly | **异常 / anomalous** | 9 | [基础历史 CSV](../../data/history/runs.csv) |
| 2026-07-14-am | 有效，高消耗警告 / valid, high-consumption warning | 9 | [逐题矩阵](../../data/history/task_matrices.csv) |
| 2026-07-14-pm | 有效，来源一致性警告 / valid, source-consistency warning | 9 | [详细页面](2026-07-14-pm.md) |
| 2026-07-15-am | 有效 / valid | 9 | [详细页面](2026-07-15-am.md) · [模型汇总 CSV](../../data/history/batches/2026-07-15-am.csv) |
| 2026-07-15-pm | **有效 / valid** | 9 | [详细页面](2026-07-15-pm.md) · [模型汇总 CSV](../../data/history/batches/2026-07-15-pm.csv) |

## 最近批次摘要 / Recent batch summary

### 2026-07-15-pm

| 排名 | 模型 | 通过 | 加权分 /100 | 费用 | 加权分/$ |
|---:|---|---:|---:|---:|---:|
| 1 | Luna Max | 9/10 | 90.08 | $16.30 | 5.53 |
| 2 | Sol Low | 8/10 | 71.69 | $10.70 | 6.70 |
| 3 | Sol High | 7/10 | 64.44 | $25.00 | 2.58 |
| 4 | Terra Max | 7/10 | 62.78 | $34.00 | 1.85 |
| 5 | Sol XHigh | 7/10 | 62.50 | $32.60 | 1.92 |
| 6 | Sol Medium | 6/10 | 54.82 | $16.60 | 3.30 |
| 7 | Sol Max | 6/10 | 54.61 | $51.40 | 1.06 |
| 8 | Terra High | 5/10 | 44.85 | $9.30 | 4.82 |
| 9 | Luna High | 5/10 | 41.40 | $6.70 | 6.18 |

[查看完整快照 / View full snapshot](2026-07-15-pm.md)

## 数据文件 / Data files

- [`data/history/runs.csv`](../../data/history/runs.csv)：早期和基础模型级历史；
- [`data/history/batches/`](../../data/history/batches/)：新增批次的独立模型级快照；
- [`data/history/task_matrices.csv`](../../data/history/task_matrices.csv)：逐题通过位图；
- [`data/weights/task_weights.csv`](../../data/weights/task_weights.csv)：当前任务权重快照。

新批次使用独立文件，报告生成器会把基础历史与 `batches/*.csv` 合并并按 `batch_id + model + effort` 去重。
