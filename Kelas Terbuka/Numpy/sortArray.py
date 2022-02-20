import numpy as np
# Vektor
a = np.floor(np.random.randn(1,6)*10)
print(a)
print(" ")

print(f" nilai max dari a = {a.max()} ")
print(f" posisi dari nilai max a = {a.argmax()} ")
print(f" nilai min dari a = {a.min()} ")
print(f" posisi dari nilai min a = {a.argmax()} ")
print(" ")

print("mengurutkan nilai a :")
print(np.sort(a))
print(np.argsort(a))

# Matrik
a = np.floor(np.random.randn(2,2)*10)
print(a)
print(" ")

print(f" nilai max dari a = {a.max()} ")
print(f" posisi dari nilai max a = {a.argmax()} ")
print(f" nilai min dari a = {a.min()} ")
print(f" posisi dari nilai min a = {a.argmin()} ")
print(" ")

print("mengurutkan nilai a :")
print(np.sort(a))
print(np.argsort(a))

# Multitype Array
dtipe = [("nama","S10"),("tinggi",int)]
data = [
    ("Caca",190),
    ("Benimaru",155),
    ("Ade",180)
]
a = np.array(data, dtype = dtipe)
print(a)

print("""
sort berdasarkan tinggi""")
print(np.sort(a, order = "tinggi"))
print("""
sort berdasarkan nama""")
print(np.sort(a, order = "nama"))