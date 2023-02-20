### List Program: Books

list_buku=[]
while True:
    print("Masukkan Judul Buku: ")
    judul = input()
    print("Masukkan Nama Penulis: ")
    penulis = input()

    buku=[judul,penulis]
    list_buku.append(buku)

    print("\n\n"+5*"=","Data Buku")
    for index, e_buku in enumerate(list_buku):
        print(f"{index+1} | {e_buku[0]} | {e_buku[1]}")
    

    ##1 for loop then this task
    print("\n\n"+10*"=")
    a = input("Continue fill the book data? (/YESYes/y/Y, NO/No,n,N): ")
    
    if a == "No" and "n" and "N":
        break
    elif a == "Yes" and "y" and "Y":
        continue
    else:
        print("\n===WTF!!??\n")
        break
