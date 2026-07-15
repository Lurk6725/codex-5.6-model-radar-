# Benchmark Task Coverage

The tracked benchmark uses ten fixed repository-level engineering tasks surfaced by Codex Radar. The short descriptions below are community transcriptions intended for analysis and navigation; consult the source site for the authoritative wording.

**Latest rate snapshot:** `2026-07-15-1722`

| ID | Short description | Historical pass rate | Interpretation |
|---:|---|---:|---|
| 01 | Ordered-map JSONPath API | 78.86% (276/350) | Relatively easy |
| 02 | Module loading and cache behavior | 79.71% (279/350) | Relatively easy |
| 03 | HTTPX multipart response parsing | 94.29% (330/350) | Easiest group |
| 04 | Bandit incremental cache controls | 39.71% (139/350) | Difficult |
| 05 | IPython session replay behavior | 38.29% (134/350) | Very difficult |
| 06 | ofetch origin-aware circuit breaker | 94.00% (329/350) | Easiest group |
| 07 | Wiki and Markdown link conversion | 16.86% (59/350) | Hardest observed task |
| 08 | CSS lexer abbreviation conversion | 50.29% (176/350) | Medium difficulty |
| 09 | fd deterministic multi-key sorting | 40.29% (141/350) | Difficult |
| 10 | Stylesheet selector structure | 61.32% (214/349) | Medium-easy |

## What the set measures well

- repository exploration;
- multi-file implementation;
- integration with existing tests;
- compatibility with an established codebase;
- medium- to long-horizon agent execution.

## What the set does not measure well

- visual design and frontend aesthetics;
- natural-language writing;
- code review without implementation;
- tiny one-line bug fixes;
- private enterprise repositories;
- long conversational analysis;
- requirements discovery and project management.

## Task-family bias

Task 07 has the lowest global pass rate and has sometimes been passed disproportionately by particular model families. This may represent genuine specialization, training overlap, implementation preference, or stochastic trajectory effects. Soft inverse weighting rewards the task while limiting its influence.

The July 15 afternoon batch illustrates this clearly: Luna Max was the only tier to pass task 07 and therefore gained a substantial weighted-score advantage. Task-weighted rankings should be read as performance on this fixed task set, not universal capability.

## Updating the task table

When historical pass rates change:

1. create a new weight snapshot;
2. do not overwrite prior report snapshots silently;
3. retain the pass rate used for every published report;
4. compare recommendation sensitivity before changing the default formula.

Data attribution: 数据来自 Codex 雷达 codexradar.com
