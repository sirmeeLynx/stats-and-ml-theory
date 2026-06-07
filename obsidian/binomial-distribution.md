---
sources:
  - video: "2.1.4 Binomial Distributions Theory"
    course_id: 141734
    item_id: 7718506
    duration: "15:25"
  - video: "2.1.5 Binomial Distributions Hands-On"
    course_id: 141734
    item_id: 7718509
    duration: "16:20"
---

# Binomial Distribution

The binomial distribution is the standard model for counting how many times a yes/no event happens across repeated trials. Each trial ends in either success or failure, and the random variable counts the total number of successes. [→ 2.1.4 @ 01:01] [→ 2.1.4 @ 07:30]

## Bernoulli: the one-trial building block

The lecture starts from the simpler **Bernoulli** case: one trial, two outcomes, success coded as 1 and failure coded as 0. [→ 2.1.4 @ 02:05] [→ 2.1.4 @ 03:24]

A useful caution from the lecture: “success” is just the event we care about. In practice it could be default on a loan, a defective part, or a positive medical finding. [→ 2.1.4 @ 02:30] [→ 2.1.4 @ 04:34]

$$
P(X=1)=p, \qquad P(X=0)=1-p
$$

## From Bernoulli to binomial

If we repeat that Bernoulli trial $n$ times and count the number of successes, we get a binomial random variable. The lecture's example asks 25 adults whether they have ever posted a video on TikTok; the count of “yes” answers is binomial. [→ 2.1.4 @ 06:43] [→ 2.1.4 @ 08:13]

We write this as

$$
X \sim \operatorname{Bin}(n,p)
$$

where $n$ is the number of trials and $p$ is the common success probability.

## Assumptions to memorize

The lecture gives four core assumptions for the binomial model: [→ 2.1.4 @ 11:35] [→ 2.1.4 @ 12:57]

1. the number of trials $n$ is fixed,
2. each trial has only two outcomes,
3. the trials are independent,
4. the probability of success is the same on every trial.

The instructor also stresses that even when these assumptions are only approximately true, the model can still be useful in practice. [→ 2.1.4 @ 13:04] [→ 2.1.4 @ 15:02]

## PMF and intuition

The probability of exactly $k$ successes is

$$
P(X=k)=\binom{n}{k}p^k(1-p)^{n-k}, \qquad k=0,1,\dots,n
$$

The lecture's intuition is:

- $p^k$ multiplies the success probabilities,
- $(1-p)^{n-k}$ multiplies the failure probabilities,
- $\binom{n}{k}$ counts how many ways those $k$ successes can be placed among the $n$ trials. [→ 2.1.4 @ 08:46] [→ 2.1.4 @ 10:41]

## Mean and variance

High-value quiz facts for $X \sim \operatorname{Bin}(n,p)$:

$$
E[X]=np
$$

$$
\operatorname{Var}(X)=np(1-p)
$$

$$
\operatorname{SD}(X)=\sqrt{np(1-p)}
$$

## Museum souvenir example

In the hands-on lecture, each museum visitor buys a souvenir with probability $0.8$, and the model looks at $n=10$ visitors. [→ 2.1.5 @ 00:31] [→ 2.1.5 @ 03:38]

Key results from the lecture:

- exactly 8 buyers: about $0.30$ [→ 2.1.5 @ 06:43]
- exactly 10 buyers: about $0.107$ or 10.7% [→ 2.1.5 @ 08:15]
- at most 7 buyers: about $0.32$ using the CDF [→ 2.1.5 @ 10:15] [→ 2.1.5 @ 11:30]
- at least 4 buyers: $1-P(X\le 3)\approx 0.999$ [→ 2.1.5 @ 13:13] [→ 2.1.5 @ 13:39]

The lecture makes an important interpretive point: even if 8 buyers is the **most likely** outcome when $p=0.8$, that still does not mean it happens with probability 0.8. In the example it is only about 0.30. [→ 2.1.5 @ 07:03] [→ 2.1.5 @ 07:38]

## Python hands-on

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import binom

n, p = 10, 0.8
k = np.arange(0, n + 1)
pmf = binom.pmf(k, n, p)

p_eq_8 = binom.pmf(8, n, p)
p_eq_10 = binom.pmf(10, n, p)
p_le_7 = binom.cdf(7, n, p)
p_ge_4 = 1 - binom.cdf(3, n, p)

plt.bar(k, pmf)
plt.xlabel('number of buyers')
plt.ylabel('probability')
plt.title('Binomial PMF: n=10, p=0.8')
plt.show()
```

Use the PMF for **exactly** questions, the CDF for **at most** questions, and complements for **at least** questions. [→ 2.1.5 @ 09:33] [→ 2.1.5 @ 12:42]

## Summary

- Binomial random variables count successes across repeated yes/no trials.
- A Bernoulli random variable is the one-trial special case.
- Core assumptions: fixed $n$, two outcomes, independence, common $p$.
- PMF: $P(X=k)=\binom{n}{k}p^k(1-p)^{n-k}$.
- Quiz facts: mean $np$, variance $np(1-p)$, and complements for “at least” probabilities.
