# Changelog / 更新日志

All notable methodology, data, recommendation, and presentation changes are documented here.  
所有重要的评分方法、数据、模型推荐和页面展示变化都会记录在此。

## Unreleased / 尚未发布

### Added / 新增

- Navigable historical batch index in `reports/history/README.md`.
- Full task-weight tables and weighted score `/100` plus weighted score `/$` rankings.
- Authorized API aggregate monitoring with archived normalized snapshots.
- Chinese, English, and combined analyses for the July 14 AM/PM and July 15 AM/PM batches.
- Dedicated historical snapshot pages for `2026-07-14-pm`, `2026-07-15-am`, and `2026-07-15-pm`.
- Per-batch aggregate files under `data/history/batches/`.
- Report generation merges the legacy aggregate CSV with per-batch files and de-duplicates by batch/model/effort.

### Changed / 变更

- Model recommendations appear before detailed weights and rankings.
- README and reports emphasize results rather than maintenance rules.
- Daily development and small-project bug-review recommendation remains **Sol Medium**, but confidence is reduced to medium after a 6/10 July 15 PM result.
- **Luna Max** returns as the preferred difficult, quota-sensitive background tier after reaching 9/10 and 90.08 weighted points at about $16.30.
- **Sol Low** remains the low-cost retryable tier after returning to 8/10; historical volatility still prevents it from becoming the important-work default.
- Within the Sol family, **Sol High** is the preferred current escalation after Medium fails. XHigh's morning 10/10 did not repeat in the afternoon.
- **Sol Max** remains non-default: it reached 6/10 and 54.61 weighted points at the highest cost in the July 15 PM batch.

### Data-quality notes / 数据质量说明

- The 2026-07-14 PM API snapshot contains eight tiers and omits Sol Max; the public page supplies Sol Max and the task matrix.
- Sol Medium's July 14 PM aggregate and per-task list disagree; the repository preserves the mismatch rather than guessing.
- The July 15 AM and PM authorized API history had not archived new snapshots at analysis time. Aggregate cost, token, and wall-time values therefore use rounded public-page values.
- The July 15 PM task matrix is complete and internally consistent: nine tiers, 60/90 total passes.
- The July 15 PM batch is valid; quality declined 9.1% from the morning while cost and tokens also declined slightly, so anomaly down-weighting is not applied.

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
