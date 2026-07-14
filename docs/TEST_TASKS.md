# Benchmark Task Coverage

The tracked benchmark uses ten fixed repository-level engineering tasks surfaced by Codex Radar. The short descriptions below are community transcriptions intended for analysis and navigation; consult the source site for the authoritative task wording.

**Latest rate snapshot:** `2026-07-14-1434`

| ID | Short description | Historical pass rate | Interpretation |
|---:|---|---:|---|
| 01 | Ordered-map JSONPath API | 78.92% (262/332) | Relatively easy |
| 02 | Module loading and cache behavior | 79.22% (263/332) | Relatively easy |
| 03 | HTTPX multipart response parsing | 94.58% (314/332) | Easiest group |
| 04 | Bandit incremental cache controls | 39.16% (130/332) | Difficult |
| 05 | IPython session replay behavior | 36.45% (121/332) | Very difficult |
| 06 | ofetch origin-aware circuit breaker | 93.67% (311/332) | Easiest group |
| 07 | Wiki and Markdown link conversion | 16.57% (55/332) | Hardest observed task |
| 08 | CSS lexer abbreviation conversion | 49.40% (164/332) | Medium difficulty |
| 09 | fd deterministic multi-key sorting | 37.65% (125/332) | Difficult |
| 10 | Stylesheet selector structure | 62.24% (206/331) | Medium-easy |

## What the set measures well

- repository exploration;
- multi-file implementation;
- integration with existing tests;
- maintaining compatibility with an established codebase;
- medium- to long-horizon agent execution.

## What the set does not measure well

- visual design and frontend aesthetics;
- natural-language writing;
- code review without implementation;
- tiny one-line bug fixes;
- private enterprise repositories;
- long conversational analysis;
- project management or requirements discovery.

## Task-family bias

Task 07 has an unusually low global pass rate but has sometimes been passed disproportionately by a specific model family or effort tier. This may represent genuine specialization, training overlap, implementation preference, or stochastic trajectory effects. The soft inverse weighting rewards the task while limiting its maximum influence.

## Updating the task table

When historical pass rates change:

1. create a new weight snapshot;
2. do not overwrite prior snapshots silently;
3. retain the pass rate used for every published report;
4. compare recommendation sensitivity before changing the default formula;
5. preserve source inconsistencies rather than guessing missing task outcomes.

Data attribution: 数据来自 Codex 雷达 codexradar.com
