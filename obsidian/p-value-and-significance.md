---
sources:
  - video: "2.2.1 Introduction to Hypothesis Testing"
    course_id: 141734
    item_id: 7718540
    duration: "18:43"
  - video: "2.2.3 Basic Concepts of Hypothesis Testing"
    course_id: 141734
    item_id: 7718544
    duration: "13:35"
  - video: "2.2.4 Template for Hypothesis Testing"
    course_id: 141734
    item_id: 7718546
    duration: "01:21"
---

# p-value and Significance

The first hypothesis-testing videos already use the **idea** of a p-value, even before
later videos formally expand on the term. The core question is: if $H_0$ were true,
how likely would this observed result be? [→ 2.2.1 @ 04:24] [→ 2.2.4 @ 01:08]

## p-value: precise definition

The **p-value** is the probability, **assuming $H_0$ is true**, of obtaining a test
statistic at least as extreme as the one observed, in the direction specified by
$H_a$.

$$
p\text{-value} = P(\text{test statistic at least as extreme as observed} \mid H_0)
$$

Examples:

- right-tailed test: $P(T \ge t_{obs} \mid H_0)$
- left-tailed test: $P(T \le t_{obs} \mid H_0)$
- two-tailed test: probability in **both tails** at least as extreme as the observed
  distance from the null value

## What the p-value is **not**

Quiz traps:

- It is **not** the probability that $H_0$ is true.
- It is **not** the probability that the observed data happened “by accident” in an
  unrestricted sense.
- It is **not** the probability that your conclusion is correct.

It is a conditional probability **under the null model**.

## Significance level $\alpha$

The **significance level** $\alpha$ is chosen **before** looking at the data. It is the
cutoff used to decide whether the evidence against $H_0$ is strong enough.

$$
\text{Reject } H_0 \text{ if p-value} < \alpha
$$

In long-run repeated testing, $\alpha$ is the probability of a **Type I error** under
that testing rule.

The course connects significance to whether a result is too extreme to be explained by
sampling variation alone. [→ 2.2.1 @ 12:20] [→ 2.2.3 @ 09:29]

## Critical region

The **critical region** (or rejection region) is the set of test-statistic values that
lead to rejection of $H_0$ at the chosen $\alpha$.

For a two-tailed $z$-test at level $\alpha$:

$$
\text{Reject } H_0 \text{ if } |z| > z_{1-\alpha/2}
$$

For a right-tailed test:

$$
\text{Reject } H_0 \text{ if } z > z_{1-\alpha}
$$

The p-value approach and the critical-region approach give the **same decision** when
they are set up for the same test.

## One-tailed vs two-tailed p-values

The p-value depends on the form of $H_a$:

- **right-tailed**: evidence for values larger than the null value
- **left-tailed**: evidence for values smaller than the null value
- **two-tailed**: evidence for values far from the null value in either direction

This is why choosing $H_a$ correctly matters. See [[null-and-alternative-hypothesis]].

## Lecture intuition: 73 vs 81 lamps

The lecture contrasts two right-tail probabilities under the old reliability rate of
$70\%$:

- $73/100$ reliable lamps gives a fairly large tail probability, so the evidence is
  weak. [→ 2.2.1 @ 06:42]
- $81/100$ reliable lamps gives a much smaller tail probability, so the evidence is
  strong. [→ 2.2.1 @ 08:45]

That is the intuition behind statistical significance.

## Python hands-on

Using the [[Normal Distribution]] for a one-sided [[Z-Score]] test:

```python
from math import sqrt
from scipy.stats import norm

p0 = 0.70
phat = 0.81
n = 100

z = (phat - p0) / sqrt(p0 * (1 - p0) / n)
p_value = 1 - norm.cdf(z)   # right tail

print(z)
print(p_value)
```

Two-sided p-value from a z statistic:

```python
from scipy.stats import norm

z = -2.1
p_two_sided = 2 * norm.cdf(-abs(z))
print(p_two_sided)
```

## Summary

- **p-value** = probability of data at least as extreme as observed, **assuming $H_0$**.
- **$\alpha$** = pre-chosen cutoff for declaring statistical significance.
- If **p-value $< \alpha$**, reject $H_0$.
- “Statistically significant” means **unlikely under $H_0$**; it does **not** mean
  “important in practice.”
- Tail choice matters: one-tailed and two-tailed tests use different p-values.
