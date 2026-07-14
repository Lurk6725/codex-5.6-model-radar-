# Latest Analysis Report — English

[Project home](../README.md) · [简体中文](latest.zh-CN.md) · [API monitor](api-latest.md) · [Historical data](history/README.md)

**Analysis cutoff:** 2026-07-14 09:00 Asia/Shanghai  
**Latest API snapshot:** `56b5641f66b1a557`  
**API source date:** `2026-07-14-am`  
**Latest available task matrix:** 2026-07-13 14:05

> This refresh contains model-level aggregates only. It does not include task outcomes, per-model run IDs, or full-versus-partial rerun markers. The report therefore updates real-time aggregate trends and recommendations without fabricating new difficulty-weighted scores.

## Model recommendations

| Work type | Current recommendation | Change |
|---|---|---|
| Mechanical, low-risk, retryable | **Terra Medium**; Sol Low is a stronger candidate pending repetition | Luna Medium fell to 1/10 and is no longer recommended |
| Daily development and small-project bug review | **Sol Medium** | Latest API result is 9/10 and it is cheaper and faster than Sol High |
| Difficult, quota-sensitive, long-running | **Try Sol Medium first; Luna Max moves to watchlist status** | Luna Max fell to 6/10, weakening its case as the clear quota-first choice |
| Maximum-capability fallback | **Sol Max, based on historical evidence** | Sol Max is absent from the latest API snapshot, so its current state is unknown |

### Main interpretation

- **The daily-default case for Sol Medium is stronger.** It ties Sol High at 9/10 while costing about 25% less, using about 21% fewer tokens, and finishing faster.
- **Sol High currently provides no clear upgrade value.** It is more expensive and slower at the same pass count.
- **Sol Low's 8/10 is notable, but one aggregate-only snapshot is not enough to make it a default.** The task mix is unknown.
- **Both Luna tiers weakened.** Luna Max moved from 7/10 to 6/10, while Luna Medium moved from 2/10 to 1/10.
- **Sol XHigh is currently one of the least attractive tiers.** It achieved only 6/10 while being the most expensive returned configuration.

## Latest API aggregate ranking

This table is sorted by pass count. `Raw score / $` divides the source score—15 points per passed task—by estimated cost. It is not the task-weighted efficiency metric.

| Rank | Model tier | Passed | Source score | Cost | Raw score / $ | Total tokens | Wall time |
|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | Sol High | 9/10 | 135 | $24.62 | 5.48 | 23.50M | 0.54h |
| 1 | **Sol Medium** | 9/10 | 135 | **$18.41** | **7.33** | **18.48M** | **0.46h** |
| 3 | Sol Low | 8/10 | 120 | $9.73 | 12.33 | 8.20M | 0.27h |
| 4 | Terra Max | 7/10 | 105 | $30.91 | 3.40 | 65.72M | 0.63h |
| 5 | Luna Max | 6/10 | 90 | $15.11 | 5.96 | 88.73M | 0.66h |
| 5 | Sol XHigh | 6/10 | 90 | $37.97 | 2.37 | 40.67M | 0.75h |
| 7 | Terra Medium | 5/10 | 75 | $5.18 | **14.48** | 8.01M | 0.39h |
| 8 | Luna Medium | 1/10 | 15 | $2.44 | 6.15 | 10.81M | 0.41h |

## Change from the preceding API snapshot

The preceding snapshot contained the same eight model tiers and represented the 2026-07-13-pm aggregate state.

| Model | Pass change | Cost change | Interpretation |
|---|---:|---:|---|
| Sol High | 6 → **9** | $26.78 → $24.62 | Strong recovery, but no advantage over Medium |
| Sol Medium | 5 → **9** | $16.14 → $18.41 | Strongest positive signal; reinforces default status |
| Sol Low | 6 → **8** | $9.37 → $9.73 | Promising, but requires repetition |
| Terra Max | 6 → **7** | $32.21 → $30.91 | Modest improvement, still expensive |
| Terra Medium | 5 → 5 | $5.96 → $5.18 | Same quality at lower cost |
| Luna Max | 7 → **6** | $18.94 → $15.11 | Cheaper but weaker |
| Sol XHigh | 7 → **6** | $33.63 → $37.97 | More expensive and less successful |
| Luna Medium | 2 → **1** | $2.43 → $2.44 | Not recommended in the current state |

Across the eight returned tiers, total passes rose from 44 to 51, about +15.9%. Aggregate estimated cost was almost flat, falling from roughly $145.46 to $144.37; total token use fell about 11%, and total wall time fell about 28%. This is a broad recovery signal from the July 13 anomalous state.

## Data confidence and limitations

1. The API returns eight tiers and **does not include Sol Max**, so this cannot be called a complete nine-tier batch.
2. The API does not expose task outcomes, so we cannot tell which difficult tasks produced the 9/10 and 8/10 results.
3. There are no per-model run IDs, update timestamps, or partial-rerun markers. We can state that aggregate values changed, not prove that every model was independently rerun.
4. The snapshot's `source_date` is `2026-07-14-am`, but `observed_at` remains `2026-07-13T22:08:07+08:00`, creating a source timestamp inconsistency.

The refresh is therefore a **strong real-time aggregate signal**, but it does not replace the task-weighted ranking.

## Latest computable task weights

The latest task matrix remains `2026-07-13-1405`. The formula is:

```text
raw_difficulty_i = 1 / sqrt(historical_pass_rate_i)
weight_i = 100 * raw_difficulty_i / sum(raw_difficulty)
weighted_score = sum(weight_i * passed_i)
```

| Task | Historical pass rate | Weight /100 |
|---:|---:|---:|
| 01 | 79% | 7.76 |
| 02 | 80% | 7.71 |
| 03 | 95% | 7.09 |
| 04 | 38% | 11.15 |
| 05 | 34% | 11.81 |
| 06 | 94% | 7.14 |
| 07 | 16% | **17.11** |
| 08 | 49% | 9.91 |
| 09 | 35% | 11.70 |
| 10 | 64% | 8.62 |
|  | **Total** | **100.00** |

The latest computable task-weighted ranking remains available through the [historical report](history/README.md) and project home page; it is not recomputed from this aggregate API snapshot.

## Final conclusion

The current usage ladder is:

```text
Low-cost mechanical work: Terra Medium
Daily development / small-project bug review: Sol Medium
Difficult work: try Sol Medium first; Luna Max is a long-running watchlist option
Final fallback: Sol Max, pending refreshed data
```

This refresh does not overturn the Sol Medium recommendation. It strengthens the broader finding that moving directly from Medium to High, XHigh, or Max often provides no stable benefit without project-specific evidence.
