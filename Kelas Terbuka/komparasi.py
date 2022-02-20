x = 5
y = 5

print("x dengan value",x,"punya alamat",hex(id(x)))
print("y dengan value",y,"punya alamat",hex(id(y)))
hasil = x is y
hasil2 = x is not y
print("x is y adalah",hasil)
print("x is not y adalah",hasil2)