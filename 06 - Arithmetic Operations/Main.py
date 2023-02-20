### Aritmatika - Arithmetic Operation

a = 10
b = 3
x = 3
y = 2
z = 4

##Penjumlahan
print("===Addition (+)===")
hasil = a+b
print(a,'+',b,'=',hasil)

##Pengurangan
print("===Subtraction (-)===")
hasil = a-b
print(a,'-',b,'=',hasil)

##Perkalian
print("===Multiplication (x)===")
hasil = a*b
print(a,'x',b,'=',hasil)

##Pembagian
print("===Division (:)===")
hasil = a/b
print(a,':',b,'=',hasil)

##Sisa Bagi
print("===Modulus (%)===")
hasil = a%b
print(a,'%',b,'=',hasil)

##Pangkat
print("===Exponentiation (^)===")
hasil = a**b
print(a,'^',b,'=',hasil)

##Pembulatan Bilangan
#Floor and Ceiling Functions
print("===Floor division (//)===")
hasil = a//b
print(a,'//',b,'=',hasil)

#EXAMPLE
hasil = x ** y * z + x / y - y % z // x
print(x, '^', y ,'x',z ,'+' ,x ,':' ,y,'-',y, '%' ,z ,'//', x, '=',hasil)

#Kurung             [()]
#Eksponen 1st       [^]
#Perkalian 2nd      [x,:,%,//]
#Penjumlahan 3rd    [+,-]

hasil = x+y*z
print(x,'+',y,'x',z,'=',hasil)

hasil = x+y*z
print((x,'+',y),'x',z,'=',hasil)
