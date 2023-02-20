## USER INPUT

#String only
user = input("Masukkan data: ")
print("Data: ", user, "tipe data = ",type(user),"\n")

print()
#Numbers
userfloat = float(input("Masukkan angka koma: "))
userint = int(input("Masukkan angka: "))
print("Angka: " ,userfloat, "tipe data = ",type(userfloat))
print("Angka: " ,userint, "tipe data = ",type(userint), "\n")

#TrueFalse - Boolean
biner = bool(int(input("Masukkan data: ")))
print("Keterangan data: ",biner, "tipe data = ", type(biner))