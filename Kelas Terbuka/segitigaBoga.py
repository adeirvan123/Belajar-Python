masukan = int(input("masukkan angka :"))
angka = 1
angka2 = 1

while angka < masukan:
    while angka2 < masukan:
        print("*"*angka2)
        angka2 += 1
    angka += 1
else:
    print("*"*angka)
  
