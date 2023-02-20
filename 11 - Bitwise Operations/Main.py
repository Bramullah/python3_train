##Operator Bitwise, Biner, Binary
#Masing-masing bit

"""
Bit
int 2> 00000010     ==  2^0,2^0,2^0,2^0,2^0,2^1,2^0,2^0
int 9> 00001001     ==  2^0,2^0,2^0,2^0,2^0,2^1,2^0,2^0

2^n

bitwise
int 2> 00000010     ==  2^0,2^0,2^0,2^0,2^0,2^0,2^1,2^0
int 1> 00001001     ==  2^0,2^0,2^0,2^0,2^0,2^0,2^0,2^1
                        ------------------------------- +
                        0  ,0  ,0  ,0  ,0  ,0  ,1  ,1   = 3

"""

##or, and, xor, not
a=9
b=5

#BITWISE OR (|)
c=a|b
print("===BITWISE OR (|)===")
print("Nilai a: ",a,', Binary: ', format(a,'08b'))
print("Nilai b: ",b,', Binary: ', format(b,'08b'))
print("           -------------------- OR (|)")
print("Nilai c: ",c,', Binary: ', format(c,'08b'))

#BITWISE AND (&)
c=a&b
print("\n===BITWISE AND (&)===")
print("Nilai a: ",a,', Binary: ', format(a,'08b'))
print("Nilai b: ",b,', Binary: ', format(b,'08b'))
print("           -------------------- AND (|)")
print("Nilai c: ",c,', Binary: ', format(c,'08b'))

#BITWISE NOT (~)
c= ~a
d= ~b
print("\n===BITWISE NOT (~)===")
print("Nilai a:  ",a,', Binary: ', format(a,'08b'))
print("           -------------------- NOT (~)")
print("Nilai b:",c,', Binary: ', format(c,'08b'))

print("Nilai b:  ",b,', Binary: ', format(b,'08b'))
print("           -------------------- NOT (~)")
print("Nilai b: ",d,', Binary: ', format(d,'08b'))

e = 0b0000001001
f = 0b0000000101
g = 0b1111111111
x = 11111111
#dengan XOR
print("\nNilai: ", g^e)
print("Binary awal: ",e, "Binary Not: ",format(g^e,'08b'))
print("Nilai: ", g^f)
print("Binary awal: ",f, "Binary Not: ",format(g^f,'08b'))

print(format(a,'08b'))
xyz = int(format(a,'08b'))
print(xyz)

q = x ^ xyz
qq = ~xyz
print(qq)




##Shifting
#Shift Right (>>)
c = a >> 1
d = b >> 1
print("\n===SHIFTING RIGHT (>>)===")
print("Nilai a:  ",a,', Binary: ', format(a,'08b'))
print("           -------------------- SHIFT RIGHT (>>)")
print("Nilai b:",c,', Binary: ', format(c,'08b'))

print("Nilai b:  ",b,', Binary: ', format(b,'08b'))
print("           -------------------- SHIFT RIGHT (>>)")
print("Nilai b: ",d,', Binary: ', format(d,'08b'))

#Shift left (<<)
c = a << 1
d = b << 1
print("\n===SHIFTING left (<<)===")
print("Nilai a:  ",a,', Binary: ', format(a,'08b'))
print("           -------------------- SHIFT LEFT (<<)")
print("Nilai b:",c,', Binary: ', format(c,'08b'))

print("Nilai b:  ",b,', Binary: ', format(b,'08b'))
print("           -------------------- SHIFT LEFT (<<)")
print("Nilai b: ",d,', Binary: ', format(d,'08b'))