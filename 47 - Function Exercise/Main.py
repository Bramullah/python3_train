import os as START
### Latihan Fungsi

##Luas & Keliling

# Normally
# while True:
#     START.system("cls")
#     print(f"{'Program Luas & Keliling':^40}")
#     print(f"{'='*40:^40}")

#     PANJANG = int(input(f"Masukkan nilai panjang :"))
#     LEBAR = int(input(f"Masukkan nilai lebar :"))

#     LUAS = PANJANG*LEBAR
#     KELILING = 2*(PANJANG+LEBAR)

#         ##Hasil
#     print(f"Hasil Luas: {LUAS}")
#     print(f"Hasil Keliling: {KELILING}")

#     print(20*"=")
#     CONTINUE = input("Do you want to continue? (Y/Yes, No/N): ")
#     if CONTINUE == "Y" and "Yes":
#         continue
#     elif CONTINUE == "N" and "No":
#         break
#     else:
#         print("!! BRUH")


##########################################################


#Usually

def header():
    '''Fungsi Header'''
    START.system("cls")
    print(f"{'Program Luas & Keliling':^40}")
    print(f"{'='*40:^40}")

def input_user():
    '''Fungsi Input User'''
    lebar = int(input(f"Masukkan nilai lebar :"))    
    panjang = int(input(f"Masukkan nilai panjang :"))
    return lebar,panjang


def hitung_luas(lebar,panjang):
    '''Fungsi Luas (Lebar, Panjang)'''
    return lebar*panjang

def hitung_keliling(lebar,panjang):
    '''Fungsi Keliling (Lebar, Panjang)'''
    return 2(lebar+panjang)

def display(message,value):
    '''Fungsi Display'''
    print("\n")
    print(f"Hasil {message}: {value}")

while True:
    header()

    LEBAR,PANJANG = input_user()
    LUAS = hitung_luas(LEBAR,PANJANG)
    KELILING = hitung_keliling(LEBAR,PANJANG)

    #Hasil
    display("Luas", LUAS)
    display("Keliling",KELILING)
    
    
    print(20*"=")
    CONTINUE = input("Do you want to continue? (Y/Yes, No/N): ")
    
    if CONTINUE == "Y" or "Yes":
        continue
    elif CONTINUE == "N" or "No":
        break
    else:
        print("!! BRUH")


## create luas or keliling or both option