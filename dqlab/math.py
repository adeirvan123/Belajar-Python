import math as m

x = [2.22,-3.33,4.44,-5.55]
total = 0
for i in x:
    total += m.ceil(i)
print(total)

x = m.ceil(-3.33)
print(x)