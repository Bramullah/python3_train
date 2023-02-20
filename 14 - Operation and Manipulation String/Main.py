## Manipulasi String

# 1. Menyambung String

nama_pertama = "Dimaz"
nama_kedua = "Dika"
nama_ketiga = "Purnama"

nama_lengkap = nama_pertama+ " " +nama_kedua+ " " +nama_ketiga

print(nama_lengkap)

# 2. Menghitung panjang string
panjang_nama = len(nama_lengkap)
print("Panjang nama: ",panjang_nama)
print("Panjang "+ nama_lengkap+ " : "+str(panjang_nama))

# 3. Operator untuk string
#Mengecheck komponen char atau string dalam string

d="d"
status=d in nama_lengkap
print(d+"ada di "+ nama_lengkap+ " = "+ str(status))

D="D"
status=d in nama_lengkap
print(D+"ada di "+ nama_lengkap+ " = "+ str(status))

d="d"
status=d not in nama_lengkap
print(d+"ada di "+ nama_lengkap+ " = "+ str(status))

D="D"
status=d not in nama_lengkap
print(D+"ada di "+ nama_lengkap+ " = "+ str(status))

# Mengulang String
print("wk"*10)
print(15*"10")

# Indexing
print("Index ke-4: "+nama_pertama[4])
print("Index ke-2: "+nama_kedua[2])
print("Index ke-0: "+nama_kedua[0])
print("Index ke-8: "+nama_lengkap[8])

print("Index ke-(-2): "+nama_lengkap[-2])
print("Index ke-(-6): "+nama_lengkap[-6])

print("Index ke-(0:6): "+nama_lengkap[0:6])
print("Index ke-(4:8): "+nama_lengkap[4:8])

print("Index bertahap (0,2,4,6,8,10): "+nama_lengkap[0:10:2])
print("Index bertahap (0,3,5,7,9,11): "+nama_lengkap[0:11:3])
print("Index bertahap (0,2,4,6,8,10): "+nama_lengkap[0:11:2])

# Item paling kecil & besar
print("Paling kecil: "+min(nama_lengkap))
print("Paling besar: "+max(nama_lengkap))

ascii_code = ord(" ")
ascii_code2 = ord("I")
print("ASCII code untuk spasi dan I adalah: "+ str(ascii_code)+" dan "+ str(ascii_code2))

# Angka ke ascii
data = 73
print("Char untuk ASCII 73 adalah: "+chr(data))

# 4. Operator dalam bentuk method
data = "Ibrahim Bramullah"
jumlah = data.count("a")
print("Jumlah o pada data: " + str(jumlah))
