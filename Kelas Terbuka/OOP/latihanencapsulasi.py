class Hero:
    # private class atribut (jumlah hero)
    __jumlah = 0
    
    def __init__(self, name, health, attPower, armor):
        self.__name = name
        self.__healthStandar = health #nyawa bawaan hero pas lvl 1 = 100 semua hero
        self.__attPowerStandar = attPower #attack bawaan hero pas lvl 1 
        self.__armorStandar = armor #armor bawaaan hero pas lvl 1
        self.__level = 1
        self.__exp = 0
        
        # darah naik seratus tiap naik level 1x 
        self.__healthMax = self.__healthStandar * self.__level
        # attack naik naik 1 setiap naik level x attack standar
        self.__attPower = self.__attPowerStandar * self.__level
        # armor naik 2 setiap naik level x defense standar
        self.__armor = self.__armorStandar * self.__level
        
        # kondisi darah aktual hero (darah = darah max (100 pada lvl 1))
        self.__health = self.__healthMax
        
        # setiap ada objek baru/hero baru ==> jumlah hero tambah 1
        Hero.__jumlah += 1
        
# buat method info menjadi atribut agar bisa menampilkan 
# private instance atribut di luar class
    @property
    def info(self):
        return "{} level {} : \n\thealth = {}/{}\n\tattack = {}\n\tarmor = {} ".format(self.__name,self.__level,self.__health,self.__healthMax,self.__attPower,self.__armor)

    @property
    def gainExp(self):
        pass
    
    @gainExp.setter
    def gainExp(self,addExp):
        self.__exp += addExp
        if (self.__exp >= 100):
            print(self.__name, 'level up')
            self.__level += 1
            self.__exp -= 100
            
            self.__healthMax = self.__healthStandar * self.__level
            self.__attPower = self.__attPowerStandar * self.__level
            self.__armor = self.__armorStandar * self.__level

    def serang(self,musuh):
        # membuat method gainExp jadi atribute biasa dan cara 
        # kasih parameternya dengan cara diberi assigment
        self.gainExp = 50
    
slardar = Hero('slardar', 100, 5, 10)
axe = Hero('axe',100,7,15)
print(slardar.info)
# mengakses setter (merubah value atribut instance private)
slardar.serang(axe)
slardar.serang(axe)
slardar.serang(axe)
print(" ")
print(slardar.info)