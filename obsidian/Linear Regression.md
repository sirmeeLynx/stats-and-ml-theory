---
sources:
  - page: "Supervised Learning - Linear Regression"
    course_id: 141736
    item_id: 7718041
  - live_class: "LVC 1: Introduction to Supervised Learning and Regression"
    course_id: 141736
    summary_file: 12604567
    transcript_file: 13795232
---

# Linear Regression

**Linear Regression** finds the **linear relationship** between independent variables
($X$) and a continuous dependent variable ($Y$). For one feature:

$$
Y = \theta_0 + \theta_1 X + R
$$

- $\theta_0$ — intercept (constant term)
- $\theta_1$ — coefficient (slope) of $X$
- $R$ — the **error / residual** = actual − predicted

$\theta_0, \theta_1$ are the **parameters**; $X, Y$ are the variables.

## Error and the best-fit line

The **residual** is the gap between actual and predicted values:

$$
R_i = Y_i - \hat{Y}_i
$$

We choose $\theta_0, \theta_1$ to **minimize the Mean Squared Error (MSE)**:

$$
\text{MSE} = \frac{1}{n}\sum_{i=1}^{n}(Y_i - \hat{Y}_i)^2
$$

The fitted model is $\hat{Y} = \hat{\theta}_0 + \hat{\theta}_1 X$. Parameters are
estimated via [[Maximum Likelihood and Empirical Risk Minimization]].

## Regression performance metrics

- **R-squared ($R^2$)** — fraction of variation in $Y$ explained by the model.
  $R^2 = 0.80$ ⇒ model captures 80% of the variance. **Higher = better fit.**
  *Caveat:* $R^2$ **always increases** when you add a feature, useful or not.
- **Adjusted R-squared** — penalizes for the number of predictors. It **increases only
  if a new variable adds value** and **decreases** if it does not. Preferred over $R^2$
  when there are multiple independent variables.
- **RMSE (Root Mean Squared Error)** — $\sqrt{\text{mean of squared residuals}}$;
  same units as $Y$. **Lower = better.**

$$
\text{RMSE} = \sqrt{\frac{1}{n}\sum_{i=1}^{n}(Y_i - \hat{Y}_i)^2}
$$

See [[Assumptions of Linear Regression]] for when the model is valid, and
[[Regularization]] / [[Bias-Variance Tradeoff]] for controlling overfitting.

## Python hands-on

```python
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_squared_error
import numpy as np

model = LinearRegression().fit(X_train, y_train)
pred = model.predict(X_test)

r2 = r2_score(y_test, pred)
rmse = np.sqrt(mean_squared_error(y_test, pred))
```

## From the live class (LVC 1): Advertising & Sales

The flagship worked example: advertising spend on **TV, Radio and Newspaper across 200
markets** versus **Sales** (a continuous target ⇒ regression). Scatter/correlation
analysis showed **TV** strongly related to sales, **Radio** weaker, and **Newspaper**
almost flat. The fitted model:

$$
\text{Sales} = 2.94 + 0.046\,(TV) + 0.19\,(Radio) - 0.001\,(News), \qquad R^2 = 0.897
$$

The quantity minimised is the **sum of squared residuals**, with $R_i = y_i - \hat{y}_i$.
Adding the interaction feature **TV·Radio** lifts $R^2$ to **0.968** — see
[[Regularization]] for why that is still "linear" regression. *Recording: LVC 1 @
00:29:34; residuals @ 00:37:11.*

## Summary

- Model: $Y = \theta_0 + \theta_1 X + R$; fit by **minimizing MSE** (least squares).
- **Residual** = actual − predicted.
- $R^2$ ↑ measures fit but always grows with more features; **adjusted $R^2$** is the
  honest metric for multiple predictors; **RMSE** lower is better.
