---
sources:
  - video: "2.1.3 Fundamental Terms in Distributions"
    course_id: 141734
    item_id: 7718504
    duration: "21:05"
---

# Distribution Terms

Probability distributions are the language that connects uncertainty, random variables, and business decisions. They describe what values a random quantity can take and how probability is assigned across those values. [→ 2.1.3 @ 12:38] [→ 2.1.3 @ 20:18]

## Random variable

A **random variable** is a numerical description of an uncertain outcome. It is the number that changes from one case to the next because the underlying situation is not perfectly predictable. [→ 2.1.3 @ 00:51] [→ 2.1.3 @ 05:21]

Examples from the lecture:

- whether a customer buys or not,
- how many students pass an exam,
- the number of insurance claims,
- the amount of liquid in a glass. [→ 2.1.3 @ 02:26] [→ 2.1.3 @ 07:01] [→ 2.1.3 @ 10:32]

## Discrete random variables

A **discrete** random variable takes separate countable values such as 0, 1, 2, or 3. The insurance-claims example is discrete because a driver can file 0 claims or 1 claim, but not 2.5 claims. [→ 2.1.3 @ 06:50] [→ 2.1.3 @ 09:43]

For a discrete distribution, probability is assigned value by value, and the probabilities must be non-negative and add up to 1. [→ 2.1.3 @ 09:12]

$$
\sum_x P(X=x) = 1
$$

## Continuous random variables

A **continuous** random variable can take any value in a range. The lecture's examples are liquid volume and temperature-like measurements where intermediate values are completely possible, so listing every value is not practical. [→ 2.1.3 @ 10:32] [→ 2.1.3 @ 11:08]

In that case, probabilities are described through regions such as “less than,” “more than,” or “between.” [→ 2.1.3 @ 11:44] [→ 2.1.3 @ 14:01]

$$
P(a \le X \le b) = \int_a^b f(x)\,dx
$$

## Probability distribution

A **probability distribution** combines the random variable and its probabilities. It tells us both the possible values and how likely those values are. [→ 2.1.3 @ 12:38] [→ 2.1.3 @ 13:02]

The lecture also shows how observed counts can be rescaled into probabilities: if an employee makes 0 sales on 16 out of 100 days, that becomes probability $0.16$ for 0 sales. [→ 2.1.3 @ 14:42] [→ 2.1.3 @ 15:58]

## PMF vs density function

For discrete random variables, the lecture uses the term **Probability Mass Function (PMF)**: probability mass is attached to each listed outcome. [→ 2.1.3 @ 13:08] [→ 2.1.3 @ 13:24]

For continuous random variables, the lecture switches to a **density function**: probability comes from areas over intervals rather than a list of pointwise probabilities. [→ 2.1.3 @ 13:39] [→ 2.1.3 @ 14:12]

## The main examples that follow

The lecture previews the major distributions used in the rest of the section:

- **Bernoulli** for yes/no outcomes, [→ 2.1.3 @ 17:07]
- **Binomial** for counts of Bernoulli successes, [→ 2.1.3 @ 18:07]
- **Uniform** when all outcomes are equally likely, [→ 2.1.3 @ 18:40]
- **Normal** when values cluster around the middle in a bell shape. [→ 2.1.3 @ 19:09]

These become the foundation for [[inferential-statistics|inferential statistics]], [[binomial-distribution|binomial]], [[uniform-distribution|uniform]], and [[Normal Distribution]] notes.

## Python preview

The lecture notes that later sessions will use Python calculators for these distributions. This small preview shows the main objects that appear next. [→ 2.1.3 @ 20:53]

```python
import numpy as np
from scipy.stats import binom, uniform, norm

# discrete PMF
k = np.arange(0, 4)
pmf = binom.pmf(k, n=3, p=0.4)

# continuous density and area
x = np.linspace(1, 5, 200)
u = uniform(loc=1, scale=4)
uniform_pdf = u.pdf(x)
uniform_left_of_3 = u.cdf(3)

# normal density
z = np.linspace(-3, 3, 200)
normal_pdf = norm.pdf(z)
```

## Summary

- A **random variable** assigns a number to an uncertain outcome.
- **Discrete** variables use listed probabilities; **continuous** variables use probability over intervals.
- A **probability distribution** describes possible values together with their probabilities.
- **PMF** is the discrete language; **density** is the continuous language.
- Quiz mindset: ask whether the problem is about a **countable outcome** or a **continuous range** before choosing a model.
