import matplotlib.pyplot as plt
import numpy as np

data = [5, 7, 9, 3, 4, -20, 3, 8, 8, 6, 90, 7, 56]
outlier_min = []
outlier_max = []
data2 = sorted(data)

# cari nilai Q1 dan Q3
q1 = np.quantile(data, .25)
q3 = np.quantile(data, .75)

# cari nilai iqr
iqr = q3 - q1

# cari nilai batas iqr
batas_iqr_min = q1-(1.5*iqr)
batas_iqr_max = q3+(1.5*iqr)
        
# bandingkan batas dengan max and min data
if (max(data) > batas_iqr_max):
  print("ada nilai pencilan high\n")
  for i in data:
    if (i > batas_iqr_max):
        outlier_max.append(i)
else:
    print("tidak ada nilai pencilan high\n")
    
if (min(data) < batas_iqr_min):
  print("ada nilai pencilan low")
  for i in data:
      if (i < batas_iqr_min):
          outlier_min.append(i)
else:
    print("tidak ada nilai pencilan low")
    
print(data2)
    
print(f"""
nilai Q1 & nilai Q3         = {q1} ; {q3}
nilai IQR                   = {iqr}
nilai batas min & batas max = {batas_iqr_min} ; {batas_iqr_max} 
nilai min dan max data      = {min(data)} ; {max(data)} 
nilai outlier high          = {outlier_max}
nilai outlier low           = {outlier_min}""")

ambil1 = data2.pop()
ambil2 = data2.pop(-2)
ambil3 = data2.pop(0)
print(data2)

box = plt.boxplot(data2)
plt.show()