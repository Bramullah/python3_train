### Manipulasi List

##Operasi
data=["Dimaz","Dika","Purnama"]

#INDEX > 0 start from front  || -1 start from back

first=data[0]
last=data[-1]
print(f"Data orang pertama: {first}")
print(f"Data orang terakhir: {last}")

#panjang index: LENGTH
panjang_data=len(data)
print(f"Panjang data: {panjang_data}\n")


## Manipulasi data

# Menambah data pada list (choose place)
print(data)
data.insert(1,"Joko")
print(data)

# Menambah data pada akhir list
data.append("Anwar")
print(data)

# Menambah list dengan list
data.extend("Kent")
print(data)

new_data=["Wayne","Kent"]
data.extend(new_data)
print(data)


# Merubah data pada list
data[7]=("Fleck")
print(data)

# Menghapus data pada list
data.remove("K")
print(data)

data_remove= ["e","t"]
data = [x for x in data if x not in data_remove]
print(data)


# Menghapus data terakhir pada list
data.pop()
print(data)

# Memanggil data terakhir yang dihapus
last_call = data.pop()
print(data)
print(last_call)


#becareful  || sets remove orders
sets=set(data)
sets2=set(last_call)
print(sets) #list become random
print(sets2) #wayne

#salah data was in data yg mau di remove
data_remove= ["e","t"]
data = [x for x in data if x in data_remove]
print(data)

#add new list data
data=["Batman","Superman"]
new_data=["Wayne","Kent"]
data.extend(new_data)
print(data)

data=["Batman","Superman"]
new_data=["Wayne","Kent"]
data.append(new_data)
print(data)
