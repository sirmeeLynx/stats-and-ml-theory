---
sources:
  - video: "2.1.12 Central Limit Theorem Theory"
    course_id: 141734
    item_id: 7718527
    duration: "03:45"
  - video: "2.1.13 Central Limit Theorem Hands-On"
    course_id: 141734
    item_id: 7718530
    duration: "13:58"
---

# Central Limit Theorem

The **Central Limit Theorem (CLT)** says that the sampling distribution of the sample mean becomes approximately normal as the sample size grows, even when the original population is not normal. [→ 2.1.12 @ 00:13]

## Why it matters

The CLT is the reason normal-based inference works so often in practice. It connects [[sampling-and-inference|sampling distributions]] to the [[Normal Distribution]].

For large $n$,

$$
\bar{X} \approx N\left(\mu, \frac{\sigma^2}{n}\right)
$$

So the center stays at $\mu$, while the spread shrinks to $\sigma/\sqrt{n}$.

## Conditions and interpretation

The lecture stresses that samples should be randomly collected and independent, and should reasonably represent the population. [→ 2.1.12 @ 00:54]

A few quiz-safe statements:

- If the population is already normal, the sample mean is normal for **any** $n$.
- If the population is not normal, the approximation improves as $n$ grows.
- $n=30$ is a common rule of thumb, not a universal law. [→ 2.1.13 @ 05:17]

## What the hands-on lecture shows

The simulation repeatedly samples from different population shapes and plots the resulting sample means.

- Uniform populations already produce a more bell-shaped distribution of means for modest $n$. [→ 2.1.13 @ 02:31]
- Increasing the sample size from 5 to 15 makes the distribution of means look more normal. [→ 2.1.13 @ 04:28]
- Even for a skewed exponential population, sample means with $n=30$ or $n=50$ look much closer to normal. [→ 2.1.13 @ 09:27]

## Python hands-on

```python
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

np.random.seed(1)

population = np.random.exponential(scale=1.0, size=100_000)

means_5 = [np.random.choice(population, size=5, replace=True).mean() for _ in range(500)]
means_30 = [np.random.choice(population, size=30, replace=True).mean() for _ in range(500)]
means_50 = [np.random.choice(population, size=50, replace=True).mean() for _ in range(500)]

fig, axes = plt.subplots(1, 3, figsize=(12, 3))
for ax, means, n in zip(axes, [means_5, means_30, means_50], [5, 30, 50]):
    sns.histplot(means, kde=True, ax=ax)
    ax.set_title(f'Sample means (n={n})')
plt.tight_layout()
plt.show()
```

The visible pattern should match the lecture: larger samples produce a more normal-looking sampling distribution and a tighter spread around the population mean. [→ 2.1.12 @ 02:53]

## Summary

- CLT: the sampling distribution of $\bar{X}$ approaches normality as $n$ increases.
- Approximate model: $\bar{X} \approx N(\mu, \sigma^2/n)$.
- The standard error is $\sigma/\sqrt{n}$.
- The theorem works even when the population is skewed or bimodal, provided the sample size is large enough.
- Quiz mindset: CLT is about the **distribution of sample means**, not the original raw data.
