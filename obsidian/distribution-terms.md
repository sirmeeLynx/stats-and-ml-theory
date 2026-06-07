---
sources:
  - video: "2.1.1 Introduction and Agenda"
    course_id: 141734
    item_id: 7718500
    duration: "03:57"
  - video: "2.1.3 Fundamental Terms in Distributions"
    course_id: 141734
    item_id: 7718504
    duration: "21:06"
  - video: "2.1.4 Binomial Distributions Theory"
    course_id: 141734
    item_id: 7718506
    duration: "15:25"
  - video: "2.1.5 Binomial Distributions Hands-On"
    course_id: 141734
    item_id: 7718509
    duration: "16:20"
  - video: "2.1.11 Sampling and Inference Foundations"
    course_id: 141734
    item_id: 7718524
    duration: "09:17"
---

# Distribution Terms

Probability distributions describe how likely different outcomes are for a random variable. They are the language used throughout [[inferential-statistics|inferential statistics]] and the rest of this section. [→ 2.1.1 @ 01:03]

*Note: the exported `2.1.3` VTT file is empty, so the timestamps below come from nearby 2.1 lectures where the same vocabulary is defined and used.*

## Random variable

A **random variable** is a numeric outcome of a random process.

- In a binary setting, the lecture encodes outcomes as `1` for success and `0` for failure. [→ 2.1.4 @ 01:56]
- One experiment or **trial** produces one observed value of that random variable. [→ 2.1.4 @ 02:13]

## Discrete vs continuous distributions

A distribution can be:

- **Discrete**: it assigns probability to countable values.
- **Continuous**: it assigns density over an interval of values.

For a discrete distribution, probabilities add to 1:

$$
\sum_x P(X=x) = 1
$$

For a continuous distribution, density integrates to 1:

$$
\int_{-\infty}^{\infty} f(x)\,dx = 1
$$

A key quiz fact: for a continuous random variable, the probability of any **single exact value** is 0. Probabilities come from **intervals**, not points.

## PMF, PDF, and CDF

### PMF — probability mass function

Use a **PMF** for discrete random variables:

$$
p(x) = P(X=x)
$$

The binomial lecture explicitly introduces the PMF as the rule that gives the probability of each count. [→ 2.1.4 @ 04:18]

### PDF — probability density function

Use a **PDF** for continuous random variables:

$$
f(x) \ge 0, \qquad P(a \le X \le b) = \int_a^b f(x)\,dx
$$

### CDF — cumulative distribution function

The hands-on binomial lecture uses the CDF as “accumulated probability up to a threshold.” [→ 2.1.5 @ 10:14]

$$
F(x) = P(X \le x)
$$

## Mean, variance, and standard deviation

The most important numerical summaries of a distribution are [[Mean]], [[Variance]], and [[Standard Deviation]].

For a discrete random variable:

$$
\mu = E[X] = \sum_x x\,p(x)
$$

$$
\operatorname{Var}(X) = \sum_x (x-\mu)^2 p(x)
$$

$$
\sigma = \sqrt{\operatorname{Var}(X)}
$$

For a continuous random variable, replace the sums with integrals:

$$
\mu = E[X] = \int_{-\infty}^{\infty} x f(x)\,dx
$$

$$
\operatorname{Var}(X) = \int_{-\infty}^{\infty} (x-\mu)^2 f(x)\,dx
$$

In inference, these summaries matter again through the [[sampling-and-inference|sampling distribution]] and the [[central-limit-theorem|Central Limit Theorem]]. [→ 2.1.11 @ 03:27] [→ 2.1.11 @ 06:35]

## Python hands-on

This small snippet shows the three most common distribution functions in SciPy.

```python
import numpy as np
from scipy.stats import binom, uniform, norm

# PMF: discrete probability at exact values
k = np.arange(0, 6)
pmf = binom.pmf(k, n=5, p=0.4)

# PDF: continuous density over a range
x = np.linspace(0, 1, 200)
uniform_pdf = uniform.pdf(x, loc=0, scale=1)

# CDF: cumulative probability up to x
uniform_cdf = uniform.cdf(x, loc=0, scale=1)

# Another PDF example: standard normal density
z = np.linspace(-3, 3, 200)
normal_pdf = norm.pdf(z, loc=0, scale=1)
```

## Summary

- A **random variable** maps outcomes of a random process to numbers.
- **Discrete** distributions use a **PMF**; **continuous** distributions use a **PDF**.
- A **CDF** gives accumulated probability: $F(x)=P(X\le x)$.
- [[Mean]], [[Variance]], and [[Standard Deviation]] summarize center and spread.
- Quiz mindset: know whether the problem is asking for an **exact value**, an **interval**, or a **cumulative probability**.
