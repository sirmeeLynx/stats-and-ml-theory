---
sources:
  - page: "Maximum Likelihood and Empirical Risk Minimization"
    course_id: 141736
    item_id: 7718042
  - live_class: "LVC 1: Introduction to Supervised Learning and Regression"
    course_id: 141736
    summary_file: 12604567
    transcript_file: 13795232
---

# Maximum Likelihood and Empirical Risk Minimization

Two equivalent ways to **estimate the parameters** ($\theta_0, \theta_1$) of a
[[Linear Regression]] model.

## Maximum Likelihood (MLE)

For a sample $(X_i, Y_i)$ with $n$ records, the **likelihood** of event $Y_i \mid X_i$
is the probability it occurs given the inputs. Under the assumption that:

- the events are **independent**, and
- the **error terms are normally distributed** (mean = prediction, std $\sigma$),

the likelihood of the whole sample is the **product** of individual likelihoods
(multiplication rule for independent events):

$$
L(\theta) = \prod_{i=1}^{n} P(Y_i \mid X_i)
$$

The parameters are chosen to **maximize** $L$. The maximum value is the
**maximum likelihood**.

## Empirical Risk Minimization (ERM)

**Risk** = error: higher error ⇒ higher risk. **Empirical risk** is the collective
error over all training records:

$$
\text{Empirical Risk} = \frac{1}{n}\sum_{i=1}^{n} \text{Loss}(Y_i, \hat{Y}_i)
$$

We estimate parameters by **minimizing** this empirical risk (e.g. minimizing MSE).

## The key relationship

> **A higher empirical risk is equivalent to a lower likelihood, and vice versa.**

So **maximizing likelihood** and **minimizing empirical risk** lead to the same
estimated parameters.

## From the live class (LVC 1)

The estimator $g$ can be obtained several ways. Two were named in class:

- **Plug-in estimators** — approximate a feature of the *true* distribution by the
  **same feature of the empirical distribution** of a sample (e.g. a population quantile
  is approximated by the analogous **sample** quantile).
- **Maximum likelihood** — build the loss/cost function from the data, treat the
  **model parameters** as the unknowns under a hypothesis, then **maximise the
  likelihood using calculus** to solve for them. These parameters are taken as best for
  the model that relates output to inputs.

*Recording: LVC 1 @ 01:00:20.*

## Summary

- **MLE**: maximize the (product of) probabilities of the observed data; assumes
  independent events with normally distributed errors.
- **ERM**: minimize the total training error (risk).
- They are two sides of the same coin: **max likelihood ⇔ min empirical risk**.
