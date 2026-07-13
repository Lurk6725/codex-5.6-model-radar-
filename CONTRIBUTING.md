# Contributing

Contributions that improve reproducibility, data quality, or statistical interpretation are welcome.

## Adding a benchmark batch

1. Confirm that the source permits the intended use.
2. Record the exact source URL and timestamp.
3. Preserve the source's model name and reasoning effort.
4. Add aggregate data to `data/history/runs.csv`.
5. Add task-level outcomes when available using the schema in `data/schema/task_results.example.csv`.
6. Mark rounded or manually transcribed values clearly in `provenance`.
7. Run the test suite and report generator.
8. Update `CHANGELOG.md` when a correction or methodology change affects rankings.

## Data review checklist

- [ ] Batch ID is unique.
- [ ] Pass count equals the sum of valid task outcomes.
- [ ] Raw IQ equals `15 × passed` for the ten-task source display.
- [ ] Token components are non-negative and internally plausible.
- [ ] Estimated cost is copied, not silently recomputed over the source field.
- [ ] Weight snapshot is identified.
- [ ] Anomaly state and reliability weight are justified.
- [ ] Source attribution is present.

## Methodology changes

A methodology PR should include:

- the proposed formula;
- the problem it solves;
- a comparison against the existing formula on historical data;
- sensitivity analysis;
- expected effect on recommendations;
- a migration plan that keeps older reports reproducible.

Do not change historical scores in place merely because current task weights changed. Recompute into a new derived version or preserve the original weight snapshot.

## Recommendation changes

A model should not become the default based on a single batch. Prefer one of these evidence standards:

- three consecutive valid batches;
- a material five-run median change;
- persistent Pareto dominance;
- a documented official configuration change;
- repeated project-specific evidence supplied with a reproducible task set.

## Pull requests

Keep data imports separate from methodology changes when practical. This makes it easier to review whether a ranking changed because of new evidence or a new formula.
