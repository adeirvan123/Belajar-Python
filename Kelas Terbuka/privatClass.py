class mahasiswa:
    prodi = "Sastra Mesin"
    __nilai = 0 # private (sebagai nilai default)

    def __init__(self,input_nama,input_nim):
        self.nama = input_nama  # public
        self.nim = input_nim    # public

    def uts(self,input_nilai):
        self.__nilai += input_nilai
        return f" nilai uts = {self.__nilai} "
        
    def uas(self,input_nilai_baru):
        self.__nilai += input_nilai_baru
        return f" nilai uas = {self.__nilai} "

    def check(self):
        if self.__nilai <= 50:
            return f" {self.nama} tidak lulus ujian dengan total nilai {self.__nilai} "
        else:
            return f" {self.nama} lulus ujian dengan total nilai {self.__nilai} "
      
# main program
otong = mahasiswa("otong surotong",4001)
ucup  = mahasiswa("michael ucup", 4002)
print(otong.uts(10))
print(otong.uas(60))
print(otong.check())
print(ucup.uts(5))
print(ucup.uas(24))
print(ucup.check())
