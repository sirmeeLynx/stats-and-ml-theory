---
sources:
  - page: "Correlation vs Causation"
    course_id: 141736
    item_id: 7718067
  - live_class: "LVC 2: Model Evaluation, Cross-Validation and Bootstrapping"
    course_id: 141736
    summary_file: 12604588
    transcript_file: 13799117
---

# Correlation vs Causation

## Correlation

A **relationship or pattern** between two variables, observable on a **scatter plot**.

- **Positive correlation** — both variables increase together.
- **Negative correlation** — one increases as the other decreases.
- **No / zero correlation** — points are randomly scattered; no consistent trend.

## Causation

**Causation** means one event **causes** another to occur (e.g. summer → more ice-cream
sales; summer → more A/C sales).

## The key principle

> **Correlation does not imply causation.**

A third (confounding) variable may drive the apparent relationship. Ice-cream sales and
A/C sales are **positively correlated** because both rise in summer — but neither
*causes* the other; the **season** is the hidden cause.

Relevant to the [[Assumptions of Linear Regression]] (multicollinearity, endogeneity).

## From the live class

The **correlation coefficient** $r$ ranges from **−1 to +1** (inclusive): the **sign**
gives the direction, the **magnitude** the strength (LVC 1 @ 01:26:01).

**Why correlation ≠ causation (LVC 2):** across countries, **chocolate consumption**
correlates strongly with **Nobel prizes won** — but the real driver is a **latent
variable**, *wealth* (wealthier countries both consume more chocolate and win more
Nobels). A **latent variable** is one not directly observed but inferred from others;
when it is present the predictors become correlated with the residuals — a condition
called **endogeneity**.

**Simpson's paradox** — a trend that holds within each subgroup can **reverse** when the
groups are pooled. In the advertising example, within each town more budget → more
sales, yet the latent variable *competition* can make the **combined** regression line
slope the wrong way. With latent variables you can still **predict**, but you lose the
**structural model** (you cannot answer "what-if" questions). Mitigation: **add more
variables** (e.g. market size) or **non-linear features**.

*Recording: LVC 2 latent variables @ 00:27:51, Simpson's paradox @ 00:33:44.*

## Summary

- Correlation = pattern/association; causation = one variable produces the change in
  the other.
- **Correlation ≠ causation** — beware confounding variables.
