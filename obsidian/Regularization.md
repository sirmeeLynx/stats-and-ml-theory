---
sources:
  - page: "Regularization - Ridge Regression & Lasso Regression"
    course_id: 141736
    item_id: 7718070
  - live_class: "LVC 2: Model Evaluation, Cross-Validation and Bootstrapping"
    course_id: 141736
    summary_file: 12604588
    transcript_file: 13799117
---

# Regularization

**Regularization** reduces **overfitting** by making a model simpler — it adds a
**penalty** to the cost function that shrinks the coefficients of less-significant
variables. It works best when there are **many features**.

A variable influences the model through its **coefficient**, so we regularize by
**regulating the coefficients**.

## Ridge Regression (L2)

Adds a penalty equal to the **regularization parameter $\lambda$ times the sum of the
squared coefficients** (second-order term → "L2"):

$$
\text{Loss}_{\text{Ridge}} = \text{MSE} + \lambda \sum_{j=1}^{p} \theta_j^2
$$

- Higher $\lambda$ → bigger penalty → coefficients **shrink** in magnitude.
- **L2 shrinks coefficients toward zero but never exactly to zero** — it reduces a
  feature's effect without removing it.

## Lasso Regression (L1)

Adds a penalty equal to $\lambda$ times the **sum of the absolute values (modulus)** of
the coefficients (first-order term → "L1"):

$$
\text{Loss}_{\text{Lasso}} = \text{MSE} + \lambda \sum_{j=1}^{p} |\theta_j|
$$

- Higher $\lambda$ → bigger penalty → coefficients shrink.
- **L1 can drive coefficients exactly to 0**, so it performs **automatic feature
  selection** (a zero coefficient removes that feature).

## Ridge vs Lasso — the exam contrast

| | Ridge (L2) | Lasso (L1) |
|--|-----------|------------|
| Penalty term | $\sum \theta_j^2$ | $\sum |\theta_j|$ |
| Order | second | first |
| Coefficients → 0? | **no** (shrinks only) | **yes** (feature selection) |

Connects to [[Bias-Variance Tradeoff]] (regularization adds bias to cut variance).

## Python hands-on

```python
from sklearn.linear_model import Ridge, Lasso

ridge = Ridge(alpha=1.0).fit(X_train, y_train)   # L2
lasso = Lasso(alpha=0.1).fit(X_train, y_train)   # L1 — some coefs become 0
```

## From the live class (LVC 2): the marketing example

Framing: regularization adds a term that **stops the parameters chasing the noise** by
penalising them. **Ridge** has a *"bias in favour of zero"* — it pushes weights toward
zero but **never exactly to zero**. **Lasso** **suppresses small weights to exactly
zero**, producing a **sparse** model (larger $\alpha$ ⇒ more zeros ⇒ sparser).

**Marketing example:** as $\alpha$ grows under Lasso, the **Newspaper** and **Radio**
coefficients are driven **exactly to 0** (those features vanish), while **TV** and the
**TV·Radio** interaction are retained.

Related idea — **non-linear features**: adding a product/transformation (e.g.
**TV·Radio**) is equivalent to adding a new variable, and it lifted the advertising
model's $R^2$ from **0.897 → 0.968**. The algorithm is still called *linear* regression
because it is **linear in the parameters**, not necessarily in the variables.

*Recording: LVC 2 Lasso @ 01:14:27, Ridge @ 01:17:43.*

## Summary

- Regularization **penalizes large coefficients** to fight overfitting.
- **Ridge = L2** (sum of squares) — shrinks, never zeroes.
- **Lasso = L1** (sum of absolute values) — can **zero out** coefficients ⇒ feature
  selection.
- Larger $\lambda$ ⇒ stronger penalty ⇒ smaller coefficients.
