---
sources:
  - video: "2.2.3 Basic Concepts of Hypothesis Testing"
    course_id: 141734
    item_id: 7718544
    duration: "13:37"
  - video: "2.2.5 Performing a Hypothesis Test"
    course_id: 141734
    item_id: 7718548
    duration: "20:33"
---

# p-value and Significance

Two numbers control the final decision in a hypothesis test: the **significance level** $\alpha$, which is fixed before the analysis, and the **p-value**, which is computed from the data. [→ 2.2.5 @ 00:25] [→ 2.2.5 @ 01:45] [→ 2.2.3 @ 09:36]

## Significance level $\alpha$

The significance level is the probability of rejecting a true null hypothesis. In other words, it is the **Type I error rate** built into the testing rule. [→ 2.2.5 @ 00:30] [→ 2.2.3 @ 09:23]

$$
\alpha = P(\text{reject } H_0 \mid H_0 \text{ true})
$$

The lecture stresses that $\alpha$ is chosen **up front** and does not change with the data. A common business choice is $\alpha = 0.05$. [→ 2.2.5 @ 00:55] [→ 2.2.5 @ 01:26] [→ 2.2.5 @ 01:42]

## p-value: the precise definition

The **p-value** is the probability, **assuming $H_0$ is true**, of observing the test statistic obtained from the sample, or something even more extreme in the direction specified by $H_a$. [→ 2.2.5 @ 01:50] [→ 2.2.5 @ 02:16]

$$
p\text{-value} = P(\text{test statistic at least as extreme as observed} \mid H_0)
$$

That is why the p-value depends on the sample and on the test statistic, while $\alpha$ does not. [→ 2.2.5 @ 02:54] [→ 2.2.5 @ 03:20]

## Rejection region and decision rule

The course also explains the **rejection region**: the set of test-statistic values that are extreme enough to reject $H_0$. [→ 2.2.3 @ 03:25] [→ 2.2.3 @ 04:16]

The p-value rule is:

$$
\text{Reject } H_0 \text{ if p-value} < \alpha
$$

[→ 2.2.5 @ 18:26] [→ 2.2.5 @ 18:57]

This is equivalent to the critical-value rule. The course shows both and emphasizes that they lead to the **same conclusion**. [→ 2.2.5 @ 15:09] [→ 2.2.5 @ 18:31]

## Worked example: delivery times

In the delivery-time example,

$$
H_0: \mu = 5,
\qquad
H_a: \mu > 5
$$

with known $\sigma = 1.3$, sample size $n = 45$, and sample mean $\bar{x} = 5.25$. [→ 2.2.5 @ 09:33] [→ 2.2.5 @ 10:45]

The test statistic is:

$$
z = \frac{5.25 - 5}{1.3 / \sqrt{45}} \approx 1.29
$$

and the one-sided p-value is:

$$
P(Z \ge 1.29) \approx 0.098
$$

[→ 2.2.5 @ 11:41] [→ 2.2.5 @ 13:17]

Because

$$
0.098 > 0.05,
$$

we **fail to reject** $H_0$. The sample mean is above $5$, but not by enough to be statistically significant at the $5\%$ level. [→ 2.2.5 @ 18:26] [→ 2.2.5 @ 19:21]

## What to remember about p-values

A p-value is evidence **against** $H_0$ only because it is computed **under** $H_0$. So the p-value is **not** “the probability that $H_0$ is true”; it is a tail probability under the null model.

See also [[Hypothesis Testing]], [[Type I and Type II Errors]], and [[One-tailed and Two-tailed Tests]].

## Python hands-on

```python
from math import sqrt
from scipy.stats import norm

mu0 = 5
sigma = 1.3
n = 45
xbar = 5.25
alpha = 0.05

z = (xbar - mu0) / (sigma / sqrt(n))
p_value = norm.sf(z)
z_crit = norm.isf(alpha)

print(z)       # about 1.29
print(p_value) # about 0.098
print(z_crit)  # about 1.645
print('Reject H0' if p_value < alpha else 'Fail to reject H0')
```

## Summary

- **$\alpha$** is fixed before the test; it controls the Type I error rate.
- **p-value** means: probability of the observed statistic, or something more extreme, **assuming $H_0$ is true**.
- Decision rule: reject $H_0$ if **p-value $< \alpha$**.
- Quiz trap: the p-value is **not** the probability that $H_0$ is true.
- A statistically significant result is one that is **unlikely under the null model**.
