barang = ['mobil','motor','kapal','truk','becak']
print(barang)

# menambahkan komponen diinde belakang
barang.append("sambal")
print(barang)

# membuat list baru tanpa merubah list lama dari data yg sama
bekas = barang[:]
bekas.append("kejahatan")
print(barang)
print(bekas)

# insert komponen ditengah2
barang.insert(1, 'racing')
print(barang)

# extend (memecah menjadi per huruf)
barang.extend('dompet')
print(barang)