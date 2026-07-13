# English Project Overview

## Project

**GPT-5.6 Codex Model Radar** is an independent, non-commercial, open-source project for long-term monitoring of GPT-5.6 Codex model families and reasoning-effort levels.

Repository:

https://github.com/FYLiu39/codex-5.6-model-radar-

## Purpose

The project uses publicly visible Codex Radar benchmark results as the source dataset and adds a reproducible analysis layer for:

- difficulty-weighted scoring;
- rolling stability and volatility;
- anomaly detection and anomaly-adjusted trends;
- estimated quota efficiency;
- cost-capability Pareto analysis; and
- practical model recommendations for different workloads.

The goal is not to replace Codex Radar. The goal is to preserve historical observations, make the scoring method transparent, and reduce overreaction to noisy single-batch results.

## Data attribution

The original benchmark observations are attributed to **Codex Radar** (`codexradar.com`, formerly `codex-reset-radar.pages.dev`). The repository is not affiliated with OpenAI, Codex Radar, or DeepSWE.

The current project only uses information that is publicly visible on the website or public summary output. It does not use private credentials, bypass authentication, or access protected endpoints.

If the project later needs automated access to a private API, a complete historical export, or permission to redistribute protected full-detail data, the repository maintainer will contact the Codex Radar maintainer first and follow the requested access, attribution, and rate-limit rules.

## Scoring method

The source benchmark uses an equal-weight pass count. This project additionally applies soft inverse-pass-rate weighting:

```text
raw_difficulty_i = 1 / sqrt(historical_pass_rate_i)
weight_i = 100 * raw_difficulty_i / sum(raw_difficulty)
weighted_score = sum(weight_i * passed_i)
```

This gives more credit to historically difficult tasks while limiting the influence of a single rare task.

The project also publishes:

- raw pass count;
- weighted score on a 0-100 scale;
- weighted IQ on a 0-150 display scale;
- weighted score per estimated dollar-equivalent cost;
- recent median and exponentially weighted trends;
- anomaly flags and reliability weights; and
- multi-run recommendations instead of latest-run-only rankings.

## Subscription-cost interpretation

The analysis treats the source site's estimated USD-equivalent cost as a relative proxy for Codex subscription quota consumption, not as an exact subscriber bill.

Based on a clarification reported from OpenAI staff, the API-only long-context price step above 272K input tokens is not added to the subscription-oriented analysis. Tokens and wall time remain visible as separate indicators of execution expansion and latency.

## Handling abnormal batches

A batch may be marked anomalous when system-wide quality drops while total cost or token use rises sharply. An anomalous batch is not deleted. It remains visible in the raw history but receives a lower reliability weight in trend calculations.

This prevents one unstable run from immediately reversing a recommendation while still preserving evidence of possible real regressions.

## Current project status

The repository currently contains:

- historical aggregate runs;
- task difficulty weights;
- scoring and anomaly-detection code;
- reproducible report generation;
- unit tests;
- methodology and data-policy documentation; and
- provisional model recommendations.

The historical dataset is still incomplete because not every earlier task-level matrix is publicly available. Any future imported data should include a timestamp, source URL, provenance note, and uncertainty label.

## Message to the Codex Radar maintainer

This project is intended to complement and credit the original benchmark. Feedback on attribution wording, public-data usage, methodology, or preferred linking is welcome. If an official public export or documented integration method becomes available, the project would be glad to use it under the maintainer's stated conditions.