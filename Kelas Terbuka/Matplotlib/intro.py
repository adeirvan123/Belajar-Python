import numpy as np
import matplotlib.pyplot as plt

# kita buat lingkaran
Pi = np.pi
sudut = np.linspace(0, 2*Pi, 100)
radius = 5

x = radius * np.cos(sudut)
y = radius * np.sin(sudut)

# inisialisasi plot
plt.plot(x,y)

# tampilkan
plt.show()