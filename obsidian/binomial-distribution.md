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

The binomial distribution models the **number of successes** in a fixed number of repeated trials when each trial has only two outcomes. [→ 2.1.4 @ 01:04]

## When to use it

Use a binomial model when all of the following are true:

1. there are exactly $n$ trials,
2. each trial has only two outcomes (success/failure),
3. the probability of success is the same on every trial,
4. the trials are independent. [→ 2.1.4 @ 11:25]

The lecture also notes that real data may violate these assumptions slightly, but the binomial model can still be a useful approximation. [→ 2.1.4 @ 13:22]

## Bernoulli as the one-trial special case

A **Bernoulli** random variable is the one-trial version of the same idea: encode success as 1 and failure as 0. [→ 2.1.4 @ 03:35]

$$
P(X=1)=p, \qquad P(X=0)=1-p
$$

If you repeat that Bernoulli trial $n$ times and count the number of successes, you get a binomial random variable.

## PMF and intuition

If $X \sim \operatorname{Bin}(n,p)$, then

$$
P(X=k)=\binom{n}{k}p^k(1-p)^{n-k}, \qquad k=0,1,\dots,n
$$

Interpretation:

- $\binom{n}{k}$ counts the number of ways to place $k$ successes in $n$ trials,
- $p^k$ is the probability of those successes,
- $(1-p)^{n-k}$ is the probability of the failures.

## Mean and variance

These are high-value quiz facts:

$$
E[X]=np
$$

$$
\operatorname{Var}(X)=np(1-p)
$$

$$
\operatorname{SD}(X)=\sqrt{np(1-p)}
$$

## Typical probability questions

- **Exactly $k$ successes**: use the PMF.
- **At most $k$ successes**: use the CDF $P(X\le k)$.
- **At least $k$ successes**: use a complement, $P(X\ge k)=1-P(X\le k-1)$. [→ 2.1.5 @ 10:14] [→ 2.1.5 @ 12:31]

## Python hands-on

The course example uses 10 museum visitors, where each visitor buys a souvenir with probability $0.8$. [→ 2.1.5 @ 00:59]

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import binom

n, p = 10, 0.8
k = np.arange(0, n + 1)
pmf = binom.pmf(k, n, p)

p_eq_8 = binom.pmf(8, n, p)      # exactly 8 buyers
p_eq_10 = binom.pmf(10, n, p)    # exactly 10 buyers
p_le_7 = binom.cdf(7, n, p)      # at most 7 buyers
p_ge_4 = 1 - binom.cdf(3, n, p)  # at least 4 buyers

plt.bar(k, pmf)
plt.xlabel('number of buyers')
plt.ylabel('probability')
plt.title('Binomial PMF: n=10, p=0.8')
plt.show()
```

Useful values from the lecture example:

- $P(X=8) \approx 0.302$ [→ 2.1.5 @ 06:41]
- $P(X=10) \approx 0.107$ [→ 2.1.5 @ 06:41]
- $P(X\le 7) \approx 0.322$ [→ 2.1.5 @ 10:14]

## Summary

- The binomial distribution counts successes in repeated **independent** yes/no trials.
- PMF: $P(X=k)=\binom{n}{k}p^k(1-p)^{n-k}$.
- Mean: $np$.
- Variance: $np(1-p)$.
- Use PMF for **exactly**, CDF for **at most**, and complements for **at least**.
