import datetime as date
import os as awal
### Template Dict Mahasiwa

mhsw_temp={
    "nama":"nama",
    "npm":"00000000",
    "sks":0,
    "lahir":date.datetime(1111,1,11)
}

data_mhsw = {}

awal.system("cls")
print(f"{'SELAMAT DATANG':^20}")
print(f"{'DATA MAHASISWA':^20}")
print("-"*20)

mhsh = dict.fromkeys(mhsw_temp.keys())
mhsh["nama"] = input("Nama Mahasiswa: ")
mhsh["npm"] = input("NPM Mahasiswa: ")
mhsh["sks"] = input("SKS Lulus: ")
tgl_lahir = int(input("Tanggal Lahir: "))
bln_lahir = int(input("Bulan Lahir: "))
thn_lahir = int(input("Tahun Lahir: "))

mhsh["lahir"] = date.datetime(thn_lahir,bln_lahir,tgl_lahir)
