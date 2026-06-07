---
sources:
  - video: "2.1.12 Central Limit Theorem Theory"
    course_id: 141734
    item_id: 7718527
    duration: "03:44"
  - video: "2.1.13 Central Limit Theorem Hands-On"
    course_id: 141734
    item_id: 7718530
    duration: "13:57"
---

# Central Limit Theorem

The **Central Limit Theorem (CLT)** says that the sampling distribution of the sample mean becomes approximately normal as the sample size grows, no matter what the population distribution looks like. [→ 2.1.12 @ 00:14] [→ 2.1.12 @ 00:21]

## Why it matters

This is the main reason the normal distribution appears everywhere in inference. Even if the population itself is skewed or bimodal, the average of many observations tends to have a bell-shaped sampling distribution. [→ 2.1.12 @ 01:57] [→ 2.1.12 @ 03:31]

A compact statement is

$$
\bar{X} \approx N\left(\mu, \frac{\sigma^2}{n}\right)
$$

so the standard error is

$$
\operatorname{SE}(\bar{X}) = \frac{\sigma}{\sqrt{n}}
$$

## Conditions from the lecture

The lecture gives two main conditions for the approximation to work well:

- the data should be randomly sampled,
- the sampled values should be independent. [→ 2.1.12 @ 00:53] [→ 2.1.12 @ 01:05]

## What changes as $n$ increases

As sample size grows:

- the distribution of $\bar{X}$ becomes more normal, [→ 2.1.12 @ 01:30]
- the sample means cluster more tightly around $\mu$, [→ 2.1.12 @ 02:54]
- because $\sigma/\sqrt{n}$ gets smaller. [→ 2.1.12 @ 02:54]

## What the hands-on lecture shows

The simulation repeats the same basic experiment many times: draw a sample, compute its mean, and then study the histogram of those means. [→ 2.1.13 @ 02:14] [→ 2.1.13 @ 03:18]

### Uniform parent distribution

For a uniform population:

- with $n=5$, a bell shape has started to appear but is still rough, [→ 2.1.13 @ 03:56] [→ 2.1.13 @ 04:25]
- with $n=15$, the sampling distribution looks more normal, [→ 2.1.13 @ 04:30] [→ 2.1.13 @ 05:08]
- with $n=30$, the “magic number” rule of thumb gives a decent normal approximation, [→ 2.1.13 @ 05:15] [→ 2.1.13 @ 05:48]
- with $n=50$, the curve is smoother and even closer to normal. [→ 2.1.13 @ 06:12] [→ 2.1.13 @ 06:27]

### Normal parent distribution

If the population itself is normal, then even fairly small samples already give a normal sample mean. The lecture shows this with a simulated normal population and sample size 5. [→ 2.1.13 @ 07:15] [→ 2.1.13 @ 08:13]

### Exponential parent distribution

For a highly skewed exponential population:

- with $n=5$, the skew is still visible in the sample means, [→ 2.1.13 @ 10:55] [→ 2.1.13 @ 11:18]
- with $n=15$, the asymmetry starts fading, [→ 2.1.13 @ 11:24] [→ 2.1.13 @ 11:40]
- with $n=30$, the histogram is close to bell-shaped, [→ 2.1.13 @ 12:05] [→ 2.1.13 @ 12:30]
- with $n=50$, the skewness has effectively disappeared. [→ 2.1.13 @ 13:05] [→ 2.1.13 @ 13:20]

The lecture's memory trick is excellent: **averages of things tend to be more normally distributed**. [→ 2.1.13 @ 13:36]

## Python hands-on

```python
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

np.random.seed(1)
population = np.random.exponential(scale=1.0, size=100_000)

def sample_means(n, reps=500):
    return np.array([
        np.random.choice(population, size=n, replace=True).mean()
        for _ in range(reps)
    ])

means_5 = sample_means(5)
means_15 = sample_means(15)
means_30 = sample_means(30)
means_50 = sample_means(50)

fig, axes = plt.subplots(1, 4, figsize=(14, 3))
for ax, means, n in zip(axes, [means_5, means_15, means_30, means_50], [5, 15, 30, 50]):
    sns.histplot(means, kde=True, ax=ax)
    ax.set_title(f'n={n}')
plt.tight_layout()
plt.show()
```

## Summary

- CLT: the sampling distribution of $\bar{X}$ approaches normality as $n$ increases.
- Standard error shrinks as $\sigma/\sqrt{n}$.
- Random sampling and independence are the key conditions highlighted in the lecture.
- If the population is already normal, small samples are fine; if not, larger samples help.
- Quiz-critical fact: CLT is about the **distribution of sample means**, not the raw population data.
