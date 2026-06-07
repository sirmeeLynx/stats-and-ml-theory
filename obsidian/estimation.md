---
sources:
  - video: "2.1.14 Estimation"
    course_id: 141734
    item_id: 7718532
    duration: "07:57"
  - video: "2.1.15 Estimation Hands-On"
    course_id: 141734
    item_id: 7718535
    duration: "12:45"
---

# Estimation

Estimation is the idea that information from a sample can be carried over to an unknown population parameter. The lecture presents it as a direct form of inference from sample statistics to population quantities. [→ 2.1.14 @ 00:06] [→ 2.1.14 @ 00:41]

## Parameter vs statistic

A **parameter** is an unknown numerical description of a population. A **statistic** is a number computed from the sample. [→ 2.1.14 @ 00:45]

Common pairs to remember:

- population mean $\mu$ vs sample mean $\bar{x}$,
- population standard deviation $\sigma$ vs sample standard deviation $s$,
- population variance $\sigma^2$ vs sample variance $s^2$. [→ 2.1.14 @ 03:24] [→ 2.1.14 @ 03:57]

## Point estimation

A **point estimate** uses one sample value to stand in for the unknown parameter. [→ 2.1.14 @ 01:11]

The wildfire example gives a sample mean of 69 thousand dollars, so the point estimate of expected wildfire damage is $69{,}000$. [→ 2.1.15 @ 00:19] [→ 2.1.15 @ 01:19]

For the population mean, the standard point estimate is

$$
\hat{\mu}=\bar{x}
$$

## Interval estimation and confidence intervals

The lecture then improves on point estimation by adding uncertainty. Instead of reporting just one number, we report a range. [→ 2.1.14 @ 02:23] [→ 2.1.14 @ 04:22]

The lecture's generic shape is

$$
\bar{x} - E \le \mu \le \bar{x} + E
$$

or more compactly,

$$
\text{estimate} \pm \text{margin of error}
$$

For means, the common forms are

$$
\bar{x} \pm z_{\alpha/2}\frac{\sigma}{\sqrt{n}}
$$

when population standard deviation is known, and

$$
\bar{x} \pm t_{\alpha/2,\,n-1}\frac{s}{\sqrt{n}}
$$

when it is estimated from the sample.

## Standard error

The lecture repeatedly distinguishes the **standard deviation of individual observations** from the **standard error of the sample mean**. For the mean,

$$
\operatorname{SE}(\bar{X})=\frac{\sigma}{\sqrt{n}}
$$

or, in practice,

$$
\operatorname{SE}(\bar{X})\approx\frac{s}{\sqrt{n}}
$$

This is the source of the uncertainty band around $\bar{x}$. [→ 2.1.14 @ 04:22] [→ 2.1.15 @ 05:08] [→ 2.1.15 @ 06:25]

## Correct interpretation of a 95% confidence interval

The statistically correct interpretation comes from the theory lecture: if we repeated the sampling process many times and rebuilt the interval each time, about 95% of those intervals would contain the true parameter. [→ 2.1.14 @ 06:18]

That repeated-sampling interpretation is the safest one to use in quizzes.

## Coffee machine example

In the hands-on example, a sample of 50 cups of black coffee gives:

- $n=50$,
- sample mean $\bar{x}=110$ milligrams,
- sample standard deviation $s=7$ milligrams. [→ 2.1.15 @ 03:13] [→ 2.1.15 @ 04:02]

Using a normal-based interval, the lecture gets about 108.06 to 111.94. [→ 2.1.15 @ 05:38] [→ 2.1.15 @ 06:10]

Using a t-interval with $n-1=49$ degrees of freedom, the result is about 108.01 to 111.99. [→ 2.1.15 @ 10:46] [→ 2.1.15 @ 11:19]

## Why t instead of z?

The lecture explains that when the population standard deviation is unknown and is estimated from the sample, the **t-distribution** is more correct. It is very close to the normal distribution, and by sample sizes around 30 or more the two become nearly indistinguishable. [→ 2.1.15 @ 08:12] [→ 2.1.15 @ 09:54]

## Python hands-on

```python
import numpy as np
from scipy.stats import norm, t

xbar, s, n = 110, 7, 50
se = s / np.sqrt(n)

z_ci = norm.interval(0.95, loc=xbar, scale=se)
t_ci = t.interval(0.95, df=n - 1, loc=xbar, scale=se)

print(se)
print(z_ci)  # about (108.06, 111.94)
print(t_ci)  # about (108.01, 111.99)
```

## Summary

- A **point estimate** gives one best-guess value; an **interval estimate** adds uncertainty.
- Confidence intervals are built from **estimate ± margin of error**.
- The standard error of the mean is $\sigma/\sqrt{n}$ or $s/\sqrt{n}$.
- Use **t** when the population standard deviation is unknown and estimated from the sample.
- Quiz-critical fact: a 95% confidence level refers to the **procedure over repeated samples**, not a probability attached to one fixed observed interval.
