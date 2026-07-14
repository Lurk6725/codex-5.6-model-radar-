# Changelog / 更新日志

All notable methodology, data, recommendation, and presentation changes are documented here.  
所有重要的评分方法、数据、模型推荐和页面展示变化都会记录在此。

## Unreleased / 尚未发布

### Added / 新增

- Navigable historical batch index in `reports/history/README.md`.
- Full latest task-weight table with historical pass rates and weights.
- Latest observed and latest complete non-anomalous model rankings.
- Weighted score `/100` and weighted score `/$` in the main ranking tables.
- Direct links from the project home page to latest and historical results.
- Authorized API aggregate monitoring with archived normalized snapshots.
- 2026-07-14 AM and PM analysis in Chinese, English, and combined reports.
- Dedicated historical snapshot page for `2026-07-14-pm`.
- Machine-readable PM task matrix and updated task-weight snapshot.

### Changed / 变更

- Model recommendations now appear before detailed weights and rankings.
- README and reports were simplified to emphasize results instead of maintenance rules.
- Chinese, English, and combined result pages remain available without a standalone bilingual-policy document.
- Low-cost retryable recommendation changed to **Sol Low** after two consecutive 8/10 results.
- Daily development and small-project bug-review recommendation remains **Sol Medium** because it ties High and XHigh in aggregate quality at lower cost.
- **Sol Max** returned to the maximum-capability fallback position after reaching the highest PM weighted score.
- Luna Max is no longer a general difficult-work recommendation.
- API documentation states that aggregate changes do not prove reruns and that the endpoint lacks task matrices, per-model run IDs, and full/partial batch markers.

### Data-quality notes / 数据质量说明

- The 2026-07-14 PM API snapshot contains eight tiers and omits Sol Max; the public page supplies Sol Max and the task matrix.
- Terra Medium and Luna Medium were replaced by Terra High and Luna High in the PM active lineup, so these are not like-for-like trend comparisons.
- Sol Medium is reported as 7/10 by the API and aggregate table, while the public per-task list contains six explicit passes. The repository preserves both source statements and reports a weighted-score range instead of guessing.
- The PM batch is valid with high-consumption and source-consistency warnings.
- The API `observed_at` field remains stale while comparison values change; `retrieved_at` and public-page update time are retained separately.

### Removed / 删除

- Redundant `docs/BILINGUAL_POLICY.md`.
- Broken or unnecessary references to the removed policy document.

## 0.1.0 — 2026-07-13

### Added

- Initial public repository structure.
- Historical aggregate run data from the Codex Radar public summary.
- Manually transcribed 2026-07-13 14:05 anomalous batch.
- Soft inverse-pass-rate task weighting.
- Difficulty-weighted score and 0–150 display mapping.
- Quota-efficiency and Pareto-frontier utilities.
- Batch anomaly detection with reliability down-weighting.
- Reproducible report generator and automated tests.
- Documentation for data provenance, subscription cost interpretation, anomaly handling, and recommendations.

### Initial recommendation

- Daily default: Sol Medium.
- Low-risk retryable work: Luna Medium or Terra Medium.
- Difficult quota-sensitive work: Luna Max.
- Maximum-capability fallback: Sol Max.

### Known limitations

- Historical public-summary rows do not always expose task-level matrices or prior-run cost.
- The 14:05 snapshot contains rounded manually transcribed values.
- Complete protected exports or private API access, if later needed, require coordination with the Codex Radar maintainer; current public-page analysis does not depend on them.
