import datetime as date
import os as awal
import string
import random
### Template Dict Mahasiwa

mhsw_temp={
    "nama":"nama",
    "npm":"00000000",
    "sks":0,
    "lahir":date.datetime(1111,1,11)
}

data_mhsw = {}

while True:
    awal.system("cls")
    print(f"{'SELAMAT DATANG':^20}")
    print(f"{'DATA MAHASISWA':^20}")
    print("-"*20)

    mhsh = dict.fromkeys(mhsw_temp.keys())
    mhsh["nama"] = input("Nama Mahasiswa: ")
    mhsh["npm"] = input("NPM Mahasiswa: ")
    mhsh["sks"] = input("SKS Lulus: ")
    tgl_lahir = int(input("Tanggal Lahir (DD): "))
    bln_lahir = int(input("Bulan Lahir (MM): "))
    thn_lahir = int(input("Tahun Lahir (YYYY): "))

    mhsh["lahir"] = date.datetime(thn_lahir,bln_lahir,tgl_lahir)

    key =''.join((random.choice(string.ascii_uppercase) for i in range(10)))
    data_mhsw.update({'key':mhsh})


    print(f"{'KEY':<6} {'Nama':<17} {'SKS':<3} {'Lahir':>15}")
    print("-"*50)

    for mahasiswa in data_mhsw:
        NAMA = data_mhsw[mahasiswa]['nama']
        NIM = data_mhsw[mahasiswa]['npm']
        SKS = data_mhsw[mahasiswa]['sks']
        LAHIR = data_mhsw[mahasiswa]['lahir'].strftime("%x")

        KEY = mahasiswa
        print(f"{KEY:<6} {NAMA:<17} {SKS:<3} {LAHIR:>15}")
    

    print("\n\n"+10*"=")
    finish = input("Add more data? (YES/Yes/Y/y, NO/No/N/n)")
    if finish == "YES" and "Yes" and "Y" and "y":
        continue
    elif finish == "NO" and "No" and "N" and "n":
        break
    else:
        print("\n===WTF!!??\n")
        break







### UNFINISH PROJECT, ADD BEASISWA TO FALUE OF BOOLEAN WITH SKS MINIMUM
# mhsw_temp={
#     "nama":"nama",
#     "npm":"00000000",
#     "sks":"0000",
#     "beasiswa":"beasiswa",
#     "lahir":date.datetime(1111,1,11)
# }

# data_mhsw = {}

# while True:
#     awal.system("cls")
#     print(f"{'SELAMAT DATANG':^20}")
#     print(f"{'DATA MAHASISWA':^20}")
#     print("-"*20)

#     mhsh = dict.fromkeys(mhsw_temp.keys())
#     mhsh["nama"] = input("Nama Mahasiswa: ")
#     mhsh["npm"] = input("NPM Mahasiswa: ")
#     mhsh["sks"] = int(input("SKS Lulus: "))
#     if mhsh["beasiswa"] == (mhsh["sks"] >= 150):
#         a= ("Mendapat Beasiswa")
#         print(mhsh)
#         print(a)
#     elif mhsh["beasiswa"] == (mhsh["sks"] < 150):
#         b= ("Tidak Mendapatkan Beasiswa")
#     else:
#         c = ("Unknown (Informasi lbh lanjut: Baak Kampus)")
        
#     tgl_lahir = int(input("Tanggal Lahir: "))
#     bln_lahir = int(input("Bulan Lahir: "))
#     thn_lahir = int(input("Tahun Lahir: "))

#     mhsh["lahir"] = date.datetime(thn_lahir,bln_lahir,tgl_lahir)
    
#     data_mhsw.update({'key':mhsh})


    
#     print("\n")
    
#     print(30*"=")

#     for mahasiswa in data_mhsw:
#         KEY = mahasiswa

#         NAMA = data_mhsw[KEY]['nama']
#         NIM = data_mhsw[KEY]['npm']
#         SKS = data_mhsw[KEY]['sks']
#         BEASISWA = data_mhsw[KEY]['beasiswa']
#         LAHIR = data_mhsw[KEY]['lahir'].strftime("%x")

#         print(f"{KEY:<6} {NAMA::<17} {SKS:<3} {BEASISWA:^9} {LAHIR:>10}")
#     print()