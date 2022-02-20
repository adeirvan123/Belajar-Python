class Hero():
    
    def __init__(self,name,health,atkPower,defPower):
        self.name = name
        self.health = health
        self.attack = atkPower
        self.defense = defPower
        
    def serang(self, lawan):
        print(self.name + ' menyerang ' + lawan.name)
        # akses metod diserang tapi dari lawan / ucup
        lawan.diserang(self, self.attack) # self itu = otong, lawan = ucup 
    
    def diserang(self, lawan, damage_lawan): # disini self = ucup,, lawan = otong
        print(self.name + ' diserang ' + lawan.name)
        attack_diterima = damage_lawan/self.defense
        print('Serangan terasa :' + str(attack_diterima))
        self.health -= attack_diterima
        print('Darah ' + self.name + ' tersisa ' + str(self.health))

otong = Hero('otong',100,30,10)
ucup = Hero('ucup',90,40,10)

otong.serang(ucup)
print("")
otong.serang(ucup)