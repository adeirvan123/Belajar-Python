import numpy as np

a = np.array([1,2,3])
b = np.array([4,5,6])
c = np.zeros((2,3))
d = np.ones((2,3))

# stacking / menumpuk = horizontal & vertikal
# pada matrix syaratnya harus sama ordonya
beb = np.hstack((a,b))
bib = np.vstack((b,a))
cuk = np.hstack((c,d))
cok = np.vstack((c,d))

print(beb)
print("")
print(bib)
print("")
print(cuk)
print("")
print(cok)