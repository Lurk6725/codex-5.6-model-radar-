# Latest Analysis Report — English

[Project home](../README.md) · [简体中文](latest.zh-CN.md) · [Historical data](history/README.md)

**Analysis cutoff:** 2026-07-13 14:05 Asia/Shanghai  
**Primary source:** Codex Radar  
**Latest batch status:** anomalous; raw results retained with trend reliability weight `0.35`

> Source benchmark data comes from Codex Radar (`codexradar.com`).

## Model recommendations

The 14:05 batch combines lower aggregate quality with higher estimated cost and token activity, so it should not receive full weight when changing the long-term recommendation.

| Work type | Current recommendation | Rationale |
|---|---|---|
| Mechanical, low-risk, retryable | Luna Medium or Terra Medium | Check recent stability first |
| General daily development | **Sol Medium** | Best current balance across normal runs |
| Difficult, quota-sensitive, long-running | **Luna Max** | Strong multi-run results, but high latency and token use |
| Maximum-capability fallback | **Sol Max** | Highest observed ceiling, but also the highest cost and volatility |

High, XHigh, and Max do not reliably form a monotonic capability ladder. Upgrade only after the current tier fails or project-specific reproducible evidence shows a real benefit.

## Latest task-difficulty weights

**Weight snapshot:** `2026-07-13-1405`  
**Formula:** `weight_i ∝ 1 / sqrt(historical_pass_rate_i)`, normalized to 100.

| Task | Short description | Historical pass rate | Weight /100 | Difficulty note |
|---:|---|---:|---:|---|
| 01 | Ordered-map JSONPath API | 79% | 7.76 | Relatively easy |
| 02 | Module loading and cache behavior | 80% | 7.71 | Relatively easy |
| 03 | HTTPX multipart response parsing | 95% | 7.09 | One of the easiest |
| 04 | Bandit incremental cache controls | 38% | 11.15 | Difficult |
| 05 | IPython session replay behavior | 34% | 11.81 | Very difficult |
| 06 | ofetch origin-aware circuit breaker | 94% | 7.14 | One of the easiest |
| 07 | Wiki and Markdown link conversion | 16% | **17.11** | Most difficult |
| 08 | CSS lexer abbreviation conversion | 49% | 9.91 | Medium |
| 09 | fd deterministic multi-key sorting | 35% | 11.70 | Very difficult |
| 10 | Stylesheet selector structure | 64% | 8.62 | Medium-easy |
|  | **Total** |  | **100.00** |  |

Weight file: [`data/weights/task_weights.csv`](../data/weights/task_weights.csv)

## Latest observed weighted ranking

**Batch:** `2026-07-13-pm-anomaly` (14:05)  
**Caution:** this is the latest observation, but it is an anomalous batch and should not be treated as the long-term hierarchy.

| Rank | Model tier | Passed | Weighted /100 | Estimated cost | Weighted/$ |
|---:|---|---:|---:|---:|---:|
| 1 | Luna Max | 7/10 | **70.31** | $18.90 | 3.72 |
| 2 | Sol XHigh | 7/10 | 66.56 | $33.60 | 1.98 |
| 3 | Sol High | 6/10 | 59.47 | $26.80 | 2.22 |
| 4 | Terra Max | 6/10 | 56.60 | $32.20 | 1.76 |
| 5 | Sol Low | 6/10 | 53.21 | $9.40 | 5.66 |
| 6 | Terra Medium | 5/10 | 50.38 | $6.00 | **8.40** |
| 7 | Sol Max | 5/10 | 48.32 | $59.80 | 0.81 |
| 8 | Sol Medium | 5/10 | 45.50 | $16.10 | 2.83 |
| 9 | Luna Medium | 2/10 | 18.24 | $2.40 | 7.60 |

## Latest complete non-anomalous ranking

To prevent the anomalous batch from directly distorting recommendations, the latest complete valid batch `2026-07-13-am` (about 09:16) is shown alongside it:

| Rank | Model tier | Passed | Weighted /100 | Estimated cost | Weighted/$ |
|---:|---|---:|---:|---:|---:|
| 1 | Sol Max | 10/10 | **100.00** | $34.94 | 2.86 |
| 2 | Sol Medium | 9/10 | **82.81** | $8.23 | **10.06** |
| 3 | Luna Max | 8/10 | 74.35 | $14.35 | 5.18 |
| 4 | Sol High | 7/10 | 72.79 | $15.01 | 4.85 |
| 5 | Sol XHigh | 7/10 | 66.75 | $26.39 | 2.53 |
| 6 | Terra Max | 7/10 | 62.38 | $30.19 | 2.07 |
| 7 | Sol Low | 5/10 | 46.28 | $5.96 | 7.77 |
| 8 | Terra Medium | 4/10 | 33.71 | $6.17 | 5.46 |
| 8 | Luna Medium | 4/10 | 33.71 | $2.42 | **13.95** |

Weighted score per dollar naturally favors very cheap models even when their absolute capability is low, so it must be read together with pass count, weighted score, and rolling stability.

## Why the 14:05 batch is down-weighted

Relative to the preceding valid morning batch:

- aggregate passes fell by roughly one fifth;
- total estimated cost rose by more than 40%;
- aggregate token activity rose by more than 40%;
- several unrelated tiers simultaneously became less successful and more expensive.

The default anomaly rule is a quality drop of at least 15% combined with a cost or token increase of at least 30%. Both conditions were met, so the batch remains visible but receives only `0.35` trend weight.

## Stable interpretation

### Sol Medium remains the daily default

Sol Medium has one of the most useful continuous histories in the repository. Its normal-run center is around 7/10 and its cost is usually much lower than High, XHigh, and Max. The anomalous 5/10 run is important service-state evidence, but not enough to erase its long-term position by itself.

### Luna Max remains the quota-sensitive difficult-work route

Luna Max has produced strong multi-run pass counts at relatively low estimated cost, but it uses very large token volumes and long wall time. It is more suitable for background execution than interactive debugging.

### Sol Max is a ceiling fallback, not a default

Sol Max has produced a 10/10 public-summary result and also a 5/10, very expensive anomalous run. Max increases potential ceiling; it does not guarantee single-run reliability.

## Confidence

| Conclusion | Confidence |
|---|---|
| Sol Medium is the best general default | Moderate to high |
| Luna Max is a strong quota-sensitive difficult tier | Moderate |
| Sol Max has the highest observed single-run ceiling | Moderate |
| The 14:05 batch represents normal model capability | Low |
| One anomalous batch should change the default ladder | Very low |

## Historical records

[Browse every recorded batch through the history index](history/README.md). Machine-readable aggregate history is stored in [`data/history/runs.csv`](../data/history/runs.csv).
