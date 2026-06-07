---
sources:
  - video: "2.1.11 Sampling and Inference Foundations"
    course_id: 141734
    item_id: 7718524
    duration: "09:17"
---

# Sampling and Inference

A **sample** is a finite subset of a larger **population**, and inferential statistics uses the sample to say something about the population. [→ 2.1.11 @ 00:39] [→ 2.1.11 @ 01:27]

## Population, sample, parameter, statistic

These pairs are essential:

- **Population**: the full group you care about.
- **Sample**: the observed subset.
- **Parameter**: a population quantity such as $\mu$ or $p$.
- **Statistic**: a sample quantity such as $\bar{x}$ or $\hat{p}$.

This note sits directly on top of [[inferential-statistics|inferential statistics]].

## Simple random sampling

The lecture highlights **simple random sampling**: each member of the population should have an equal chance of selection. [→ 2.1.11 @ 02:36]

That matters because biased sampling produces biased inference.

## Sampling distribution

A **sampling distribution** is the distribution of a statistic over many repeated samples of the same size. [→ 2.1.11 @ 03:27]

For the sample mean $\bar{X}$, two results are especially important:

$$
E[\bar{X}] = \mu
$$

$$
\operatorname{Var}(\bar{X}) = \frac{\sigma^2}{n}
$$

$$
\operatorname{SE}(\bar{X}) = \frac{\sigma}{\sqrt{n}}
$$

The lecture emphasizes that the standard deviation of the sampling distribution of the mean is called the **standard error**. [→ 2.1.11 @ 08:09]

## Why larger samples help

As $n$ increases, $\sigma/\sqrt{n}$ decreases, so the sample mean varies less from sample to sample. Larger samples therefore give more stable estimates. [→ 2.1.11 @ 07:54]

A subtle but important point from the lecture: these mean and standard-error formulas still hold even if the original population is not normal. [→ 2.1.11 @ 08:37]

## Python hands-on

```python
import numpy as np

np.random.seed(42)
population = np.random.exponential(scale=10, size=100_000)
mu = population.mean()
sigma = population.std(ddof=0)

n = 25
sample_means = [
    np.random.choice(population, size=n, replace=True).mean()
    for _ in range(2_000)
]

sample_means = np.array(sample_means)
print(mu)                           # population mean
print(sample_means.mean())          # close to mu
print(sample_means.std(ddof=1))     # close to sigma / sqrt(n)
print(sigma / np.sqrt(n))
```

This is the computational version of the lecture's sampling-distribution story.

## Summary

- A **sampling distribution** is the distribution of a statistic across repeated samples.
- For the sample mean, $E[\bar{X}] = \mu$.
- The standard error of the mean is $\sigma/\sqrt{n}$.
- Larger samples reduce sampling variability.
- Quiz mindset: distinguish the **population distribution** from the **sampling distribution**.
