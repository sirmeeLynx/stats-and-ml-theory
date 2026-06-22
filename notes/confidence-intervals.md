---
sources:
  - video: "2.2.7 Confidence Intervals and Hypothesis Testing"
    course_id: 141734
    item_id: 7718552
    duration: "02:39"
  - video: "2.2.6 One-tailed and Two-tailed Tests"
    course_id: 141734
    item_id: 7718550
    duration: "09:35"
---

# Confidence Intervals

This video connects [[Estimation]] and [[Hypothesis Testing]]: both ask which parameter values are still supported by the data. [→ 2.2.7 @ 00:06] [→ 2.2.7 @ 01:07]

## What a confidence interval is saying

The lecture's informal wording is that a $95\%$ confidence interval gives a range of parameter values that the data support. If the interval is from $9$ to $11$, then values between $9$ and $11$ remain plausible given the sample. [→ 2.2.7 @ 00:20] [→ 2.2.7 @ 00:58]

For the usual z-based interval for a population mean with known $\sigma$,

$$
\bar{x} \pm z_{\alpha/2}\frac{\sigma}{\sqrt{n}}
$$

where $z_{\alpha/2}$ is the positive cutoff leaving area $\alpha/2$ in the upper tail.

## CI / test duality

The key message of the video is that a confidence interval and a **two-sided** hypothesis test are answering the same question: does the data support a proposed null value $\mu_0$? [→ 2.2.7 @ 01:10] [→ 2.2.7 @ 01:33]

For

$$
H_0: \mu = \mu_0
\qquad
H_a: \mu \ne \mu_0,
$$

using the same assumptions and the same confidence/significance level,

- if $\mu_0$ is **inside** the $100(1-\alpha)\%$ confidence interval, **fail to reject** $H_0$
- if $\mu_0$ is **outside** the interval, **reject** $H_0$

That is exactly the video's summary: the confidence interval contains all values of $\mu_0$ for which the null hypothesis would **not** be rejected. [→ 2.2.7 @ 01:37] [→ 2.2.7 @ 02:06]

Algebraically, the two rules are the same:

$$
\mu_0 \notin \bar{x} \pm z_{\alpha/2}\frac{\sigma}{\sqrt{n}}
\iff
\left|\frac{\bar{x} - \mu_0}{\sigma / \sqrt{n}}\right| > z_{\alpha/2}
$$

## Example using the bottle data

Using the bottle-filling example from [[One-tailed and Two-tailed Tests]],

$$
\bar{x} = 580,\quad \sigma = 50,\quad n = 36
$$

so the $95\%$ confidence interval is

$$
580 \pm 1.96\frac{50}{\sqrt{36}} = 580 \pm 16.33
$$

which gives

$$
(563.67,\ 596.33)
$$

Because $600$ lies **outside** this interval, the corresponding two-sided test rejects

$$
H_0: \mu = 600
$$

at $\alpha = 0.05$. This matches the two-tailed z-test from the previous lecture. [→ 2.2.6 @ 04:30] [→ 2.2.6 @ 07:22] [→ 2.2.7 @ 01:43]

## Important limit of the shortcut

This confidence-interval shortcut matches a **two-sided** hypothesis test. A one-sided test needs the matching **one-sided confidence bound**, not an ordinary two-sided interval.

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

print(ci)                # about (563.67, 596.33)
print(reject_two_sided)  # True
```

## Summary

- A confidence interval gives the set of parameter values still **supported by the data**.
- For a matching **two-sided** test, values **inside** the CI are not rejected; values **outside** are rejected.
- Quiz-critical fact: if the null value lies outside a $95\%$ CI, reject the corresponding two-sided test at $\alpha = 0.05$.
- Quiz-critical fact: CI/test duality is about **two-sided** tests unless you switch to a one-sided bound.
