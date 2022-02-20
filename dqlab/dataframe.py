import pandas as pd

data = [{'harga': '500', 'jarak_ke_pusat': '15', 'tanah': '70', 'bangunan': '50'}, {'harga': '400', 'jarak_ke_pusat': '30', 'tanah': '70', 'bangunan': '60'}, {'harga': '300', 'jarak_ke_pusat': '55', 'tanah': '70', 'bangunan': '60'}, {'harga': '700', 'jarak_ke_pusat': '30', 'tanah': '100', 'bangunan': '50'}, {'harga': '1000', 'jarak_ke_pusat': '25', 'tanah': '100', 'bangunan': '70'}, {'harga': '650', 'jarak_ke_pusat': '50', 'tanah': '100', 'bangunan': '70'}, {'harga': '2000', 'jarak_ke_pusat': '20', 'tanah': '120', 'bangunan': '100'}, {'harga': '1200', 'jarak_ke_pusat': '50', 'tanah': '120', 'bangunan': '80'}, {'harga': '1800', 'jarak_ke_pusat': '50', 'tanah': '150', 'bangunan': '100'}, {'harga': '3000', 'jarak_ke_pusat': '15', 'tanah': '150', 'bangunan': '90'}]
output = {'Prediksi harga rumah':  1200}

df = pd.DataFrame(data)
print(df)
