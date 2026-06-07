---
sources:
  - video: "2.1.14 Estimation"
    course_id: 141734
    item_id: 7718532
    duration: "07:57"
  - video: "2.1.15 Estimation Hands-On"
    course_id: 141734
    item_id: 7718535
    duration: "12:46"
---

# Estimation

Estimation uses sample statistics to learn about unknown population parameters. The lecture presents it as the direct bridge from data to inference. [→ 2.1.14 @ 00:10]

## Parameter vs statistic

A **parameter** is a number that describes a population, while a **statistic** is computed from a sample. [→ 2.1.14 @ 00:47]

Examples:

- population mean $\mu$ vs sample mean $\bar{x}$,
- population proportion $p$ vs sample proportion $\hat{p}$,
- population SD $\sigma$ vs sample SD $s$.

## Point estimation

A **point estimate** is one best-guess value for a parameter. [→ 2.1.14 @ 01:13]

For the population mean, the usual point estimate is

$$
\hat{\mu}=\bar{x}
$$

The hands-on lecture gives a wildfire-damage example with a point estimate of $69$ thousand dollars. [→ 2.1.15 @ 01:18]

## Interval estimation and confidence intervals

An **interval estimate** gives a range of plausible values instead of a single number. [→ 2.1.14 @ 02:22]

Confidence intervals have the general form

$$
\text{estimate} \pm \text{margin of error}
$$

For a mean with known population SD,

$$
\bar{x} \pm z_{\alpha/2}\frac{\sigma}{\sqrt{n}}
$$

For a mean with unknown population SD, use the sample SD and a t critical value:

$$
\bar{x} \pm t_{\alpha/2,\,n-1}\frac{s}{\sqrt{n}}
$$

The standard error is therefore

$$
\operatorname{SE}(\bar{X})=\frac{\sigma}{\sqrt{n}} \quad \text{or} \quad \frac{s}{\sqrt{n}}
$$

## Correct confidence-interval interpretation

This is a common quiz trap.

A 95% confidence interval does **not** mean “there is a 95% probability that the parameter is inside this specific observed interval.”

The correct interpretation is: if we repeatedly took samples and built intervals the same way, about 95% of those intervals would contain the true parameter. [→ 2.1.14 @ 06:22]

## Python hands-on

The lecture's coffee-machine example uses $n=50$, $\bar{x}=110$, and $s\approx 7$. [→ 2.1.15 @ 03:17]

```python
import numpy as np
from scipy.stats import norm, t

xbar, s, n = 110, 7, 50
se = s / np.sqrt(n)

# normal-based interval
z_critical = norm.ppf(0.975)
z_margin = z_critical * se
z_ci = (xbar - z_margin, xbar + z_margin)

# t-based interval (preferred when sigma is unknown)
t_critical = t.ppf(0.975, df=n - 1)
t_margin = t_critical * se
t_ci = (xbar - t_margin, xbar + t_margin)

print(se)
print(z_ci)  # about (108.06, 111.94)
print(t_ci)  # about (108.01, 111.99)
```

The lecture also emphasizes that the **standard error**, not the raw SD, is what appears in the confidence interval formula. [→ 2.1.15 @ 05:12]

## When to use z vs t

- Use a **z interval** when the population SD $\sigma$ is known.
- Use a **t interval** when $\sigma$ is unknown and you substitute the sample SD $s$.
- As $n$ gets large, the t interval and z interval become very similar.

## Summary

- A **point estimate** gives one number; an **interval estimate** gives a range.
- For means, the core CI shape is $\bar{x} \pm \text{critical value} \times \text{SE}$.
- Standard error is $\sigma/\sqrt{n}$ or $s/\sqrt{n}$.
- Use **t** instead of **z** when the population SD is unknown.
- Quiz mindset: confidence refers to the **procedure over repeated samples**, not a probability attached to one fixed parameter after the fact.
