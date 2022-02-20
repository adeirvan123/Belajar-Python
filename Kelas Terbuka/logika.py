print("NO. 1")
#----0++++5----8++++11----
inputan = float(input("Masukkan angka : "))
hasil = (inputan>0 and inputan<5) or (inputan>8 and inputan<11)
print("Hasil No 1 adalah",hasil)
print(" ")

print("No. 2")
#++++0----5++++8----11++++
inputan2 = float(input("Masukkan angka : "))
hasil2 = (inputan2>5 and inputan2<8) or (inputan2<0) or (inputan2>11)
print("hasil No 2 adalah",hasil2)
print(" ")
