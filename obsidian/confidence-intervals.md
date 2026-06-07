---
sources:
  - video: "2.2.7 Confidence Intervals and Hypothesis Testing"
    course_id: 141734
    item_id: 7718552
    duration: "02:38"
---

# Confidence Intervals

This short video links [[Estimation]] to [[Hypothesis Testing]] by showing that a confidence interval gives the set of parameter values that remain compatible with the observed data. [→ 2.2.7 @ 00:05] [→ 2.2.7 @ 01:23]

See also [[Hypothesis Testing]], [[p-value-and-significance|p-value and Significance]], [[type-i-and-type-ii-errors|Type I and Type II Errors]], [[Normal Distribution]], [[Z-Score]], and [[Estimation]].

## What a confidence interval means

The course uses the usual informal wording: a $95\%$ confidence interval gives a range of plausible values for an unknown parameter. For example, if the interval is from $9$ to $11$, we informally say we are $95\%$ confident the true parameter lies between $9$ and $11$. [→ 2.2.7 @ 00:19] [→ 2.2.7 @ 00:37]

More precisely, the **method** is designed so that in repeated sampling, about $95\%$ of such intervals would contain the true parameter.

For a population mean with known standard deviation, the usual two-sided interval is

$$
\bar{x} \pm z_{1-\alpha/2}\frac{\sigma}{\sqrt{n}}
$$

with confidence level $1-\alpha$.

## Compatibility with the data

The key bridge in the video is this idea:

> A parameter value is inside the confidence interval exactly when it is still compatible with the data under the model.

That is the same question a hypothesis test asks: is a proposed null value $\mu_0$ still plausible, given the observed sample? [→ 2.2.7 @ 01:02] [→ 2.2.7 @ 01:12]

## Duality with a two-sided hypothesis test

For a two-sided test

$$
H_0: \mu = \mu_0
\qquad
H_a: \mu \ne \mu_0
$$

using the **same assumptions, same standard error, and same confidence/significance level**, the rule is:

- if $\mu_0$ is **inside** the $100(1-\alpha)\%$ confidence interval, **fail to reject** $H_0$
- if $\mu_0$ is **outside** the $100(1-\alpha)\%$ confidence interval, **reject** $H_0$

This is exactly the video's summary: the confidence interval contains all values of $\mu_0$ for which the null hypothesis would **not** be rejected. [→ 2.2.7 @ 01:35] [→ 2.2.7 @ 02:04] [→ 2.2.7 @ 02:25]

Algebraically, these are the same rule:

$$
\mu_0 \notin \bar{x} \pm z_{1-\alpha/2}\frac{\sigma}{\sqrt{n}}
\iff
\left|\frac{\bar{x}-\mu_0}{\sigma/\sqrt{n}}\right| > z_{1-\alpha/2}
$$

The right-hand side is just the usual two-sided $z$-test rejection rule.

## Small numerical example

Suppose

$$
\bar{x}=580, \quad \sigma=50, \quad n=36
$$

Then a $95\%$ confidence interval for $\mu$ is

$$
580 \pm 1.96\frac{50}{\sqrt{36}} = 580 \pm 16.33
$$

so

$$
(563.67,\ 596.33)
$$

If you test

$$
H_0: \mu = 600
\qquad
H_a: \mu \ne 600
$$

then $600$ lies **outside** the $95\%$ interval, so you would reject $H_0$ at $\alpha=0.05$.

## Important limit of the rule

This confidence-interval shortcut matches a **two-sided** hypothesis test. It does **not** directly match a one-sided test unless you use the corresponding **one-sided** confidence bound.

That distinction is a common quiz trap.

## Python hands-on

```python
from math import sqrt
from scipy.stats import norm

xbar = 580
sigma = 50
n = 36
alpha = 0.05
mu0 = 600

margin = norm.isf(alpha / 2) * sigma / sqrt(n)
ci = (xbar - margin, xbar + margin)
reject_two_sided = not (ci[0] <= mu0 <= ci[1])

print(ci)                # (563.666..., 596.333...)
print(reject_two_sided)  # True
```

## Summary

- A confidence interval is a range of parameter values that are **compatible with the data** under the model.
- For a two-sided test at level $\alpha$, the matching $100(1-\alpha)\%$ CI contains exactly the null values that would **not** be rejected.
- Quiz-critical fact: if the null value is **outside** the $95\%$ CI, reject the corresponding two-sided test at $\alpha=0.05$.
- Quiz-critical fact: this duality is for **two-sided** tests with matching assumptions; one-sided tests need one-sided bounds.
- Quiz-critical fact: a CI is about the **parameter**, not about where most individual sample observations fall.
