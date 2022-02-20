from collections import deque
antrian = deque([1,2,3,4,5,6]) #tipe data deque bukan list
print(antrian)

#menambah data
antrian.append(7)
print(f"data masuk = 7")
print(f"data sekarang = {antrian} ")
print("")

#mengambil data secara queues
out = antrian.popleft()
print(f"""data keluar = {out} 
data sekarang = {antrian} 
""")

out = antrian.popleft()
print(f"""data keluar = {out} 
data sekarang = {antrian} """)

# masih gagal queues dalam loop
# for i in antrian:
#     antrian.popleft()
#     print(i)
#     print(f"data menjadi {antrian} ")
# else:
#     print("nilai pada data antrian sudah habis")

