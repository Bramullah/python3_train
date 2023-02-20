### Segitiga pada Loop

print("Masukkan Alas SEGITIGA:")
alas = int(input())

#A. For Loop HAT
print("\n"+5*"="+"FOR HAT")
lurus= int(alas/2)
mulai = 1

for i in range(alas):
    print(" "*lurus,"*"*mulai)
    lurus-=1
    mulai+=1

#B. While Loop HAT
print(5*"="+"While HAT")
lurus= int(alas/2)
mulai = 1

while True:
    print(" "*lurus,"*"*mulai)
    lurus-=1
    mulai+=1

    if mulai >= alas+1:
        break


#1. For Loop Triangle
print("\n"+5*"="+"FOR TRIANGLE")
mulai = 1

for i in range(alas):
    print("*"*mulai)
    lurus-=1
    mulai+=1

k = 2 * alas - 2  # It is used for number of spaces  
for i in range(0, alas):  
    for j in range(0, k):  
        print(end=" ")  
    k = k - 2   # decrement k value after each iteration  
    for j in range(0, i + 1):  
        print("* ", end="")  # printing star  
    print("")  

#2. While Loop Triangle
print(5*"="+"While TRIANGLE")
mulai = 1

while True:
    print("*"*mulai)
    lurus-=1
    mulai+=1

    if mulai >= alas+1:
        break


#3. Odds Loop Triangle
print(5*"="+"Odds TRIANGLE")
mulai = 1
lurus= int(alas/2)

while True:
    if (lurus%2):
        print(lurus)
        print(" "*lurus,"*"*mulai)
        lurus-=1
        mulai+=1
    else:
        mulai +=1
        continue

#4. Even Loop Triangle
print(5*"="+"Even TRIANGLE")