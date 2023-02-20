###MODULE TO IMPORT
import MATH
from FROM import tambah,kali,pangkat

#Unk Task/Operation/Function within
from MATH import *
from FROM import *

##NORMAL MODULE
output1 = MATH.tambah(1,2,3,4,5)
output2 = MATH.kali(1,2,3,4,5)
output3 = MATH.pangkat(3)

print(output1)
print(output2)
print(output3(3))

#FROM MODULE
output1 = tambah(1,2,3,4,5)
output2 = kali(1,2,3,4,5)
output3 = pangkat(3)

print()
print(output1)
print(output2)
print(output3(3))