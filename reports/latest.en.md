# Latest Analysis Report — English

[Project home](../README.md) · [简体中文](latest.zh-CN.md) · [API monitor](api-latest.md) · [Historical data](history/README.md)

**Analysis cutoff:** 2026-07-14 14:34 Asia/Shanghai  
**Batch:** `2026-07-14-pm`  
**API snapshot:** `e0ac3269c1279e22`  
**Sources:** authorized Codex Radar API plus the public task matrix

> The API provides precise aggregate data for eight tiers; the public page supplies Sol Max, nine-tier task outcomes, and updated historical pass rates. The source reports Sol Medium as 7/10, but its public per-task list contains only six explicit passes. This report therefore preserves the inconsistency and reports a weighted-score range instead of guessing the missing task.

## Model recommendations

| Work type | Current recommendation | Conclusion |
|---|---|---|
| Mechanical, low-risk, retryable | **Sol Low** | Two consecutive 8/10 runs; weighted score 78.94 and weighted/$ 8.46, though older results remain volatile |
| Daily development and small-project bug review | **Sol Medium** | Aggregate 7/10, tying High and XHigh while costing about 38% and 55% less; confidence is medium due to the task-list mismatch |
| Difficult work and final fallback | **Sol Max** | Highest weighted score at 83.33 and passed task 07; its $49.90 cost makes it a fallback, not a default |
| Not recommended as defaults | Terra High, Luna High, Luna Max, Sol XHigh | Current absolute quality, cost, or stability is not competitive |

## Latest task weights

```text
raw_difficulty_i = 1 / sqrt(historical_pass_rate_i)
weight_i = 100 * raw_difficulty_i / sum(raw_difficulty)
weighted_score = sum(weight_i * passed_i)
```

**Weight snapshot:** `2026-07-14-1434`

| Task | Historical pass rate | Weight /100 |
|---:|---:|---:|
| 01 | 78.92% (262/332) | 7.85 |
| 02 | 79.22% (263/332) | 7.83 |
| 03 | 94.58% (314/332) | 7.17 |
| 04 | 39.16% (130/332) | 11.14 |
| 05 | 36.45% (121/332) | 11.55 |
| 06 | 93.67% (311/332) | 7.20 |
| 07 | 16.57% (55/332) | **17.13** |
| 08 | 49.40% (164/332) | 9.92 |
| 09 | 37.65% (125/332) | 11.36 |
| 10 | 62.24% (206/331) | 8.84 |
|  |  | **100.00** |

## Latest task-weighted ranking

| Rank | Model tier | Passed | Weighted /100 | Cost | Weighted/$ |
|---:|---|---:|---:|---:|---:|
| 1 | **Sol Max** | 8/10 | **83.33** | $49.90 | 1.67 |
| 2 | **Sol Low** | 8/10 | **78.94** | $9.33 | **8.46** |
| 3–5* | **Sol Medium** | 7/10 | **66.18–75.48** | $16.85 | 3.93–4.48 |
| 3–5 | Sol High | 7/10 | 66.20 | $27.03 | 2.45 |
| 3–5 | Sol XHigh | 7/10 | 66.20 | $37.05 | 1.79 |
| 6 | Terra Max | 7/10 | 62.48 | $34.91 | 1.79 |
| 7 | Luna Max | 6/10 | 52.97 | $16.33 | 3.24 |
| 8 | Luna High | 5/10 | 41.42 | $5.88 | 7.05 |
| 9 | Terra High | 3/10 | 22.21 | $9.14 | 2.43 |

\* The public per-task list explicitly shows Sol Medium passing tasks 03, 04, 05, 06, 08, and 09—six tasks—while the API and aggregate table report 7/10. If a seventh task was passed, it must be one of the listed failures 01, 02, 07, or 10, producing a weighted score between 66.18 and 75.48. The machine-readable matrix preserves the six-pass bitmap and seven-pass aggregate with a source-mismatch marker.

## Most informative findings

### Sol Low moves from watchlist to low-cost recommendation

Sol Low reached 8/10 in both morning and afternoon runs. This time it passed the highest-weight task 07 and task 10, producing 78.94 at only $9.33. Its older history includes 3/10 and 4/10 results, so it remains unsuitable for high-value, non-retryable work, but it is now the preferred cheap tier for mechanical and low-risk tasks.

### Sol Max restores its maximum-capability case

Sol Max recovered from 6/10 to 8/10, while cost fell from about $60.20 to $49.90. It passed task 07 and achieved the highest weighted score, 83.33. This restores its value as a final fallback, but its weighted/$ of 1.67 is too low for routine use.

### Sol Medium remains the daily default, with a data warning

The source aggregate reports Medium, High, and XHigh at 7/10. Medium costs $16.85 versus $27.03 for High and $37.05 for XHigh, so it remains the best default even without relying on the task structure. However, the task-list inconsistency prevents a precise weighted score for this run.

### High and XHigh offer no upgrade value

High and XHigh have identical public task bitmaps and both score 66.20. High is about 27% cheaper than XHigh. Upgrading from Medium to XHigh has no support in this batch, and High should only be used when project-specific reproduction shows Medium fails.

### Terra and Luna changed active effort tiers

Terra Medium and Luna Medium from the morning batch were replaced by Terra High and Luna High in the afternoon. These are not like-for-like trend comparisons. Terra High scored 3/10; Luna High scored 5/10 and is cheap, but has only one observed run. Neither is promoted to a default recommendation.

## Change from the morning batch

| Model | Pass change | Cost change | Interpretation |
|---|---:|---:|---|
| Sol Max | 6 → **8** | $60.20 → $49.90 | Strong recovery; maximum-capability fallback restored |
| Sol XHigh | 6 → **7** | $37.97 → $37.05 | Slight recovery, still poor value |
| Sol High | 9 → **7** | $24.62 → $27.03 | Lower quality and higher cost |
| Sol Medium | 9 → **7** | $18.41 → $16.85 | Lower aggregate result, but still the cheapest equal-score Sol tier |
| Sol Low | 8 → **8** | $9.73 → $9.33 | Consecutive stability strengthens the low-cost recommendation |
| Terra Max | 7 → 7 | $30.91 → $34.91 | Same pass count at higher cost |
| Luna Max | 6 → 6 | $15.11 → $16.33 | Same pass count at higher cost |

Terra High and Luna High are new active tiers in this batch and should not be directly compared with the morning Medium tiers.

## Batch status

Across nine tiers:

- passes: **58/90**;
- estimated cost: about **$206.40**;
- total tokens: about **363.7M**;
- versus the morning batch: quality +1.8%, cost +0.9%, tokens +8.2%.

Quality did not decline and cost did not spike enough to meet the anomaly rule. The batch is recorded as:

> **Valid, with high-consumption and Sol Medium source-consistency warnings.**

## Final recommendation

```text
Low-cost, retryable work: Sol Low
Daily development and small-project bug review: Sol Medium
High-value difficult work: try Medium first, then escalate to Sol Max
Avoid as defaults: Sol XHigh, Terra High, Luna High, Luna Max
```

Machine-readable task outcomes are stored in [`data/history/task_matrices.csv`](../data/history/task_matrices.csv), and aggregate history is stored in [`data/history/runs.csv`](../data/history/runs.csv).
