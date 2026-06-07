---
sources:
  - video: "2.2.1 Introduction to Hypothesis Testing"
    course_id: 141734
    item_id: 7718540
    duration: "18:43"
  - video: "2.2.4 Template for Hypothesis Testing"
    course_id: 141734
    item_id: 7718546
    duration: "01:21"
---

# Hypothesis Testing

Hypothesis testing asks whether sample data provide **strong enough evidence**
against a status-quo claim about a population parameter. The lecture frames this as
moving from a sample to a decision about the population. [→ 2.2.1 @ 03:04]

A **hypothesis** is a claim about a population parameter such as a mean $\mu$ or a
proportion $p$. In hypothesis testing, we do **not** ask only for an estimate; we ask
whether the data are compatible with a particular claim. [→ 2.2.1 @ 13:59]

## Why this is different from estimation

A point estimate like $\hat p = 0.73$ or $\hat p = 0.81$ is not enough by itself. The
real question is whether those values are **significantly** above the historical value
$0.70$, rather than just a result of sampling variation. This is the bridge from
[[Estimation]] to hypothesis testing. [→ 2.2.1 @ 11:53]

In the lamp example, the historical reliability rate is $70\%$, and a sample of
$100$ lamps gives $73$ reliable lamps under a new process. The course asks:

$$
\text{If the true reliability is still } 0.70, \text{ how likely is it to see } 73
\text{ or more reliable lamps just by chance?}
$$

[→ 2.2.1 @ 04:24]

That same logic is repeated for $81$ reliable lamps out of $100$. A result that is
common under the status quo is weak evidence; a result that is rare under the status
quo is strong evidence against it. [→ 2.2.1 @ 08:38]

## Core idea

Hypothesis testing starts by assuming the **null hypothesis** is true, then checking
how surprising the observed sample would be under that assumption. [→ 2.2.1 @ 10:27]

- If the observed result is **not very surprising**, we **fail to reject** $H_0$.
- If the observed result is **very surprising**, we **reject** $H_0$.

This is the logic behind the standard decision rule:

$$
\text{Reject } H_0 \text{ if p-value} < \alpha.
$$

See also [[null-and-alternative-hypothesis]], [[p-value-and-significance]], and
[[hypothesis-test-procedure]].

## Lamp example intuition

For the lecture's reliability example, the old process has reliability $p_0 = 0.70$.
A sample of $n=100$ lamps gives either $73$ or $81$ reliable lamps.

- Seeing $73/100$ is presented as fairly plausible under the old process, so it is
  **not enough evidence** to claim improvement. [→ 2.2.1 @ 06:42]
- Seeing $81/100$ is presented as much rarer under the old process, so it is
  **strong evidence** that the process changed. [→ 2.2.1 @ 08:45]

## Python hands-on

Using the lecture's setup, an exact one-sided binomial test is:

```python
from scipy.stats import binomtest

# H0: p = 0.70, Ha: p > 0.70
result_73 = binomtest(k=73, n=100, p=0.70, alternative='greater')
result_81 = binomtest(k=81, n=100, p=0.70, alternative='greater')

print(result_73.pvalue)
print(result_81.pvalue)
```

A normal-approximation version uses a [[Z-Score]] and the [[Central Limit Theorem]]:

```python
from math import sqrt
from scipy.stats import norm

n = 100
p0 = 0.70
phat = 0.81
se = sqrt(p0 * (1 - p0) / n)

z = (phat - p0) / se
p_value = 1 - norm.cdf(z)   # right-tailed test

print(z, p_value)
```

## Summary

- Hypothesis testing evaluates a **claim about a population parameter**, not just a
  sample estimate.
- The question is whether the sample result is too extreme to be explained by
  **sampling variation alone**.
- A small tail probability under $H_0$ is evidence against $H_0$.
- Quiz trap: a large sample estimate does **not automatically** imply significance.
  You must compare it to what would be expected under the null model.
