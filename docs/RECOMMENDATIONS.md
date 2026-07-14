# Model Recommendation Framework

Recommendations are provisional and should change only when several valid batches support the change. The current ladder reflects data through `2026-07-14-pm`.

## Current recommendation ladder

### 1. Mechanical, low-risk, retryable tasks

Use **Sol Low**.

Why:

- two consecutive 8/10 aggregate results on 2026-07-14;
- the latest task-weighted score is 78.94;
- the latest weighted score per estimated dollar is 8.46;
- it is substantially cheaper and faster than the higher Sol tiers.

Typical work:

- documentation edits;
- renaming and formatting;
- small test additions;
- clearly specified changes;
- executing an already approved plan.

Caveat: older Sol Low runs include 3/10 and 4/10 results. Use it where retrying or escalating is inexpensive.

### 2. General daily development and small-project bug review

Use **Sol Medium** as the default starting point.

Reasons:

- the largest useful history sample among the evaluated mid/high Sol tiers;
- lower cost than High, XHigh, and Max;
- higher reasoning tiers have not shown monotonic gains;
- in the latest aggregate, Medium tied High and XHigh at 7/10 while costing much less.

The 2026-07-14 PM source has a data-quality warning: the aggregate/API reports Medium as 7/10, while the public task list contains six explicit passes. This prevents a unique task-weighted score for that run, but it does not change the aggregate cost advantage over High and XHigh.

Typical work:

- multi-file feature implementation;
- bug fixing and user-experience review;
- moderate refactoring;
- test-driven changes;
- repository exploration followed by implementation.

### 3. Difficult work and maximum-capability fallback

Use **Sol Max** only after a cheaper tier fails or when failure is unusually costly.

The latest batch gives Sol Max the highest task-weighted score, 83.33, and it passed the highest-weight task 07. However, it cost about $49.90 and achieved only 1.67 weighted points per estimated dollar.

Use it when:

- Sol Medium or Sol Low already failed;
- the task has unusually high value;
- passing one additional difficult task justifies a large quota increase;
- maximum demonstrated capability matters more than latency or cost.

### 4. Tiers not recommended as defaults

- **Sol XHigh:** same latest task bitmap as High at higher cost; aggregate score also ties Medium.
- **Sol High:** can be useful only with project-specific evidence; it is not an automatic upgrade from Medium.
- **Terra Max:** reasonable aggregate quality but expensive for its weighted result.
- **Terra High:** latest result is 3/10; only one observed High-tier batch.
- **Luna Max:** high token and wall-time use without a current quality advantage.
- **Luna High:** cheap and 5/10 in its first observed batch, but insufficient history for a default recommendation.

## Decision table

| Priority | Suggested tier | Upgrade condition |
|---|---|---|
| Lowest-cost useful attempt | **Sol Low** | Failure is inexpensive and retrying is acceptable |
| Daily balance | **Sol Medium** | Default for important normal work and bug review |
| Maximum-capability fallback | **Sol Max** | Medium/Low failed or failure cost is very high |
| Project-specific alternative | High, XHigh, Terra, or Luna tiers | Only after repository-specific evidence shows an advantage |

## Prompt-scope controls for quota stability

For narrowly scoped tasks, consider adding:

```text
Do not create sub-agents.
Read only files required for this task.
Do not redesign the approved plan.
Run only tests directly related to the change.
Record unrelated issues instead of fixing them.
Stop immediately once the acceptance criteria pass.
Ask before expanding scope or changing architecture.
```

These controls cannot fix a metering issue, but they can reduce unnecessary agent expansion.

## When recommendations should change

A default tier should change only when at least one of these holds:

1. three consecutive valid batches show clear dominance;
2. the five-run median changes materially;
3. a cost-quality Pareto relationship persists across multiple batches;
4. an official model or Codex configuration change explains a structural shift;
5. project-specific private benchmarks consistently disagree with the public set.

A source inconsistency must be recorded rather than resolved by guessing. Exact task-weighted recommendations should wait for a corrected task matrix when aggregate and per-task totals conflict.
