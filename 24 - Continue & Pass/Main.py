### Continue & Pass  || Control Flow

#Continue
print(5*"="+"Continue"+5*"=")
angka = 0
print(f"Angka Awal: {angka} \n")

while angka < 10:
    angka+=1
    if angka ==10:
        print("===Toko Ditutup\n")
        continue

    print(f"Angka sekarang: {angka}")

    if angka ==7:
        print("===User tidak hadir\n")
        continue

    print(f"Antrian nomer: {angka}\n")

    if angka ==1:
        print("===User Pertama\n")
        continue

#Pass
print(5*"="+"Pass"+5*"=")
angka = 0
print(f"Angka Awal: {angka} \n")

while angka < 10:
    angka+=1
    if angka ==10:
        print("===Toko Ditutup\n")
        pass

    print(f"Angka sekarang: {angka}")

    if angka ==7:
        print("===User tidak hadir\n")
        pass

    print(f"Antrian nomer: {angka}\n")