# Model Recommendation Framework

Recommendations are provisional and should change only when several valid batches support the change. The current ladder reflects data through `2026-07-15-am`.

## Current recommendation ladder

### 1. Low-cost, retryable work

Use **Sol Low** when failure is inexpensive and retrying or escalating is acceptable.

Current caution: after two 8/10 rounds, Low fell to 6/10 on July 15. It remains useful for mechanical work, but should not be described as consistently reliable.

Typical work:

- formatting and renaming;
- documentation edits;
- small, clearly specified changes;
- executing an approved plan;
- cheap first attempts before escalation.

### 2. General daily development

Use **Sol Medium** as the default starting point.

Reasons:

- it reached 9/10 and 82.98 weighted points in the latest batch;
- it remains substantially cheaper than XHigh and Max;
- its multi-round history is stronger and more stable than Low;
- higher reasoning tiers have not shown monotonic gains.

Typical work:

- multi-file feature implementation;
- focused bug fixing;
- small-project bug review;
- moderate refactoring;
- repository exploration followed by implementation.

### 3. High-value difficult work

Start with **Sol Medium**. If it fails and the task is valuable enough to justify a large quota increase, try **Sol XHigh** next.

XHigh reached 10/10 in `2026-07-15-am`, including the hardest task 07, at lower cost than Sol Max. This is strong current evidence, but still only one perfect batch; its long-run median remains closer to seven tasks.

### 4. Specialist route

Consider **Terra Max** for work resembling task 07 or for long-running background execution where its family-specific task profile is relevant.

In the latest batch, Terra Max reached 8/10 and 79.93 weighted points while passing task 07. This is a specialist signal, not evidence that it universally beats Sol Medium.

### 5. Max is not an automatic upgrade

Do not select **Sol Max** solely because it is the highest reasoning label.

In `2026-07-15-am`, Sol Max and Sol High passed exactly the same tasks and both scored 74.06, while Max cost $60.10 and High cost $23.50. Max should be used only when project-specific evidence shows a benefit or when cheaper tiers have already failed.

## Decision table

| Priority | Suggested tier | Upgrade condition |
|---|---|---|
| Lowest cost | Sol Low | Failure is cheap and retryable |
| Daily balance | Sol Medium | Default for important normal work |
| Difficult escalation | Sol XHigh | Medium failed and the task value justifies higher quota |
| Task-07-like specialist work | Terra Max | Task profile or private evidence supports it |
| Highest label | Sol Max | Only with project-specific evidence; never automatic |

## Why weighted score per dollar is not enough

Cheap tiers can lead the efficiency table while passing too few tasks. Apply an absolute quality threshold before using cost efficiency as a recommendation signal. For important work, a tier below roughly 60 weighted points should not become the default solely because it is inexpensive.

## Prompt-scope controls

For narrow tasks, add explicit scope controls:

```text
Do not create sub-agents.
Read only files required for this task.
Do not redesign the approved plan.
Run only tests directly related to the change.
Record unrelated issues instead of fixing them.
Stop once the acceptance criteria pass.
Ask before expanding scope or changing architecture.
```

## When recommendations should change

A default tier should change only when at least one of these holds:

1. three consecutive valid batches show clear dominance;
2. the five-run median changes materially;
3. a cost-quality Pareto relationship persists across multiple batches;
4. an official model or Codex configuration change explains a structural shift;
5. project-specific private benchmarks consistently disagree with the public set.
