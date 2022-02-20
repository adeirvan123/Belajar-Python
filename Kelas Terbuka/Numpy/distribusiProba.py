import itertools as it

teks = input("input kalimat : ")
print("\nOutput: ")

ateks = teks.split(' ')
for i in range(len(ateks),0,-1):
    line = it.combinations(ateks,i)
    for j in line:
        # combinasi hasilnya array
        print(' '.join(j))
