---
sources:
  - page: "The Assumptions of Linear Regression"
    course_id: 141736
    item_id: 7718066
  - live_class: "LVC 2: Model Evaluation, Cross-Validation and Bootstrapping"
    course_id: 141736
    summary_file: 12604588
    transcript_file: 13799117
---

# Assumptions of Linear Regression

[[Linear Regression]] is only reliable if these assumptions hold. If violated, the
model's inferences on unseen data may be untrustworthy.

## The five assumptions

1. **Linearity** — the relationship between independent variables and the dependent
   variable must be **linear**. A line cannot capture a non-linear pattern, leading to
   high error.

2. **No Multicollinearity** — independent variables should **not be correlated** with
   each other. Multicollinearity gives the model repeated information, reduces the
   precision of estimated coefficients, and weakens statistical power. Include only
   non-correlated predictors. (Checked via **VIF**.)

3. **Homoscedasticity** — the error terms have **constant variance** (equally spread
   around the best-fit line). The least-squares derivation assumes this; violation
   (heteroscedasticity) makes results unreliable.

4. **Normal Distribution of error terms** — residuals should be normally distributed.
   Non-normal errors make confidence intervals too wide or narrow and destabilize
   coefficient estimation.

5. **No Endogeneity** — independent variables must **not be correlated with the error
   terms**. Endogeneity biases the estimated parameters.

## Memory hooks

- **L**inearity, **M**ulticollinearity, **H**omoscedasticity, **N**ormality of errors,
  **E**ndogeneity.
- Multicollinearity = correlation **among predictors**; endogeneity = correlation
  **between predictors and errors**.

See [[Correlation vs Causation]] and [[Regularization]] (which helps when many
correlated features exist).

## From the live class (LVC 2): diagnosing violations

- **Heteroscedasticity** — the residual variance is **not constant** along the
  regression line (the least-squares formulas assume *homoscedasticity*). With one
  feature you can spot it on a scatter plot; with many features, plot **residuals vs
  predicted values** and check whether the spread stays constant. **Outliers** are a
  common cause.
- **Multicollinearity** — correlation **among the independent features**. Then the
  feature matrix $X$ is **not full rank**, so $X^{T}X$ is **not invertible** — yet the
  standard-error formulas require $(X^{T}X)^{-1}$. Fix by **removing** some of the
  collinear features so the information each carries becomes unique. (Mild correlation
  that does not fully duplicate a feature is fine — $X$ can still be full rank.)

*Recording: LVC 2 multicollinearity @ 00:16:55.*

## Summary

- Five assumptions: **linearity, no multicollinearity, homoscedasticity, normal
  errors, no endogeneity**.
- Homoscedasticity = **constant error variance**.
- Multicollinearity is about correlation *between independent variables*.
