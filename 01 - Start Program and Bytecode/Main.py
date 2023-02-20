import time
start_time = time.time()

print("This is Hello World #1")
print("Random Things to add on #2")

#This was comment
"""Multi
    Comment"""

a = 10 #variable?
print(a)

"""Test speed with
compile vs interpred"""
# python -m py_compile 'filename'.py

for i in range(1,1000):
    a=20

print (time.time() - start_time, "detik")
