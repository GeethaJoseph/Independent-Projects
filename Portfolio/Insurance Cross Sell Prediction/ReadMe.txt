The dataset is the customer details of an Insurance company that has provided Health Insurance to its customers.

Objective :To build a model to predict whether the policyholders (customers) from past year will also be interested in Vehicle Insurance provided by the company.

Features:

Id
Gender
Age
Driving_License
Region_Code
Previously_Insured
Vehicle_Age
Vehicle_Damage
Annual_Premium
PolicySalesChannel
Vintage
Response

EDA of the data is done
Missing values are imputed
Data is normalized as we are considering algorithms based on distance also like KNN and Logistic Regression
Some of the features are log transformed as they don't follow normal distribution
Categorical features are are one hot encoded
KFold Cross Validation is used
Hyperperparameter tuning done usig GridSearch
Various classification models like KNN, Logistic Regression, Decision Tree and Naive Bayes Classifier are used for prediction
Precision, Recall, F1 score, ROC-AUC curve are used performance metrics

A web app is created using Flask and deployed in the localhost