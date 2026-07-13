# Benchmark Task Coverage

The tracked benchmark uses ten fixed repository-level engineering tasks surfaced by Codex Radar. The short descriptions below are community transcriptions intended for analysis and navigation; consult the source site for the authoritative task wording.

| ID | Short description | Recent historical pass rate | Interpretation |
|---:|---|---:|---|
| 01 | Ordered-map JSONPath API | 79% | Relatively easy |
| 02 | Module loading and cache behavior | 80% | Relatively easy |
| 03 | HTTPX multipart response parsing | 95% | Easiest group |
| 04 | Bandit incremental cache controls | 38% | Difficult |
| 05 | IPython session replay behavior | 34% | Very difficult |
| 06 | ofetch origin-aware circuit breaker | 94% | Easiest group |
| 07 | Wiki and Markdown link conversion | 16% | Hardest observed task |
| 08 | CSS lexer abbreviation conversion | 49% | Medium difficulty |
| 09 | fd deterministic multi-key sorting | 35% | Very difficult |
| 10 | Stylesheet selector structure | 64% | Medium-easy |

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

Task 07 has an unusually low global pass rate but has sometimes been passed disproportionately by a specific model family. This may represent genuine specialization, training overlap, implementation preference, or stochastic trajectory effects. The soft inverse weighting rewards the task while limiting its maximum influence.

## Updating the task table

When historical pass rates change:

1. create a new weight snapshot;
2. do not overwrite prior snapshots silently;
3. retain the pass rate used for every published report;
4. compare recommendation sensitivity before changing the default formula.

Data attribution: 数据来自 Codex 雷达 codexradar.com
