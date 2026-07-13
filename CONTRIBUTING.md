# Contributing / 贡献指南

Contributions that improve reproducibility, data quality, statistical interpretation, or bilingual accessibility are welcome.  
欢迎提交能够改进可复现性、数据质量、统计解释或中英文可读性的贡献。

## Adding a benchmark batch / 新增测试批次

1. Confirm that the source permits the intended use. / 确认数据来源允许当前使用方式。
2. Record the exact source URL and timestamp. / 记录准确来源 URL 和时间。
3. Preserve the source's model name and reasoning effort. / 保留来源模型名称与推理强度。
4. Add aggregate data to `data/history/runs.csv`.
5. Add task-level outcomes when available using `data/schema/task_results.example.csv`.
6. Mark rounded or manually transcribed values clearly in `provenance`.
7. Run the test suite and report generator.
8. Update `CHANGELOG.md` when a correction or methodology change affects rankings.
9. Publish the analysis in both Simplified Chinese and English.

## Required bilingual outputs / 必须提供的双语文件

Every formal benchmark update must update all three report entry points:

- `reports/latest.zh-CN.md` — complete Simplified Chinese analysis;
- `reports/latest.en.md` — complete English analysis;
- `reports/latest.md` — combined bilingual report.

每次正式测试更新必须同时更新以上三个文件。中文和英文版本必须使用相同数据、异常判断、模型推荐、置信度和限制条件。

The generated report command must also produce:

- `reports/latest.generated.zh-CN.md`;
- `reports/latest.generated.en.md`;
- `reports/latest.generated.md`.

If only one language is ready, keep the update as a draft and do not replace the formal `latest` files. See [`docs/BILINGUAL_POLICY.md`](docs/BILINGUAL_POLICY.md).

## Data review checklist / 数据检查清单

- [ ] Batch ID is unique. / 批次 ID 唯一。
- [ ] Pass count equals the sum of valid task outcomes. / 通过数与逐题结果一致。
- [ ] Raw IQ equals `15 × passed` for the ten-task source display.
- [ ] Token components are non-negative and internally plausible.
- [ ] Estimated cost is copied from the source, not silently recomputed over it.
- [ ] Weight snapshot is identified.
- [ ] Anomaly state and reliability weight are justified.
- [ ] Source attribution is present.
- [ ] Chinese and English reports contain identical figures.
- [ ] Chinese and English reports reach the same recommendation.
- [ ] Both languages state the same confidence and limitations.

## Methodology changes / 方法变更

A methodology pull request should include:

- the proposed formula;
- the problem it solves;
- a comparison against the existing formula on historical data;
- sensitivity analysis;
- expected effect on recommendations;
- a migration plan that keeps older reports reproducible;
- matching Chinese and English explanations.

Do not change historical scores in place merely because current task weights changed. Recompute into a new derived version or preserve the original weight snapshot.

不要仅因为当前题目权重发生变化就直接覆盖历史分数。应生成新的衍生版本，或保留原始权重快照以确保历史可复现。

## Recommendation changes / 推荐变更

A model should not become the default based on a single batch. Prefer one of these evidence standards:

- three consecutive valid batches;
- a material five-run median change;
- persistent Pareto dominance;
- a documented official configuration change;
- repeated project-specific evidence supplied with a reproducible task set.

模型不应因为单轮结果就成为默认推荐。推荐变化必须在中文和英文报告中同时解释证据、风险和置信度。

## Pull requests / 拉取请求

Keep data imports separate from methodology changes when practical. This makes it easier to review whether a ranking changed because of new evidence or a new formula.

数据导入和评分方法修改尽量拆分提交，以便区分排行榜变化究竟来自新数据还是新公式。
