Benchmarks for Kaggle's [Predict Closed Questions on Stack Overflow](https://www.kaggle.com/c/predict-closed-questions-on-stack-overflow) competition

The benchmarks require several Python packages:

 - numpy
 - pandas
 - sklearn

These packages can be installed with easy_install or pip, or Windows users can [download compiled versions of these packages](http://www.lfd.uci.edu/~gohlke/pythonlibs/)

To run the benchmarks, you also need to [download the data](https://www.kaggle.com/c/predict-closed-questions-on-stack-overflow/data). The only files necessary for the benchmarks are train-sample.csv and public_leaderboard.csv. Two variables need to be updated in competition_utilities.py as well: data_path should be set to the path to the data, and submissions_path should be set to the location for writing the submission files.