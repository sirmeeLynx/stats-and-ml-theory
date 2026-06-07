---
sources:
  - video: "2.2.3 Basic Concepts of Hypothesis Testing"
    course_id: 141734
    item_id: 7718544
    duration: "13:35"
---

# Type I and Type II Errors

Because decisions are made from samples, hypothesis tests can make mistakes. The
lecture organizes these mistakes by combining the **true state of $H_0$** with the
**decision** we make. [→ 2.2.3 @ 08:25]

## The 2×2 decision table

| Reality | Decision: reject $H_0$ | Decision: fail to reject $H_0$ |
|---|---|---|
| $H_0$ true | **Type I error** | correct decision |
| $H_0$ false | correct decision (**power**) | **Type II error** |

## Type I error

A **Type I error** happens when we reject a null hypothesis that is actually true.
This is a **false positive**. [→ 2.2.3 @ 09:04]

$$
\alpha = P(\text{reject } H_0 \mid H_0 \text{ true})
$$

The lecture also identifies $\alpha$ as the **significance level**. [→ 2.2.3 @ 09:25]

## Type II error

A **Type II error** happens when $H_0$ is false, but we fail to reject it. This is a
**false negative**. [→ 2.2.3 @ 10:57]

$$
\beta = P(\text{fail to reject } H_0 \mid H_0 \text{ false for a specified alternative})
$$

## Power

The **power** of a test is the probability of correctly rejecting a false null
hypothesis, for a specified alternative. [→ 2.2.3 @ 09:55]

$$
\text{Power} = 1 - \beta
$$

A powerful test is good at detecting a real effect when the effect truly exists.
[→ 2.2.3 @ 10:10]

## Medical-test analogy from the lecture

The course uses cancer screening as an intuition builder:

- $H_0$: the patient does **not** have cancer. [→ 2.2.3 @ 12:00]
- Rejecting $H_0$ means concluding the patient **does** have cancer.
- A **Type I error** is a **false positive**: the patient is healthy, but the test says
  cancer is present. [→ 2.2.3 @ 12:30]
- A **Type II error** is a **false negative**: the patient has cancer, but the test
  misses it. [→ 2.2.3 @ 13:01]

This example is a good quiz shortcut for remembering the difference.

See also [[p-value-and-significance]] and [[hypothesis-test-procedure]].

## Python hands-on

A simple simulation view of Type I error uses many samples generated under $H_0$ and
counts how often the test rejects:

```python
import numpy as np
from scipy.stats import ttest_1samp

rng = np.random.default_rng(0)
alpha = 0.05
rejections = 0
trials = 5000

for _ in range(trials):
    sample = rng.normal(loc=70, scale=10, size=20)  # H0 true: mu = 70
    result = ttest_1samp(sample, popmean=70)
    if result.pvalue < alpha:
        rejections += 1

print(rejections / trials)   # should be close to alpha
```

## Summary

- **Type I error** = reject a true $H_0$ = **false positive**.
- **Type II error** = fail to reject a false $H_0$ = **false negative**.
- **$\alpha$** is the Type I error rate set by the testing rule.
- **Power** is $1-\beta$.
- Quiz trap: power is **not** $1-\alpha$; it is **$1-\beta$**.
