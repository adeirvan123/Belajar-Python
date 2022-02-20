class mahasiswa:
    jumlah_mahasiswa = 0

    def __init__(self, input_nama, input_nim, input_prodi):
        self.nama = input_nama
        self.nim = input_nim
        self.prodi = input_prodi
        mahasiswa.jumlah_mahasiswa += 1

# main program
otong = mahasiswa("otong surotong", 4001, "teknik mesin")
ucup = mahasiswa("michale ucup", 4002, "teknik listrik")
nana = mahasiswa("nana nini", 4003, "keperawatan")

print(mahasiswa.jumlah_mahasiswa)