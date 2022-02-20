class Hero():
    pass

hero1 = Hero()
hero2 = Hero()
hero3 = Hero()

hero1.name = "sven"
hero1.attack = {'asem':[21,'mengapa'],'asin':['rusak']}

hero2.name = "rexxar"
hero2.attack = 9999

hero3.name = 'ucup'
hero3.attack = 500

print(hero1)
print(hero1.__dict__)
print(hero1.name)