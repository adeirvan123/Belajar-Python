nama = "Ade"
Kelas = 2

def sekolah(siswa,kelasnya):
    global nama,kelas
    nama = siswa
    kelas = kelasnya
    print(f"nama saya berubah jadi {nama} dan naik kelas {kelas}")

sekolah("Namrud", 30)
print(nama)
print(kelas)