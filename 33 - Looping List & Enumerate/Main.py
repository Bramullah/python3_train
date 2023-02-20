### Looping from list

## For Loop
kumpulan_angka= [4,3,2,1,6,8]
for angka in kumpulan_angka:
    print(f"Angka: {angka}")

peserta = {"Dimaz", "Dika", "Purnama", "Joko", "Anwar"}

for nama in peserta:
    print(f"Nama: {nama}")


## For Loop and Range
print()
#20
too_many_angka=[7,8,9,4,5,6,1,2,3,0,0,1,2,3,4,5,6,7,8,9]
#6
panjang = len(kumpulan_angka)
for number in range(panjang):
    print(f"Number: {too_many_angka[number]}")


## WhileLoop
print()
mulai=0
while mulai < panjang:
    print(f"While ke-{mulai}: {kumpulan_angka[mulai]}")
    mulai+=1

##list comprehension
print()
data=["Ibrahim",1,2,3,"Bramullah"]

[print(f"Data: {i}")
for i in data
]

angka_kuadrat = [i**2 for i in kumpulan_angka]
print(sorted(angka_kuadrat))


# enumerate
print()
datas=["Ibrahim",1,2,3,"Bramullah"]
for index,datas in enumerate(data):
    print(f"Urutan ke- {index}, Data: {datas}")




##Becareful
#While
print()
mulai=0
while mulai < panjang:
    print(f"!1: {mulai}")
    mulai+=1

#For & range
print()
panjang = len(kumpulan_angka)
for number in range(panjang):
    print(f"!2: {number}")