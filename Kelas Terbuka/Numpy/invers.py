import numpy as np

a = np.array([(1,-1),
              (1,1)])
print(a)
print("")

# invers matrix
a_inv = np.linalg.inv(a)
print("invers matrix a = ")
print(a_inv)
print("")
print("pembuktian :")
print(f"""invers jika dikali matrix hasilnya akan = singular 
{np.dot(a,a_inv)} """)

# determinan
det_a = np.linalg.det(a)
det_a_inv = np.linalg.det(a_inv)
print("")
print(det_a)
print(det_a_inv)