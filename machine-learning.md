#### Explain linear regression:
There are two types of linear regression: Simple and Multiple.
Simple linear regression is useful for finding relationship between two continuous variables. One is predictor or independent variable and other is response or dependent variable. Core idea is to obtain a line that best fits the data. The best fit line is the one for which
total prediction are is as small as possible.
of the form: Y(pred) = b0 + b1*x
error = SUM(i=1 to n) (actual_output - predicted_output)^2

b1 = SUM(i=1 to n) (xi - xbar)(yi-ybar) / (SUM(i=1 to n) (xi - xbar)^2)
b1 = (X^T X)^(-1) X^(T)Y

R-squared might not be good for several reasons:
- only valid in linear models
-
Have to check that residuals do not exhibit any pattern (homoskedasticity)
1. Regression sum of squares (SSR)
This gives information about how far estimated regression line is from the horizontal ‘no relationship’ line (average of actual output).
Error = SUM(i=1 to n) (predicted_output - average_of_actual_output)^2
2. Sum of Squared error (SSE)
How much the target value varies around the regression line (predicted value)
error = SUM(i=1 to n) (actual_output - predicted_output)^2
3. Total sum of squares (SSTO)
How much data point moves around the mean
Error = SUM(i=1 to n) (actual_output - average_of_actual_output)^2

R^2 = 1-(SSE/SSTO)

Value of R2 may end up being negative if the regression line is made to pass through a point forcefully. This will lead to forcefully making regression line to pass through the origin (no intercept) giving an error higher than the error produced by the horizontal line. This will happen if the data is far away from the origin.
2*SUM(y_pred - y_actual)(y_pred - y_bar)
When the above term is not equal to 0, then R2 can become negative (either of the terms become negative). This tells that the horizontal line is better than the obtained regression line.


To keep or not to keep the predictor:
Null hypothesis is the initial claim that researcher specify using previous research or knowledge.
Low P-value: Rejects null hypothesis indicating that the predictor value is related to the response
High P-value: Changes in predictor are not associated with change in target


https://medium.com/@saishruthi.tn/is-r-sqaure-value-always-between-0-to-1-36a8d17807d1
https://towardsdatascience.com/linear-regression-detailed-view-ea73175f6e86

#### What is the difference between Lasso and Ridge Regression?
Because overfit is an extremely common issue in many machine learning problems, there are different approaches to solving it. The main concept behind avoiding overfit is simplifying the models as much as possible. Simple models do not (usually) overfit. On the other hand, we need to pay attention the to gentle trade-off between overfitting and underfitting a model.

One of the most common mechanisms for avoiding overfit is called regularization. Regularized machine learning model, is a model that its loss function contains another element that should be minimized as well. Let’s see an example for the ridge regression:

L = ∑( Ŷi– Yi)^2 + λ∑ β^2

so by also punishing the β we add a contraint to minimize them as much as possible


Ridge regression is an extension for linear regression. It is basically a regularized linear regression model.
The λ parameter is a scalar that should be learned as well, using cross validation.

A super important fact we need to notice about ridge regression is that it enforces the β coefficients to be lower, but it does not enforce them to be zero. That is, it will not get rid of irrelevant features but rather minimize their impact on the trained model.

The loss in the lasso function is in the form:
L = ∑( Ŷi– Yi)2 + λ∑ |β|
The only difference from Ridge regression is that the regularization term is in absolute value. But this difference has a huge impact on the trade-off we’ve discussed before. Lasso method overcomes the disadvantage of Ridge regression by not only punishing high values of the coefficients β but actually setting them to zero if they are not relevant. Therefore, you might end up with fewer features included in the model than you started with, which is a huge advantage.
https://codingstartups.com/practical-machine-learning-ridge-regression-vs-lasso/

#### What can you use Naive Bayes for:
Working on a classification problem. Can use naive bayes:
P(A|B) = [P(B|A) * P(A)]/P(B)

