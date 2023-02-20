## Operasi Logika / Boolean

# not, or, and, xor

#NOT (Bukan)
print("===NOT (not)===")
a = True
c = not a
print("Data a: ",a)
print("Data c: ",c)

#OR (True = True)
#SUM [False 0 || True 1]
print("\n===OR (or)===")
a=True
b=True
c= a or b
print(a,'or',b,'=',c)
a=True
b=False
c= a or b
print(a,'or',b,'=',c)
a=False
b=True
c= a or b
print(a,'or',b,'=',c)
a=False
b=False
c= a or b
print(a,'or',b,'=',c)
print("--3 Object--")
a=True
b=False
d = a or b or a
e = b or a or b
print(a,'or',b,'or',b,'=',d)
print(b,'or',a,'or',b,'=',e)


# AND (2 True = True)
#Times [False 0 || True 1]
print("\n===AND (and)===")
a=True
b=True
c= a and b
print(a,'and',b,'=',c)
a=True
b=False
c= a and b
print(a,'and',b,'=',c)
a=False
b=True
c= a and b
print(a,'and',b,'=',c)
a=False
b=False
c= a and b
print(a,'and',b,'=',c)
print("--3 Object--")
a=True
b=False
d = a and b and a
e = b and a and b
print(a,'and',b,'and',b,'=',d)
print(b,'and',a,'and',b,'=',e)

# XOR (Salah satu true = True)
print("\n===XOR (^)===")
a=True
b=True
c= a ^ b
print(a,'xor',b,'=',c)
a=True
b=False
c= a ^ b
print(a,'xor',b,'=',c)
a=False
b=True
c= a ^ b
print(a,'xor',b,'=',c)
a=False
b=False
c= a ^ b
print(a,'xor',b,'=',c)
print("--3 Object--")
a=True
b=False
d = a ^ b ^ a
e = b ^ a ^ b
print(a,'xor',b,'xor',b,'=',d)
print(b,'xor',a,'xor',b,'=',e)