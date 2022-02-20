data_name = "Irvan"
data_age = 21
data_gender = "pria"
data_hobby = "sleep"

print("\n"+5*"-"+"Data Diri"+5*"-")
format_data = f"""
nama   = {data_name}
usia   = {data_age}
gender = {data_gender}
hobi   = {data_hobby}
"""
print(format_data)

print(5*"-"+"Data Diri"+5*"-")
data_name = "Fernando"
format_data = f"""
nama   = {data_name:>8}
usia   = {data_age:>8}
gender = {data_gender:>8}
hobi   = {data_hobby:>8}
"""
print(format_data)