##Global & Local Scope

#GLOBAL
#CAN BE ACCESS ANYWHERE OUTSIDE (:)
GLOBAL = "Dimaz"

def fungsi():
    print(f"fungsi menampilkan {GLOBAL}")

fungsi()

for i in range(0,6):
    print(f"Loop {i}: {GLOBAL}")

if True:
    print(f"IF {GLOBAL}")


#LOCAL
#CANT BE ACCESS ANYWHERE OUTSIDE (:)

def lokal():
    inside="Dimaz"
    return inside

lokal()
#print(f"{inside}")


### study case:
angka=0
def ubah_angka(changes):
    angka=changes
    

print(f"Before {angka}")
###Nggak ke rewrite
ubah_angka(10)
print(f"After {angka}")
    

### USE GLOBAL WITHIN LOCAL
name = "Dika"
def ubah_angka(changes,nama):
    global angka,name
    angka=changes
    name=nama

print(f"Global Wihin Local: {angka,name}")
print(f"Global within Lokal: {name}")



####EXCEPT FOR AND IF?
for x in range(0,5):
    x = "NAMAx"

print(x)

if True:
    WTF = "NAMAif"

print(WTF)