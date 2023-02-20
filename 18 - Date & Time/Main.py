### Date & Time
import datetime as dt

hari_ini = dt.date.today()
print(f"Hari: {hari_ini}  Tanggal: {hari_ini:%A}")

#BECAREFUL
hari_ini = dt.date.today()
print(f"Hari: {hari_ini}  Tanggal: {hari_ini:%a}")
print(f"{hari_ini:%c}\n")

#OtherDate
tgl= int(input("Masukkan Tanggal\t:"))
bln= int(input("Masukkan Bulan\t\t:"))
thn= int(input("Masukkan Tahun\t\t:"))
print(f"\nTanggal lahir Anda: {dt.date(thn,bln,tgl)}")

tgl_lahir = dt.date(thn,bln,tgl)
print(f"Hari kelahiran Anda: {tgl_lahir:%A}\n")

u_hari= hari_ini - tgl_lahir
u_bulan= (u_hari.days % 365.25) // 30
u_tahun= str(int(u_hari.days // 365.25 - 1))

days = str(u_hari)
print(days[0:9])
print(u_bulan)
print(u_tahun+" Tahun")