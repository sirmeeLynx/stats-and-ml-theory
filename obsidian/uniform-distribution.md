---
sources:
  - video: "2.1.6 Uniform Distributions Theory"
    course_id: 141734
    item_id: 7718511
    duration: "05:06"
  - video: "2.1.7 Continuous Uniform Distribution Hands-on"
    course_id: 141734
    item_id: 7718514
    duration: "07:36"
---

# Uniform Distribution

A uniform distribution means all outcomes in the allowed range are treated as equally likely. It is the natural model when there is no reason to favor one outcome over another. [→ 2.1.6 @ 00:14] [→ 2.1.6 @ 01:39]

## Discrete uniform distribution

The lecture starts with the fair die: each value from 1 to 6 has probability $1/6$. [→ 2.1.6 @ 00:34]

If there are $m$ equally likely discrete outcomes, then

$$
P(X=x)=\frac{1}{m}
$$

for each allowed value $x$.

## Continuous uniform distribution

For a continuous uniform random variable on $[a,b]$, every interval of the same length has the same probability. [→ 2.1.6 @ 03:57]

Its density is constant:

$$
f(x)=\frac{1}{b-a}, \qquad a \le x \le b
$$

and zero otherwise.

The CDF is

$$
F(x)=\frac{x-a}{b-a}, \qquad a \le x \le b
$$

Important quiz fact: because this is a **continuous** distribution,

$$
P(X=c)=0
$$

for any single exact value $c$.

## Mean and variance

For $X \sim U(a,b)$,

$$
E[X]=\frac{a+b}{2}
$$

$$
\operatorname{Var}(X)=\frac{(b-a)^2}{12}
$$

## Python hands-on

The hands-on lecture models bug-fix times as roughly uniform from 1 hour to 5 hours. [→ 2.1.7 @ 03:12]

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import uniform

rv = uniform(loc=1, scale=4)   # U(1, 5)
x = np.linspace(1, 5, 200)
pdf = rv.pdf(x)

p_lt_3 = rv.cdf(3)             # P(X < 3) = 0.5
p_gt_2 = 1 - rv.cdf(2)         # P(X > 2) = 0.75
median = rv.ppf(0.50)          # 3
q25 = rv.ppf(0.25)             # 2

plt.plot(x, pdf)
plt.xlabel('time (hours)')
plt.ylabel('density')
plt.title('Continuous Uniform Distribution on [1, 5]')
plt.show()
```

Lecture values to remember:

- $P(X<3)=0.5$ [→ 2.1.7 @ 04:19]
- $P(X>2)=0.75$ [→ 2.1.7 @ 04:45]
- median $=3$ and 25th percentile $=2$ [→ 2.1.7 @ 05:16]

## Summary

- Uniform means **equal likelihood across the support**.
- A fair die is a **discrete uniform** example.
- On $[a,b]$, the continuous uniform density is $1/(b-a)$.
- Mean: $(a+b)/2$.
- Variance: $(b-a)^2/12$.
- Use it when the problem states that every outcome in a range is equally plausible.
