# # format untuk string
# nama = "otong"
# format_str = f"hello {nama}"
# print(format_str)

# # untuk angka
# angka = 2005.6
# format_angka = f"angka adalah = {angka}"
# print(format_angka)

# # tipe bilangan juga bisa dimasukkan
# desimal = 50.5656 #koma pake titik
# format_dsm = f"desimal adalah = {desimal:.2f}"
# print(format_dsm)

# # menampilkan angka jutaan dengan tanda koma
# jutaan = 2000000
# format_jt = f"harganya adalah Rp.{jutaan:,}"
# print(format_jt)

# # menampilkan tanda + dan -
# angka_min = -70
# angka_plus = +60.7790
# format_min = f"nilai angak min = {angka_min:+d}"
# format_plus = f"nilai angka plus = {angka_plus:+.2f}"
# print(format_min)
# print(format_plus)

# # menampilkan persen tanpa setting
# persen = 0.04567
# format_sen = f"nilai % no setting = {persen:%}"
# print(format_sen)

# # menampilkan persentase
# persen = 0.04567
# format_persen = f"nilai persen = {persen:.2%}"
# print(format_persen)

# # mengoperasikan aritmatika di curveholder {}
# jumlah = 10
# harga = 12000
# format_total = f"total pembelian = Rp.{jumlah*harga:,}"
# print(format_total)

# mengubah ke binary, octal , dan hexadesimal
angka = 255
binary = bin(angka)
octal = oct(angka)
hexadesimal = hex(angka)
format_bilangan = f"""nilai biner = {binary}, 
nilai octal = {octal}, 
nilai hexadesimal = {hexadesimal}"""
print(format_bilangan)