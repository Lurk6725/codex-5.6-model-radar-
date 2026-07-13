# GPT‑5.6 Codex Model Radar

A community-maintained, reproducible monitor for **GPT‑5.6 Luna, Terra, and Sol** in Codex, including reasoning-effort comparisons, difficulty-weighted scoring, cost-efficiency analysis, anomaly detection, and practical model recommendations.

> Data attribution: source benchmark data comes from **Codex Radar** (`codexradar.com`, formerly `codex-reset-radar.pages.dev`). This repository is an independent secondary analysis project and is not affiliated with OpenAI, Codex Radar, or DeepSWE.

## English project statement

This is an independent, non-commercial, open-source secondary-analysis project. It studies publicly visible Codex Radar benchmark results and adds reproducible difficulty weighting, stability analysis, anomaly handling, cost-efficiency metrics, and practical model recommendations.

The current repository does **not** use a private API, bypass authentication, or access protected endpoints. Publicly displayed benchmark results are recorded with attribution and transformed through original analysis code. If the project later adds automated full-data synchronization, private API access, or redistribution of a complete historical dataset, the repository maintainer will first coordinate with the Codex Radar maintainer.

A longer English overview is available in [`docs/PROJECT_OVERVIEW_EN.md`](docs/PROJECT_OVERVIEW_EN.md).

## What this repository tracks

- Model families: **Luna, Terra, Sol**
- Reasoning efforts: **low, medium, high, xhigh, max** when available
- Fixed repository-level engineering tasks derived from the Codex Radar / DeepSWE test set
- Raw pass count, task-level outcomes, tokens, wall time, and estimated cost
- Difficulty-weighted quality score
- Quality-per-cost score for subscription-oriented comparison
- Rolling stability, volatility, and anomalous-batch flags
- Practical recommendations for low-risk work, daily development, difficult work, and maximum-quality fallback

## Current working conclusions

These are provisional and must be interpreted together with the historical data and anomaly flags:

| Use case | Current default |
|---|---|
| Mechanical, low-risk, retryable work | Luna Medium or Terra Medium, depending on recent stability |
| General daily Codex work | **Sol Medium** |
| Difficult work, quota-sensitive, long-running | **Luna Max** |
| Maximum-capability fallback | **Sol Max**, only after cheaper tiers fail |

High, XHigh, and Max do **not** show monotonic gains in every batch. Single-run results are noisy; recommendations are based on rolling statistics rather than the latest 10-task score alone.

## Scoring overview

The source site's equal-weight score gives every task the same value. This project additionally calculates a soft inverse-pass-rate weight:

```text
raw_difficulty_i = 1 / sqrt(historical_pass_rate_i)
weight_i = 100 * raw_difficulty_i / sum(raw_difficulty)
weighted_score = sum(weight_i * passed_i)
```

This rewards difficult tasks without allowing one rare task to dominate the entire leaderboard.

Primary metrics:

1. **Weighted score (0–100)** — difficulty-adjusted capability.
2. **Weighted IQ (0–150)** — weighted score multiplied by 1.5 for comparison with the source site's display scale.
3. **Quota efficiency** — weighted score divided by the source site's estimated USD-equivalent cost.
4. **Rolling stability** — median and exponentially weighted results over recent valid batches.
5. **Anomaly-adjusted trend** — suspicious batches are retained but down-weighted.

See [`docs/METHODOLOGY.md`](docs/METHODOLOGY.md) for the full formulas.

## Subscription-cost interpretation

OpenAI staff clarification reported by the community indicates that the API-only long-context price step above 272K input tokens does **not** apply to ChatGPT/Codex subscription quota accounting. Therefore this project:

- does not add the API 2× input / 1.5× output long-context multiplier to subscription analysis;
- treats Codex Radar's estimated USD-equivalent cost as a **relative quota proxy**, not an exact subscriber bill;
- keeps total tokens and wall time as separate indicators of agent expansion and latency.

See [`docs/COSTS.md`](docs/COSTS.md).

## Repository layout

```text
.
├── data/
│   ├── history/runs.csv          # historical aggregate benchmark runs
│   ├── schema/task_results.example.csv
│   └── weights/task_weights.csv  # task pass rates and current weights
├── docs/
│   ├── PROJECT_OVERVIEW_EN.md
│   ├── DATA_SOURCES.md
│   ├── METHODOLOGY.md
│   ├── COSTS.md
│   ├── ANOMALIES.md
│   └── RECOMMENDATIONS.md
├── radar/
│   ├── scoring.py
│   └── anomaly.py
├── scripts/
│   └── build_report.py
├── reports/latest.md
└── tests/
```

## Reproduce the analysis

```bash
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -e .
pytest
python scripts/build_report.py
```

## Data policy

This project analyzes benchmark information that is publicly visible on Codex Radar and always attributes the original source.

Current maintenance may use:

1. manually verified public website snapshots;
2. public summary data exposed by the source site; and
3. original calculations produced by this repository.

The project does not use private credentials, evade access controls, or present itself as an official Codex Radar mirror. Permission is not treated as a prerequisite for the present public-page analysis. However, before adding automated full-history synchronization, private API access, or redistribution of a complete protected dataset, the project will contact the Codex Radar maintainer and follow any stated access and attribution requirements.

Each imported batch should retain its original timestamp, source URL, provenance note, and any uncertainty caused by rounded or partial data.

## Limitations

- The active test set contains only ten tasks, so one task changes raw pass rate by ten percentage points.
- Each model/task is generally observed once per batch; agent trajectories are stochastic.
- Difficulty weights are based on historical global pass rates and may encode task-family bias.
- Estimated cost is a relative proxy for subscription usage, not an official account-level debit.
- A model can be best for this test set without being best for UI design, writing, code review, or a specific private repository.

## License

Code and original analysis are released under the MIT License. Third-party benchmark data remains subject to its source terms and attribution requirements.