import datetime as dt
## Keys & Nesting Dict


mhsw={
    "Nama":"Ibrahim Bramullah",
    "NPM":"50420562",
    "SKS":"150",
    "Beasiswa":True,
    "Lahir":dt.datetime(2003,2,2)
}

mhsw2={
    "Nama":"Joko Anwar",
    "NPM":"50420563",
    "SKS":"150",
    "Beasiswa":True,
    "Lahir":dt.datetime(2004,2,2)
}

mhsw3={
    "Nama":"Dimaz Purnama",
    "NPM":"51420560",
    "SKS":"150",
    "Beasiswa":False,
    "Lahir":dt.datetime(2000,2,2)
}

data_mhsw={
    "k1":mhsw,
    "k2":mhsw2,
    "k3":mhsw3
}

print(data_mhsw)

##Print dict within dict
# < LEFT | ^ CENTER | > RIGHT
print(f"{'KEY':<6} {'Nama':<17} {'SKS':<3} {'Beasiswa':^9} {'Lahir':>10}")
print("-"*50)

for mahasiswa in data_mhsw:
    NAMA = data_mhsw[mahasiswa]['Nama']
    NIM = data_mhsw[mahasiswa]['NPM']
    SKS = data_mhsw[mahasiswa]['SKS']
    BEASISWA = data_mhsw[mahasiswa]['Beasiswa']
    LAHIR = data_mhsw[mahasiswa]['Lahir'].strftime("%x")

    KEY = mahasiswa
    print(f"{KEY:<6} {NAMA::<17} {SKS:<3} {BEASISWA:^9} {LAHIR:>10}")
print()

#becareful
print("===BECAREFUL")
print(f"{'KEY':.<6} {'Nama':;<17} {'SKS':\'<5} {'Beasiswa':\"^9} {'Lahir':>10}")