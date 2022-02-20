import statistics as st
import math as m

rentang = [40,23,41,50,49,32,41,29,52,58]
gaji2 = [41,38,39,45,47,41,44,41,37,42]
gaji = sorted(rentang)
data2 = []
data3 = []
rata2 = st.mean(gaji)

print(f"gaji dicompany 2 = {gaji} ")
print(f"dengan rata2 = {rata2} ")

# mencari simpangan rerata
for i in range(0,10):
    data = rentang[i] - rata2
    data2.append(data)

# kuadratkan simpangan reratanya
for i in range(0,10):
    data = data2[i]**2
    data3.append(data)

# nilai varian populasi
varian = sum(data3)/len(gaji)

print(f"nilai simpangan reratanya {data2} ")
print(f"dengan jumlah simpangan =  {sum(data2)}")
print("")
print(f"hasil kuadrat simpangan rerata = {data3}")
print(f"dengan jumlah = {sum(data3)}")
print("")
print(f"nilai variance gaji company 2 = {varian:.2f} :) ")

varian3 = st.variance(gaji2)

print("="*100)
varian2 = st.variance(gaji)
print(varian2)
print(f"{varian3:.2f}")

S_deviasi = m.sqrt(varian)

print("="*100)
print(S_deviasi)
