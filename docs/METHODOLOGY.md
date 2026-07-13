# Scoring Methodology

## 1. Why the source score needs a companion metric

Codex Radar currently evaluates ten fixed repository-level engineering tasks. Its display score is effectively:

```text
source_iq = 15 × passed_tasks
```

That scale is simple and transparent, but it treats a task with a 95% historical pass rate exactly the same as a task with a 16% pass rate. This project keeps the source score and adds a difficulty-adjusted score.

## 2. Difficulty weights

For task `i`, let `p_i` be its historical pass rate in `(0, 1]`.

```text
raw_i = 1 / sqrt(p_i)
weight_i = 100 × raw_i / sum(raw_j)
```

The square-root inverse is deliberately softer than `1 / p_i`:

- difficult tasks receive more credit;
- a single rare task cannot dominate the whole benchmark;
- weights remain easy to explain and reproduce.

The weight snapshot used for a batch must be stored with the batch or versioned separately. A run should be scored using pass rates known before that run whenever possible, preventing the run from changing its own difficulty weights.

## 3. Weighted capability score

For binary result `x_i ∈ {0, 1}`:

```text
weighted_score = sum(weight_i × x_i)
weighted_iq = 1.5 × weighted_score
```

The first score ranges from 0 to 100. The second ranges from 0 to 150 only to make comparison with the source site's display scale intuitive. It is not a psychometric IQ score.

## 4. Quota efficiency

```text
quota_efficiency = weighted_score / estimated_cost_usd
```

The cost is the USD-equivalent estimate reported by Codex Radar. For subscription users this is treated as a relative quota proxy, not a literal bill.

Quota efficiency must never be shown without absolute capability. A very cheap model can lead this metric while failing most tasks.

Recommended display:

- weighted score;
- raw pass count;
- estimated cost;
- weighted score per USD;
- wall time;
- recent median and range.

## 5. Rolling stability

A ten-task, one-run-per-task benchmark has substantial trajectory noise. The default stability view therefore includes:

- latest valid score;
- latest 3-run median;
- latest 5-run median;
- exponentially weighted score, newest runs emphasized;
- minimum and maximum over the displayed window;
- number of valid observations.

For an EWMA-like trend, with observations ordered oldest to newest:

```text
time_weight_t = (1 - alpha) ^ age_t
trend = sum(score_t × time_weight_t × reliability_t)
        / sum(time_weight_t × reliability_t)
```

Default `alpha = 0.5`.

## 6. Anomalous batches

A batch is provisionally flagged when both conditions hold against the previous comparable batch:

```text
total pass count falls by at least 15%
AND
(total estimated cost OR total tokens rises by at least 30%)
```

Flagged data is retained. Its default reliability weight is `0.35`, rather than deleting the observation. This preserves evidence of real service regressions while preventing one system-wide failure from rewriting long-term model recommendations.

The anomaly rule is implemented in `radar/anomaly.py`.

## 7. Pareto frontier

A model configuration is dominated when another configuration:

- costs no more;
- scores no less;
- and is strictly better on at least one of those dimensions.

Non-dominated configurations form the cost-quality Pareto frontier. A dominated tier may still have a practical role because of latency, behavior, or task specialization, so the frontier is descriptive rather than a deletion rule.

## 8. Recommendation logic

Recommendations are based on multiple objectives rather than a single leaderboard:

### Retryable / mechanical work

Prioritize low cost, but require a minimum recent capability floor.

### Daily development

Prioritize 5-run stability, moderate cost, and low anomaly sensitivity.

### Difficult, quota-sensitive work

Prioritize strong rolling capability per unit cost, accepting longer wall time.

### Maximum-quality fallback

Prioritize the highest demonstrated upper bound only after cheaper tiers fail.

## 9. Statistical limitations

- Ten tasks are too few for precise model ranking.
- One task changes raw success rate by ten percentage points.
- Task-level results are correlated by language, repository, and implementation style.
- Difficulty is estimated from the same model ecosystem being compared.
- Agent trajectories introduce randomness even when model and prompt are unchanged.
- Cost, tokens, and wall time can change because of harness updates rather than model intelligence.

For those reasons, this project avoids claims such as “Model A is definitively smarter than Model B” based on a single batch.
