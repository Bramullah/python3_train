## Latihan Logika dan Komparasi
# Gabungan area dan rentang dari angka

#1Input, 2Batas || 3,10
#Input and OR
print("----1 INPUT")
inputUser = float(input("\nMasukkan Angka (<3 atau >10): "))
atau = (inputUser < 3) or (inputUser > 10)
print("Angka yang dimnasukkan:",atau)

#1Input, 2Batas || 3,10
#Input and AND
inputUser = float(input("\nMasukkan Angka (>3 dan <10): "))
dan = (inputUser > 3) and (inputUser < 10)
print("Angka yang dimnasukkan:",dan)

#----

#1Input, 4 Batas || 0,5,8,11

inputUser = float(input("\nMasukkan Angka dengan ketentuan:\n>0 dan <5\nataudalam\n>8 dan <11:\n"))
oneinput = ((inputUser > 0) and (inputUser < 5)) or ((inputUser > 8) and (inputUser < 11))
print("Angka yang dimnasukkan:",oneinput)

#1Input, 4 Batas || 0,5,8,11
inputUser = float(input("\nMasukkan Angka dengan ketentuan:\n<0 dan >5\nataudalam\n<8 dan >11:\n"))
oneinput = (inputUser < 0) or ((inputUser > 5) and (inputUser < 8)) or (inputUser > 11)
print("Angka yang dimnasukkan:",oneinput)

print("\n\n----2 INPUT")
#2Input, 4 Batas || 0,5,8,11
inputUser = float(input("Masukkan Angka dengan ketentuan:\n>0 dan <5:\n"))
inputUser2 = float(input("\nMasukkan Angka dengan ketentuan:\n>8 dan <11:\n"))
oneinput = ((inputUser > 0) and (inputUser < 5)) or ((inputUser2 > 8) and (inputUser2 < 11))
print("Angka yang dimnasukkan:",oneinput)

#2Input, 4 Batas || 0,5,8,11
inputUser = float(input("\nMasukkan Angka dengan ketentuan:\n<0 atau >11:\n"))
inputUser2 = float(input("\nMasukkan Angka dengan ketentuan:\n>5 dan <8:\n"))
oneinput = (inputUser < 0) or ((inputUser2 > 5) and (inputUser2 < 8)) or (inputUser > 11)
print("Angka yang dimnasukkan:",oneinput)