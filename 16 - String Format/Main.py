### Format String

#Normally:

##String
nama="Ibe"
format_str=f"Hello {nama}, salam kenal"
print(format_str)

##Boolean
boolean=True
format_str= f"Boolean: {boolean}"
print(format_str)

##Angka

#Double/Float
angka=2005.5
format_str=f"Angka: {angka}"
print(format_str)
print(type(format_str))

#Bil.Bulat
angka = 15
format_str=f"Angka Bilangan Bulat: {angka:d}"
print(format_str)

#Ordo Ribuan
angka=200000000
format_str=f"Angka dalam data: {angka:,}"
print(format_str)

#Bil.Desimal
angka=2005.583411
format_str=f"Angka: {angka:.2f}"
print(format_str)

#Menampilkan leading zero (awal nol atau spasi)
angka=2005.583411
format_str=f"Angka: {angka:010.3f}"
print(format_str)

angka=2005.583411
format_str=f"Angka: {angka:12.3f}"
print(format_str)

#Menampilkan tanda + atau -
angka_minus=-10
angka_plus=+10
format_minus=f"Minus= {angka_minus:+d}"
format_plus=f"Minus= {angka_plus:+d}"
print(format_minus)
print(format_plus)

#Dengan Koma
angka_minus=-10.583411
angka_plus=+10.583411
format_minus=f"Minus= {angka_minus:+.2f}"
format_plus=f"Minus= {angka_plus:+.2f}"
print(format_minus)
print(format_plus)

#Persen
persentase=0.045
format_persen=f"Persen: {persentase:.2%}"
print(format_persen)

# Melakukkan operasi Aritmatika dalam placeholder
harga=10000
jumlah=5

format_string=f"harga total = Rp. {harga*jumlah:,}"
print(format_string)

#format angka (binary, octal, hexadecimal)
angka=255
format_binary = f"Binary: {bin(angka)}"
format_octal = f"Octal: {octal(angka)}"
format_hex = f"Hex: {hex(angka)}"

print(format_binary)
print(format_octal)
print(format_hex)