### Teknik menduplikat list

# Semua terkoneksi dengan satu address
a = ["A","B","C"]
b = a

a[1]="="
print(a)
print(b)
b.remove("=")
print(a)
print(b)


# copy file >
c=a.copy()
d=b.copy()

c.insert(1,"B")
new_data=["D","C"]
d.extend(new_data)
print(a)
print(b)
print(c)
print(d)


#c.insert(2,"B")



#Address
print("")
print(hex(id(a)))
print(hex(id(b)))
print(hex(id(c)))
print(hex(id(d)))