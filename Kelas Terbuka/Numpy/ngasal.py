hewan = ['anjing','babi']
for i in range(0,len(hewan)):
    if (i==1):
        print(hewan[i], 'ada lima')
        break # break, jadi saat perulangan indek ke 1, setalah print diatas
              # maka program akan berakhir, jadi print yg dibawah tidak dieksekusi
    print(hewan[i])