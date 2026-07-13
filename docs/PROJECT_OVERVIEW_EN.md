# GPT‑5.6 Codex Model Radar — English Overview

## Project

**GPT‑5.6 Codex Model Radar** is an independent, non-commercial, open-source project for long-term monitoring of GPT‑5.6 Codex model families and reasoning-effort levels.

Repository: https://github.com/FYLiu39/codex-5.6-model-radar-

## Purpose

The project uses publicly visible Codex Radar benchmark results as the source dataset and adds a reproducible analysis layer for:

- difficulty-weighted scoring;
- rolling stability and volatility;
- anomaly detection and anomaly-adjusted trends;
- estimated quota efficiency;
- cost-capability Pareto analysis; and
- practical model recommendations for different workloads.

The goal is to preserve historical observations, make the scoring method transparent, and reduce overreaction to noisy single-batch results—not to replace Codex Radar.

## Data attribution

Original benchmark observations are attributed to **Codex Radar** (`codexradar.com`, formerly `codex-reset-radar.pages.dev`). The repository is not affiliated with OpenAI, Codex Radar, or DeepSWE.

The project uses publicly visible website or summary information. It does not use private credentials, bypass authentication, or access protected endpoints. Private API access, protected full-history exports, or redistribution of protected detailed data would require coordination with the source maintainer.

## Scoring method

```text
raw_difficulty_i = 1 / sqrt(historical_pass_rate_i)
weight_i = 100 * raw_difficulty_i / sum(raw_difficulty)
weighted_score = sum(weight_i * passed_i)
```

This gives more credit to historically difficult tasks while limiting the influence of one rare task.

Published metrics include:

- raw pass count;
- weighted score on a 0–100 scale;
- weighted IQ on a 0–150 display scale;
- weighted score per estimated dollar-equivalent cost;
- recent median, mean, and range;
- anomaly flags and reliability weights; and
- multi-run recommendations rather than latest-run-only rankings.

## Subscription-cost interpretation

The source site's estimated USD-equivalent cost is treated as a relative proxy for Codex subscription quota consumption, not an exact subscriber bill. Based on a clarification reported from OpenAI staff, the API-only long-context price step above 272K input tokens is not added to subscription-oriented analysis. Tokens and wall time remain separate execution-expansion and latency indicators.

## Handling anomalous batches

A batch may be marked anomalous when system-wide quality drops while total cost or token use rises sharply. The batch remains visible in raw history but receives a lower reliability weight in trend calculations. This preserves possible regression evidence without allowing one unstable run to reverse the recommendation immediately.

## Results and history

- [Latest bilingual analysis](../reports/latest.md)
- [Latest English analysis](../reports/latest.en.md)
- [Historical batch index](../reports/history/README.md)
- [Raw aggregate run history](../data/history/runs.csv)
- [Latest task-weight snapshot](../data/weights/task_weights.csv)

## Current limitations

- The active test set contains only ten tasks;
- each model/task is generally observed once per batch;
- task trajectories are stochastic;
- historical difficulty weights may encode model-family preferences;
- earlier public summaries may omit task-level matrices or cost fields;
- estimated cost is not an official subscription debit; and
- fixed benchmark tasks do not represent every private software repository.
