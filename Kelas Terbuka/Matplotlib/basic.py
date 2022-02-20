import numpy as np
import matplotlib.pyplot as plt

"""
$$ cara membuat plot $$
1. buat dulu datanya
2. inisialisasi plotnya
3. tampilkan plotnya
"""
a = np.arange(1,6,1)
b = a**2
c = np.array([8,10,12,14,16])

print(a)
print(b)
print(c)
print("")

plt.plot(a,b)
plt.plot(b,c)
plt.show()
