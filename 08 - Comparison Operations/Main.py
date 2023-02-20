## Operasi Komparasi

#Boolean (True or False)

# >, <, >=, <=, ==, !=, is, is not

X = 24
Y = 25
Z = 26

# Lebih besar dari >
print("===Greater Then (>)===")
hasil = X > 23
hasil = Y > 25
hasil = Z > 27

print(X,'>',23,'=',hasil)
print(Y,'>',25,'=',hasil)
print(Z,'>',27,'=',hasil)

print("\n===Less Than (<)===")
hasil = X < 23
hasil = Y < 25
hasil = Z < 27

print(X,'<',23,'=',hasil)
print(Y,'<',25,'=',hasil)
print(Z,'<',27,'=',hasil)

print("\n===Greater Than or Equal To (>=)===")
hasil = X >= 23
hasil = Y >= 25
hasil = Z >= 27

print(X,'>=',23,'=',hasil)
print(Y,'>=',25,'=',hasil)
print(Z,'>=',27,'=',hasil)

print("\n===Less Than or Equal To (<=)===")
hasil = X <= 23
hasil = Y <= 25
hasil = Z <= 27

print(X,'<=',23,'=',hasil)
print(Y,'<=',25,'=',hasil)
print(Z,'<=',27,'=',hasil)

print("\n===Equal (==)===")
hasil = X == 23
hasil = Y == 25
hasil = Z == 27

print(X,'==',23,'=',hasil)
print(Y,'==',25,'=',hasil)
print(Z,'==',27,'=',hasil)

print("\n===Unequal (!=)===")
hasil = X != 23
hasil = Y != 25
hasil = Z != 27

print(X,'!=',23,'=',hasil)
print(Y,'!=',25,'=',hasil)
print(Z,'!=',27,'=',hasil)


##is, is not
#Komparasi Object (Nilai yang disimpan)

print("\n===Object Identity (is)===")

a=5
b=5
print("Nilai x: ",a, 'id = ', hex(id(a)))
print("Nilai x: ",b, 'id = ', hex(id(b)))

hasil = a is b
print("a is b = ", hasil)

print("\n===Object Identity (is not)===")

a=5
b=10
print("Nilai x: ",a, 'id = ', hex(id(a)))
print("Nilai x: ",b, 'id = ', hex(id(b)))

hasil = a is not b
print("a is b = ", hasil)