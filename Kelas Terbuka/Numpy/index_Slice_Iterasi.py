import numpy as np

a = np.arange(10)**2
hasil = 1
print(a)
print("")

# mengambil indek ke 
print(f" indek ke -  0 = {a[7]} ")
print(f" indek ke akhir = {a[-1]} ")
print("")

# slicing
print(f" nilai dari 0 - 5 = {a[0:4]} ")
print(f" nilai dari 5 - akhir {a[4:]} ")
print(f" nilai dari awal - 6 {a[:5]} ")
print("")

# iterasi
for i in a:
    print(f" nilai ke {hasil} = {i} ")
    hasil+=1