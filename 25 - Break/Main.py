### Break  || Control Flow


print(5*"="+"Continue From String"+5*"=")
angka = 0
print(f"Angka Awal: {angka} \n")

while angka < 10:
    angka+=1
    if angka ==10:
        print("===Wawancara hari ini berakhir\n")
        break
    print(f"Angka sekarang: {angka}")

    if angka ==7:
        print("===Toko Ditutup\n")
        break
    print(f"Antrian nomer: {angka}\n")


print(5*"="+"Continue From User"+5*"=")
users= int(input("Wawancara pada hari ini: "))
angka = 0
while True:
    angka+=1
    if angka ==10:
        print("===Wawancara hari ini berakhir\n")
        break
    print(f"Angka sekarang: {angka}")

    if angka ==users:
        print("===Toko Ditutup\n")
        break
    print(f"Antrian nomer: {angka}\n")