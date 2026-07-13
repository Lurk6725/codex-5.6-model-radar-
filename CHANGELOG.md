# Changelog

All notable methodology, data, and recommendation changes are documented here.

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
- Full API access requires authorization from Codex Radar.
