class Hero():
    # class variabel public & private
    jumlah = 0
    __privateJumlah = 0
    
    def __init__(self,name,health):
        # variabel instance public
        self.name = name
        self.health = health
        
        # variabel instance private
        self.__private = "private coy"
        # variabel instance protected
        self.__protected = "protected cuy"
        
lina = Hero('lina',100)

lina.__protected = 'bisa nggak'
lina.__private = 'merubah'

print(lina.__protected)
print(lina.name)
print(lina.__private)
print(lina.health)
print(lina.jumlah)
print("bawah adalah var class private")
print(lina.__privateJumlah)