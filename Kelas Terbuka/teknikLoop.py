band = ["Galiloe",
        "Baby Metal",
        "Slipknot",
        "Linkin Park"]

lagu = ["Eir Aoi",
        "Kingslayer",
        "Duality",
        "What I've done"]

# memberikan indexing list / tuple (enumerate)
for index,var in enumerate(band):
    print(index,":",var)
print("="*100)

# menggabungkan 2 list list / tuple
for aseq,wakwau in zip(band,lagu):
    print(f" {aseq} menyanyikan lagu {wakwau} ")

# Set
playlist = {"nangka", "apel", "pisang", "manggis", "bengkoan", "srikaya"}
for buah in sorted(playlist):
    print(buah)

# dictionary
song = {"Galiloe":"eir aoi",
        "Baby Metal":"kingslayer",
        "Slipknot":"duality",
        "Linkin Park":"numb"}

for penyanyi,musyrikk in song.items():
    print(f" {penyanyi} menyanyikan lagu berjudul : {musyrikk} ")

# reversed (dibalik)
for i in reversed(range(1,11,1)):
    print(i)