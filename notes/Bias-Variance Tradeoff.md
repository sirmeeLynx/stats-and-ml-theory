---
sources:
  - page: "Bias-Variance Trade-off"
    course_id: 141736
    item_id: 7718069
  - live_class: "LVC 2: Model Evaluation, Cross-Validation and Bootstrapping"
    course_id: 141736
    summary_file: 12604588
    transcript_file: 13799117
    recording: "overfitting @ 00:11:49"
---

# Bias-Variance Tradeoff

## Data splits

- **Training data** — largest fraction; used to fit the model.
- **Validation data** — smaller fraction; used to tune parameters and check the model
  iteratively.
- **Testing / unseen data** — held out; final check that the model generalizes.

**Model complexity** rises with the number of parameters (coefficients) to estimate.

## Overfitting vs underfitting

- **Overfitting** — model fits the training data *too* closely (including noise);
  training error ≪ test error. Fails to **generalize**.
- **Underfitting** — model is too simple, fails to capture the pattern; **poor on both**
  training and test data.

> A model cannot overfit and underfit at the same time.

## Bias and variance

- **Bias** — how much predictions differ from the true values *on the training data*
  (the **training error**). Comes from the model's assumptions. **High bias →
  underfitting** (too many simplifying assumptions).
- **Variance** — how much the model's performance changes if trained on *different*
  data. **High variance → overfitting** (fits training data, including noise, too
  closely).

## The tradeoff

| Situation | Bias | Variance | Result |
|-----------|------|----------|--------|
| Too simple | high | low | **underfit** |
| Too complex | low | high | **overfit** |

- Increasing bias (simplifying an overfit model) **lowers variance**, improving
  generalization.
- Decreasing bias (making an underfit model more complex) **raises variance**.

The goal is the **sweet spot** balancing the two. [[Regularization]] and
[[Cross-Validation]] are the practical tools to manage it.

## The U-shaped validation curve

As you **add features**, the **training error keeps dropping** — eventually the model
starts **fitting the noise** (overfitting). The **validation error**, however, follows a
**U-shape**: it falls, bottoms out, then rises again. The **right number of features
sits in the valley** of that curve — flexible enough to learn the signal, not so complex
it memorises noise. The professor's loose shorthand: **bias ≈ training error, variance ≈
testing error**, and we want **both low**. Too few features → underfit; too many →
overfit.

## Summary

- **High bias = underfit; high variance = overfit.**
- More complexity → less bias, more variance (and vice versa) — that exchange is the
  **bias-variance tradeoff**.
- Validation/test data reveal whether you have overfit.
