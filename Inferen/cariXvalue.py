from os import stat
from numpy import std
from scipy import stats

probabilitas = (10/100)
z_score = stats.norm.ppf(probabilitas)
x_value = (z_score*10)+50

print(probabilitas,"\n")
print(z_score)
print(x_value)
