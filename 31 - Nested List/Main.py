## List within list
d1=[0,1,2]
d2=[3,4,5]
dplus=(d1+d2)

print(dplus)

list_2d=[d1,d2,6,7,8,9]
print(list_2d)

#Example of usage:
contestant1=["Ibrahim",21,"Boys"]
contestant2=["Bramullah",20,"Boys"]
contestant3=["Devi",20,"Girls"]

list_all_c=[contestant1,contestant2,contestant3]
print(f"{list_all_c}\n")

for c in list_all_c:
    print(f"Nama   : {c[0]}")
    print(f"Umur   : {c[1]}")
    print(f"Kelamin: {c[2]}\n")


### becareful ~~ reference
#comment all code below, and see the diffrent
# ctrl+/  || ctrl+alt+/

copy_peserta = list_all_c.copy()
contestant1[0]="Forfeit"
contestant1[1]="-"
contestant1[2]="-"


print(list_all_c)
print(copy_peserta)
for c in list_all_c:
    print(f"Nama   : {c[0]}")
    print(f"Umur   : {c[1]}")
    print(f"Kelamin: {c[2]}\n")