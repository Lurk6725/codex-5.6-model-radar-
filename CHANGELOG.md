# Changelog / 更新日志

All notable methodology, data, recommendation, and publication-format changes are documented here.  
所有重要的评分方法、数据、模型推荐和发布格式变化都会记录在此。

## Unreleased / 尚未发布

### Added / 新增

- Complete Simplified Chinese project overview in `docs/PROJECT_OVERVIEW_ZH_CN.md`.
- Bilingual publication policy in `docs/BILINGUAL_POLICY.md`.
- Separate Chinese and English latest reports plus a combined bilingual entry page.
- Chinese, English, and combined outputs from `scripts/build_report.py`.
- CI checks requiring both language versions for formal and generated reports.
- README landing page with both Simplified Chinese and English project explanations.

### Changed / 变更

- Contribution rules now require identical data, anomaly decisions, recommendations, confidence, and limitations in both languages.
- Public-page analysis is distinguished from optional future private API or full-history integration.

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
- Private API access or protected full-history export, if later needed, requires coordination with the Codex Radar maintainer; current public-page analysis does not depend on it.
