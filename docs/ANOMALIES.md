# Anomaly Detection and Batch Reliability

## Why batch-level anomaly detection matters

A sudden model score change can reflect:

- stochastic agent trajectory;
- a model backend update;
- Codex harness changes;
- context compaction or tool-routing changes;
- temporary infrastructure degradation;
- an evaluator or repository failure.

When many configurations simultaneously become more expensive and less successful, treating the batch as an ordinary model comparison can produce absurd recommendations.

## Default rule

Compare the current complete batch with the previous comparable complete batch.

Flag the batch when:

```text
pass_drop >= 15%
AND
(cost_increase >= 30% OR token_increase >= 30%)
```

The 2026-07-13 14:05 snapshot is stored with `anomaly=true` and a reliability weight of `0.35` because the recorded batch showed a broad quality drop alongside substantial resource growth.

## What an anomaly flag does

It does **not** delete the batch.

- Raw tables still show the original values.
- Latest-state reports can still warn users about the degraded service state.
- Rolling recommendations multiply the batch's time weight by its reliability weight.
- Long-term medians may be shown both with and without anomalous batches.

## What an anomaly flag does not prove

It does not prove that the model itself was degraded. The flag describes the observed benchmark batch, not the root cause.

## Additional diagnostics

Future versions should add:

- median absolute deviation for total cost and total tokens;
- invalid-task rate;
- task-level simultaneous failure count;
- model-family correlation of score changes;
- repeated identical pass matrices across efforts;
- source-side notices about known incidents or harness changes.

## Suggested UI labels

| Reliability weight | Label |
|---:|---|
| 1.00 | Normal batch |
| 0.70 | Mild concern |
| 0.35 | Anomalous batch |
| 0.00 | Invalid / excluded from trend |

A zero weight should be reserved for objectively invalid data, such as failed evaluation infrastructure, not simply surprising results.
