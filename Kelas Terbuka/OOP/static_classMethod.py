class Hero:
    # private class variabel
    __jumlah = 0
    
    def __init__(self, name):
        self.name = name
        Hero.__jumlah += 1
    
    # method ini hanya berlaku untuk objek karena ada self
    def getJumlah(self):
        return Hero.__jumlah
    
    # method ini tidak berlaku untk objek tapi hanya untuk class
    def getJumlah1():
        return Hero.__jumlah
    
    # method static (decorator) nempel ke objek dan class
    @staticmethod
    def getJumlah2():
        return Hero.__jumlah
    
    @classmethod
    def getJumlah3(cls):
        return cls.__jumlah
    
sniper = Hero('sniper')
print(sniper.getJumlah())
rikimaru = Hero('rikimaru')
print(sniper.getJumlah3())
handoyo = Hero("dio")
print(rikimaru.getJumlah2())