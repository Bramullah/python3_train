### *args

## Memasukkan data/argument

#Normally

def fungsi(nama,tinggi,berat):
    '''Normal Function'''
    print(f"{nama} punya tinggi {tinggi} dan berat badan {berat}")

##normal()
fungsi("Ibrahim",172,60)

def fungsi(data_list):
    '''Normal Function Insert to List'''
    data = data_list.copy()
    nama = data[0]
    tinggi = data[1]
    berat = data[2]
    
    print(f"{nama} punya tinggi {tinggi} dan berat badan {berat}")

##withlist[]
fungsi(["Bramullah",174,55])


## *args
# def fungsi(*args)

def fungsi (*data_diri):
    '''Normal Function Insert to List'''
    nama = data_diri[0]
    tinggi = data_diri[1]
    berat = data_diri[2]
    
    print(f"{nama} punya tinggi {tinggi} dan berat badan {berat}")

# normal output with list or many input
fungsi("Ibramullah",177,65)


### REAL CASE

def count(*data:int) -> int:
    '''Menambah input (Angka)'''
    output = 0
    for angka in data:
        output +=angka
    return output

nine= count(1,2,3,4,5,6,7,8,9)
six = count(1,2,3,7,8,9)

print(nine)
print(six)
