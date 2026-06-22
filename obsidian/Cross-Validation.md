---
sources:
  - page: "Cross-Validation"
    course_id: 141736
    item_id: 7718071
  - live_class: "LVC 2: Model Evaluation, Cross-Validation and Bootstrapping"
    course_id: 141736
    summary_file: 12604588
    transcript_file: 13799117
---

# Cross-Validation

**Cross-Validation** checks a model's performance by repeatedly splitting the training
data into **train** and **validation** parts before final approval — giving a more
robust estimate of how the model generalizes.

## K-Fold Cross-Validation

The most common method:

1. Randomly divide the data into **K equal folds** (e.g. 1000 obs → 5 folds of 200).
2. Hold out **one fold as validation**, train on the remaining $K-1$ folds.
3. Measure performance on the held-out fold.
4. **Repeat K times**, each time using a *different* fold for validation.
5. Average the K scores for the overall performance estimate.

Every observation is used for validation **exactly once** and for training $K-1$ times.

## Why use it

- More reliable than a single train/validation split (less dependent on one lucky/
  unlucky split).
- Helps detect [[Bias-Variance Tradeoff|overfitting]] and tune hyperparameters
  (e.g. the $\lambda$ in [[Regularization]]).

Contrast with [[Bootstrapping]] (resampling **with replacement**); K-fold partitions
**without replacement**.

## Python hands-on

```python
from sklearn.model_selection import cross_val_score, KFold

kf = KFold(n_splits=5, shuffle=True, random_state=1)
scores = cross_val_score(model, X, y, cv=kf, scoring="r2")
print(scores.mean())
```

## From the live class (LVC 2): from validation set to K-fold

The progression taught:

1. **Single validation set** — split off a hold-out to validate/tune the model.
   *Drawbacks:* (a) some data is **wasted** (never trained on), and (b) the validation
   error has **high randomness** (it depends on the one lucky/unlucky split).
2. **LOOCV (Leave-One-Out CV)** — train on **$n-1$** points, test on the 1 left out,
   **repeat $n$ times**, average the errors. *Pros:* no variability from a random
   validation set (every point is validated exactly once) and almost all data is used
   for training. *Cons:* you must **train $n$ times** (expensive), and the $n$ models
   overlap heavily so their prediction errors are **highly dependent**.
3. **K-fold CV** — the practical compromise (a coarser LOOCV): split into $K$ folds,
   rotate the hold-out, average. As $K$ rises the per-fold error tends to rise; pick the
   $K$ at a sensible error threshold (commonly 5 or 10).

*Recording: LVC 2 LOOCV @ 01:43:11.*

## Summary

- **K-fold CV**: split into K folds, rotate which fold is the validation set, average
  the K results.
- Each record validates **once**, trains $K-1$ times.
- Gives a robust generalization estimate and supports hyperparameter tuning.
