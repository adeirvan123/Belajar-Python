from scipy import stats

mean = 45
std = 12

def zScore(value):
    zscore = (value-mean)/std    
    return zscore

z_score1 = zScore(39)
# z_score2 = zScore(54)
p1 = stats.norm.cdf(z_score1)
# p2 = stats.norm.cdf(z_score2)
x = 1-p1
visitor = 200*x

print("luasan area 39 adalah = ", p1 )
print("luasan area diatas 39 adalah = ",x)
print("banyaknya orang pada probabilitas itu =", visitor  )

# print(f"""luasan area yg termasuk z-score 1 = {p1} dengan persentase {p1*100:.2f}%
# luasan area yg termasuk z-score 2 = {p2} dengan persentase {p2*100:.2f}%
# luasan antara kedua z-score adalah {x} dengan persentase {x*100:.2f}% 

# total dari 200 pengunjung = {visitor:.0f} """)

# print(f" {p1:.4f} ")