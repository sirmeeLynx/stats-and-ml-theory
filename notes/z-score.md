---
sources:
  - video: "2.1.8 Normal Distributions Theory"
    course_id: 141734
    item_id: 7718516
    duration: "16:59"
  - video: "2.1.10 Z-Score Hands-On"
    course_id: 141734
    item_id: 7718522
    duration: "06:47"
---

# Z-Score

A z-score is the standardized version of a value: it tells us how many standard deviations above or below the mean that value sits. [→ 2.1.8 @ 15:56] [→ 2.1.10 @ 03:39]

## Formula

$$
z=\frac{x-\mu}{\sigma}
$$

Standardizing converts a normal variable into the **standard normal** distribution with mean 0 and standard deviation 1. [→ 2.1.8 @ 14:24] [→ 2.1.8 @ 15:10]

## How to interpret it

- $z>0$: the value is above the mean.
- $z<0$: the value is below the mean.
- $|z|$: the distance from the mean in standard deviation units.

The lecture's examples make this concrete: a height with z-score 1 is one standard deviation above average, while a bone-density score of -1.5 is one and a half standard deviations below average. [→ 2.1.8 @ 16:06] [→ 2.1.8 @ 16:31]

## Why z-scores matter

Raw scores on different scales are not directly comparable. Z-scores fix that by putting all variables onto the same standardized scale. [→ 2.1.10 @ 02:22] [→ 2.1.10 @ 06:03]

This is why z-scores connect the [[Normal Distribution]] to fair comparisons across different tests, measurements, or business metrics.

## SAT vs ACT example

The lecture compares two fellowship candidates:

- SAT scores have mean 1000 and standard deviation 200,
- ACT scores have mean 20 and standard deviation 5,
- the top observed scores are 1350 on SAT and 30 on ACT. [→ 2.1.10 @ 00:47] [→ 2.1.10 @ 01:16] [→ 2.1.10 @ 02:07]

Standardizing the stated numbers gives:

$$
z_{\text{SAT}}=\frac{1350-1000}{200}=1.75
$$

$$
z_{\text{ACT}}=\frac{30-20}{5}=2.0
$$

So the ACT student performed better relative to that exam's own population, because 2.0 standard deviations above the mean is stronger than 1.75. This is the real point of the example: compare relative standing, not raw score magnitudes. [→ 2.1.10 @ 04:00] [→ 2.1.10 @ 05:09]

## Python hands-on

```python
from scipy.stats import norm

sat_score, sat_mean, sat_sd = 1350, 1000, 200
act_score, act_mean, act_sd = 30, 20, 5

sat_z = (sat_score - sat_mean) / sat_sd
act_z = (act_score - act_mean) / act_sd

sat_percentile = norm.cdf(sat_z)
act_percentile = norm.cdf(act_z)

print(sat_z)          # 1.75
print(act_z)          # 2.0
print(sat_percentile)
print(act_percentile)
```

## Summary

- A z-score measures distance from the mean in **standard deviation units**.
- Formula: $z=(x-\mu)/\sigma$.
- Standardizing creates the standard normal with mean 0 and standard deviation 1.
- Z-scores make cross-scale comparisons fair.
- Quiz fact: bigger positive z-score means stronger performance relative to the underlying distribution.
