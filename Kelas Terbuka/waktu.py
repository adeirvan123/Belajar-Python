import datetime as dt #cara mengimpor class datetime sebagai var dt

hari = int(input ("masukkan tanggal lahir : "))
bulan = int(input("masukkan bulan lahir   : "))
tahun = int(input("masukkan tahun lahir   : "))

waktu = dt.date(tahun, bulan, hari) #library .date untuk akses thn,bln,hari

format_date = f"""5
5kamu lahir pada = {waktu} 
pada hari {waktu:%A} 
""" # :%A -> pada format string var waktu berarti untuk meliat hari
print(format_date)