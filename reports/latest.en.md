# Latest Analysis Report — English

[Project home](../README.md) · [简体中文](latest.zh-CN.md) · [API monitor](api-latest.md) · [Historical data](history/README.md)

**Analysis cutoff:** 2026-07-15 17:22 Asia/Shanghai  
**Batch:** `2026-07-15-pm`  
**Weight snapshot:** `2026-07-15-1722`  
**Source:** Codex Radar public aggregate table, task matrix, and historical pass counts

> The authorized API history had not yet archived this round. Cost, token, and wall-time fields therefore use the rounded values displayed on the public page; task-weighted scores come directly from the public matrix.

## Model recommendations

| Work type | Current recommendation | Rationale |
|---|---|---|
| Low-cost and retryable | **Sol Low** | 8/10 and 71.69 weighted points, but historical lows make it unsuitable for important one-shot work |
| Daily development and small-project bug review | **Sol Medium** | It fell to 6/10; its multi-run median, price, and scope discipline still support the default, with lower confidence |
| Difficult, quota-sensitive, background execution | **Luna Max** | 9/10, 90.08 weighted points, task 07 passed, and only $16.30 |
| Escalation within the Sol family | **Prefer Sol High** | High tied XHigh at 7/10 while costing less and scoring slightly higher; the morning XHigh 10/10 did not repeat |
| Do not upgrade automatically | Sol Max | 6/10, 54.61 weighted points, and $51.40 made it clearly dominated by cheaper tiers |

The main change is that **Luna Max returns as the preferred difficult-work value tier.** Sol XHigh's perfect morning result did not persist. Sol Medium remains the daily default, but confidence falls from high to medium after this weaker round.

## Latest task-difficulty weights

| Task | Historical pass rate | Weight /100 |
|---:|---:|---:|
| 01 | 78.86% (276/350) | 7.93 |
| 02 | 79.71% (279/350) | 7.88 |
| 03 | 94.29% (330/350) | 7.25 |
| 04 | 39.71% (139/350) | 11.17 |
| 05 | 38.29% (134/350) | 11.37 |
| 06 | 94.00% (329/350) | 7.26 |
| 07 | 16.86% (59/350) | **17.14** |
| 08 | 50.29% (176/350) | 9.92 |
| 09 | 40.29% (141/350) | 11.09 |
| 10 | 61.32% (214/349) | 8.99 |
|  |  | **100.00** |

## Latest task-weighted ranking

| Rank | Model tier | Passed | Weighted /100 | Cost | Weighted/$ |
|---:|---|---:|---:|---:|---:|
| 1 | **Luna Max** | 9/10 | **90.08** | $16.30 | **5.53** |
| 2 | **Sol Low** | 8/10 | **71.69** | $10.70 | **6.70** |
| 3 | Sol High | 7/10 | 64.44 | $25.00 | 2.58 |
| 4 | Terra Max | 7/10 | 62.78 | $34.00 | 1.85 |
| 5 | Sol XHigh | 7/10 | 62.50 | $32.60 | 1.92 |
| 6 | Sol Medium | 6/10 | 54.82 | $16.60 | 3.30 |
| 7 | Sol Max | 6/10 | 54.61 | $51.40 | 1.06 |
| 8 | Terra High | 5/10 | 44.85 | $9.30 | 4.82 |
| 9 | Luna High | 5/10 | 41.40 | $6.70 | 6.18 |

The ranking is ordered by weighted score. Weighted score per dollar favors cheap tiers with lower absolute reliability and must not be used without a minimum quality threshold.

## Most informative results

### Luna Max again leads difficult-work value

Luna Max passed 9/10, missing only task 08, and was the only tier to pass task 07. At $16.30 it produced 90.08 weighted points. Its trade-off remains latency and token use: about four hours and 91.0M tokens, so it is better suited to background work than interactive sessions.

### Sol XHigh's 10/10 did not repeat

XHigh fell from 10/10 in the morning to 7/10 and 62.50 weighted points. High also reached 7/10, but scored 64.44 at $25.00 versus XHigh at $32.60. The morning result demonstrated ceiling, not stable dominance.

### Sol Medium remains the default with lower confidence

Medium reached only 6/10 and 54.82 weighted points this round. It remains cheaper than High, XHigh, and Max, has a multi-run median near 7/10, and is less prone to scope expansion, so the daily default does not change yet. Important failures should escalate rather than repeatedly retrying Medium.

### Sol Low recovered its low-cost value

Low returned to 8/10 at $10.70 and 6.70 weighted points per dollar. It remains appropriate for clearly specified, retryable work, but historical 3/10 and 4/10 rounds prevent it from becoming the default for important tasks.

### Sol Max remains hard to justify

Max tied Medium at 6/10 with almost the same weighted score, while costing roughly 3.1 times as much. The current data still do not support treating Max as automatically stronger.

## Change from the morning batch

| Metric | July 15 AM | July 15 PM | Change |
|---|---:|---:|---:|
| Total passes | 66/90 | **60/90** | -9.1% |
| Total cost | about $205.89 | about **$202.58** | -1.6% |
| Total tokens | about 366.7M | about **360.7M** | -1.6% |

Quality declined, but not by the 15% anomaly threshold, and cost and tokens did not rise in the opposite direction.

## Batch status

> **Valid batch.** No anomaly down-weight is applied. Rounded aggregate fields may later be replaced by a more precise authorized API snapshot without changing the task matrix or weighted ranking.

## Practical route

```text
Low-cost, retryable work: Sol Low
Daily development and small-project bug review: Sol Medium, with lower confidence this round
Difficult, quota-sensitive background work: Luna Max
Sol-family escalation: prefer High; do not promote XHigh from one perfect morning result
Do not select Max automatically
```

Machine-readable data:

- [`data/history/batches/2026-07-15-pm.csv`](../data/history/batches/2026-07-15-pm.csv)
- [`data/history/task_matrices.csv`](../data/history/task_matrices.csv)
- [`data/weights/task_weights.csv`](../data/weights/task_weights.csv)
