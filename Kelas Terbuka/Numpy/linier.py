import numpy as np

A = np.array([(2,3),(1,2)])
Y = np.array([(23),(14)])
print(A)
print(Y)
print(" ")

# menyelesaikan persamaan linier
A_inv = np.linalg.inv(A)
print(f"Hasil dari x1 dan x2 = ")
print(np.cross(A_inv,Y))
print("")

# cara cepat pakai method solve()
print("Cara Cepat Slurrr = ")
print(np.linalg.solve(A, Y))
