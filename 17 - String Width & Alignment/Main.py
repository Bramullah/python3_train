### Width & Multiline

##Data

data_nama = "Ibrahim Bramullah"
data_umur = 20
data_tinggi = 171.7
data_nomer_sepatu = 45

#String
data_string = f"Nama: {data_nama}, Umur: {data_umur}, Tinggi: {data_tinggi}, Ukuran Sepatu: {data_nomer_sepatu}"
print(5*"="+"Data String"+"="*5)
print(data_string)

#String Multiline (newline)
data_string = f"Nama: {data_nama}\nUmur: {data_umur}\nTinggi: {data_tinggi}\nUkuran Sepatu: {data_nomer_sepatu}"
print("\n"+5*"="+"Data String"+"="*5)
print(data_string)

#String Multiline (Triplets)
data_string = f"""Nama: {data_nama}
Umur: {data_umur}
Tinggi: {data_tinggi}
Ukuran Sepatu: {data_nomer_sepatu}"""
print("\n"+5*"="+"Data String"+"="*5)
print(data_string)

#WIDHT
data_string = f"""Nama  : {data_nama:>5}
Umur  : {data_umur:>5}
Tinggi: {data_tinggi:>5}
Sepatu: {data_nomer_sepatu:>5}
"""
print("\n"+5*"="+"Data String"+"="*5)
print(data_string)