# Latest Analysis Report — English

[Project home](../README.md) · [简体中文](latest.zh-CN.md) · [API monitor](api-latest.md) · [Historical data](history/README.md)

**Analysis cutoff:** 2026-07-15 08:03 Asia/Shanghai  
**Batch:** `2026-07-15-am`  
**Weight snapshot:** `2026-07-15-0803`  
**Source:** Codex Radar public aggregate table, task matrix, and historical pass counts

> At analysis time, the authorized API history had not yet archived this batch. Cost, token, and wall-time fields therefore use the rounded values displayed on the public page. Task outcomes and historical pass counts come from the public matrix. More precise API aggregates may later replace only those rounded fields without changing the task-weighted result.

## Model recommendations

| Work type | Current recommendation | Rationale |
|---|---|---|
| Low-cost and retryable | **Sol Low** | It fell to 6/10, so confidence in the cheap tier is back to medium |
| Daily development and small-project bug review | **Sol Medium** | 9/10, 82.98 weighted points, and $17.80 remain the best quality/cost/stability balance |
| High-value difficult work | **Start with Sol Medium, then escalate to Sol XHigh** | XHigh reached 10/10, but its long-run median remains below this one perfect batch |
| Task-07-like specialization | **Terra Max as a specialist candidate** | It reached 8/10 and passed the hardest task at lower cost than Sol XHigh and Sol Max |
| Do not upgrade automatically | Sol Max and Sol High | They had identical task outcomes, while High cost about 39% as much as Max |

The main recommendation does not change: **Sol Medium remains the daily default.** The new evidence strengthens Sol XHigh as an escalation tier after failure, not as a permanent default.

## Latest task-difficulty weights

| Task | Historical pass rate | Weight /100 |
|---:|---:|---:|
| 01 | 78.59% (268/341) | 7.92 |
| 02 | 79.77% (272/341) | 7.86 |
| 03 | 94.43% (322/341) | 7.23 |
| 04 | 39.59% (135/341) | 11.16 |
| 05 | 37.54% (128/341) | 11.46 |
| 06 | 93.84% (320/341) | 7.25 |
| 07 | 17.01% (58/341) | **17.02** |
| 08 | 49.85% (170/341) | 9.94 |
| 09 | 39.00% (133/341) | 11.24 |
| 10 | 62.06% (211/340) | 8.91 |
|  |  | **100.00** |

## Latest task-weighted ranking

| Rank | Model tier | Passed | Weighted /100 | Cost | Weighted/$ |
|---:|---|---:|---:|---:|---:|
| 1 | **Sol XHigh** | 10/10 | **100.00** | $34.80 | 2.87 |
| 2 | **Sol Medium** | 9/10 | **82.98** | $17.80 | **4.66** |
| 3 | Terra Max | 8/10 | 79.93 | $28.30 | 2.82 |
| 4 | Sol High | 8/10 | 74.06 | $23.50 | 3.15 |
| 5 | Sol Max | 8/10 | 74.06 | $60.10 | 1.23 |
| 6 | Sol Low | 6/10 | 59.73 | $8.80 | 6.79 |
| 7 | Luna Max | 6/10 | 54.98 | $17.10 | 3.22 |
| 8 | Terra High | 6/10 | 50.41 | $9.20 | 5.48 |
| 9 | Luna High | 5/10 | 46.42 | $6.30 | **7.37** |

The ranking is ordered by weighted score, with lower cost breaking ties. Weighted score per dollar favors cheap tiers with lower absolute reliability and must not be used without an absolute-quality threshold.

## Most informative results

### Sol XHigh reached 10/10

XHigh passed all ten tasks, including task 07, and reached 100 weighted points. At $34.80 it was also far cheaper than Sol Max. This makes it the strongest current escalation option after Medium fails. However, XHigh has usually landed around 6–8/10 in prior rounds, so the perfect result still needs two or three additional batches before becoming a structural conclusion.

### Sol Medium remains the daily default

Medium passed 9/10 and missed only task 07. At 82.98 weighted points and $17.80, it retained a large cost advantage over XHigh and delivered better task coverage than High. It remains the best starting tier for daily coding, focused bug review, and normal repository work.

### Sol Max was strictly dominated by Sol High

Max and High passed exactly the same tasks—01 through 06, 08, and 09—and both scored 74.06. High cost $23.50 versus Max at $60.10. This round provides no evidence for upgrading from High to Max.

### Terra Max showed specialist value

Terra Max passed task 07 and scored 79.93, above Sol High and Sol Max despite the same raw 8/10 pass count. It is a plausible specialist option for task-07-like work or long background execution, not a universal replacement for Medium.

### Sol Low lost its recent stability claim

After two consecutive 8/10 rounds, Sol Low fell to 6/10. It remains inexpensive and useful for retryable work, but should no longer be described as continuously stable and is unsuitable for important one-shot tasks.

### Luna High's efficiency lead is misleading

Luna High ranked first on weighted score per dollar at 7.37, but its absolute weighted score was only 46.42 with 5/10 tasks passed. This is another example of why cost efficiency requires a minimum quality threshold.

## Change from the previous batch

| Metric | July 14 PM | July 15 AM | Change |
|---|---:|---:|---:|
| Total passes | 58/90 | **66/90** | **+13.8%** |
| Total cost | about $206.40 | about **$205.89** | essentially flat |
| Total tokens | about 363.7M | about **366.7M** | +0.8% |

Quality improved materially without a corresponding cost or token spike, so this batch does not meet the anomaly rule.

## Batch status

> **Valid batch.** No reliability down-weight is applied. Aggregate cost, token, and wall-time values remain rounded until the authorized API archives a more precise snapshot.

## Practical route

```text
Low-cost, retryable work: Sol Low; escalate important tasks
Daily development and small-project bug review: Sol Medium
High-value difficult work: try Sol XHigh after Medium fails
Task-07-like specialist work: consider Terra Max
Do not choose Max automatically; it was much less cost-effective than High
```

Machine-readable data:

- [`data/history/batches/2026-07-15-am.csv`](../data/history/batches/2026-07-15-am.csv)
- [`data/history/task_matrices.csv`](../data/history/task_matrices.csv)
- [`data/weights/task_weights.csv`](../data/weights/task_weights.csv)
