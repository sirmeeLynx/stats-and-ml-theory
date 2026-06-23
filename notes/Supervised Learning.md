---
sources:
  - page: "Basic Terminologies"
    course_id: 141736
    item_id: 7718040
  - page: "Supervised Learning - Linear Regression"
    course_id: 141736
    item_id: 7718041
  - live_class: "LVC 1: Introduction to Supervised Learning and Regression"
    course_id: 141736
    summary_file: 12604567
    transcript_file: 13795232
    recording: "@ 00:29:34"
---

# Supervised Learning

**Supervised learning** trains an algorithm on **labeled data** — data already tagged
with the correct output (the *label*). After training, the model predicts the label
for new instances where it is unknown. The analogy: a teacher (the labels) grades a
student's answers (the predictions); the **error** is what the model minimizes.

This contrasts with **unsupervised learning** (clustering,
[[Dimensionality Reduction (PCA)|PCA]], dimensionality
reduction), which has *no* labeled target.

## Two kinds of supervised problems

| Type | Output variable | Example |
|------|-----------------|---------|
| **Regression** | continuous | house price, income, age, duration |
| **Classification** | categorical | spam / not-spam, loan approve / deny |

- A **continuous variable** can take infinitely many numeric values in a range
  (e.g. monthly income).
- A **categorical variable** takes a finite set of distinct values (e.g. handwritten
  digit 0–9).

## Dependent vs independent variables

- The **dependent variable** ($Y$) is the one we estimate (e.g. Salary).
- The **independent variables** ($X$) are the features that affect it (Age, Education,
  Experience).

## Supporting statistics

- [[Variance]] and [[Standard Deviation]] measure spread about the [[Mean]]. SD is the
  square root of variance, so it shares the data's units and is more interpretable.
- A **point estimate** is a single-number guess for a population parameter; a
  [[Confidence Intervals|confidence interval]] is a range around it that contains the
  parameter with a stated confidence. **Higher confidence ⇒ wider interval.**

See [[Linear Regression]] for the first regression algorithm and [[Classification]]
for logistic regression and K-NN.

## The supervised-learning workflow

The professor framed a supervised-learning project as **four steps**:

1. **Formulation** — identify the output feature and the input features (define the
   problem precisely).
2. **Solution** — establish the relation between output and inputs using the algorithm
   and the available data.
3. **Performance assessment** — measure the model (there are many metrics) and compare
   it with alternatives.
4. **Interpretation** — translate the result back into business terms for
   decision-making.

He also contrasted **two ways to attack a data-science problem**:

- **Data → ML → Prediction** (machine-learning approach): build a formula — the *model*
  — straight from data; the theory need not explain why it works.
- **Data → Stats → Model → Prediction** (statistical approach): use statistical theory
  to build an **interpretable** model.

The input→output mapping is an **estimator** $y = g(x_1, x_2, \dots, x_n)$, trained on
the available data and used to predict unseen data.

## Summary

- Supervised = learn from **labeled** data; unsupervised = no labels.
- **Regression** predicts a continuous target; **classification** predicts a category.
- Quiz mindset: if the target is a number → regression; if it is a class/label →
  classification.
