# Latest Analysis Report

**Analysis cutoff:** 2026-07-13 14:05 Asia/Shanghai  
**Primary source:** Codex Radar  
**Batch status:** anomalous; retained with reliability weight `0.35`

> 数据来自 Codex 雷达 codexradar.com

## Executive summary

The 14:05 batch should not be ignored, but it should not receive the same trend weight as a normal batch. Relative to the preceding morning batch, the recorded aggregate quality fell while cost and token activity rose sharply across several model tiers. This indicates a batch-level or harness-level disturbance rather than a clean measurement of model hierarchy.

The long-term recommendation is therefore unchanged:

| Work type | Recommendation |
|---|---|
| Mechanical and retryable | Luna Medium or Terra Medium, with recent stability checked first |
| Daily development | **Sol Medium** |
| Difficult and quota-sensitive | **Luna Max** |
| Maximum-capability fallback | **Sol Max** after cheaper tiers fail |

## 14:05 anomalous batch

| Model tier | Passed | Difficulty-weighted score | Estimated cost | Score / $ |
|---|---:|---:|---:|---:|
| Luna Max | 7/10 | 70.31 | $18.90 | 3.72 |
| Sol XHigh | 7/10 | 66.56 | $33.60 | 1.98 |
| Sol High | 6/10 | 59.47 | $26.80 | 2.22 |
| Terra Max | 6/10 | 56.60 | $32.20 | 1.76 |
| Sol Low | 6/10 | 53.21 | $9.40 | 5.66 |
| Terra Medium | 5/10 | 50.38 | $6.00 | 8.40 |
| Sol Max | 5/10 | 48.32 | $59.80 | 0.81 |
| Sol Medium | 5/10 | 45.50 | $16.10 | 2.83 |
| Luna Medium | 2/10 | 18.24 | $2.40 | 7.60 |

These results are preserved in `data/history/runs.csv` as `2026-07-13-pm-anomaly` with rounded snapshot values.

## Why the batch is down-weighted

Compared with the preceding morning batch recorded during analysis:

- aggregate passes fell by roughly one fifth;
- aggregate estimated cost rose by more than 40%;
- aggregate token activity rose by more than 40%;
- several unrelated tiers simultaneously became less successful and more expensive.

Under the repository's default rule, a quality drop of at least 15% combined with a cost or token increase of at least 30% triggers an anomaly flag.

## Stable interpretation

### Sol Medium remains the daily default

The public history contains the largest useful sample for Sol Medium and shows a recent sequence centered around seven passes out of ten, with occasional stronger and weaker runs. Its normal-batch cost is substantially below High, XHigh, and Max.

### Luna Max remains the quota-sensitive difficult-work candidate

Luna Max has produced strong multi-run pass counts at relatively low estimated cost, though with high total tokens and long wall time. It is attractive for background execution, not necessarily interactive debugging.

### Sol Max remains a fallback, not a default

Sol Max has demonstrated the highest single-batch ceiling, including a 10/10 public-summary run, but it also produced a weak and very expensive result in the anomalous batch. Maximum effort is not a reliability guarantee.

### Reasoning effort is not monotonic

High, XHigh, and Max have repeatedly failed to improve in a clean staircase. Recommendations should move upward only after the current tier fails or project-specific evidence shows a real advantage.

## Confidence

| Conclusion | Confidence |
|---|---|
| Sol Medium is the best general default | Moderate to high |
| Luna Max is a strong quota-sensitive difficult tier | Moderate |
| Sol Max has the highest ceiling | Moderate |
| 14:05 represents normal model capability | Low |
| One latest batch should change the default ladder | Very low |

## Next data needed

- complete task-level matrices for every batch;
- exact timestamps for partial versus full reruns;
- source-side harness/configuration change notes;
- additional independent repetitions of Max tiers;
- direct subscriber-quota calibration separated from API billing.
