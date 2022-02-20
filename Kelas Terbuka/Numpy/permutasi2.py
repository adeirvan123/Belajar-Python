import itertools as it

data = ['A','B','C','D']
hitung = 0

kombinasi = it.combinations(data,2)

for com in kombinasi:
    print(com)
    hitung +=1
print(hitung)




# permutasi = it.permutations(range(4),2)
# hasil = len(list(permutasi))

# print(hasil)
