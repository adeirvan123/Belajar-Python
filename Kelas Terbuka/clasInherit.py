class Ojek():

    def __init__(self,nama,tipe_motor,asal):
        self.nama = nama
        self.tipe_motor = tipe_motor
        self.asal = asal
    
    def cek_id_ojek(self):
        print(f"""
Nama Penegemudi = {self.nama}
Tipe Motor      = {self.tipe_motor}
Asal Pengemudi  = {self.asal}
        """)

class Gojek(Ojek):
    
    def cek_id_ojek(self):
        print(f"Periksa ID Pengemudi")


ojek1 = Ojek("Otong", "Matic", "Nganjuk")
ojek2 = Gojek("Ucup", "manual", "Rejoso")
ojek1.cek_id_ojek()
ojek2.cek_id_ojek()