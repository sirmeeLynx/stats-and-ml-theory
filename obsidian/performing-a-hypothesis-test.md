---
sources:
  - video: "2.2.5 Performing a Hypothesis Test"
    course_id: 141734
    item_id: 7718548
    duration: "20:32"
---

# Performing a Hypothesis Test

This video turns the abstract [[hypothesis-test-procedure|Hypothesis Test Procedure]] into one full worked example: define the hypotheses, choose $\alpha$, compute a test statistic, and make the decision. [→ 2.2.5 @ 00:05] [→ 2.2.5 @ 05:01]

See also [[Hypothesis Testing]], [[p-value-and-significance|p-value and Significance]], [[type-i-and-type-ii-errors|Type I and Type II Errors]], [[Normal Distribution]], [[Z-Score]], and [[Estimation]].

## Worked example from the lecture

An e-commerce company historically delivers in an average of $5$ days with known population standard deviation $\sigma = 1.3$ days. A new manager worries deliveries are getting **slower**, so she takes a random sample of $n=45$ orders and finds a sample mean of $\bar{x}=5.25$ days. [→ 2.2.5 @ 05:35] [→ 2.2.5 @ 06:12]

The business question is directional: are deliveries taking **more than** $5$ days on average? That makes this a **right-tailed** test. [→ 2.2.5 @ 06:48]

$$
H_0: \mu = 5
\qquad
H_a: \mu > 5
$$

## Step 1 — Fix the significance level

The lecture emphasizes that the significance level $\alpha$ is chosen **before** looking at the data. It controls the long-run probability of a [[type-i-and-type-ii-errors|Type I and Type II Errors]] Type I error (a false positive). In business settings, the usual choice is $\alpha = 0.05$. [→ 2.2.5 @ 00:24] [→ 2.2.5 @ 01:20]

$$
\alpha = P(\text{reject } H_0 \mid H_0 \text{ true})
$$

## Step 2 — Check why a $z$-test is being used

The video uses a one-sample $z$-test because:

- the sample is random [→ 2.2.5 @ 08:28]
- the outcome (delivery time) is continuous [→ 2.2.5 @ 08:00]
- the sample size is large: $n=45>30$, so the sampling distribution of $\bar{x}$ is approximately normal by the CLT [→ 2.2.5 @ 08:10] [→ 2.2.5 @ 10:12]
- the population standard deviation is treated as known: $\sigma=1.3$ [→ 2.2.5 @ 08:24] [→ 2.2.5 @ 09:31]

So the test statistic is the usual [[Z-Score]]:

$$
z = \frac{\bar{x}-\mu_0}{\sigma/\sqrt{n}}
$$

## Step 3 — Compute the test statistic

Substitute the lecture's numbers:

$$
z = \frac{5.25-5}{1.3/\sqrt{45}} \approx 1.29
$$

So the sample mean is about $1.29$ standard errors above the null mean. [→ 2.2.5 @ 10:50] [→ 2.2.5 @ 11:40]

## Step 4 — Compute the p-value

For a right-tailed test, the p-value is the area to the **right** of the observed $z$ value under the standard normal curve:

$$
p\text{-value} = P(Z \ge 1.29) = 1-\Phi(1.29) \approx 0.0985
$$

The lecture describes this as the probability of seeing a result this large or larger if the null model were true. [→ 2.2.5 @ 01:55] [→ 2.2.5 @ 12:59] [→ 2.2.5 @ 13:42]

Because

$$
0.0985 > 0.05,
$$

we **fail to reject** $H_0$. [→ 2.2.5 @ 18:25] [→ 2.2.5 @ 19:14]

## Step 5 — Critical-value view of the same decision

The equivalent rejection-region rule is:

$$
\text{Reject } H_0 \text{ if } z > z_{1-\alpha}
$$

At $\alpha=0.05$,

$$
z_{1-\alpha} = z_{0.95} \approx 1.645
$$

Since

$$
1.29 < 1.645,
$$

the test statistic is **not** in the rejection region, so we again fail to reject $H_0$. [→ 2.2.5 @ 15:08] [→ 2.2.5 @ 16:30]

This is the key equivalence:

- critical-value view: $1.29 < 1.645$
- p-value view: $0.0985 > 0.05$

Both rules give the same conclusion. [→ 2.2.5 @ 17:08] [→ 2.2.5 @ 18:53]

## Final conclusion in context

The sample mean $5.25$ is **above** $5$, but not by enough to be statistically significant at the $5\%$ level. The correct conclusion is:

> Fail to reject $H_0$; there is insufficient evidence that the mean delivery time now exceeds $5$ days.

That is a classic quiz trap: a sample mean larger than the null value does **not** automatically imply significance. [→ 2.2.5 @ 19:20] [→ 2.2.5 @ 20:16]

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
p_value = norm.sf(z)          # right-tail probability
z_crit = norm.isf(alpha)      # right-tail critical value

print(z)       # 1.290039...
print(p_value) # 0.098518...
print(z_crit)  # 1.644853...

if p_value < alpha:
    print("Reject H0")
else:
    print("Fail to reject H0")
```

## Summary

- A full hypothesis test combines **hypotheses, assumptions, a test statistic, a p-value, and a conclusion**.
- In this example,

$$
H_0: \mu=5, \quad H_a: \mu>5, \quad z\approx1.29, \quad p\approx0.0985
$$

- Because $p > 0.05$, we **fail to reject** $H_0$.
- Equivalent rule: because $1.29 < 1.645$, the statistic is not in the rejection region.
- Quiz-critical fact: **"above the null" is not enough**; it must be extreme enough under the null model.
- Quiz-critical fact: say **fail to reject**, not **accept** $H_0$.
