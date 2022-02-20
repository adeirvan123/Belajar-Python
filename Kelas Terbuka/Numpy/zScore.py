from scipy import stats
z_score1 = 6
z_score2 = 1.23
p1 = stats.norm.cdf(z_score1)
p2 = stats.norm.cdf(z_score2)
x = p2-p1
print(f"""luasan area yg termasuk z-score 1 = {p1} dengan persentase {p1*100:.2f}%
luasan area yg termasuk z-score 2 = {p2} dengan persentase {p2*100:.2f}%

luasan antara kedua z-score adalah {x} dengan persentase {x*100:.2f}% """)