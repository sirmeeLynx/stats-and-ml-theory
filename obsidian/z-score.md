---
sources:
  - video: "2.1.10 Z-Score Hands-On"
    course_id: 141734
    item_id: 7718522
    duration: "06:48"
---

# Z-Score

A **z-score** tells you how many standard deviations a value is above or below the mean. The lecture presents it as the standard way to compare results measured on different scales. [→ 2.1.10 @ 00:05] [→ 2.1.10 @ 00:34]

## Formula

$$
z=\frac{x-\mu}{\sigma}
$$

where:

- $x$ is the observed value,
- $\mu$ is the mean,
- $\sigma$ is the standard deviation.

You can also go back from a z-score to the original scale:

$$
x=\mu+z\sigma
$$

## How to interpret it

- $z>0$: the value is above the mean.
- $z<0$: the value is below the mean.
- $|z|$ tells you how far from the mean the value is, in SD units.

This is why z-scores are useful in the [[Normal Distribution]] and in [[inferential-statistics|inferential statistics]] more broadly.

## When to use z-scores

Use z-scores when:

- you want to compare two observations from different scales,
- you want to standardize a variable,
- or you want to translate a raw score into the language of the standard normal distribution. [→ 2.1.10 @ 04:02] [→ 2.1.10 @ 06:09]

## Python hands-on

The lecture compares SAT and ACT scores by standardizing them. [→ 2.1.10 @ 03:41]

```python
from scipy.stats import norm

sat_score, sat_mean, sat_sd = 1350, 1000, 200
act_score, act_mean, act_sd = 30, 20, 5

sat_z = (sat_score - sat_mean) / sat_sd
act_z = (act_score - act_mean) / act_sd

sat_percentile = norm.cdf(sat_z)
act_percentile = norm.cdf(act_z)

print(sat_z)         # 1.75
print(act_z)         # 2.0
print(sat_percentile)
print(act_percentile)
```

Using the stated numbers from the lecture, the correct standardized scores are:

- SAT: $z=(1350-1000)/200=1.75$
- ACT: $z=(30-20)/5=2.0$

So the ACT score is farther above its own test mean and is therefore stronger relative to peers. [→ 2.1.10 @ 05:07]

## Relation to the standard normal

If $X$ is normally distributed, standardizing it gives a variable with mean 0 and standard deviation 1. That is the bridge between raw values and probability lookups using the standard normal table or `scipy.stats.norm`.

## Summary

- A z-score measures distance from the mean in **standard deviation units**.
- Formula: $z=(x-\mu)/\sigma$.
- Z-scores let you compare values across different scales.
- Larger positive z-scores mean better performance relative to the distribution.
- In a quiz, check the arithmetic carefully: subtract the mean first, then divide by the SD.
