---
sources:
  - page: "LDA and QDA"
    course_id: 141736
    item_id: 7718139
  - live_class: "LVC 3: Introduction to Supervised Learning and Classification"
    course_id: 141736
    summary_file: 12604566
    transcript_file: 13808560
    recording: "Bayes rule @ 00:43:02, posterior @ 00:59:23"
---

# LDA and QDA

**Linear Discriminant Analysis (LDA)** and **Quadratic Discriminant Analysis (QDA)** are
classification methods built on **Bayes' theorem** and prior/posterior probabilities.

## Prior and posterior probabilities

- **Prior probability** $P(\text{class }k)$ — probability of a class *before* seeing the
  features. E.g. 48 good of 80 products ⇒ prior(good) = 48/80 = 0.6, prior(defective) =
  0.4.
- **Posterior probability** $P(\text{class }k \mid X)$ — probability of a class *after*
  observing features $X$. This is what we use to predict.

**Bayes' theorem** links them:

$$
P(k \mid X) = \frac{P(X \mid k)\,P(k)}{P(X)}
$$

For a single feature, $P(X \mid k)$ is modeled as a **normal distribution**; for
multiple features we use the **covariance matrix** (the generalization of variance to
multiple variables — its diagonal entries are the per-variable variances).

## LDA vs QDA — the key distinction

Both predict the class that **maximizes the log of the posterior probability**. The
difference is the covariance assumption:

| | LDA | QDA |
|--|-----|-----|
| Covariance matrices | **same** for all classes | **different** per class |
| Decision boundary | **linear** | **quadratic / non-linear** |
| Best when | **few** observations | **large** dataset |

- **LDA** — assumes all classes share **one covariance matrix**; draws a **linear**
  boundary that best separates classes. Preferred with **small** samples.
- **QDA** — allows **different covariance matrices** per class; draws a **quadratic**
  (more flexible) boundary; performs better on **large** datasets.

Relates to [[Classification]] and [[Normal Distribution]].

## Derivation and loan-default results

Both methods come from a **Gaussian model-based** classifier combined with **Bayes'
rule**. Each class $k$ has a **prior** $\pi_k = P(Y=k)$ and a (multivariate) **normal**
$P(X\mid Y=k)$ with mean vector $\mu_k$ and covariance matrix $C_k$. Bayes converts these
into the **posterior** $P(Y=k\mid X) \propto \pi_k\,P(X\mid Y=k)$, and we **pick the
class with the largest log-posterior**:

$$
\log(\pi_k \gamma_k) - \tfrac{1}{2}(X-\mu_k)^{T} C_k^{-1} (X-\mu_k)
$$

- If the covariances **differ** per class → the boundary is **quadratic** → **QDA**.
- If all covariances are **equal** ($C_k = C$) → the boundary is **linear** → **LDA**.
  LDA also **minimises the within-class** distance and **maximises the between-class**
  distance.

**Loan-default misclassification rates** (using all features): **LDA 2.75%, QDA 2.70%**
— both beat the 3.33% base rate of the dumb "everyone no-default" model.

## Summary

- Both use **Bayes' theorem** (prior × likelihood → posterior) and predict the class
  with the **highest log-posterior**.
- **LDA = same covariance ⇒ linear boundary** (good for small data).
- **QDA = different covariances ⇒ quadratic boundary** (good for large data).
