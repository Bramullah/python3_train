### Keyword *args
## **kwargs

#normal
def fungsi (*data_diri):
    '''Normal Function *args'''
    nama = data_diri[0]
    tinggi = data_diri[1]
    berat = data_diri[2]
    
    print(f"{nama} punya tinggi {tinggi} dan berat badan {berat}")

## normal output with list or many input
fungsi("Ibramullah",177,65)


# kwargs function
def fungsi(**kwargs):
    '''Fungsi Keyword agrs'''
    nama = kwargs["nama"]
    tinggi = kwargs["tinggi"]
    berat = kwargs["berat"]
    print(f"{nama} punya tinggi {tinggi} dan berat badan {berat}")

## simple input
fungsi(nama="ibe",tinggi=175,berat=75)


###study case
def math(*args:int, **kwargs:int) -> int:
    '''Study case args and kwargs'''
    output = 0
    if kwargs["operation"] == "tambah" and "+":
        for angka in args:
            output += angka
    elif kwargs["operation"] == "kali" and "x" and "*":
        output = 1
        for angka in args:
            output *=angka
    else:
        print("Theres no operation")


    return output

hasil = math(1,2,3,4,operation="tambah")
hasil2 = math(1,2,3,4,operation="kali")
print(f"Penjumlahan angka: {hasil}")
print(f"Perkalian angka: {hasil2}")


###!!!! How about kurang dan bagi??