class Hero():
    #class variabel (static)
    jumlah_hero = 0
    
    def __init__(self, inputName, inputHealth, inputAttack):
        #Instance variabel
        self.name = inputName
        self.health = inputHealth
        self.attack = inputAttack
        Hero.jumlah_hero += 1
        print("nama hero ini adalah ", self.name)
        
hero1 = Hero('sven',[100,500],50)
print(Hero.jumlah_hero)
hero2 = Hero('mirana',70,20)
print(Hero.jumlah_hero)
hero3 = Hero('otong',1000,60)
print(Hero.jumlah_hero)
