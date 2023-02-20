### Operator dalam bentuk methods

# Merubah case dari string

# Merubah semua ke upper case

salam = "hi!"
print("Normal = "+salam)
salam = salam.upper()
print("Normal = "+salam)
salam = salam.lower()
print("Normal = "+salam)

## Pengecekan dengan isX method

#Lower Case
salam = "heyyhoo"
apakah_lower = salam.islower()
print(salam + " is lower = " + str(apakah_lower))

#Upper Case
salam = "HEYYHOO"
apakah_lower = salam.isupper()
print(salam + " is upper = " + str(apakah_lower))

### !!!ManyMore

#isalpha (all huruf)
#isalnum (all huruf & number)
#isdecimal (all number)
#isspace (theres spasi, tab, newline)
#istitle (start with upper at the start of string at every word)
#startswith() || endswith()
#join() || split()
# Alokasi karakter, rjust() || ljust() || center()


#istittle
judul = "\n\nIt Is Okay Not To Be Orkay"
cek_judul = judul.istitle()
print(judul + " adalah title? "+ str(cek_judul))

judul = "It is Okay Not To Be Orkay"
cek_judul = judul.istitle()
print(judul + " adalah title? "+ str(cek_judul))

#startswith
cek_start = "\nDobrei Utra".startswith("Dobrei")
print(cek_start)
#endswith
cek_last = "Dobrei Future".endswith("Future")
print(cek_last)

#startswith
cek_start = "Dobrei Utra".startswith("Utra")
print("false"+ str(cek_start))
#endswith
cek_last = "Dobrei Future".endswith("Dobrei")
print("false"+ str(cek_last))

#join()
print("\n\n")
newword = ['aku','sayang','kamu']
gabung = ','.join(newword)
print(newword)
print(gabung)
gabung = ' '.join(newword)
print(gabung)

#split()
print(gabung.split(' '))

# Alokasi karakter, rjust() || ljust() || center()
#biasanya:
print("\n")
print(5*"="+"data"+"="*5)

kanan = "kanan".rjust(10)
print("'"+kanan+"'")
kiri = "kiri".ljust(10)
print("'"+kiri+"'")
center = "center".center(10)
print("'"+center+"'")

satuduatiga = "satuduatiga".rjust(20,"~")
print("'"+satuduatiga+"'")
empatlimaenam = "empatlimaenam".ljust(20,"-")
print("'"+empatlimaenam+"'")
tujuhdelapansembilan = "tujuhdelapansembilan".center(30,"_")
print("'"+tujuhdelapansembilan+"'")


# kebalikannya (remove), strip()
print("\n")
kanan = "kanan".strip()
print("'"+kanan+"'")
kiri = "kiri".strip()
print("'"+kiri+"'")
center = "center".strip()
print("'"+center+"'")

satuduatiga = "satuduatiga".strip("~")
print("'"+satuduatiga+"'")
empatlimaenam = "empatlimaenam".strip("-")
print("'"+empatlimaenam+"'")
tujuhdelapansembilan = "tujuhdelapansembilan".strip("_")
print("'"+tujuhdelapansembilan+"'")