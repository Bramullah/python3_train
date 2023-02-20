### Default Argument

#normal
def say_hi(name):
    '''Fungsi Normal'''
    print(f"Hi {name}")

a = input("Your name was: ")
say_hi(a)


#default
def say_hoy(name = "Beauty"):
    '''Fungsi Default Argument'''
    print(f"Hi {name}")

say_hoy()


#other default
def say_hello(name, pesan = "Howdyy!?"):
    '''Other Default'''
    print(f"Hello {name}, {pesan}")

say_hello(a,"Hello Gergous")
say_hello(a)

#still other default + call
def number(angka, pangkat):
    '''Changing Default'''
    hasil = angka**pangkat
    return hasil

print(number(2,5))

#more complex number and call
def call(input1=1, input2=2, input3=3, input4=4):
    hasil = input1+input2+input3+input4
    return hasil

print(call())
print(call(input4=14))