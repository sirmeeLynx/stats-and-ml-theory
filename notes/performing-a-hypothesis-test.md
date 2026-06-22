---
sources:
  - video: "2.2.5 Performing a Hypothesis Test"
    course_id: 141734
    item_id: 7718548
    duration: "20:33"
---

# Performing a Hypothesis Test

This lecture turns the template into one full worked example. The business question is whether an e-commerce firm's average delivery time has become **more than 5 days**. [→ 2.2.5 @ 05:37] [→ 2.2.5 @ 06:49]

## The setup

From prior data, the company has population mean delivery time $\mu = 5$ days and known population standard deviation $\sigma = 1.3$ days. A random sample of $n = 45$ orders gives a sample mean of $\bar{x} = 5.25$ days. [→ 2.2.5 @ 05:37] [→ 2.2.5 @ 06:18]

Because the concern is specifically that deliveries are getting **slower**, the hypotheses are:

$$
H_0: \mu = 5
\qquad
H_a: \mu > 5
$$

This is a **one-tailed (right-tailed)** test. [→ 2.2.5 @ 06:54] [→ 2.2.5 @ 09:51]

## Step 1 — Fix the significance level

The significance level is chosen before seeing the data. It is the probability of rejecting a true null hypothesis, so it controls the **Type I error** rate. [→ 2.2.5 @ 00:25] [→ 2.2.5 @ 01:02]

$$
\alpha = P(\text{reject } H_0 \mid H_0 \text{ true})
$$

The lecture uses the common business choice $\alpha = 0.05$. [→ 2.2.5 @ 01:18] [→ 2.2.5 @ 15:03]

## Step 2 — Check the assumptions and choose the test

The video uses a one-sample **z-test** because:

- delivery time is a continuous variable [→ 2.2.5 @ 08:02]
- the sample is random [→ 2.2.5 @ 08:30]
- $n = 45 > 30$, so the [[Central Limit Theorem]] supports a normal model for the sample mean [→ 2.2.5 @ 08:10]
- the population standard deviation is treated as known: $\sigma = 1.3$ [→ 2.2.5 @ 08:25]

So the test statistic is:

$$
z = \frac{\bar{x} - \mu_0}{\sigma / \sqrt{n}}
$$

[→ 2.2.5 @ 10:26] [→ 2.2.5 @ 11:06]

## Step 3 — Compute the test statistic

Substituting the lecture's numbers gives:

$$
z = \frac{5.25 - 5}{1.3 / \sqrt{45}} \approx 1.29
$$

So the observed sample mean is about $1.29$ standard errors above the null value. [→ 2.2.5 @ 11:41] [→ 2.2.5 @ 12:05]

## Step 4 — Compute the p-value

For a right-tailed test, the p-value is the area to the **right** of the observed z-value:

$$
p\text{-value} = P(Z \ge 1.29) \approx 0.098
$$

The lecture interprets this as: if the true mean really were $5$, there is about a $9.8\%$ chance of seeing a sample mean this large or larger just from sampling variation. [→ 2.2.5 @ 12:46] [→ 2.2.5 @ 13:48]

Because

$$
0.098 > 0.05,
$$

we **fail to reject** $H_0$. [→ 2.2.5 @ 18:26] [→ 2.2.5 @ 19:03]

## Step 5 — Critical-value view of the same result

The same decision can be made using a rejection region. For a right-tailed z-test at level $\alpha$:

$$
\text{Reject } H_0 \text{ if } z > z_{\alpha}
$$

where $z_{\alpha}$ is the positive cutoff leaving tail area $\alpha$ on the right. At $\alpha = 0.05$,

$$
z_{\alpha} \approx 1.645
$$

[→ 2.2.5 @ 15:09] [→ 2.2.5 @ 15:45]

Since

$$
1.29 < 1.645,
$$

the statistic does **not** fall in the rejection region, so we again fail to reject $H_0$. [→ 2.2.5 @ 16:32] [→ 2.2.5 @ 18:03]

## Final conclusion in context

The sample mean is above $5$, but it is **not far enough above $5$** to count as statistically significant at the $5\%$ level. The correct business conclusion is:

> Fail to reject $H_0$; there is insufficient evidence that the average delivery time now exceeds 5 days.

[→ 2.2.5 @ 19:22] [→ 2.2.5 @ 20:17]

See also [[p-value and Significance]] and [[One-tailed and Two-tailed Tests]].

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
p_value = norm.sf(z)        # right-tail probability
z_crit = norm.isf(alpha)    # right-tail critical value

print(z)       # about 1.29
print(p_value) # about 0.098
print(z_crit)  # about 1.645
print('Reject H0' if p_value < alpha else 'Fail to reject H0')
```

## Summary

- This example uses a **one-sample right-tailed z-test**.
- Here, $z \approx 1.29$ and $p \approx 0.098$.
- Because $p > 0.05$, we **fail to reject** $H_0$.
- The critical-value and p-value approaches agree.
- Quiz trap: a sample mean above the null value is **not automatically significant**.
