---
sources:
  - video: "2.2.1 Introduction to Hypothesis Testing"
    course_id: 141734
    item_id: 7718540
    duration: "18:44"
---

# Hypothesis Testing

Hypothesis testing asks whether sample data give **strong enough evidence** against a status-quo claim about a population parameter. The course introduces it as the next step after probability, sampling, and [[Estimation]]. [→ 2.2.1 @ 00:18] [→ 2.2.1 @ 11:55]

## From a sample to a population claim

The opening example is a bulb factory whose historical reliability rate is $70\%$. After a process change, a sample of $100$ bulbs contains $73$ reliable bulbs. The real question is not just whether $73 > 70$, but whether that sample result is strong evidence that the **population reliability** has improved. [→ 2.2.1 @ 02:00] [→ 2.2.1 @ 03:24] [→ 2.2.1 @ 04:22]

This is the core move of [[Inferential Statistics]]: use a sample to judge a statement about the population. [→ 2.2.1 @ 03:05]

## The null-model logic

The lecture's key idea is: **assume the old process is still true**, then ask how likely the observed sample would be just from sampling variation. [→ 2.2.1 @ 04:42] [→ 2.2.1 @ 10:29]

For the bulb example, that means asking:

$$
P(X \ge 73 \mid X \sim \operatorname{Binomial}(100, 0.70))
$$

If this probability is large, the sample is still plausible under the old process, so there is weak evidence against the status quo. If it is very small, the sample is hard to explain under the old process, so we have strong evidence that something changed. [→ 2.2.1 @ 05:42] [→ 2.2.1 @ 10:47]

## Why $73/100$ is weak evidence but $81/100$ is strong evidence

The lecture contrasts two samples drawn under the same historical benchmark of $70\%$:

- With **$73$ reliable bulbs out of $100$**, the right-tail probability is about **$0.30$**. That is too common to count as strong evidence of improvement. [→ 2.2.1 @ 06:37] [→ 2.2.1 @ 06:58] [→ 2.2.1 @ 07:31]
- With **$81$ reliable bulbs out of $100$**, the right-tail probability is about **$0.01$**. That is rare enough to be convincing evidence that the process has improved. [→ 2.2.1 @ 08:47] [→ 2.2.1 @ 09:30] [→ 2.2.1 @ 10:16]

So hypothesis testing is not about whether a sample estimate is numerically bigger than the old value. It is about whether the observed difference is **too large to be explained by chance alone**. [→ 2.2.1 @ 08:02] [→ 2.2.1 @ 12:15]

## Beyond estimation

A point estimate like $\hat p = 0.73$ or $\hat p = 0.81$ is useful, but the lecture stresses that hypothesis testing asks a different question:

> Is the estimate **significantly** different from the benchmark, or could sampling variation explain it?

[→ 2.2.1 @ 11:55] [→ 2.2.1 @ 12:10] [→ 2.2.1 @ 13:06]

A hypothesis is therefore a **statement about a population parameter**, such as a mean or a proportion, that the data will challenge or support. [→ 2.2.1 @ 14:11] [→ 2.2.1 @ 14:47]

See also [[Null and Alternative Hypothesis]], [[p-value and Significance]], and [[Hypothesis Test Procedure]].

## Python hands-on

The bulb example can be reproduced with an exact one-sided binomial test:

```python
from scipy.stats import binomtest

# Historical reliability is 70%; test whether the new process is better.
result_73 = binomtest(k=73, n=100, p=0.70, alternative='greater')
result_81 = binomtest(k=81, n=100, p=0.70, alternative='greater')

print(result_73.pvalue)  # about 0.30
print(result_81.pvalue)  # about 0.01
```

A normal approximation gives the same intuition:

```python
from math import sqrt
from scipy.stats import norm

p0 = 0.70
n = 100
phat = 0.81

z = (phat - p0) / sqrt(p0 * (1 - p0) / n)
p_value = norm.sf(z)

print(z)
print(p_value)
```

## Summary

- Hypothesis testing starts with a **status-quo model** and asks whether the sample is too extreme under that model.
- A sample estimate alone is not enough; the key question is whether it is **significantly** different from the benchmark.
- In the lecture's bulb example, $73/100$ is still plausible under $70\%$, but $81/100$ is much harder to explain by chance.
- Quiz mindset: testing is about **population claims**, not just sample values.
