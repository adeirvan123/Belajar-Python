import numpy as np

# a1 = np.array([1,3])
# b1 = np.array([2,1])

# # perkalian dot vektor
# c1 = np.dot(a1,b1)
# print(c1)

a2 = np.array([1,3,0])
b2 = np.array([2,1,0])

# perkalian cross vektor
c2 = np.cross(a2, b2)
c3 = np.cross(b2, a2)

print(c2)
print(c3)
