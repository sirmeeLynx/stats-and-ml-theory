---
sources:
  - video: "2.2.4 Template for Hypothesis Testing"
    course_id: 141734
    item_id: 7718546
    duration: "01:21"
  - video: "2.2.3 Basic Concepts of Hypothesis Testing"
    course_id: 141734
    item_id: 7718544
    duration: "13:35"
  - video: "2.2.1 Introduction to Hypothesis Testing"
    course_id: 141734
    item_id: 7718540
    duration: "18:43"
---

# Hypothesis Test Procedure

The course gives a standard template for carrying out a hypothesis test. [→ 2.2.4 @ 00:05]

## Step 1 — Identify the key question

State the population claim clearly. Are you testing for a change, an improvement, or
simply a difference? [→ 2.2.4 @ 00:26]

## Step 2 — State $H_0$ and $H_a$

Write the null and alternative hypotheses in symbols. [→ 2.2.4 @ 00:30]

Example:

$$
H_0: \mu = \mu_0
\qquad
H_a: \mu > \mu_0
$$

See [[null-and-alternative-hypothesis]].

## Step 3 — Prepare the data

Collect the sample and understand how it was obtained. The inference only makes sense
if the sampling procedure is appropriate. [→ 2.2.4 @ 00:37]

## Step 4 — Choose the right test and check assumptions

Choose a test whose statistic matches the parameter and data type. The lecture notes
that different tests use different reference distributions, such as the [[Normal Distribution]],
$t$ distribution, $F$ distribution, or $\chi^2$ distribution. These connect naturally to
[[Z-Score]] ideas and the [[Central Limit Theorem]]. [→ 2.2.3 @ 05:42]

Common test statistics:

$$
z = \frac{\hat p - p_0}{\sqrt{p_0(1-p_0)/n}}
$$

$$
t = \frac{\bar x - \mu_0}{s / \sqrt{n}}
$$

A **test statistic** is a number computed from the sample and compared against the
null distribution. [→ 2.2.3 @ 04:05]

## Step 5 — Compute the decision rule

There are two equivalent ways to state the rule:

### Critical-region form

Define a **critical region**: the set of test-statistic values that are so extreme
under $H_0$ that they lead to rejection.

For a right-tailed $z$-test at significance level $\alpha$:

$$
\text{Reject } H_0 \text{ if } z > z_{1-\alpha}
$$

### p-value form

Compute the p-value and compare it to $\alpha$:

$$
\text{Reject } H_0 \text{ if p-value} < \alpha
$$

The available transcripts motivate this as “how likely would this sample result be if
$H_0$ were true?” [→ 2.2.1 @ 10:27]

## Step 6 — Conclude in words

State the conclusion in context:

- “Reject $H_0$; there is sufficient evidence that …”
- “Fail to reject $H_0$; there is insufficient evidence that …”

The course strongly prefers this wording over “accept $H_0$.” [→ 2.2.3 @ 03:04]

## Python hands-on

A one-sample $t$-test in SciPy:

```python
import numpy as np
from scipy.stats import ttest_1samp

sample = np.array([72, 75, 70, 74, 76, 71, 73, 77])
result = ttest_1samp(sample, popmean=70, alternative='greater')

print(result.statistic)
print(result.pvalue)
```

A manual decision rule using $\alpha = 0.05$:

```python
alpha = 0.05
if result.pvalue < alpha:
    print("Reject H0")
else:
    print("Fail to reject H0")
```

## Summary

1. identify the question
2. state $H_0$ and $H_a$
3. prepare the data
4. choose the test and check assumptions
5. compute the test statistic / p-value
6. conclude in words

Quiz-critical facts:

- A **test statistic** is computed from sample data.
- A **critical region** is the rejection region.
- The decision must be reported as **reject** or **fail to reject** $H_0$.
- The same logic can be expressed either with a **critical value** or with a
  **p-value**.
