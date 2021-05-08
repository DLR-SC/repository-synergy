[![Build Status](https://travis-ci.org/alex-pirozhenko/sklearn-pmml.svg)](https://travis-ci.org/alex-pirozhenko/sklearn-pmml)
[![Join the chat at https://gitter.im/alex-pirozhenko/sklearn-pmml](https://badges.gitter.im/Join%20Chat.svg)](https://gitter.im/alex-pirozhenko/sklearn-pmml?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)

# sklearn-pmml

A library that allows serialization of SciKit-Learn estimators into PMML

# Installation
The easiest way is to use pip:
```
pip install sklearn-pmml
```

# Supported models
- DecisionTreeClassifier
- DecisionTreeRegressor
- GradientBoostingClassifier
- RandomForestClassifier

# PMML output

## Classification
Classifier converters can only operate with categorical outputs, and for each categorical output variable ```varname``` 
the PMML output contains the following outputs:
- categorical ```varname``` for the predicted label of the instance
- double ```varname.label``` for the probability for a given label

## Regression
Regression model PMML outputs the numeric response variable named as the output variable
