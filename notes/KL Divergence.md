---
sources:
  - page: "Kullback-Leibler (KL) Divergence"
    course_id: 141735
    item_id: 7718210
---

# KL Divergence

Sometimes we need to quantify **how different one probability distribution is from
another** — for example, comparing an observed distribution with a theoretical one.
**Divergence** is such a measure.

A key property: divergence is **not symmetric** — scoring how $p$ differs from $q$ gives a
different value than how $q$ differs from $p$.

## Kullback–Leibler divergence

The **Kullback–Leibler (KL) divergence** quantifies how much one distribution $p$ differs
from another distribution $q$. For discrete distributions:

$$
D_{KL}(p \,\|\, q) = \sum_{i} p(i)\, \log \frac{p(i)}{q(i)}
$$

Two points to remember:

- **Lower is better** — the smaller the KL divergence, the more closely the two
  distributions match. If they are **identical**, $D_{KL} = 0$.
- It is **asymmetric**:

$$
D_{KL}(p \,\|\, q) \neq D_{KL}(q \,\|\, p)
$$

**Intuition:** divergence is large when $p$ assigns **high** probability to an event that
$q$ assigns **low** probability to. The reverse case (small $p$, large $q$) also adds
divergence, but less than the former — which is exactly why the measure is not symmetric.

## Where it shows up

KL divergence is the objective minimised by [[Dimensionality Reduction (PCA)|t-SNE]] when
matching high- and low-dimensional similarity distributions, and it underlies many
information-theoretic and probabilistic models.

## Python hands-on

```python
from scipy.special import rel_entr   # rel_entr(p, q) = p * log(p/q), elementwise

p = [0.1, 0.4, 0.5]
q = [0.2, 0.3, 0.5]
kl_pq = sum(rel_entr(p, q))          # not equal to sum(rel_entr(q, p))
```

## Summary

- KL divergence measures **how far** distribution $p$ is from $q$.
- $D_{KL}(p\|q)=\sum_i p(i)\log\frac{p(i)}{q(i)}$; it is **0** for identical distributions
  and grows with mismatch.
- It is **asymmetric** ($D_{KL}(p\|q)\neq D_{KL}(q\|p)$), so the order matters.
