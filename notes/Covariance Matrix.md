---
sources:
  - page: "The Covariance Matrix"
    course_id: 141735
    item_id: 7718208
---

# Covariance Matrix

## Variance and covariance

**Variance** measures how far a single random variable is spread around its
[[Mean|mean]]. For a variable $x$ with $n$ samples and mean $\bar{x}$:

$$
\sigma^2(x) = \frac{1}{n}\sum_{i=1}^{n}(x_i - \bar{x})^2
$$

**Covariance** measures how *two* variables vary **together** — e.g. a person's income
and their expenditure:

$$
\sigma(x, y) = \frac{1}{n}\sum_{i=1}^{n}(x_i - \bar{x})(y_i - \bar{y})
$$

- Positive covariance ⇒ the variables tend to rise together.
- Negative covariance ⇒ one tends to rise as the other falls.
- The variance is just the covariance of a variable **with itself**: $\sigma^2(x)=\sigma(x,x)$.

## The covariance matrix

Collecting these for a set of variables gives the **covariance matrix**. For two
dimensions $x$ and $y$:

$$
\Sigma =
\begin{bmatrix}
\sigma(x,x) & \sigma(x,y) \\
\sigma(y,x) & \sigma(y,y)
\end{bmatrix}
$$

- The **variances** sit on the **diagonal**.
- The **covariances** sit on the **off-diagonal** elements, and the matrix is symmetric
  ($\sigma(x,y)=\sigma(y,x)$).

This matrix is central to [[Dimensionality Reduction (PCA)|PCA]]: its
[[Eigenvectors and Eigenvalues|eigenvectors]] become the principal components, and its
eigenvalues give the variance explained along each.

## Python hands-on

```python
import numpy as np

X = np.array([[2.1, 8.0], [2.5, 10.5], [3.6, 12.1], [4.0, 14.2]])
np.cov(X, rowvar=False)   # 2x2 covariance matrix (variances on the diagonal)
```

## Summary

- **Variance** = spread of one variable; **covariance** = joint variation of two.
- The **covariance matrix** stores variances on its diagonal and covariances off it; it
  is symmetric.
- It is the object PCA diagonalises to find directions of maximum variance.
