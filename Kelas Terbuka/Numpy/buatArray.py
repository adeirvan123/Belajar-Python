import numpy as np

# membuat vector
a = np.array([1,2,3,4,5])
b = np.array([1.5,2.5,3.6])

# membuat vector dengan range
c = np.arange(1,11,2)

# membuat linspace
d = np.linspace(1, 11, 4)

# membuat array multidimensi/matrix
e = np.array([(1,2,3), (4,5,6)])

# matrix dengan nilai 0
f = np.zeros((5,5))

# matrix dengan nilai 1
g = np.ones((5,5))

# matrix identitas
h = np.identity(5)
print("buat array")
print(a)
print(b)
print("")
print("vector range")
print(c)
print("")
print("linspace vector")
print(d)
print("")
print("buat matrix")
print(e)
print("")
print("matrix nilai 0")
print(f)
print("")
print("matrix niali 1")
print(g)
print("")
print("matrix identitas")
print(h)