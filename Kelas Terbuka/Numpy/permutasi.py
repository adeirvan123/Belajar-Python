import math as m

n = m.factorial(52)
a = 52
b = 5
c = m.factorial(5)
minus = m.factorial(a-b)

output = n/(minus*c)
print(f" kombinasi dari 5 pengambilan terhadap 52 {output}")

n1 = m.factorial(13)
a1 = 13
b1 = 5
c1 = m.factorial(5)
minus1 = m.factorial(a1-b1)

output1 = n1/(minus1*c1)
print(f" kombinasi dari 5 pengambilan terhadap 13 diamond {output1}")

hasil_akhir = output1/output
print(f"hasil probabilitasnya adalah = {hasil_akhir} ")
