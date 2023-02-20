### Fungsi dengan argumen (input)

#definition [nama](argument/input)
#    badan fungsi


def hello_world_with_name(nama):
    print(f"Hi {nama}, welcome")

hello_world_with_name("Ibrahim")

def tambah(a1,a2):
    hasil = a1+a2
    print(f"{a1}+{a2}={hasil}")

tambah(10,10)
tambah(999,1)

def say_hi(esports):
    data_esports = esports.copy()
    for e_esports in data_esports:
        print(f"Welcome team: {e_esports}")


all_esports=["Dota 2","FIFA","CSGO"]

#sayhi function (argument/input)
say_hi(all_esports)

#try to create input with list and put in in input

