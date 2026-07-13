# Subscription Cost Interpretation

## API billing and subscription quota are different questions

OpenAI's API may use separate short- and long-context price tiers. Community reporting of an OpenAI employee clarification states that the API-only long-context surcharge above 272K input tokens does **not** apply to ChatGPT/Codex subscription users.

Accordingly, this project does not multiply subscription-oriented estimates by the API long-context factors.

## What the source cost means here

Codex Radar reports an estimated USD-equivalent cost derived from model token prices and its quota calibration. This project uses that field as a **relative quota proxy**:

```text
quota_efficiency = difficulty_weighted_score / estimated_cost_usd
```

It is useful for comparing configurations under the same methodology, but it is not guaranteed to equal:

- the dollar value of a Plus or Pro plan;
- an exact debit shown in a user's account;
- a fixed amount of five-hour or weekly quota;
- the cost of the same task in a private repository.

## Why total tokens are not the quota metric

Luna, Terra, and Sol have different token prices. A Luna run can use many more tokens while still having a lower estimated quota cost. Therefore:

- use estimated cost for cross-model quota efficiency;
- use total tokens to diagnose context growth and repeated agent work;
- use wall time to evaluate latency;
- use pass rate and weighted score to evaluate quality.

Do not rank subscription value by total tokens alone.

## Cache-write uncertainty

Codex tooling may not expose every cache-write field directly. If the source estimates cache creation from the maximum observed prefix, the resulting cost is an estimate rather than a billing-grade reconstruction.

The repository should preserve both the source cost and any independently calculated cost instead of replacing one with the other.

Suggested columns:

```text
source_cost_usd
recomputed_cost_usd
cost_method
cost_confidence
```

## Recommended interpretation bands

| Use | Confidence |
|---|---|
| Compare two tiers in the same batch | Moderate to high |
| Compare rolling median costs across nearby batches | Moderate |
| Convert a run into exact Plus/Pro quota percentage | Low unless directly calibrated |
| Predict another user's account usage | Low |

## Reporting rule

Every report should present quality and cost separately before presenting a composite efficiency score. A low-capability model must not be called “best” solely because it is cheap.
