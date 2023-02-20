### DEEEEPPPP! List within list
d1=[0,1,2]
d2=[3,4,5]
dplus=(d1+d2)

print(dplus)

list_2d=[d1,d2,6,7,8,9]
copy_2d=list_2d.copy()
print(list_2d)
print(copy_2d)


## Mengambil data
data1=list_2d[0]
data2=list_2d[1][2]
print(f"3 Angka pertama: {data1}")
print(f"Angka ke 5: {data2}\n\n")

## Address Upper List
print(f"Address asli: {hex(id(list_2d))}")
print(f"Address copy: {hex(id(copy_2d))}")

#Address member within List
print(f"Address asli: {hex(id(list_2d[0]))}")
print(f"Address copy: {hex(id(copy_2d[0]))}")


## Data list within changes, while data on list didnt

list_2d[1][0]=5
list_2d[2]=9
print(f"Data: {list_2d}")
print(f"Data Copy: {copy_2d}")

### copy List  ==  shallow copy
### deepcopy == deeper copy

from copy import deepcopy

list_2d=[d1,d2,6,7,8,9]
deepcopy_2d=deepcopy(list_2d)
print(list_2d)
print(deepcopy_2d)

list_2d[1][0]=100
list_2d[2]=100
print(f"Data: {list_2d}")
print(f"Data Deep Copy: {deepcopy_2d}")


###Address Final
## Address Upper List
print(f"\n\nAddress asli: {hex(id(list_2d))}")
print(f"Address copy: {hex(id(copy_2d))}")
print(f"Address copy: {hex(id(deepcopy_2d))}")

#Address member within List
print(f"\nAddress asli: {hex(id(list_2d[0]))}")
print(f"Address copy: {hex(id(copy_2d[0]))}")
print(f"Address copy: {hex(id(deepcopy_2d[0]))}")