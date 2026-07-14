# 历史测试数据 / Historical Benchmark Data

[返回项目首页 / Back to project home](../../README.md) · [最新分析 / Latest analysis](../latest.md) · [原始 CSV / Raw CSV](../../data/history/runs.csv) · [逐题矩阵 / Task matrices](../../data/history/task_matrices.csv)

本页按批次保存项目目前收录的公开历史数据。空白费用或加权分表示当时公开摘要缺少足够字段，项目不会使用后续权重倒推并覆盖原始记录。

This page preserves every recorded public batch. Blank cost or weighted-score fields mean that the source summary did not retain enough information; later weights are not used to overwrite historical observations.

## 批次索引 / Batch index

| 批次 / Batch | 状态 / Status | 模型数 | 跳转 / Jump |
|---|---|---:|---|
| 2026-07-10-am | 正常 / valid | 4 | [查看 / View](#2026-07-10-am) |
| 2026-07-10-pm_2 | 正常，部分档位 / valid, partial | 2 | [查看 / View](#2026-07-10-pm_2) |
| 2026-07-10-n | 正常 / valid | 4 | [查看 / View](#2026-07-10-n) |
| 2026-07-11-pm | 正常 / valid | 8 | [查看 / View](#2026-07-11-pm) |
| 2026-07-12-am | 正常 / valid | 9 | [查看 / View](#2026-07-12-am) |
| 2026-07-12-pm | 正常 / valid | 9 | [查看 / View](#2026-07-12-pm) |
| 2026-07-13-am | 正常 / valid | 9 | [查看 / View](#2026-07-13-am) |
| 2026-07-13-pm-anomaly | **异常 / anomalous** | 9 | [查看 / View](#2026-07-13-pm-anomaly) |
| 2026-07-14-am | **有效，高消耗警告 / valid, high-consumption warning** | 9 | [查看 / View](#2026-07-14-am) |
| 2026-07-14-pm | **有效，高消耗与来源一致性警告 / valid, high-consumption and source-consistency warnings** | 9 | [查看 / View](2026-07-14-pm.md) |

---

<a id="2026-07-10-am"></a>
## 2026-07-10-am

| 模型 / Model | 通过 | 原始 IQ | 总 Token | 耗时 | 加权分 | 费用 |
|---|---:|---:|---:|---:|---:|---:|
| Sol Medium | 8/10 | 120 | 15.01M | 11.9m | — | — |
| Sol Low | 7/10 | 105 | 9.73M | 12.2m | — | — |
| Terra Medium | 5/10 | 75 | 11.40M | 12.4m | — | — |
| Luna Medium | 2/10 | 30 | 13.37M | 11.1m | — | — |

[返回索引 / Back](#批次索引--batch-index)

<a id="2026-07-10-pm_2"></a>
## 2026-07-10-pm_2

> 部分档位更新 / Partial-tier update.

| 模型 / Model | 通过 | 原始 IQ | 总 Token | 耗时 |
|---|---:|---:|---:|---:|
| Sol XHigh | 7/10 | 105 | 43.52M | 23.1m |
| Sol High | 7/10 | 105 | 24.04M | 14.9m |

[返回索引 / Back](#批次索引--batch-index)

<a id="2026-07-10-n"></a>
## 2026-07-10-n

| 模型 / Model | 通过 | 原始 IQ | 总 Token | 耗时 |
|---|---:|---:|---:|---:|
| Sol Max | 9/10 | 135 | 70.34M | 134.6m |
| Sol Medium | 7/10 | 105 | 13.50M | 37.7m |
| Terra Medium | 5/10 | 75 | 10.04M | 33.9m |
| Luna Medium | 3/10 | 45 | 13.97M | 33.9m |

[返回索引 / Back](#批次索引--batch-index)

<a id="2026-07-11-pm"></a>
## 2026-07-11-pm

| 模型 / Model | 通过 | 原始 IQ | 总 Token |
|---|---:|---:|---:|
| Sol Max | 9/10 | 135 | 88.10M |
| Sol XHigh | 8/10 | 120 | 22.70M |
| Sol High | 6/10 | 90 | 13.07M |
| Sol Medium | 7/10 | 105 | 7.98M |
| Sol Low | 3/10 | 45 | 3.18M |
| Terra Medium | 6/10 | 90 | 8.11M |
| Luna Max | 9/10 | 135 | 111.41M |
| Luna Medium | 3/10 | 45 | 10.82M |

[返回索引 / Back](#批次索引--batch-index)

<a id="2026-07-12-am"></a>
## 2026-07-12-am

| 模型 / Model | 通过 | 原始 IQ | 总 Token |
|---|---:|---:|---:|
| Sol Max | 7/10 | 105 | 70.57M |
| Sol XHigh | 8/10 | 120 | 25.77M |
| Sol High | 6/10 | 90 | 15.15M |
| Sol Medium | 6/10 | 90 | 7.46M |
| Sol Low | 4/10 | 60 | 4.61M |
| Terra Max | 8/10 | 120 | 79.66M |
| Terra Medium | 4/10 | 60 | 8.94M |
| Luna Max | 9/10 | 135 | 90.19M |
| Luna Medium | 5/10 | 75 | 9.07M |

[返回索引 / Back](#批次索引--batch-index)

<a id="2026-07-12-pm"></a>
## 2026-07-12-pm

| 模型 / Model | 通过 | 原始 IQ | 总 Token |
|---|---:|---:|---:|
| Sol Max | 7/10 | 105 | 55.75M |
| Sol XHigh | 7/10 | 105 | 25.17M |
| Sol High | 7/10 | 105 | 17.91M |
| Sol Medium | 7/10 | 105 | 8.54M |
| Sol Low | 3/10 | 45 | 2.95M |
| Terra Max | 9/10 | 135 | 74.38M |
| Terra Medium | 6/10 | 90 | 8.86M |
| Luna Max | 7/10 | 105 | 103.96M |
| Luna Medium | 2/10 | 30 | 12.79M |

[返回索引 / Back](#批次索引--batch-index)

<a id="2026-07-13-am"></a>
## 2026-07-13-am

| 排名 | 模型 / Model | 通过 | 加权分 /100 | 费用 | 加权分/$ |
|---:|---|---:|---:|---:|---:|
| 1 | Sol Max | 10/10 | 100.00 | $34.94 | 2.86 |
| 2 | Sol Medium | 9/10 | 82.81 | $8.23 | 10.06 |
| 3 | Luna Max | 8/10 | 74.35 | $14.35 | 5.18 |
| 4 | Sol High | 7/10 | 72.79 | $15.01 | 4.85 |
| 5 | Sol XHigh | 7/10 | 66.75 | $26.39 | 2.53 |
| 6 | Terra Max | 7/10 | 62.38 | $30.19 | 2.07 |
| 7 | Sol Low | 5/10 | 46.28 | $5.96 | 7.77 |
| 8 | Terra Medium | 4/10 | 33.71 | $6.17 | 5.46 |
| 8 | Luna Medium | 4/10 | 33.71 | $2.42 | 13.95 |

[返回索引 / Back](#批次索引--batch-index)

<a id="2026-07-13-pm-anomaly"></a>
## 2026-07-13-pm-anomaly

> **异常批次 / Anomalous batch.** 长期趋势可靠度权重 `0.35`。

| 排名 | 模型 / Model | 通过 | 加权分 /100 | 费用 | 加权分/$ |
|---:|---|---:|---:|---:|---:|
| 1 | Luna Max | 7/10 | 70.31 | $18.90 | 3.72 |
| 2 | Sol XHigh | 7/10 | 66.56 | $33.60 | 1.98 |
| 3 | Sol High | 6/10 | 59.47 | $26.80 | 2.22 |
| 4 | Terra Max | 6/10 | 56.60 | $32.20 | 1.76 |
| 5 | Sol Low | 6/10 | 53.21 | $9.40 | 5.66 |
| 6 | Terra Medium | 5/10 | 50.38 | $6.00 | 8.40 |
| 7 | Sol Max | 5/10 | 48.32 | $59.80 | 0.81 |
| 8 | Sol Medium | 5/10 | 45.50 | $16.10 | 2.83 |
| 9 | Luna Medium | 2/10 | 18.24 | $2.40 | 7.60 |

[返回索引 / Back](#批次索引--batch-index)

<a id="2026-07-14-am"></a>
## 2026-07-14-am

> **有效批次，附高消耗警告 / Valid batch with high-consumption warning.** 公开网页提供九档逐题矩阵；API 提供八档精确汇总，Sol Max 由网页补齐。

| 排名 | 模型 / Model | 通过 | 加权分 /100 | 费用 | 加权分/$ | 总 Token |
|---:|---|---:|---:|---:|---:|---:|
| 1 | Sol Medium | 9/10 | 82.75 | $18.41 | 4.49 | 18.48M |
| 2 | Sol High | 9/10 | 82.75 | $24.62 | 3.36 | 23.50M |
| 3 | Sol Low | 8/10 | 71.63 | $9.73 | 7.36 | 8.20M |
| 4 | Terra Max | 7/10 | 62.92 | $30.91 | 2.04 | 65.72M |
| 5 | Luna Max | 6/10 | 60.29 | $15.11 | 3.99 | 88.73M |
| 6 | Sol Max | 6/10 | 59.15 | $60.20 | 0.98 | 72.00M |
| 7 | Sol XHigh | 6/10 | 54.64 | $37.97 | 1.44 | 40.67M |
| 8 | Terra Medium | 5/10 | 45.25 | $5.18 | 8.73 | 8.01M |
| 9 | Luna Medium | 1/10 | 11.65 | $2.44 | 4.78 | 10.81M |

[详细分析 / Detailed analysis](../latest.md) · [逐题位图 / Task bitmaps](../../data/history/task_matrices.csv) · [返回索引 / Back](#批次索引--batch-index)

---

## 数据说明 / Data notes

- `data/history/runs.csv` 保存模型级汇总；
- `data/history/task_matrices.csv` 保存可复现的十题通过位图；
- 早期摘要缺少费用或逐题矩阵时显示 `—`，不会使用后续权重倒推；
- `2026-07-13-pm-anomaly` 是异常批次；
- `2026-07-14-am` 的 API 时间字段存在陈旧值，批次时间以公开网页 07:46 为准；
- `2026-07-14-pm` 的 Sol Medium 逐题列表与汇总通过数不一致，详细页保留两份来源陈述。

- `data/history/runs.csv` stores aggregate runs;
- `data/history/task_matrices.csv` stores reproducible ten-task pass bitmaps;
- missing early fields remain blank rather than being reconstructed with later weights;
- `2026-07-13-pm-anomaly` is down-weighted;
- the 2026-07-14 AM API timestamp was stale, so the public-page time of 07:46 is used;
- the 2026-07-14 PM Sol Medium task list conflicts with its aggregate pass count, and the detailed page preserves both source statements.
