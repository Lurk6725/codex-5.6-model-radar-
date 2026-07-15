# Model Recommendation Framework

Recommendations are provisional and should change only when several valid batches support the change. The current ladder reflects data through `2026-07-15-pm`.

## Current recommendation ladder

### 1. Low-cost, retryable work

Use **Sol Low** when failure is inexpensive and retrying or escalating is acceptable.

It reached 8/10 in the latest batch and remains inexpensive, but prior 3/10 and 4/10 rounds prevent it from becoming the default for important one-shot work.

Typical work:

- formatting and renaming;
- documentation edits;
- small, clearly specified changes;
- executing an approved plan;
- cheap first attempts before escalation.

### 2. General daily development

Use **Sol Medium** as the default starting point, with **medium confidence** after the latest 6/10 round.

Reasons:

- its recent and long-run median remains near seven tasks;
- it is substantially cheaper than High, XHigh, and Max;
- its multi-round history is stronger than Low;
- it is generally easier to constrain than higher Sol reasoning tiers;
- one weak batch is not enough to replace the default.

Typical work:

- multi-file feature implementation;
- focused bug fixing;
- small-project bug review;
- moderate refactoring;
- repository exploration followed by implementation.

### 3. Difficult, quota-sensitive background work

Use **Luna Max** when long execution time and high token consumption are acceptable.

In `2026-07-15-pm`, Luna Max reached 9/10 and 90.08 weighted points, uniquely passed task 07, and cost about $16.30. Its main trade-offs are roughly four hours of wall time and about 91M tokens.

### 4. Escalation within the Sol family

If Sol Medium fails and the task should remain in the Sol family, prefer **Sol High** before XHigh or Max unless private project evidence says otherwise.

In the latest batch High and XHigh both reached 7/10, while High was cheaper and scored slightly higher. XHigh's morning 10/10 demonstrates ceiling, but the afternoon regression shows that one perfect batch is not stable evidence.

### 5. Max is not an automatic upgrade

Do not select **Sol Max** solely because it is the highest reasoning label.

In `2026-07-15-pm`, Sol Max reached only 6/10 and 54.61 weighted points at about $51.40. Multiple cheaper tiers produced higher quality.

## Decision table

| Priority | Suggested tier | Upgrade condition |
|---|---|---|
| Lowest cost | Sol Low | Failure is cheap and retryable |
| Daily balance | Sol Medium | Default for important normal work; confidence currently medium |
| Difficult background work | Luna Max | Long latency and token use are acceptable |
| Sol-family escalation | Sol High | Medium failed and staying within Sol matters |
| Higher Sol labels | XHigh or Max | Only with project-specific evidence; never automatic |

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
