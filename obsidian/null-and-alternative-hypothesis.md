---
sources:
  - video: "2.2.2 Hypothesis Formulation"
    course_id: 141734
    item_id: 7718542
    duration: "09:44"
  - video: "2.2.1 Introduction to Hypothesis Testing"
    course_id: 141734
    item_id: 7718540
    duration: "18:43"
---

# Null and Alternative Hypothesis

In hypothesis testing, we write **two mutually exclusive statements** about a
population parameter: the **null hypothesis** $H_0$ and the **alternative hypothesis**
$H_a$. [→ 2.2.2 @ 00:41]

## Null hypothesis $H_0$

The **null hypothesis** is the baseline, status quo, or historical claim we start
from. It is the claim we test **against**. [→ 2.2.2 @ 01:06]

$$
H_0:\ \theta = \theta_0
$$

Common meanings of $H_0$:

- “no change”
- “no improvement”
- “the specification still holds”
- “the historical value is still correct”

The course is explicit that we do **not** try to prove $H_0$ true; we check whether
there is enough evidence to reject it. [→ 2.2.2 @ 01:24]

## Alternative hypothesis $H_a$

The **alternative hypothesis** is the research claim or business claim we want the
data to support. It represents a meaningful difference from the null. [→ 2.2.2 @ 01:36]

$$
H_a:\ \theta \ne \theta_0,\quad \theta > \theta_0,\quad \text{or}\quad \theta < \theta_0
$$

In business language: if no convincing data are available, we stay with $H_0$; the
data must establish $H_a$. [→ 2.2.2 @ 01:59]

## Examples from the lecture

### Mean example

For wood beams specified to have mean length $8.5$ m:

$$
H_0: \mu = 8.5
$$
$$
H_a: \mu \ne 8.5
$$

This is a **two-tailed** test because the alternative allows either direction away
from $8.5$. [→ 2.2.2 @ 03:22]

### Proportion example

For the hotel-chain example:

$$
H_0: p = 0.20
$$
$$
H_a: p > 0.20
$$

This is a **right-tailed** (one-tailed) test because the claim is specifically that
the proportion is **greater than** $0.20$. [→ 2.2.2 @ 05:54]

## Equality goes with the null

Quiz-critical rule from the lecture:

- the **equality** sign is attached to the null hypothesis
- the **inequality** sign is attached to the alternative hypothesis

[→ 2.2.2 @ 08:00]

That is why we usually write:

$$
H_0: \mu = \mu_0
$$
$$
H_a: \mu \ne \mu_0 \quad \text{or} \quad \mu > \mu_0 \quad \text{or} \quad \mu < \mu_0
$$

## One-tailed vs two-tailed tests

The form of $H_a$ determines the tail structure:

| Alternative | Test type | Meaning |
|---|---|---|
| $H_a: \theta > \theta_0$ | right-tailed | looking for an increase |
| $H_a: \theta < \theta_0$ | left-tailed | looking for a decrease |
| $H_a: \theta \ne \theta_0$ | two-tailed | looking for any difference |

Choose the tail direction from the **research question**, not after seeing the data.
The lecture foreshadows this when it contrasts $\mu \ne 8.5$ with $p > 0.20$.
[→ 2.2.2 @ 06:24]

See also [[hypothesis-testing]], [[hypothesis-test-procedure]], and
[[p-value-and-significance]].

## Python hands-on

It helps to encode the hypotheses in plain language before running a test:

```python
mu0 = 8.5
print(f"H0: mu = {mu0}")
print(f"Ha: mu != {mu0}")

p0 = 0.20
print(f"H0: p = {p0}")
print(f"Ha: p > {p0}")
```

For the hotel example, a one-sided proportion test in SciPy can be written as:

```python
from scipy.stats import binomtest

# Example: 28 accompanied travelers out of 100
result = binomtest(k=28, n=100, p=0.20, alternative='greater')
print(result.pvalue)
```

## Summary

- $H_0$ is the **status quo / baseline** claim.
- $H_a$ is the **research or improvement** claim.
- The two hypotheses must be **mutually exclusive**.
- Quiz trap: we usually say **reject $H_0$** or **fail to reject $H_0$** — not
  “accept $H_0$.”
- Quiz trap: the equality sign belongs with **$H_0$**, while direction/difference is
  expressed in **$H_a$**.
