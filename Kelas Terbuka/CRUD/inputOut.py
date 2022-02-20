# untuk membuat file eksternal (CRUD) ada 4 macam :
 
# w = untuk write, yaitu mode menulis dan menghapus file lama, 
# jika belum ada file maka akan dibuat
# r = untuk read, yaitu mode membaca file ke terminal
# a = untuk append, yaitu mode menambahkan isi ke ke paling akhir
# r+ = write and read mode

# mode menulis write
file = open("data.txt", "w")

file.write("ini dibuat oleh write")
file.write("\nini data ke 2")
file.write("\nini data ke 3")
file.close()

# # mode membaca read
file2 = open("data.txt", "r")

# print(file2.read())
print(file2.read(10))
print(file2.readline())
file2.close()

# mode append
file3 = open("data.txt","a")

file3.write("\ngua tambahin aja broo")
file3.close()

