from scipy import stats
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

n = 6
p = 0.6
k = np.arange(0,n+1)
print(f"nilai k dimulai dari {k}\n")

# binomial menggunakan ardgumen (k,n,p) 
# jumlah menang, jumlah trial, %menang
# pmf (probability mass function (fungsi peluang massa))
binom = stats.binom.pmf(k,n,p)
print(binom,"\n")

for i in range(0,n+1):
    print(f"jumlah menang k ke ~ {i} ~ punya probabilitas binomial (n,p) = {binom[i]}")
print(f"\ndengan jumlah peluang selamat karna safety belt adalah = {sum(binom)} ")

nama = ['andre','beni','sinta']
skor = [15,70,25]

satu = dict(zip(nama,skor))
print(satu)