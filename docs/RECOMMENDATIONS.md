# Model Recommendation Framework

Recommendations are provisional and should change only when several valid batches support the change.

## Current recommendation ladder

### 1. Mechanical, low-risk, retryable tasks

Use **Luna Medium** or **Terra Medium** only when recent rolling stability is acceptable.

Typical work:

- documentation edits;
- renaming and formatting;
- small test additions;
- a clearly specified single-file change;
- executing an already approved plan.

Do not infer reliability from quota efficiency alone. These tiers have historically produced low absolute pass counts in some batches.

### 2. General daily development

Use **Sol Medium** as the default starting point.

Reasons:

- the largest useful history sample among the evaluated mid/high tiers;
- recent results generally cluster around seven successful tasks out of ten, with occasional stronger and weaker batches;
- substantially lower cost than High, XHigh, and Max;
- higher reasoning tiers have not shown monotonic gains.

Typical work:

- multi-file feature implementation;
- bug fixing;
- moderate refactoring;
- test-driven changes;
- repository exploration followed by implementation.

### 3. Difficult work, quota-sensitive, background execution acceptable

Use **Luna Max** as an experimental high-difficulty value tier.

It has shown strong rolling pass counts at a lower estimated cost than flagship Sol tiers, but often uses far more tokens and wall time. It is best when waiting is acceptable and quota efficiency matters more than interactive speed.

### 4. Maximum-capability fallback

Use **Sol Max** only when:

- a cheaper tier has already failed;
- the task has unusually high value;
- one more successful task is worth a large quota increase;
- maximum demonstrated capability matters more than consistency or cost.

Sol Max has achieved the highest observed single-batch ceiling, but it has also shown large batch-to-batch variance.

## Why High and XHigh are not automatic upgrades

Increasing reasoning effort can:

- explore more alternatives;
- run more tests;
- spend more time validating;
- also overthink, expand scope, or follow an unproductive path for longer.

A tier should be promoted only when rolling data show a meaningful success-rate gain that justifies cost and latency. One successful batch is not enough.

## Decision table

| Priority | Suggested tier | Upgrade condition |
|---|---|---|
| Lowest cost | Luna Medium / Terra Medium | Failure is inexpensive |
| Daily balance | Sol Medium | Default for important normal work |
| Difficult and quota-sensitive | Luna Max | Long background execution is acceptable |
| Fast high-effort exploration | Sol High or XHigh only if project-specific evidence supports it | Measured advantage in your repository |
| Highest possible ceiling | Sol Max | Cheaper tiers failed or failure cost is very high |

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
