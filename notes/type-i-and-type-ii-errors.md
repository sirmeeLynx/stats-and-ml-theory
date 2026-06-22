---
sources:
  - video: "2.2.3 Basic Concepts of Hypothesis Testing"
    course_id: 141734
    item_id: 7718544
    duration: "13:37"
---

# Type I and Type II Errors

Because hypothesis-test decisions are based on samples, they can be wrong. The lecture organizes those mistakes by combining the **truth about $H_0$** with the **decision we make**. [→ 2.2.3 @ 08:26] [→ 2.2.3 @ 09:03]

## The 2×2 decision table

| Reality | Reject $H_0$ | Fail to reject $H_0$ |
|---|---|---|
| $H_0$ true | **Type I error** | correct decision |
| $H_0$ false | correct decision (**power**) | **Type II error** |

## Type I error

A **Type I error** happens when we reject the null hypothesis even though it is actually true. This is a **false positive**. [→ 2.2.3 @ 09:06] [→ 2.2.3 @ 12:48]

$$
\alpha = P(\text{reject } H_0 \mid H_0 \text{ true})
$$

The course also calls $\alpha$ the **level of significance**. [→ 2.2.3 @ 09:27] [→ 2.2.3 @ 09:40]

## Type II error

A **Type II error** happens when $H_0$ is false, but we fail to reject it. This is a **false negative**. [→ 2.2.3 @ 10:39] [→ 2.2.3 @ 11:08] [→ 2.2.3 @ 12:59]

$$
\beta = P(\text{fail to reject } H_0 \mid H_0 \text{ false})
$$

## Power

The **power** of a test is the probability of correctly rejecting a false null hypothesis. [→ 2.2.3 @ 09:57] [→ 2.2.3 @ 10:08]

$$
\text{Power} = 1 - \beta
$$

A more powerful test is better at detecting a real effect when the effect truly exists. [→ 2.2.3 @ 10:11] [→ 2.2.3 @ 13:21]

## Cancer-screening analogy from the lecture

The course uses a medical-test analogy:

- $H_0$: the patient does **not** have cancer. [→ 2.2.3 @ 12:00]
- Rejecting $H_0$ means the test says the patient **does** have cancer. [→ 2.2.3 @ 12:24]
- A **Type I error** means a healthy patient is flagged as having cancer: a **false positive**. [→ 2.2.3 @ 12:35] [→ 2.2.3 @ 12:50]
- A **Type II error** means the patient has cancer, but the test misses it: a **false negative**. [→ 2.2.3 @ 13:02] [→ 2.2.3 @ 13:14]
- In that setting, a **powerful** test is one that can detect the disease when it really exists. [→ 2.2.3 @ 13:17] [→ 2.2.3 @ 13:33]

See also [[p-value and Significance]] and [[Hypothesis Test Procedure]].

## Python hands-on

A generic z-test view of power uses the critical cutoff from $\alpha$ and then computes $\beta$ under a chosen alternative:

```python
from scipy.stats import norm

alpha = 0.05
z_crit = norm.isf(alpha)   # right-tail cutoff

# Example: suppose the true mean under the alternative is 0.8 standard errors above H0.
delta = 0.8
beta = norm.cdf(z_crit - delta)
power = 1 - beta

print(z_crit)
print(beta)
print(power)
```

## Summary

- **Type I error** = reject a true $H_0$ = **false positive**.
- **Type II error** = fail to reject a false $H_0$ = **false negative**.
- **$\alpha$** is the Type I error rate.
- **Power** is **$1-\beta$**, not **$1-\alpha$**.
- Quiz shortcut: cancer example -> false positive = Type I, false negative = Type II.
