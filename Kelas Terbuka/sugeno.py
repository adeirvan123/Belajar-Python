# global variabel
u = 0; u1 = 0; u2 = 200; u3 = 500; u4 = 1000
mf1 = 0; mf2 = 0; mf3 = 0; mf4 = 0

def negatif():
    global mf1
    a = -100; b = -50; c = 0; d = 5
    mf1 = max(min(min((error-a)/(b-a),(d-error)/(d-c)),1),0)
    r1 = mf1*u1
    return r1

def positif_kecil():
    global mf2
    a1 = 0; b1 = 5; c1 = 10
    mf2 = max(min((error-a1)/(b1-a1),(c1-error)/(c1-b1)),0)
    r2 = mf2*u2
    return r2
  
def positif_sedang():
    global mf3
    a2 = 5; b2 = 15; c2 = 29
    mf3 = max(min((error-a2)/(b2-a2),(c2-error)/(c2-b2)),0)
    r3 = mf3*u3
    return r3

def positif_besar():
    global mf4
    a3 = 22; b3 = 30; c3 = 50; d3 = 55
    mf4 = max(min(min((error-a3)/(b3-a3),(d3-error)/(d3-c3)),1),0)
    r4 = mf4*u4
    return r4
    
def defuzzyfikasi():
    global u
    # defuzzyfikasi
    u = (negatif() + positif_kecil() + positif_sedang() + positif_besar())/( mf1+mf2+mf3+mf4 )
    return u

# main program :
sp = float(input("Masukkan nilai Set point = "))
nilaiAktual = float(input("Masukkan suhu aktual : "))
error = sp - nilaiAktual
print(f"Error = {error:.2f} ")

# panggil fungsi defuzzyfikasi
defuzzyfikasi()

# print nilai membership function
print(f"""Nilai mf1 : {mf1:.3f}
      Nilai mf2 : {mf2:.3f} 
      Nilai mf3 : {mf3:.3f} 
      Nilai mf4 : {mf4:.3f} 
      """)

# print nilai defuzzyfikasi
print(f"Nilai Deffuzy {u:.2f}\n")

# membuat hasil defuzzyfikasi menjadi pwm untuk mengatur ssr 
sisa = 1000 - u;
print(f"""waktu untuk ssr on {u:.2f} milisecond 
sedangkan waktu untuk ssr off {sisa:.2f} milisecond 
""")
