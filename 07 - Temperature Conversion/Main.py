##Konversi Temperatur

# C, R, F, K
# Celcius, Reamur, Fahrenheit, Kelvin

"""
C
    R > 4/5 C
    F > 9/5 C + 32
    K > C + 273

R
    C > 5/4 R
    F > 9/4 R + 32
    K > 5/4 R + 273

F
    C > 5/9 (F-32)
    R > 4/9 (F-32)

K
    C > K-273
    R > 4/5 (K-273)
"""

### Celcius
print("===CELCIUS===")
celcius = float(input("Masukkan suhu dalam Celcius: "))
print("Suhu dalam Celcius:      ",celcius)

reamur = (4/5) * celcius
fahrenheit = ((9/5) * celcius) + 32
kelvin = celcius + 273

print("Suhu dalam Reamur:       ",reamur)
print("Suhu dalam Fahrenheit:   ",fahrenheit)
print("Suhu dalam Kelvin:       ",kelvin)

### Reamur
print("\n===Reamur===")
reamur = float(input("Masukkan suhu dalam Reamur: "))
print("Suhu dalam Reamur:       ",reamur)

reamur = (5/4) * celcius
fahrenheit = ((9/4) * celcius) + 32
kelvin = (5/4) * reamur  + 273

print("Suhu dalam Celcius:      ",celcius)
print("Suhu dalam Fahrenheit:   ",fahrenheit)
print("Suhu dalam Kelvin:       ",kelvin)

### Fahrenheit
print("\n===Fahrenheit===")
fahrenheit = float(input("Masukkan suhu dalam Fahrenheit: "))
print("Suhu dalam Fahrenheit:   ",fahrenheit)

celcius = (5/9) * (fahrenheit - 32)
reamur = (4/9) * (fahrenheit - 32)
kelvin = (fahrenheit+459.67) * 5/9

print("Suhu dalam Celcius:      ",celcius)
print("Suhu dalam Reamur:       ",reamur)
print("Suhu dalam Kelvin:       ",kelvin)

### Kelvin
print("\n===Kelvin===")
kelvin = float(input("Masukkan suhu dalam Kelvin: "))
print("Suhu dalam Kelvin:        ",kelvin)

celcius = kelvin - 273
reamur = (4/5) * (kelvin - 273)
fahrenheit = 1.8 * (kelvin - 273) + 32

print("Suhu dalam Celcius:      ",celcius)
print("Suhu dalam Reamur:       ",reamur)
print("Suhu dalam Fahrenheit:   ",fahrenheit)