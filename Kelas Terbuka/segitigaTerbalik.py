masukan = int(input("masukkan angka :"))
angka = 1
angka2 = 1
angka3 = masukan

while angka < masukan:
    while angka2 < masukan:
        print("*"*angka3)
        angka3 -= 1
        angka2 += 1
    angka += 1
else:
    print("*"*1)
  