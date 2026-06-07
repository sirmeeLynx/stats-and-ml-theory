---
sources:
  - video: "2.2.6 One-tailed and Two-tailed Tests"
    course_id: 141734
    item_id: 7718550
    duration: "09:34"
---

# One-tailed and Two-tailed Tests

This video explains that the **tail structure** comes from the form of the alternative hypothesis and the business question, not from whichever direction the sample happened to go. [→ 2.2.6 @ 01:24] [→ 2.2.6 @ 01:44]

See also [[Hypothesis Testing]], [[null-and-alternative-hypothesis|Null and Alternative Hypothesis]], [[p-value-and-significance|p-value and Significance]], [[type-i-and-type-ii-errors|Type I and Type II Errors]], [[Normal Distribution]], [[Z-Score]], and [[Estimation]].

## The alternative hypothesis determines the tails

The null still carries the equality sign, while the alternative determines whether the rejection region is on one side or both sides. [→ 2.2.6 @ 00:58] [→ 2.2.6 @ 01:17]

| Alternative hypothesis | Test type | Rejection direction |
|---|---|---|
| $H_a: \mu > \mu_0$ | right-tailed | upper tail only |
| $H_a: \mu < \mu_0$ | left-tailed | lower tail only |
| $H_a: \mu \ne \mu_0$ | two-tailed | both tails |

Choose this **before** seeing the data. The lecture is explicit that it depends on the business problem, not on the observed sample. [→ 2.2.6 @ 01:24] [→ 2.2.6 @ 01:32]

## What changes and what does not

A major quiz point from the video:

- the **test statistic** does **not** change [→ 2.2.6 @ 01:55] [→ 2.2.6 @ 09:21]
- the **rejection region** changes [→ 2.2.6 @ 02:00]
- the **p-value** changes because the tail area being measured changes [→ 2.2.6 @ 09:19]

For a $z$-test, the statistic is still

$$
z = \frac{\bar{x} - \mu_0}{\sigma/\sqrt{n}}
$$

regardless of whether the test is one-sided or two-sided.

## Rejection rules at significance level $\alpha$

### Right-tailed test

$$
\text{Reject } H_0 \text{ if } z > z_{1-\alpha}
$$

At $\alpha=0.05$, the critical value is about $1.645$. [→ 2.2.6 @ 02:35] [→ 2.2.6 @ 02:44]

### Left-tailed test

$$
\text{Reject } H_0 \text{ if } z < -z_{1-\alpha}
$$

At $\alpha=0.05$, the critical value is about $-1.645$. [→ 2.2.6 @ 08:38] [→ 2.2.6 @ 08:56]

### Two-tailed test

$$
\text{Reject } H_0 \text{ if } |z| > z_{1-\alpha/2}
$$

Here the significance level is split across both tails:

$$
\alpha/2 \text{ in the left tail and } \alpha/2 \text{ in the right tail}
$$

So at $\alpha=0.05$ we use $0.025$ in each tail, giving critical values $\pm 1.96$. [→ 2.2.6 @ 02:46] [→ 2.2.6 @ 07:03] [→ 2.2.6 @ 07:22]

## Bottle-filling example from the lecture

A soft-drink manufacturer claims each bottle contains $600$ ml with known population standard deviation $\sigma=50$ ml. A random sample of $n=36$ bottles has mean $\bar{x}=580$ ml. [→ 2.2.6 @ 03:13] [→ 2.2.6 @ 04:29]

The common test statistic is:

$$
z = \frac{580-600}{50/\sqrt{36}} = \frac{-20}{50/6} = -2.4
$$

[→ 2.2.6 @ 05:17] [→ 2.2.6 @ 05:50]

### Left-tailed version: underfilling is the concern

If the question is whether customers are receiving **less** than $600$ ml,

$$
H_0: \mu = 600
\qquad
H_a: \mu < 600
$$

This is a left-tailed test. The rejection rule at $\alpha=0.05$ is

$$
z < -1.645
$$

Since

$$
-2.4 < -1.645,
$$

we reject $H_0$. The one-sided p-value is

$$
P(Z \le -2.4) \approx 0.0082
$$

so the result is significant. [→ 2.2.6 @ 03:35] [→ 2.2.6 @ 08:25] [→ 2.2.6 @ 08:59]

### Two-tailed version: any deviation from $600$ is a problem

If the quality-control question is whether the filling process is **off target in either direction**,

$$
H_0: \mu = 600
\qquad
H_a: \mu \ne 600
$$

This is a two-tailed test. The rejection rule at $\alpha=0.05$ is

$$
|z| > 1.96
$$

Since

$$
|-2.4| = 2.4 > 1.96,
$$

we again reject $H_0$. The two-sided p-value is

$$
2P(Z \le -2.4) \approx 0.0164
$$

[→ 2.2.6 @ 04:07] [→ 2.2.6 @ 07:20] [→ 2.2.6 @ 07:40]

## Why two-tailed tests are harder to reject

At the same $\alpha$, a two-tailed test uses more extreme critical values because the error budget is split across two tails.

- one-tailed at $\alpha=0.05$: critical value about $1.645$
- two-tailed at $\alpha=0.05$: critical values about $\pm1.96$

So a statistic like $z=1.80$ would reject in a right-tailed test but **not** in a two-tailed test. This is a common quiz trap.

## Python hands-on

```python
from math import sqrt
from scipy.stats import norm

mu0 = 600
xbar = 580
sigma = 50
n = 36
alpha = 0.05

z = (xbar - mu0) / (sigma / sqrt(n))
p_left = norm.cdf(z)
p_two = 2 * norm.cdf(-abs(z))
zcrit_left = norm.ppf(alpha)
zcrit_two = norm.ppf(1 - alpha / 2)

print(z)          # -2.4
print(p_left)     # 0.008197...
print(p_two)      # 0.016395...
print(zcrit_left) # -1.644853...
print(zcrit_two)  # 1.959963...
```

## Summary

- Tail choice comes from **$H_a$ and the business question**, not the sample.
- The **test statistic stays the same**; the **rejection region** and **p-value** change.
- In a two-tailed test, the significance level is split:

$$
\alpha \to \alpha/2 \text{ in each tail}
$$

- At $\alpha=0.05$, one-tailed critical values are about $\pm1.645$, while two-tailed critical values are $\pm1.96$.
- Quiz-critical fact: a two-tailed p-value is larger than the matching one-tailed p-value for the same observed $|z|$ under a symmetric null distribution.
