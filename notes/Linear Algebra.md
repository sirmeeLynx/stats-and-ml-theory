---
sources:
  - page: "Basics of Linear Algebra"
    course_id: 141735
    item_id: 7718206
---

# Linear Algebra

A little **linear algebra** goes a long way in machine learning: it is the language used
to express the data and the operations inside almost every algorithm. Data is most often
represented with **matrices** and **vectors**.

## Matrices and vectors

- A **matrix** of size $m \times n$ is a two-dimensional array with $m$ rows and $n$
  columns. Input data is typically stored this way — one row per observation, one column
  per feature.
- A **vector** is a one-dimensional array: a single row (**row vector**) or a single
  column (**column vector**).

$$
X = \begin{bmatrix} 1 & 2 \\ 3 & 4 \\ 5 & 6 \end{bmatrix}\!, \qquad
Y = \begin{bmatrix} 7 \\ 8 \\ 9 \end{bmatrix}
$$

Here $X$ is a $3\times 2$ matrix and $Y$ is a column vector.

## Addition and subtraction

Two matrices (or two vectors) must be the **same size** to be added or subtracted. The
operation is **element-wise** — corresponding entries are combined:

$$
\begin{bmatrix} a_1 \\ a_2 \\ a_3 \end{bmatrix} +
\begin{bmatrix} b_1 \\ b_2 \\ b_3 \end{bmatrix} =
\begin{bmatrix} a_1+b_1 \\ a_2+b_2 \\ a_3+b_3 \end{bmatrix}
$$

## Matrix × vector

To multiply a matrix by a column vector, the matrix must have as **many columns** as the
vector has elements. Each output entry is the dot product of a matrix row with the vector:

$$
\begin{bmatrix} 1 & 2 & 3 \\ 4 & 5 & 6 \\ 7 & 8 & 9 \end{bmatrix}
\begin{bmatrix} 2 \\ 1 \\ 3 \end{bmatrix}
= \begin{bmatrix} 1\cdot2+2\cdot1+3\cdot3 \\ \vdots \\ \vdots \end{bmatrix}
= \begin{bmatrix} 13 \\ \vdots \\ \vdots \end{bmatrix}
$$

## Matrix × matrix (dot product)

To multiply two matrices, the number of **columns in the first** must equal the number of
**rows in the second**. If $A$ is $m\times k$ and $B$ is $k\times n$, then $AB$ is
$m\times n$. Entry $(i,j)$ is the dot product of row $i$ of $A$ with column $j$ of $B$:

$$
\begin{bmatrix} 1 & 2 & 3 \\ 4 & 5 & 6 \end{bmatrix}
\begin{bmatrix} 7 & 10 \\ 8 & 11 \\ 9 & 12 \end{bmatrix}
= \begin{bmatrix} 50 & 68 \\ 122 & 167 \end{bmatrix}
$$

For example, the top-left entry is $1\cdot7 + 2\cdot8 + 3\cdot9 = 50$.

> Matrix multiplication is **not commutative**: $AB \neq BA$ in general.

## Determinant

The **determinant** is a single number defined only for a **square** matrix (equal rows
and columns). For a $2\times2$ matrix:

$$
A = \begin{bmatrix} a & b \\ c & d \end{bmatrix}, \qquad
\det(A) = ad - bc
$$

The determinant tells us, among other things, whether a matrix is **invertible**: a
matrix with $\det(A)=0$ has no inverse. This fact is the key that unlocks
[[Eigenvectors and Eigenvalues]].

## Python hands-on

In Python, vectors and matrices are **NumPy arrays**.

```python
import numpy as np

A = np.array([[1, 2, 3], [4, 5, 6]])
B = np.array([[7, 10], [8, 11], [9, 12]])

A @ B                      # matrix product
np.dot(A, B)               # same thing
np.linalg.det(np.array([[1, 2], [3, 4]]))   # determinant
```

## Summary

- Data lives in **matrices** ($m\times n$) and **vectors** (1-D).
- Addition/subtraction is **element-wise** and needs matching sizes.
- For a product, inner dimensions must match; entries are **dot products** of rows × columns.
- The **determinant** exists only for square matrices; $\det=0$ ⇒ non-invertible.
- These ideas underpin [[Eigenvectors and Eigenvalues]], the [[Covariance Matrix]], and
  [[Dimensionality Reduction (PCA)]].
