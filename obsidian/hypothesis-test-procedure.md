---
sources:
  - video: "2.2.4 Template for Hypothesis Testing"
    course_id: 141734
    item_id: 7718546
    duration: "01:22"
  - video: "2.2.3 Basic Concepts of Hypothesis Testing"
    course_id: 141734
    item_id: 7718544
    duration: "13:37"
  - video: "2.2.5 Performing a Hypothesis Test"
    course_id: 141734
    item_id: 7718548
    duration: "20:33"
---

# Hypothesis Test Procedure

The course gives a short template for doing a hypothesis test. It is a **five-step workflow**: identify the question, state the hypotheses, prepare the data, choose the right test, then perform the test and conclude. [→ 2.2.4 @ 00:27] [→ 2.2.4 @ 01:03]

## Step 1 — Identify the key question

State clearly what population claim you care about. Are you testing for an increase, a decrease, or any difference? [→ 2.2.4 @ 00:27]

## Step 2 — State $H_0$ and $H_a$

Write the [[Null and Alternative Hypothesis|null and alternative hypotheses]] in symbols.

$$
H_0:\ \theta = \theta_0
\qquad
H_a:\ \theta > \theta_0,\ \theta < \theta_0,\ \text{or}\ \theta \ne \theta_0
$$

[→ 2.2.4 @ 00:31]

## Step 3 — Prepare the data

Collect the sample and understand how it was obtained. The transcript stresses understanding the **sampling procedure**, because the inference depends on how the data were collected. [→ 2.2.4 @ 00:38]

## Step 4 — Choose the right test statistic and check assumptions

The lecturer says to find the right test, the right **test statistic**, and to check the assumptions before computing anything. [→ 2.2.4 @ 00:46] [→ 2.2.4 @ 00:59]

A **test statistic** is a number computed from the sample that will be compared to its null distribution. Because it comes from a sample, it is a random variable. [→ 2.2.3 @ 04:07] [→ 2.2.3 @ 05:01]

Typical examples are:

$$
z = \frac{\bar{x} - \mu_0}{\sigma / \sqrt{n}}
\qquad
\text{and}
\qquad
t = \frac{\bar{x} - \mu_0}{s / \sqrt{n}}
$$

The course also notes that different tests use different reference distributions, such as the [[Normal Distribution]], $t$, $F$, or $\chi^2$ distributions. [→ 2.2.3 @ 05:43] [→ 2.2.3 @ 06:29]

## Step 5 — Perform the test and conclude

This final step contains the numerical work: choose the significance level, compute the test statistic, get the p-value or critical region, then state the decision in words. [→ 2.2.4 @ 01:03] [→ 2.2.5 @ 00:25]

Two equivalent decision rules appear throughout the section:

$$
\text{Reject } H_0 \text{ if p-value} < \alpha
$$

and

$$
\text{Reject } H_0 \text{ if the test statistic falls in the rejection region}
$$

The **rejection region** (or **critical region**) is the set of test-statistic values extreme enough to trigger rejection. [→ 2.2.3 @ 03:25] [→ 2.2.3 @ 04:16] [→ 2.2.5 @ 14:16]

The conclusion should be written in context:

- “Reject $H_0$; there is sufficient evidence that ...”
- “Fail to reject $H_0$; there is insufficient evidence that ...”

The course prefers this wording over “accept $H_0$.” [→ 2.2.3 @ 08:32] [→ 2.2.5 @ 19:16]

## Python hands-on

A compact SciPy workflow for a one-sample test is:

```python
import numpy as np
from scipy.stats import ttest_1samp

sample = np.array([72, 75, 70, 74, 76, 71, 73, 77])
result = ttest_1samp(sample, popmean=70, alternative='greater')

alpha = 0.05
print(result.statistic)
print(result.pvalue)
print('Reject H0' if result.pvalue < alpha else 'Fail to reject H0')
```

## Summary

1. identify the question
2. state $H_0$ and $H_a$
3. prepare the data
4. choose the test statistic and check assumptions
5. perform the test and conclude

Quiz-critical facts:

- A **test statistic** is computed from the sample.
- A **critical region** is the same as a **rejection region**.
- The decision must be reported as **reject** or **fail to reject** $H_0$.
- The p-value rule and the critical-value rule give the **same decision** when they come from the same test.
