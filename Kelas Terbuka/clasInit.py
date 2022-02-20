class mahasiswa:
    
    def __init__(self,input_nama,input_nim):
        self.nama = input_nama
        self.nim = input_nim

    def belajar(self,kondisi):
        print(self.nama,"sedang belajar",kondisi)
       
    def tidur(self):
        print(f" {self.nama} sedang tidur ")
      
# main program
otong = mahasiswa("otong surotong",4002)
print(otong.nama)
print(otong.nim)
print(otong.belajar("sejarah"))



