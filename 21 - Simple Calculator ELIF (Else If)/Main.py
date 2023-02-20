### Simple Kalkulator ELIF

print(5*"=")
kal = float(input("Masukkan angka: "))
ope = input("Operator: ")
kal2 = float(input("Masukkan angka: "))
print(5*"="+"\n")

if ope=="+":
    print(f"Hasilnya: {kal+kal2}")
elif ope=="-":
    print(f"Hasilnya: {kal-kal2}")
elif ope==":" or ope=="/":
    print(f"Hasilnya: {kal/kal2}")
elif ope=="x" or ope=="X" or ope=="*":
    print(f"Hasilnya: {kal*kal2}")
elif ope=="^" or ope=="**":
    print(f"Hasilnya: {kal**kal2}")
elif ope=="%":
    print(f"Sisa bagi: {kal%kal2}")
else:
    print("Operator salah")