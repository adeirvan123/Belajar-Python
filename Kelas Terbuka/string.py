# alokasi karakter rjust() {kanan}, 
# ljust {kiri}, center() {tengah}.

kanan = "kanan".rjust(10)
print("'"+kanan+"'")

print("")

kiri = "kiri".ljust(10,"-")
print("'"+kiri+"'")

print("")

tengah = "tengah".center(20,"_")
print("'"+tengah+"'")

print("")

# kebalikannya -> strip()
tengah = tengah.strip("_") #menghilangkan tanda :
print("'"+tengah+"''")









# nama = "kurniawan_tamvan"
# print(len(nama)) #panjang
# print("mengambil index ke 0 - 4 = " + nama[0:5])
# print("mengambil index ke 0,2,4,6,8,10,12,14,16 = " + nama[0:16:2])
# print("mengambil index ke 0 - 4 = " + nama[-1])

# #mengambil nilai max & min
# print("nilai max adalah " + max(nama))
# print("nilai min adalah " + min(nama))

# ascii_code = ord("_")
# print(r"melihat nilai ascii untuk '_' = " + str(ascii_code))
# print(r"melihat nilai ascii untuk 'w' = " + str(ord("w")))

