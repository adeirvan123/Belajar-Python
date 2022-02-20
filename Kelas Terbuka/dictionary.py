member1 = {
    "ID" : 101,
    "Nama":["Ade","Irvan"],
    "Pekerjaan":"Mahasiswa",
    "Status Member":"Gold"
    }

member2 = {
    "ID" : 102,
    "Nama":"Yadi Sembako",
    "Pekerjaan":"Sirkusman",
    "Status Member":"Diamond"
    }

# membuat list pada dictionary
list_member = {1:member1,2:member2}
print(list_member[1]["ID"])