How naive bayes work:
data:
| weather | play    |
|---------|---------|
| sunny   |  No     |
| overcast|  Yes    |
| Rainy   |  Yes    |
| Sunny   |  Yes    |
...

Frequency & likelihood table:
| weather |   NO    |   YES   |proba occ|
|---------|---------|---------|---------|
| Overcast|    0    |    4    |    4/14 |
| Rainy   |    3    |    2    |    5/14 |
| Sunny   |    2    |    3    |    5/14 |
| Total   |    5    |    9    |
| Value   |   5/14  |   9/14  |

Step 3: Now, use Naive Bayesian equation to calculate the posterior probability for each class. The class with the highest posterior probability is the outcome of prediction.

Problem: Players will play if weather is sunny. Is this statement is correct?

We can solve it using above discussed method of posterior probability.

P(Yes | Sunny) = P( Sunny | Yes) * P(Yes) / P (Sunny)

Here we have P (Sunny |Yes) = 3/9 = 0.33, P(Sunny) = 5/14 = 0.36, P( Yes)= 9/14 = 0.64

Now, P (Yes | Sunny) = 0.33 * 0.64 / 0.36 = 0.60, which has higher probability.


P(y|X) = P(X|y) * P(y)/P(X)
X = (X_1, X_2, X_3..., X_n)



which can be expressed as:

P(y|X_1,X_2....X_n) = [P(X_1|y) * P(X_2|y) * ... * P(X_n|y) * P(y)]/[P(X_1) * ... * P(X_n)]
Now as denominator remains constant for a given input we can write:
P(y|X_1,X_2....X_n) proportional to P(y) PRODUCT(i=1 to n) (X_i|y)

Now, we need to create a classifier model. For this, we find the probability of given set of inputs for all possible values of the class variable y and pick up the output with maximum probability. This can be expressed mathematically as:
<!-- Pick the maximum likelihood! -->

y = argmax(y) P(y) PRODUCT(i=1 to n) P(X_i|y)
This is for discrete.
For continuous:

P(X_i|y) = 1/ sqrt(2PI(sigma^2))exp(-(X_i-u_y)^2/(2sigma^2))



https://www.geeksforgeeks.org/naive-bayes-classifiers/

#### What is Logistic Regression?
#### Why do you need to apply feature scaling to logistic regression?
Consider a scenario where we need to classify whether an email is spam or not. If we use linear regression for this problem, there is a need for setting up a threshold based on which classification can be done. Say if the actual class is malignant, predicted continuous value 0.4 and the threshold value is 0.5, the data point will be classified as not malignant which can lead to serious consequence in real time.
Linear regression is unbounded and hence not suitable for classification. Comes logistic regressoin.

S shape!
<!-- https://towardsdatascience.com/logistic-regression-detailed-overview-46c4da4303bc -->
<!-- https://christophm.github.io/interpretable-ml-book/logistic.html -->

#### XgBoost
Boosting is a sequential technique which works on the principle of an ensemble. It combines a set of weak learners and delivers improved prediction accuracy. At any instant t, the model outcomes are weighed based on the outcomes of previous instant t-1. The outcomes predicted correctly are given a lower weight and the ones miss-classified are weighted higher. Note that a weak learner is one which is slightly better than random guessing. For example, a decision tree whose predictions are slightly better than 50%. Let's understand boosting in general with a simple illustration.
<!-- https://www.datacamp.com/community/tutorials/xgboost-in-python#what -->



#### To see which model we like the best we can use different parameters:
BIC: Bayesian Information Criterion
AIC: Aikake Information Criterion




Nubank:
What is classification model capacity?
How to deal with classification model overfitting

IBM:
Difference between supervised & unsupervised learning.  

How do you evaluate the performance of a regression prediction model as opposed to a classification prediction model?

What do you know about Tensorflow?  

Describe precision and recall.  

Define a confidence interval?

If you have a table with a billion rows, how would you add a column inserting data from the original source without affecting the user experience?

How do you validate a machine learning model.  


What is the matrix used to evaluate the predictive model?
