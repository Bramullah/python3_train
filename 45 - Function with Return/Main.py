### Fungsi Kembali

def fungsi_kuadrat(input_angka):
    '''Fungsi Kuadrat''' ##helper for def
    output_kuadrat = input_angka**2
    return output_kuadrat

out = fungsi_kuadrat(5)
print(out)
print(10+fungsi_kuadrat(5))

def fungsi_tambah(angka1,angka2):
    '''Fungsi Tambah'''
    return angka1+angka2

a = fungsi_tambah(10,8)
print(a)

def math_ope(angka1,angka2):
    tambah = angka1 + angka2
    kurang = angka1 - angka2
    kali = angka1 * angka2
    bagi = angka1 / angka2

    return tambah,kurang,kali,bagi

q,w,e,r = math_ope(9,5)
print(f"Hasil Penjumlahan :{q}")
print(f"Hasil Pengurangan :{w}")
print(f"Hasil Perkalian   :{e}")
print(f"Hasil Pembagian   :{r}")

#canmake a simple calculator with input
