# class
class mahasiswa:
    nama = "nama"

    def belajar(self,kondisi):
        print(self.nama,"sedang belajar",kondisi)
       
    def tidur(self):
        print(f" {self.nama} sedang tidur ")
      
# main program
otong = mahasiswa()
yadi = mahasiswa()

otong.nama = "Otong Surotong"
yadi.nama = "yadi Sembako"

print("="*100)
print(otong.belajar("matematika"))
print(yadi.tidur())