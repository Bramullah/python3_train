### Operasi pada list

data_angka = [1,4,7,2,5,8,3,6,9,1,0,5,9,3,5,7,8,4,2,6]
print(data_angka)

##Jumlah / count
jmlh_data = data_angka.count(1)
print(jmlh_data)

index1=data_angka.index(0)
print(index1)


## find all the indices of the value 1 in data_angka
#value = int(input()) if with input :)
value = 1
indices = []
start = 0
while True:
    try:
        index = data_angka.index(value, start)
        indices.append(index)
        start = index + 1
    except ValueError:
        break

print(indices)

#index()  > value,start,stop

## Sorting List / mengurutkan
--1. 
urutkan = sorted(data_angka)
dibalik = sorted(data_angka, reverse=True)
print(urutkan)
print(dibalik)

--2.
data_angka.sort()
print(data_angka)
data_angka.reverse()
print(data_angka)


#becareful
print(data_angka.sort())