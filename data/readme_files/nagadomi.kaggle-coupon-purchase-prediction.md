# Kaggle-Coupon-Purchase-Prediction

Code for [Coupon Purchase Prediction](https://www.kaggle.com/c/coupon-purchase-prediction) (RECRUIT Challenge).

Note: This code is able to achieve a 5th place score (Private LB: 0.008776). But this is not a full version of my submitted solution (Private LB: 0.008905). My submitted solution is average of this solution and another XGBoost solution. This repositoy provides a simple version of 5th place solution. 

## Dependency (development environment)

- OS: Ubuntu 14.04
- Python: 2.7
- pip: numpy(1.9), scipy, pandas, sklearn, sklearn-pandas, chainer

## Data

Place the [data files](https://www.kaggle.com/c/coupon-purchase-prediction/data) into a subfolder ./data. And unzip. (requires `coupon_list_train.csv`, `coupon_list_test.csv`, `user_list.csv` and `coupon_detail_train.csv`)

## Local testing

validation-set: last 4 weeks.

    $ python make_data.py --validation
    $ python train.py --validation

## Run

    $ ./run.sh
    $ ls -la submission_mlp.csv

It takes around 5 hours on 4 core CPU and 16GB RAM.
If you get an out-of-memory error, use `run_low_memory.sh`.
