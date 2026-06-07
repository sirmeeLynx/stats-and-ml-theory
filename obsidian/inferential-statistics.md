---
sources:
  - video: "2.1.1 Introduction and Agenda"
    course_id: 141734
    item_id: 7718500
    duration: "03:56"
  - video: "2.1.2 Introduction to Inferential Statistics"
    course_id: 141734
    item_id: 7718502
    duration: "22:11"
---

# Inferential Statistics

Inferential statistics takes us beyond describing the data we already have. Its job is to use a [[sampling-and-inference|sample]] to say something useful about a larger population and support decisions about cases we have not yet observed. [→ 2.1.1 @ 00:18] [→ 2.1.2 @ 05:31]

## From descriptive summaries to population conclusions

The lecture contrasts two kinds of questions:

- **descriptive** questions: What is the mean, median, range, variance, or correlation in this data set?
- **inferential** questions: What do these observed values tell me about the wider population the data came from? [→ 2.1.2 @ 00:17] [→ 2.1.2 @ 04:52]

In business terms, descriptive statistics gives a snapshot or dashboard of what already happened. Inferential statistics asks what that evidence means for future customers, future production, future sales, or other unobserved cases. [→ 2.1.2 @ 02:03] [→ 2.1.2 @ 03:57]

## Sample vs population

The birth-weight example in the lecture is the core picture to remember:

- the **histogram** summarizes the sample,
- the **smooth curve** represents the population distribution,
- probability questions about future babies belong to the population model, not just the sample count. [→ 2.1.2 @ 06:53] [→ 2.1.2 @ 08:24] [→ 2.1.2 @ 10:43]

Useful notation:

- population mean: $\mu$
- population standard deviation: $\sigma$
- sample mean: $\bar{x}$
- sample standard deviation: $s$

The inferential move is:

$$
\text{sample evidence} \rightarrow \text{population statement}
$$

## Why probability distributions matter

Inference needs probability models. Once a sample is linked to a population distribution, questions like “what fraction lies below 3000 grams?” become probability or area calculations. That is why the course next introduces [[distribution-terms|distribution terms]] and specific models such as the [[binomial-distribution|Binomial Distribution]], [[uniform-distribution|Uniform Distribution]], and [[Normal Distribution]]. [→ 2.1.1 @ 00:50] [→ 2.1.2 @ 11:01] [→ 2.1.2 @ 21:54]

## Business questions the lecture highlights

The same inferential logic appears in several settings:

- quality testing: is a new process better than the old one? [→ 2.1.2 @ 12:48]
- weather-based decisions: what is the chance temperature exceeds a threshold? [→ 2.1.2 @ 15:19]
- training and sales: do trained staff really perform better in future groups? [→ 2.1.2 @ 17:39]
- marketing: did a campaign lift conversion enough to justify investment? [→ 2.1.2 @ 19:08]

These are not questions about one finished spreadsheet. They are questions about generalizing from data to action.

## Estimation and uncertainty

The lecture emphasizes that business inference needs not only an answer but also a sense of how reliable that answer is. That is why this section leads into [[estimation|estimation]], where a point estimate is expanded into a range with uncertainty around it. [→ 2.1.2 @ 17:08] [→ 2.1.2 @ 20:29]

A generic interval form is

$$
\text{estimate} \pm \text{margin of error}
$$

## Python sketch: sample histogram vs population curve

This mirrors the lecture's birth-weight example: count directly from the sample, then compare it with a model-based population probability.

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

# illustrative birth-weight sample in grams
weights = np.array([2750, 2890, 3010, 3120, 3300, 3410, 3520, 3610, 3720, 3890])

xbar = weights.mean()
s = weights.std(ddof=1)

# descriptive answer from the sample
sample_prop_below_3000 = (weights < 3000).mean()

# inferential answer from a smooth population model
rv = norm(loc=xbar, scale=s)
model_prob_below_3000 = rv.cdf(3000)

x = np.linspace(weights.min() - 200, weights.max() + 200, 300)
plt.hist(weights, bins=6, density=True, alpha=0.4, label='sample histogram')
plt.plot(x, rv.pdf(x), color='crimson', label='population model')
plt.legend()
plt.show()
```

## Summary

- Inferential statistics uses a **sample** to say something about a **population**.
- Descriptive statistics summarizes what happened; inference supports conclusions beyond the observed data.
- Probability distributions are the bridge from sample evidence to population-level probability statements.
- Good inference also reports **uncertainty**, not just one number.
- Quiz mindset: always ask **what is the sample**, **what is the population**, and **what conclusion is being generalized**.
