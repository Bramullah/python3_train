import string as STR
### TypeHINTS

## Menghindari error pada output, sementara
## pada code tidak terdapat error

def input_pangkat():
    pangkat= int(input("Masukkan Pangkat: "))
    return pangkat

def input_nama():
    name= str(input("Masukkan Nama: "))
    return name


def sepuluh_pangkat(argument:int) -> int:
    '''Fungsi dengan HINTS'''
    output = 10**argument
    return output

pangkat=input_pangkat()
HASIL = sepuluh_pangkat(pangkat)
print(HASIL)

def display(argument:STR):
    '''Fungsi dengan HINTS'''
    print(argument)

name=(input_nama())
display(name)