class Hero():
    # class variabel (static)
    jumlah_hero = 0
    
    def __init__(self, inputName, inputHealth, inputAttack, inputArmor):
        # Instance variabel
        self.name = inputName
        self.health = inputHealth
        self.attack = inputAttack
        self.armor = inputArmor
        Hero.jumlah_hero += 1
    
    # void function, tanpa return, tanpa parameter
    def siapa(self):
        print(f"namaku adalah {self.name} ")
        
    # metod dengan parameter/argumen, tanpa return
    def healthUp(self,up):
        self.health += up
    
    # method dengan return, tanpa parameter
    def getHealth(self):
        return self.health
    
    # method dengan return dan parameter
    def addHealth(self, potion):
        return print(f"nyawa setelah memakai potion : {self.health + potion}" )
        
hero1 = Hero('sniper',100,10,5)
hero2 = Hero('asuka',90,50,30)

hero1.siapa()
hero1.healthUp(10)

print(hero1.getHealth())
hero1.addHealth(50)

        