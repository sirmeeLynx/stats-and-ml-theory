---
sources:
  - page: "Bootstrapping"
    course_id: 141736
    item_id: 7718068
  - live_class: "LVC 2: Model Evaluation, Cross-Validation and Bootstrapping"
    course_id: 141736
    summary_file: 12604588
    transcript_file: 13799117
    recording: "@ 01:55:47"
---

# Bootstrapping

**Bootstrapping** is a statistical procedure that **resamples a single dataset** to
create many simulated samples (each called a **bootstrap sample**).

## How it works — sampling *with replacement*

- Draw an item at random, then **put it back** before the next draw.
- Every item has an equal chance of selection on each draw, so **one item can appear
  multiple times** in the same bootstrap sample.
- Each bootstrap sample's size can be **smaller than or equal to** the original dataset.

Example: from a dataset, draw 3-record bootstrap samples — a given record (say index 7)
may repeat twice in one sample, while another sample may have all unique records.

## Why it matters

Bootstrapping lets us estimate the **variability** of a statistic (e.g. a coefficient
or a [[Confidence Intervals|confidence interval]]) without assuming a particular
distribution. It underpins ensemble methods like **bagging**.

Contrast with [[Cross-Validation]] (which partitions data **without** replacement).

## Standard error via bootstrap

Bootstrapping is used **when we cannot collect more data** from the population — we
synthesise many datasets (each the same size $n$, sampled **with replacement**) and
recompute the estimate $\theta$ on each. With $m$ bootstrap estimates:

$$
\theta_{ave} = \frac{1}{m}\sum_{i=1}^{m}\theta_i, \qquad
Var(\theta) = \frac{1}{m}\sum_{i=1}^{m}(\theta_i - \theta_{ave})^2, \qquad
se(\theta) = \sqrt{Var(\theta)}
$$

Plotting the $\theta_i$ gives a **sampling distribution**; by the **central limit
theorem** we can trust its spread as a measure of the estimate's variability. This
removes the dependence of the result on any single data point.

## Summary

- Bootstrapping = **resampling with replacement** to build many simulated samples.
- Items **can repeat** within a sample; sample size ≤ original.
- Used to estimate the sampling variability of a statistic.
