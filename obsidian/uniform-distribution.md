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

A uniform distribution represents uncertainty that is spread evenly across the allowed values. The lecture's intuition is: do not favor one outcome over another. [→ 2.1.6 @ 00:16] [→ 2.1.6 @ 01:41]

## Discrete uniform distribution

The simplest example is a fair die. Outcomes 1 through 6 are all possible, and each one has the same probability. [→ 2.1.6 @ 00:35] [→ 2.1.6 @ 00:58]

If there are $m$ equally likely outcomes, then each one gets probability

$$
P(X=x)=\frac{1}{m}
$$

for the allowed values of $x$. [→ 2.1.6 @ 02:59]

## Continuous uniform distribution

When the variable can take any value in an interval, the lecture switches to the **continuous** uniform model. The example is temperature ranging from 12 to 17 with no bias toward either end of the range. [→ 2.1.6 @ 03:44] [→ 2.1.6 @ 04:19]

For $X \sim U(a,b)$, the density is flat:

$$
f(x)=\frac{1}{b-a}, \qquad a \le x \le b
$$

and the area to the left of $x$ is

$$
F(x)=\frac{x-a}{b-a}, \qquad a \le x \le b
$$

## Bug-fix time example

The hands-on lecture models bug-fix times in hours. After plotting a histogram and density estimate, the fitted shape looks fairly flat on top, so a continuous uniform distribution on 1 to 5 hours is treated as a reasonable model. [→ 2.1.7 @ 01:39] [→ 2.1.7 @ 02:46] [→ 2.1.7 @ 03:03]

The lecture then uses three kinds of questions:

- **left-tail probability**: $P(X<3)=0.5$ [→ 2.1.7 @ 04:20] [→ 2.1.7 @ 04:37]
- **right-tail probability**: $P(X>2)=0.75$ using $1-\text{CDF}$ [→ 2.1.7 @ 04:46] [→ 2.1.7 @ 05:07]
- **percentiles**: the median is 3 and the 25th percentile is 2 [→ 2.1.7 @ 05:46] [→ 2.1.7 @ 06:45]

## CDF vs PPF

The lecture uses two matching tools:

- **CDF**: put in a number, get the probability to the left of it. [→ 2.1.7 @ 03:42]
- **PPF** (percent point function): put in a probability, get the cutoff value that leaves that much probability to the left. [→ 2.1.7 @ 05:46] [→ 2.1.7 @ 07:01]

## Python hands-on

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import uniform

rv = uniform(loc=1, scale=4)   # uniform on [1, 5]
x = np.linspace(1, 5, 200)

pdf = rv.pdf(x)
p_lt_3 = rv.cdf(3)
p_gt_2 = 1 - rv.cdf(2)
median = rv.ppf(0.50)
q25 = rv.ppf(0.25)

plt.plot(x, pdf)
plt.xlabel('bug-fix time (hours)')
plt.ylabel('density')
plt.title('Continuous Uniform Distribution on [1, 5]')
plt.show()
```

## Summary

- Uniform means **equal likelihood across the support**.
- A fair die is the discrete version; a flat interval is the continuous version.
- In the continuous case, probabilities come from **areas**, so CDF and PPF are the main tools.
- The bug-fix example uses a uniform model on 1 to 5 hours.
- Quiz mindset: if the problem says “all values in the range are equally likely,” think **uniform**.
