# Latest Analysis Report — English

[Project home](../README.md) · [简体中文](latest.zh-CN.md) · [API monitor](api-latest.md) · [Historical data](history/README.md)

**Analysis cutoff:** 2026-07-14 07:46 Asia/Shanghai  
**Batch:** `2026-07-14-am`  
**Sources:** authorized Codex Radar API plus the public task matrix

> The API supplied eight model-level summaries but omitted Sol Max and task outcomes. The public page supplied Sol Max, the full nine-tier task matrix, and updated historical pass rates.

## Model recommendations

| Work type | Recommendation | Rationale |
|---|---|---|
| Mechanical, low-risk, retryable | **Terra Medium**; Sol Low remains a volatile stronger candidate | Terra Medium is cheap; Sol Low reached 8/10 but has a weak long-run median |
| Daily development and small-project bug review | **Sol Medium** | It tied Sol High at 9/10 with identical task outcomes while costing less |
| Difficult, quota-sensitive, long-running | **Try Sol Medium first; Luna Max is specialized/watchlist only** | Luna Max reached 6/10 and uniquely passed task 07, but general quality was lower |
| Maximum-capability fallback | **Sol Max only as a historical-ceiling fallback** | It reached only 6/10 at the highest cost |

## Latest task weights

**Weight snapshot:** `2026-07-14-0746`  
**Formula:** `weight_i ∝ 1 / sqrt(historical_pass_rate_i)`, normalized to 100.

| Task | Historical pass rate | Weight /100 |
|---:|---:|---:|
| 01 | 78.88% | 7.80 |
| 02 | 79.81% | 7.76 |
| 03 | 94.41% | 7.13 |
| 04 | 38.82% | 11.12 |
| 05 | 35.40% | 11.65 |
| 06 | 93.48% | 7.17 |
| 07 | 16.15% | **17.25** |
| 08 | 49.38% | 9.86 |
| 09 | 36.02% | 11.55 |
| 10 | 63.24% | 8.71 |
|  | **Total** | **100.00** |

## Latest task-weighted ranking

| Rank | Model tier | Passed | Weighted /100 | Cost | Weighted/$ |
|---:|---|---:|---:|---:|---:|
| 1 | **Sol Medium** | 9/10 | **82.75** | $18.41 | **4.49** |
| 2 | Sol High | 9/10 | **82.75** | $24.62 | 3.36 |
| 3 | Sol Low | 8/10 | 71.63 | $9.73 | 7.36 |
| 4 | Terra Max | 7/10 | 62.92 | $30.91 | 2.04 |
| 5 | Luna Max | 6/10 | 60.29 | $15.11 | 3.99 |
| 6 | Sol Max | 6/10 | 59.15 | $60.20 | 0.98 |
| 7 | Sol XHigh | 6/10 | 54.64 | $37.97 | 1.44 |
| 8 | **Terra Medium** | 5/10 | 45.25 | **$5.18** | **8.73** |
| 9 | Luna Medium | 1/10 | 11.65 | $2.44 | 4.78 |

The ranking is sorted by weighted quality, with lower cost as the tie-breaker. Weighted score per dollar naturally favors cheap models and must be read together with absolute quality and stability.

## Interpretation

- **Sol Medium remains the strongest default.** It passed every task except task 07. Sol High passed the exact same tasks at about 34% higher cost.
- **Sol Low is promising but volatile.** Its previous valid pass counts were 7, 3, 4, 3, and 5, so one 8/10 result is not enough to make it the default.
- **Luna Max is specialized rather than generally superior.** It was the only tier to pass task 07, which lifts its weighted score despite only 6/10.
- **Max and XHigh again failed to improve monotonically.** Sol Max and Sol XHigh both scored 6/10 at much higher cost than Medium.
- **Luna Medium is no longer recommended**, after scoring 1/10.

## Batch status

The batch produced 57 passes out of 90. That is about 16% above the July 13 anomalous batch and only about 6.6% below the July 13 morning valid batch. Total estimated cost was about $204.59 and total tokens about 336.1M, both substantially above the prior valid morning batch.

Because quality did not fall by the 15% required by the project's anomaly rule, this is recorded as a **valid batch with a high-consumption warning**, not as an anomalous batch.

## Final usage ladder

```text
Low-cost and retryable: Terra Medium
Higher success but volatile: Sol Low (watchlist)
Daily development and small-project bug review: Sol Medium
Special long-chain or task-07-like work: consider Luna Max
Highest tiers: use only after Medium fails and project-specific evidence supports the upgrade
```

[Task matrix CSV](../data/history/task_matrices.csv) · [Aggregate history CSV](../data/history/runs.csv)