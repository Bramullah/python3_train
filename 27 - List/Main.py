### LIST
#[start, stop, step]

#array / kumpulan data
listangka=[0,1,2,3,4,5,6,7,8,9,10]
liststring=["Dimaz","Dika","Purnama"]
listboolean=[True,False,True,False]
mixlist=[1,"1",True]

print(listangka)
print(liststring)
print(listboolean)
print(mixlist)

# list in range
data_range = range(0,10)
print(data_range)
data_list = list(data_range)
print(data_list)

data_range = range(0,10,2)
data_list = list(data_range)
print(data_list)

# for in list
for_list=[i for i in range(0,10)]
print(for_list)

#for pangkat
for_list=[i**2 for i in range(0,10)]
print(for_list)

# for-if list
for_if_list= [i for i in range(0,10) if i !=5]
print(for_if_list)

# for-if list genap
for_if_list= [i for i in range(0,10) if i%2 ==0]
print(for_if_list)

# for-if list ganjil
for_if_list= [i for i in range(0,10) if i%2 !=0]
print(for_if_list)

# for-if list genap kuadrat
for_if_list= [i**2 for i in range(0,10) if i%2 ==0]
print(for_if_list)

# for-if list ganjil kuadrat
for_if_list= [i**2 for i in range(0,10) if i%2 !=0]
print(for_if_list)