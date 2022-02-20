import numpy as np

# membuat matrix dengan tipe data tertentu
a = np.array(([1,2,3],[4,5,6]), dtype = float)

# membuat array / matrix dengan menggunakan function
def kuadrat(kolom,baris):
    return baris**2

def jumlah(kolom,baris):
    return (kolom + baris)

b = np.fromfunction(kuadrat, (1,10), dtype = int)
c = np.fromfunction(jumlah, (4,4), dtype = float)

# membuat array / matrix dengan iterable :
iterable = (x*2 for x in range(5))
d = np.fromiter(iterable, dtype = int)

# multitype array
dtipe = [('nama','S255'), ('tinggi',int)]
data = [
    ('ucup',150),
    ('otong',160),
    ('mario',180)
]
e = np.array(data, dtype = dtipe)
print("print fungsi kuadrat")
print(b)
print("")
print("print fungsi jumlah")
print(c)
print("")
print("print perulangan")
print(d)
print("")
print("print multitype (susahhh)")
print(e)
print("")