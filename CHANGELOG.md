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
- 2026-07-14 AM aggregate trend analysis in Chinese, English, and combined reports.

### Changed / 变更

- Model recommendations now appear before detailed weights and rankings.
- README and reports were simplified to emphasize results instead of maintenance rules.
- The report generator now outputs recommendations, weights, observed ranking, valid ranking, and rolling stability in that order.
- Chinese, English, and combined result pages remain available without a standalone bilingual-policy document.
- Daily recommendation remains Sol Medium; the latest API snapshot strengthens this conclusion because Medium tied High at 9/10 with lower cost and resource use.
- Luna Max was reduced from a clear difficult-work recommendation to a watchlist option after the latest aggregate result fell to 6/10.
- Luna Medium was removed from the low-risk recommendation after falling to 1/10 in the latest aggregate snapshot.
- API documentation now states that aggregate changes do not prove reruns and that the endpoint lacks task matrices, per-model run IDs, and full/partial batch markers.

### Data-quality notes / 数据质量说明

- The 2026-07-14 AM API snapshot contains eight tiers and omits Sol Max.
- The snapshot `source_date` changed to `2026-07-14-am`, while the API `observed_at` value remained unchanged, so freshness metadata is inconsistent.
- Task-weighted scores remain based on the latest available task matrix and are not recomputed from aggregate API values.

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
