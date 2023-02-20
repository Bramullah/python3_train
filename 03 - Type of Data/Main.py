# a =10, a variable || 10 value

#integer
integer = 1
print("Data: ",integer)
print("Bertipe: ", type(integer))
print()

#float
float = 0.584684
print("Data: ",float)
print("Bertipe: ", type(float))
print()

#str (string)
string = "Kamu nanyaaee"
print("Data: ",string)
print("Bertipe: ", type(string))
print()

#Boolean (Biner)
bool = True
print("Data: ",bool)
print("Bertipe: ", type(bool))

bool = False
print("Data: ",bool)
print("Bertipe: ", type(bool))
print()

# import C language
from ctypes import c_char, c_double
c_char = "Ini lebih panjang" 
c_double = c_double(100.12345678901)

print(c_char)
print(c_double)
print("Bertipe: ", type(c_char))
print("Bertipe: ", type(c_double))