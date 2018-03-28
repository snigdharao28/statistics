#importing the necessary libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#acquiring the dataset
dataset = pd.read_csv('/home/snigdharao/Desktop/psqt_aat/uspop_stat.csv')


#procuring X values
X = dataset.iloc[:, [1]].values

#procuring Y values
Y = dataset.iloc[:, [2]].values

#determining mean
mean_X = X.mean()
mean_Y= Y.mean()
total = mean_X + mean_Y
tot_mean = total.mean()

#determining standard deviation
std_X = np.std(X)
std_Y = np.std(Y)

#determining variance
var_X = pow(std_X,2)
var_Y = pow(std_Y,2)

#sum of squared difference
differences = [i - tot_mean for i in X]
sq_differences = [d ** 2 for d in differences]
ssd = sum(sq_differences)

#ssd within x
differences_ssw_X = [i - mean_X for i in X]
sq_differences_ssw_X = [dx ** 2 for dx in differences_ssw_X]
ssd_X = sum(sq_differences_ssw_X)

#ssd within y
differences_ssw_Y = [j - mean_Y for j in Y]
sq_differences_ssw_Y = [dy ** 2 for dy in differences_ssw_Y]
ssd_Y = sum(sq_differences_ssw_Y)

#ssd within total
ssw = ssd_X + ssd_Y

#ssd between x
differences_ssb_X = [mean_X - tot_mean for i in X]
sq_differences_ssb_X = [dx ** 2 for dx in differences_ssb_X]
ssb_X = sum(sq_differences_ssb_X)

#ssd between y
differences_ssb_Y = [mean_Y - tot_mean for i in Y]
sq_differences_ssb_Y = [dy ** 2 for dy in differences_ssb_Y]
ssb_Y = sum(sq_differences_ssb_Y)

ssb = ssb_X + ssb_Y
chi1 = ssw/1

den = 154

chi2 = ssb/154

f_statistic = chi1/chi2










