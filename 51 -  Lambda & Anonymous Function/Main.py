#### Fungsi Anonymous dan Lambda

###Lambda

#normal function
def f_kuadrat(angka):
    return angka**2

print(f"Function = {f_kuadrat(5)}")

#lambda
kuadrat = lambda angka: angka**2
print(f"Lambda: {kuadrat(6)}")

#listing sort
data_list = ["A","B","C"]
data_list.sort()
print(f"List = {data_list}")

#function list sort
def f_l_sort(nama):
    return len(nama)

##Key = syarat
data_list.sort(key=f_l_sort)
print(f"Function List = {data_list}")

#lambda list
data_list.sort(key=lambda nama: len(nama))

##filter lambda
#function filter :
angka=[0,1,2,3,4,5,6,7,8,9,10]

def kurang_dari(number):
    return number <5

data_angka = list(filter(kurang_dari,angka))
print(f"Function Filter: {data_angka}")

#lambda filter
data_angka = list(filter(lambda angkas: angkas<5,angka))
print(f"Lambda Filter: {data_angka}")

#GENAP
data_angka = list(filter(lambda angkas: angkas%2==0,angka))
print(f"Lambda Genap: {data_angka}")

#GANJIL
data_angka = list(filter(lambda angkas: (angkas%2!=0),angka))
print(f"Lambda Ganjil: {data_angka}")

###Anonymous
##curring <= from Haskell Curry

#normally
def pangkat(angka,n):
    a=angka**n
    return a

output=pangkat(5,2)
print(f"Fungsi function = {output}")

#curry

def pangkat(n):
    return lambda a: a**n

output=pangkat(2)
output2=pangkat(3)
print(f"Pangkat 2: {output(10)}")
print(f"Pangkat 3: {output2(10)}")
print(f"Pangkat random: {pangkat(5)(2)}")

