# Statistics and Machine Learning Theory

Study notes for the Statistics for Data Science track, built from the course
video lectures. Each note links to the exact video and timestamp where a concept
is explained, and concepts cross-link to form a knowledge graph.

## Foundations

- [[Statistics]]
- [[Inferential Statistics]] — sample → population, parameters vs statistics
- [[Distribution Terms]] — random variables, PMF / PDF / CDF
- [[Mean]] · [[Variance]] · [[Standard Deviation]]

## Distributions

- [[Binomial Distribution]] — $P(X=k)=\binom{n}{k}p^k(1-p)^{n-k}$
- [[Uniform Distribution]] — discrete and continuous
- [[Normal Distribution]] — empirical rule, percentiles
- [[Z-Score]] — standardization $z=\frac{x-\mu}{\sigma}$

## Sampling & Estimation

- [[Sampling and Inference]] — sampling distributions, standard error
- [[Central Limit Theorem]] — sampling distribution of the mean → normal
- [[Estimation]] — point estimates, confidence intervals, z vs t

## Hypothesis Testing

- [[Hypothesis Testing]] — overview
- [[Null and Alternative Hypothesis]] — $H_0$ vs $H_a$
- [[Hypothesis Test Procedure]]
- [[p-value and Significance]] — decide via p-value $< \alpha$
- [[Type I and Type II Errors]] — false positive vs false negative
- [[Performing a Hypothesis Test]] — worked example
- [[One-tailed and Two-tailed Tests]]
- [[Confidence Intervals]] — CI / test duality

## Machine Learning — Supervised Learning

### Regression

- [[Supervised Learning]] — labeled data; regression vs classification
- [[Linear Regression]] — $Y=\theta_0+\theta_1 X+R$; MSE, $R^2$, adjusted $R^2$, RMSE
- [[Maximum Likelihood and Empirical Risk Minimization]] — max likelihood ⇔ min risk
- [[Assumptions of Linear Regression]] — linearity, multicollinearity, homoscedasticity, normal errors, endogeneity
- [[Correlation vs Causation]] — correlation ≠ causation
- [[Bias-Variance Tradeoff]] — overfit (high variance) vs underfit (high bias)
- [[Regularization]] — Ridge (L2) vs Lasso (L1, feature selection)
- [[Bootstrapping]] — resampling with replacement
- [[Cross-Validation]] — K-fold

### Classification

- [[Classification]] — logistic regression (sigmoid), K-NN
- [[Classification Performance Metrics]] — confusion matrix, accuracy, precision, recall, F1
- [[LDA and QDA]] — Bayes-based; same vs different covariance
