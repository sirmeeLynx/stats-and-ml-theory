---
sources:
  - video: "2.1.11 Sampling and Inference Foundations"
    course_id: 141734
    item_id: 7718524
    duration: "09:16"
---

# Sampling and Inference

A sample is only a finite slice of a larger population, but business decisions usually care about the whole population. This note is about how that jump is made. [→ 2.1.11 @ 00:41] [→ 2.1.11 @ 01:28]

## Representative samples matter

The lecture stresses that inference only makes sense if the sample is representative of the population. A simple way to formalize that is a **simple random sample**, where every member of the population has an equal chance of being chosen. [→ 2.1.11 @ 02:19] [→ 2.1.11 @ 02:39]

This is the sampling foundation underneath [[inferential-statistics|inferential statistics]].

## Sampling distribution

A **sampling distribution** is the distribution of a statistic over many repeated samples. If two analysts each draw a sample of size 100, they will generally get different values of the sample mean $\bar{X}$. The distribution of all those possible $\bar{X}$ values is the sampling distribution. [→ 2.1.11 @ 03:28] [→ 2.1.11 @ 04:24]

## Key facts for the sample mean

If the population has mean $\mu$ and standard deviation $\sigma$, then the lecture gives two crucial results for the sampling distribution of $\bar{X}$:

$$
E[\bar{X}] = \mu
$$

$$
\operatorname{SD}(\bar{X}) = \frac{\sigma}{\sqrt{n}}
$$

Equivalently,

$$
\operatorname{Var}(\bar{X}) = \frac{\sigma^2}{n}
$$

The quantity $\sigma/\sqrt{n}$ is the **standard error** of the sample mean. [→ 2.1.11 @ 06:39] [→ 2.1.11 @ 07:00] [→ 2.1.11 @ 08:10]

## Why larger samples help

The lecture's intuition is cancellation: large and small values average each other out, so the variability of the sample mean is smaller than the variability of individual observations. As $n$ grows, $\sigma/\sqrt{n}$ gets smaller, so the estimate becomes more stable. [→ 2.1.11 @ 07:19] [→ 2.1.11 @ 08:00]

## One subtle but important fact

These two properties of the sample mean do **not** depend on the population being normal. The lecture explicitly says that $E[\bar{X}]=\mu$ and $\operatorname{SD}(\bar{X})=\sigma/\sqrt{n}$ hold even when the population distribution itself is not normal. [→ 2.1.11 @ 08:38]

The next question is whether the **shape** of the sampling distribution becomes normal. That is exactly the topic of the [[central-limit-theorem|Central Limit Theorem]]. [→ 2.1.11 @ 09:05]

## Python hands-on

```python
import numpy as np

np.random.seed(42)
population = np.random.exponential(scale=10, size=100_000)
mu = population.mean()
sigma = population.std(ddof=0)

n = 25
sample_means = np.array([
    np.random.choice(population, size=n, replace=True).mean()
    for _ in range(2000)
])

print(sample_means.mean())      # close to mu
print(sample_means.std(ddof=1)) # close to sigma / sqrt(n)
print(sigma / np.sqrt(n))
```

## Summary

- A **sampling distribution** is the distribution of a statistic across repeated samples.
- For the sample mean, the center is $\mu$ and the spread is $\sigma/\sqrt{n}$.
- $\sigma/\sqrt{n}$ is the **standard error**.
- Larger samples reduce sampling variability.
- Quiz mindset: distinguish the **population distribution** from the **sampling distribution of a statistic**.
