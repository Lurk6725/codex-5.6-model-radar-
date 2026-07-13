# Data Sources and Provenance

## Primary benchmark source

The primary source is **Codex Radar**:

- Website: `https://codexradar.com/`
- Former host: `https://codex-reset-radar.pages.dev/`
- Public summary: `https://codex-reset-radar.pages.dev/current.json`

Required attribution:

> 数据来自 Codex 雷达 codexradar.com

Codex Radar publishes a recurring ten-task repository-level coding evaluation with model, reasoning effort, pass count, tokens, wall time, and estimated cost. Visible task-level outcomes may be manually transcribed into this repository with a timestamp and provenance note.

## Full API restriction

The public summary states that the full JSON API and derivative integrations require authorization. This repository therefore does not:

- bypass authorization;
- embed a private API key;
- automate high-frequency requests to a protected endpoint;
- republish unavailable private fields as if they were public.

Authorized exports can be committed by the repository owner after confirming that redistribution is permitted.

## Secondary sources

Secondary context may include:

- OpenAI official Codex documentation and rate cards;
- public statements by OpenAI employees;
- DeepSWE documentation or paper;
- public community discussions used to interpret anomalies.

Secondary sources do not replace the benchmark's raw task outcomes.

## Provenance values

Every row should use one of these provenance labels:

| Label | Meaning |
|---|---|
| `public_summary` | Directly present in the public summary JSON |
| `manual_snapshot` | Manually transcribed from a visible website snapshot |
| `manual_snapshot_rounded` | Transcribed from a screenshot or rounded display values |
| `authorized_export` | Imported from an API/export with explicit authorization |
| `derived` | Calculated from other versioned fields in this repository |
| `example_only` | Schema example; must not enter production rankings |

## Reproducibility rules

A historical record must not be silently overwritten. Corrections should:

1. preserve the original commit history;
2. document the correction in `CHANGELOG.md`;
3. state which source field was wrong;
4. regenerate reports with the corrected data;
5. avoid retroactively changing the weight snapshot unless the earlier weight was itself erroneous.

## Timestamp convention

- Store timestamps in ISO 8601.
- Preserve the source timezone.
- Codex Radar commonly reports in `Asia/Shanghai`.
- Human labels such as `2026-07-13-am` may be retained as stable batch IDs, but they do not replace exact timestamps when available.

## Attribution and independence

This repository is an independent analysis. It is not affiliated with or endorsed by OpenAI, Codex Radar, or the DeepSWE authors. Model and product names belong to their respective owners.
