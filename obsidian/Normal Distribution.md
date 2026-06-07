---
sources:
  - video: "2.1.8 Normal Distributions Theory"
    course_id: 141734
    item_id: 7718516
    duration: "16:59"
  - video: "2.1.9 Normal Distributions Hands-On"
    course_id: 141734
    item_id: 7718519
    duration: "14:09"
---

# Normal Distribution

The normal distribution is the course's most important continuous model: a symmetric bell-shaped curve where values near the middle are more likely than values far into the tails. [→ 2.1.8 @ 00:14] [→ 2.1.8 @ 01:03]

## Parameters and shape

The lecture emphasizes that the normal distribution is described by two population parameters: the mean $\mu$ and the standard deviation $\sigma$. Their sample counterparts are $\bar{x}$ and $s$. [→ 2.1.8 @ 01:40] [→ 2.1.8 @ 03:22]

The probability density function is

$$
f(x)=\frac{1}{\sigma\sqrt{2\pi}}\exp\left(-\frac{(x-\mu)^2}{2\sigma^2}\right)
$$

## Mean, median, and mode line up

Because the curve is symmetric, its center is uniquely defined:

- the **mean** is the balance point,
- the **median** splits the distribution into 50% below and 50% above,
- the **mode** is the peak. [→ 2.1.8 @ 06:08] [→ 2.1.8 @ 07:02]

For a normal distribution, these three are all at the same location.

## Empirical rule: 68-95-99.7

The lecture's main shortcut is the empirical rule:

- about 68% of observations lie within $\mu \pm \sigma$, [→ 2.1.8 @ 08:10]
- about 95% lie within $\mu \pm 2\sigma$, [→ 2.1.8 @ 08:55]
- about 99.7% lie within $\mu \pm 3\sigma$. [→ 2.1.8 @ 09:17]

The delivery-time example uses mean 40 minutes and standard deviation 10 minutes, so the quick intervals are 30 to 50, 20 to 60, and 10 to 70 minutes. [→ 2.1.8 @ 10:16] [→ 2.1.8 @ 11:05]

## Standardization and the standard normal

Any normal variable can be translated to the **standard normal** by subtracting the mean and dividing by the standard deviation. The resulting distribution has mean 0 and standard deviation 1. [→ 2.1.8 @ 14:24] [→ 2.1.8 @ 15:10]

This is the bridge to the [[z-score|z-score]].

## Hands-on: SAT score model

In the hands-on lecture, the sample of SAT scores gives an estimated mean of 1007.46 and an estimated standard deviation of 204.43. These are then used to define a normal model for the population. [→ 2.1.9 @ 03:31]

A useful visual idea from the lecture:

- the **blue** curve is the empirical density of the data,
- the **red** curve is the normal PDF with the same mean and standard deviation,
- if they track closely, the normal model is a reasonable approximation. [→ 2.1.9 @ 05:38] [→ 2.1.9 @ 06:18]

The lecture then uses the normal model to answer:

- $P(X<800) \approx 0.155$ [→ 2.1.9 @ 06:54] [→ 2.1.9 @ 08:02]
- $P(X>1300) \approx 0.07$ [→ 2.1.9 @ 08:16] [→ 2.1.9 @ 09:10]
- 90th percentile $\approx 1269$ [→ 2.1.9 @ 10:36] [→ 2.1.9 @ 11:05]
- 95th percentile $\approx 1344$ [→ 2.1.9 @ 12:15] [→ 2.1.9 @ 12:24]

## Python hands-on

```python
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import norm

mu, sigma = 1007.46, 204.43
rv = norm(loc=mu, scale=sigma)

x = np.linspace(mu - 4 * sigma, mu + 4 * sigma, 400)
pdf = rv.pdf(x)

p_lt_800 = rv.cdf(800)
p_gt_1300 = 1 - rv.cdf(1300)
p90 = rv.ppf(0.90)
p95 = rv.ppf(0.95)

plt.plot(x, pdf, color='crimson', label='normal PDF')
plt.axvline(800, color='gray', linestyle='--')
plt.axvline(1300, color='gray', linestyle='--')
plt.legend()
plt.show()
```

## Summary

- A normal distribution is a **symmetric bell-shaped** continuous distribution.
- It is determined by $\mu$ and $\sigma$.
- Mean = median = mode.
- Empirical rule: **68% / 95% / 99.7%** within 1 / 2 / 3 standard deviations.
- Quiz mindset: use the empirical rule for quick checks, then use CDF or PPF for exact calculations.
