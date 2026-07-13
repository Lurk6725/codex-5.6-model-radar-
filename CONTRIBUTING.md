# Contributing / 贡献指南

欢迎提交能够改进数据质量、可复现性、统计解释或中英文可读性的贡献。  
Contributions that improve data quality, reproducibility, statistical interpretation, or bilingual readability are welcome.

## 新增测试批次 / Adding a benchmark batch

1. 记录准确的来源 URL、批次时间和模型档位。  
   Record the exact source URL, batch timestamp, model family, and effort tier.
2. 将汇总数据加入 `data/history/runs.csv`。
3. 有逐题结果时，按 `data/schema/task_results.example.csv` 保存。
4. 人工抄录、四舍五入或部分重跑必须写入 `provenance`。
5. 更新 `data/weights/task_weights.csv` 时保留新的权重快照 ID。
6. 更新 `reports/history/README.md`，为新批次增加可跳转记录。
7. 更新中文、英文和合并版最新分析：
   - `reports/latest.zh-CN.md`
   - `reports/latest.en.md`
   - `reports/latest.md`
8. 运行测试和报告生成脚本。

## 数据检查 / Data review

- [ ] Batch ID 唯一 / Batch ID is unique.
- [ ] 通过数与逐题结果一致 / Pass count matches task-level outcomes.
- [ ] 十题原始 IQ 等于 `15 × passed` / Raw IQ equals `15 × passed`.
- [ ] Token、时间和费用字段非负且合理。
- [ ] 来源费用按原值保存，不静默覆盖为重新估算值。
- [ ] 权重快照、异常状态和可靠度权重有明确说明。
- [ ] 中文和英文报告使用相同数据、推荐与限制条件。
- [ ] 历史索引包含新批次跳转。

## 方法变更 / Methodology changes

方法修改应说明：

- 新公式及其解决的问题；
- 在历史数据上的对比；
- 敏感性分析；
- 对排名和推荐的影响；
- 如何保留旧结果的可复现性。

A methodology change should document the new formula, historical comparison, sensitivity analysis, ranking impact, and reproducibility plan.

不要因为当前权重变化直接覆盖旧批次分数。应保留原始权重快照，或生成新的衍生版本。  
Do not overwrite historical scores merely because the current weight snapshot changed.

## 推荐变更 / Recommendation changes

模型不应因为单轮结果直接成为默认推荐。优先使用以下证据：

- 连续三个正常批次；
- 最近五轮中位数发生明显变化；
- 持续的 Pareto 优势；
- 已记录的官方配置变化；
- 私人项目中的可复现实验。

A default recommendation should not change from one run alone. Explain the evidence, uncertainty, and failure modes in both language versions.
