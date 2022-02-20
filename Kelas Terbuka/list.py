data = [0,1,2,3,6,5,6]

# mengakses data dari list
subdata1 = data[5]
print(subdata1)
print("")

# memotong data dari list
subdata = data[0:4]
print(subdata)
print("")

# menambah data dari list
data2 = [100,200,300,400,500,600,700]
sum_list = data + data2
print(sum_list)
print("")

# mengubah content dari list
a = data[:]
a[2] = 87
print(a)
print(data)
print("")

# merubah content dengan menggunakan slicing
data[2:4] = [120,121]
print(data)
print("")

# multidmensional list dan cara mengaksesnya
multi_list = [data,data2]
print(multi_list)
print(" ")

print(multi_list[0][2])
print("")

# method pada list {.append()}
data.append(999)
print(data)
print("")

# fungsi pada list
panjang_list = len(data)
print(panjang_list)