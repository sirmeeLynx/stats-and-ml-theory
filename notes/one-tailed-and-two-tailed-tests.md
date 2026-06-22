---
sources:
  - video: "2.2.6 One-tailed and Two-tailed Tests"
    course_id: 141734
    item_id: 7718550
    duration: "09:35"
---

# One-tailed and Two-tailed Tests

The form of the alternative hypothesis determines whether a test is **one-tailed** or **two-tailed**. The lecture is explicit that this depends on the **business problem**, not on the sample you happened to observe. [→ 2.2.6 @ 01:15] [→ 2.2.6 @ 01:30]

## Tail choice comes from $H_a$

| Alternative | Test type | Rejection region |
|---|---|---|
| $H_a: \mu > \mu_0$ | right-tailed | upper tail only |
| $H_a: \mu < \mu_0$ | left-tailed | lower tail only |
| $H_a: \mu \ne \mu_0$ | two-tailed | both tails |

A one-tailed test asks whether the parameter is too large **or** too small. A two-tailed test asks whether it is too far away from the null value in **either** direction. [→ 2.2.6 @ 01:00] [→ 2.2.6 @ 01:18]

## What changes and what does not

A key quiz point from the lecture:

- the **test statistic stays the same** [→ 2.2.6 @ 01:57] [→ 2.2.6 @ 09:30]
- the **rejection region changes** [→ 2.2.6 @ 02:02]
- the **p-value changes** because the tail area being measured changes [→ 2.2.6 @ 09:20]

For a z-test, the statistic is still

$$
z = \frac{\bar{x} - \mu_0}{\sigma / \sqrt{n}}
$$

regardless of whether the test is one-sided or two-sided.

## Critical-value rules

Let $z_{\alpha}$ be the positive standard-normal cutoff leaving area $\alpha$ in the upper tail.

### Right-tailed test

$$
\text{Reject } H_0 \text{ if } z > z_{\alpha}
$$

At $\alpha = 0.05$, $z_{\alpha} \approx 1.645$. [→ 2.2.6 @ 02:35]

### Left-tailed test

$$
\text{Reject } H_0 \text{ if } z < -z_{\alpha}
$$

At $\alpha = 0.05$, the cutoff is about $-1.645$. [→ 2.2.6 @ 08:57]

### Two-tailed test

$$
\text{Reject } H_0 \text{ if } |z| > z_{\alpha/2}
$$

Here the significance level is split equally across both tails, so at $\alpha = 0.05$ we use $0.025$ in each tail and get critical values $\pm 1.96$. [→ 2.2.6 @ 02:45] [→ 2.2.6 @ 07:22]

## Bottle-filling example

A soft-drink manufacturer claims bottles average $600$ ml, with known population standard deviation $\sigma = 50$ ml. A random sample of $n = 36$ bottles has sample mean $\bar{x} = 580$ ml. [→ 2.2.6 @ 03:15] [→ 2.2.6 @ 04:31]

The common test statistic is:

$$
z = \frac{580 - 600}{50 / \sqrt{36}} = -2.4
$$

[→ 2.2.6 @ 05:16] [→ 2.2.6 @ 05:55]

### Left-tailed version: underfilling is the concern

If the concern is specifically that customers are getting **less than** $600$ ml,

$$
H_0: \mu = 600
\qquad
H_a: \mu < 600
$$

Then we compare $-2.4$ to the left-tail cutoff $-1.645$. Since

$$
-2.4 < -1.645,
$$

we reject $H_0$. The one-sided p-value is approximately

$$
P(Z \le -2.4) \approx 0.0082
$$

[→ 2.2.6 @ 03:35] [→ 2.2.6 @ 08:41] [→ 2.2.6 @ 09:00]

### Two-tailed version: any deviation is a problem

If the concern is that the process is **off target in either direction**,

$$
H_0: \mu = 600
\qquad
H_a: \mu \ne 600
$$

Then we compare the same statistic to the two-tailed cutoff $1.96$. Since

$$
|-2.4| = 2.4 > 1.96,
$$

we reject $H_0$ again. The two-sided p-value is approximately

$$
2P(Z \le -2.4) \approx 0.0164
$$

[→ 2.2.6 @ 04:08] [→ 2.2.6 @ 07:22]

## Why two-tailed tests are harder to reject

At the same $\alpha$, a two-tailed test spreads the error budget across both tails, so the cutoff is more extreme:

- one-tailed at $\alpha = 0.05$: $\pm 1.645$ on the relevant side
- two-tailed at $\alpha = 0.05$: $\pm 1.96$

That is why the same observed statistic usually has a **larger p-value** in the two-tailed version. [→ 2.2.6 @ 02:45] [→ 2.2.6 @ 09:20]

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
zcrit_two = norm.isf(alpha / 2)

print(z)          # -2.4
print(p_left)     # about 0.0082
print(p_two)      # about 0.0164
print(zcrit_left) # about -1.645
print(zcrit_two)  # about 1.96
```

## Summary

- Tail choice comes from **$H_a$ and the business question**, not the data.
- The **test statistic stays the same**; the **rejection region** and **p-value** change.
- In a two-tailed test, the significance level is split: $\alpha/2$ in each tail.
- Quiz-critical fact: one-tailed and two-tailed tests can give different p-values for the **same** observed z-score.
