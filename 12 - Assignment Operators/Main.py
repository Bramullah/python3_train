##Operasi ditambah dengan assignment

print("\nPenjumalahan, Pengurangan, Perkalian, Pembagian, Modulus, Lower Floor, dan Pangkat \n")

a=5 # assignment

print("Nilai a=",a)
#Penjumlahan
a += 1
print("Nilai a +=1",a)
#Pengurangan
a -= 2
print("Nilai a -=2",a)
#Perkalian
a *= 5
print("Nilai a *=5",a)
#Pembagian
a /= 2
print("Nilai a /=2",a)
#Modulus
a %= 3
print("Nilai a %=3",a)
#Lower Floor
b = 10
b //= 3
print("Nilai b //=3",b)
#Pangkat
b **=a
print("Nilai b **=a",b)

##Operasi Bitwise
print("\nOR, AND, XOR\n")

#OR
c=True
print("\nNilai c=",c)
c|=False
print("c|=False, maka nilai C: ",c)
c=False
print("Nilai c=",c)
c|=False
print("c|=False, maka nilai C: ",c)

#AND
c=True
print("\nNilai c=",c)
c&=False
print("c&=False, maka nilai C: ",c)
c=True
print("Nilai c=",c)
c&=True
print("c&=True, maka nilai C: ",c)

#XOR
c=True
print("\nNilai c=",c)
c^=False
print("c^=False, maka nilai C: ",c)
c=True
print("Nilai c=",c)
c^=True
print("c^=True, maka nilai C: ",c)


#Moving
print("\n<< & >>\n")

d = 0b0100
print("\nNilai d=",format(d,'04b'))
d >>=2
print("\nNilai d>>=2: ",format(d,'04b'))
d <<=2
print("\nNilai d<<=1: ",format(d,'04b'))