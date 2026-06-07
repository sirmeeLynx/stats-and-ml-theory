---
sources:
  - video: "2.1.1 Introduction and Agenda"
    course_id: 141734
    item_id: 7718500
    duration: "03:57"
  - video: "2.1.2 Introduction to Inferential Statistics"
    course_id: 141734
    item_id: 7718502
    duration: "22:11"
---

# Inferential Statistics

Inferential statistics uses a **sample** to learn about a larger **population**. It is the part of statistics that moves from describing observed data to making estimates, comparisons, and decisions under uncertainty. [→ 2.1.1 @ 00:22]

*Note: the exported `2.1.2` VTT file is empty, so the timestamps below come from `2.1.1` and nearby 2.1 lectures that introduce and apply the same inferential-statistics ideas.*

## Core idea: sample \(\rightarrow\) population

The course frames this section as the move from descriptive statistics to conclusions with business value: we observe a sample, but we care about the full population. [→ 2.1.1 @ 00:29] [→ 2.1.1 @ 02:11]

A few core symbols are worth memorizing:

- Population mean: $\mu$
- Population proportion: $p$
- Sample mean: $\bar{x}$
- Sample proportion: $\hat{p}$

A sample statistic is used as an estimate of a population parameter:

$$
\hat{\mu} = \bar{x}, \qquad \hat{p} = \frac{x}{n}
$$

## Why probability distributions matter

The agenda explicitly introduces **random variables** and **probability distributions** before topics like binomial, uniform, normal, sampling, and estimation. [→ 2.1.1 @ 00:50] [→ 2.1.1 @ 01:34]

This matters because inference is never just “one number from one sample.” It depends on the idea that repeated samples would vary, and probability distributions describe that variation.

## What inferential statistics is used for

Use inferential statistics when:

- you only observe part of a population,
- you need to estimate an unknown population quantity,
- you want to attach uncertainty to that estimate,
- or you need to generalize from data to decisions. [→ 2.1.1 @ 02:58]

This section of the course leads directly into [[distribution-terms|distribution terms]], the [[binomial-distribution|binomial distribution]], the [[uniform-distribution|uniform distribution]], the [[Normal Distribution]], [[z-score|Z-Score]], [[sampling-and-inference|sampling and inference]], [[central-limit-theorem|Central Limit Theorem]], and [[estimation|estimation]].

## Point estimates vs interval estimates

A **point estimate** gives one best-guess number, such as $\bar{x}$ for $\mu$.

An **interval estimate** gives a plausible range:

$$
\text{estimate} \pm \text{margin of error}
$$

The agenda names estimation as both a single-number and interval-based task. [→ 2.1.1 @ 02:58]

## Python hands-on

A simple way to see inference is to compare a population value to the value from one random sample.

```python
import numpy as np

np.random.seed(7)

# large synthetic population
population = np.random.normal(loc=72, scale=8, size=100_000)
mu = population.mean()

# one sample from that population
sample = np.random.choice(population, size=120, replace=False)
xbar = sample.mean()
s = sample.std(ddof=1)

print(mu)    # population mean (unknown in real life)
print(xbar)  # sample mean used to estimate mu
print(s)     # sample standard deviation
```

In real inferential problems, you only see the sample, so $\bar{x}$ and $s$ are what you compute directly.

## Summary

- Inferential statistics uses a **sample** to say something about a **population**.
- Sample quantities are **statistics**; population quantities are **parameters**.
- Probability distributions are essential because sample results vary from one sample to another.
- Point estimates give one value; interval estimates add uncertainty.
- Quiz mindset: always ask **what is observed (sample)** and **what is being inferred (population)**.
