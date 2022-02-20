class Hero():
    def __init__(self,name,health,attackPower):
        # make it private variabel instance (protected)
        self.__name = name
        self.__health = health
        self.__attPower = attackPower
        
    # getter (memanggil name variabel)
    def getName(self):
        return self.__name
    
    def getHealth(self):
        return self.__health
    
    def getAttack(self):
        return self.__attPower
    
    # setter (merubah nilai dari var private)
    def diserang(self,damageDiterima):
        self.__health -= damageDiterima
    
    def attackBaru(self,nilaiBaru):
        self.__attPower += nilaiBaru
        
# awal mulai game
rikimartin = Hero('rikimartin',120,15)

# game berjalan
print(rikimartin.getName())
print(rikimartin.getHealth())
print("setelah diserang lawan :::>>>")
rikimartin.diserang(45)
print(rikimartin.getHealth())
rikimartin.attackBaru(50)
print(f"atack baru rikirmartin menajadi {rikimartin.getAttack()} ")