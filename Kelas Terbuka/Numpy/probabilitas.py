# mencari probabilitas classic atau theoritical
# rumus = total outcome pada event/total outcome pada sample space

# cari P(E) dari dadu genap & P(E) dibawah 5
dadu = [1,2,3,4,5,6]
ada = 0
ada2 = 0

for i in dadu:
    if (i%2 == 0):
        ada+=1
    if (i<5):
        ada2+=1
        print(i)

peluang = ada/len(dadu)
peluang2 = ada2/len(dadu)
print(f"peluang mata dadu genap adalah          = {peluang} ")
print(f"peluang mata dadu kurang dari 5 adalah  = {peluang2:.2f} ")

