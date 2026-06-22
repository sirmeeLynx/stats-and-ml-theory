---
sources:
  - video: "2.2.2 Hypothesis Formulation"
    course_id: 141734
    item_id: 7718542
    duration: "09:45"
---

# Null and Alternative Hypothesis

A hypothesis test is built from **two mutually exclusive statements** about a population parameter: the null hypothesis $H_0$ and the alternative hypothesis $H_a$. [→ 2.2.2 @ 00:42]

## Null hypothesis $H_0$

The **null hypothesis** is the baseline or status-quo statement that the data are tested against. It is where the analysis begins. [→ 2.2.2 @ 01:08] [→ 2.2.2 @ 01:19]

$$
H_0:\ \theta = \theta_0
$$

The lecture is explicit that we do **not** try to prove $H_0$ true. We ask whether the data give enough evidence to reject it. [→ 2.2.2 @ 01:26]

## Alternative hypothesis $H_a$

The **alternative hypothesis** is the claim we want the data to establish: a change, an improvement, or any meaningful departure from the null. [→ 2.2.2 @ 01:34] [→ 2.2.2 @ 01:52]

$$
H_a:\ \theta \ne \theta_0,\quad \theta > \theta_0,\quad \text{or}\quad \theta < \theta_0
$$

In business terms, the course puts it this way: in the absence of new evidence, the null stands; the alternative must be supported by the data. [→ 2.2.2 @ 02:00] [→ 2.2.2 @ 02:08]

## Example 1 — lumber length

For lumber specified to have mean length $8.5$ meters, the population parameter is the mean $\mu$. [→ 2.2.2 @ 03:19]

$$
H_0: \mu = 8.5
$$

$$
H_a: \mu \ne 8.5
$$

This is a **two-tailed** formulation because any departure from $8.5$ matters. [→ 2.2.2 @ 03:58] [→ 2.2.2 @ 04:11]

## Example 2 — business travelers with companions

The second example starts with the belief that **$20\%$** of men on business travel bring a companion, and the hotel chain suspects the proportion is higher. [→ 2.2.2 @ 05:02] [→ 2.2.2 @ 05:21]

$$
H_0: p = 0.20
$$

$$
H_a: p > 0.20
$$

This is a **right-tailed** test because only an increase beyond $20\%$ supports the hotel's claim. [→ 2.2.2 @ 05:55] [→ 2.2.2 @ 06:17]

## Equality goes with the null

A quiz-safe rule from the lecture is:

- the **equality** sign belongs in $H_0$
- the **inequality** belongs in $H_a$

[→ 2.2.2 @ 06:43] [→ 2.2.2 @ 08:01]

The transcript also explains **why**: the sampling distribution used for probability calculations is built under a **specific null value**, so the null must pin the parameter down to an equality statement. [→ 2.2.2 @ 08:21] [→ 2.2.2 @ 08:54]

## Tail choice comes from $H_a$

| Alternative | Test type | Meaning |
|---|---|---|
| $H_a: \theta > \theta_0$ | one-tailed (right) | looking for an increase |
| $H_a: \theta < \theta_0$ | one-tailed (left) | looking for a decrease |
| $H_a: \theta \ne \theta_0$ | two-tailed | looking for any difference |

This tail choice should follow the **business question**, not the observed sample. See [[One-tailed and Two-tailed Tests]].

See also [[Hypothesis Testing]] and [[Hypothesis Test Procedure]].

## Python hands-on

```python
from scipy.stats import binomtest

# Hotel-chain example: test whether the true proportion is greater than 20%.
result = binomtest(k=28, n=100, p=0.20, alternative='greater')
print(result.pvalue)
```

## Summary

- $H_0$ is the **status quo**; $H_a$ is the **claim the data must establish**.
- The two hypotheses must be **mutually exclusive**.
- Put the **equality** in $H_0$ and the direction or difference in $H_a$.
- Quiz wording: we **reject $H_0$** or **fail to reject $H_0$**; we do not say we “accept $H_0$.”
