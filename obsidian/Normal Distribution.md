---
sources:
  - video: "2.1.8 Normal Distributions Theory"
    course_id: 141734
    item_id: 7718516
    duration: "17:00"
  - video: "2.1.9 Normal Distributions Hands-On"
    course_id: 141734
    item_id: 7718519
    duration: "14:10"
---

# Normal Distribution

The normal distribution is the most important continuous distribution in this section: it is symmetric, bell-shaped, and fully determined by a [[Mean]] $\mu$ and a [[Standard Deviation]] $\sigma$. [→ 2.1.8 @ 00:12] [→ 2.1.8 @ 01:39]

## Key properties

The lecture highlights the following facts:

- The curve is symmetric around the mean. [→ 2.1.8 @ 01:02]
- The center and spread are controlled by $\mu$ and $\sigma$. [→ 2.1.8 @ 01:39]
- For a normal distribution, mean = median = mode. [→ 2.1.8 @ 06:41]
- In the population notation of the course, $\mu$ and $\sigma$ are parameters; sample analogues are $\bar{x}$ and $s$. [→ 2.1.8 @ 03:20]

The density function is

$$
f(x)=\frac{1}{\sigma\sqrt{2\pi}}\exp\left(-\frac{(x-\mu)^2}{2\sigma^2}\right)
$$

## Empirical rule: 68-95-99.7

For a normal distribution:

- about 68% of values lie within 1 standard deviation of the mean,
- about 95% lie within 2 standard deviations,
- about 99.7% lie within 3 standard deviations. [→ 2.1.8 @ 08:09]

This is often called the **empirical rule**.

If the mean delivery time is 40 and the SD is 10, then the lecture uses these quick intervals: [→ 2.1.8 @ 10:14]

- roughly 68% between 30 and 50,
- roughly 95% between 20 and 60,
- roughly 99.7% between 10 and 70.

## Standard normal and z-scores

Any normal variable can be standardized using a [[z-score|z-score]]:

$$
z=\frac{x-\mu}{\sigma}
$$

This converts $X \sim N(\mu,\sigma^2)$ into the **standard normal** with mean 0 and SD 1.

## When to use it

Use the normal distribution when:

- the variable is continuous,
- the distribution is approximately symmetric and bell-shaped,
- or the problem explicitly states a normal model.

It is also central to inference because of the [[central-limit-theorem|Central Limit Theorem]].

## Python hands-on

The hands-on lecture estimates exam-score parameters around $\mu \approx 1007.46$ and $\sigma \approx 204.43$, then uses SciPy to answer probability and percentile questions. [→ 2.1.9 @ 03:29]

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

mu, sigma = 1007.46, 204.43
rv = norm(loc=mu, scale=sigma)

x = np.linspace(mu - 4 * sigma, mu + 4 * sigma, 400)
pdf = rv.pdf(x)

p_lt_800 = rv.cdf(800)         # about 0.155
p_gt_1300 = 1 - rv.cdf(1300)   # about 0.076
p90 = rv.ppf(0.90)             # about 1269.45
p95 = rv.ppf(0.95)             # about 1343.72

plt.plot(x, pdf)
plt.xlabel('score')
plt.ylabel('density')
plt.title('Normal Distribution')
plt.show()
```

Lecture values worth remembering:

- $P(X<800) \approx 0.155$ [→ 2.1.9 @ 07:01]
- 90th percentile $\approx 1269$ [→ 2.1.9 @ 10:40]
- 95th percentile $\approx 1344$ [→ 2.1.9 @ 10:40]

## Summary

- A normal distribution is a symmetric bell-shaped continuous distribution.
- It is fully specified by $\mu$ and $\sigma$.
- Mean = median = mode.
- Empirical rule: **68% / 95% / 99.7%** within 1 / 2 / 3 SDs.
- Use CDFs for probabilities and inverse CDFs (percentiles) for cutoff values.

