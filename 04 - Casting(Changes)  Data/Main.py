# Casting / Changes variable
# tipe data = int, float, bool, str
##INTEGER
data_int = 1
print("Data: ", data_int, " ,type = ",type(data_int))

print("====INTEGER====")
data_float = float(data_int)
data_str = str(data_int)
data_bool = bool(data_int)
print("Data: ",data_float, " ,type = ",type(data_float))
print("Data: ",data_str, " ,type = ",type(data_str))
print("Data: ",data_bool, " ,type = ",type(data_bool))

print()
##FLOAT
data_float = 1.5
print("Data: ", data_float, " ,type = ",type(data_float))

print("====FLOAT====")
data_int = int(data_float)
data_str = str(data_float)
data_bool = bool(data_float)
print("Data: ",data_int, " ,type = ",type(data_int))
print("Data: ",data_str, " ,type = ",type(data_str))
print("Data: ",data_bool, " ,type = ",type(data_bool))

print()
##BOOLEAN
data_boolean = True
print("Data: ", data_boolean, " ,type = ",type(data_boolean))

print("====BOOLEAN T ====")
data_int = int(data_boolean)
data_str = str(data_boolean)
data_float = bool(data_float)
print("Data: ",data_int, " ,type = ",type(data_int))
print("Data: ",data_str, " ,type = ",type(data_str))
print("Data: ",data_float, " ,type = ",type(data_float))

data_boolean = False
print("Data: ", data_boolean, " ,type = ",type(data_boolean))

print("====BOOLEAN F ====")
data_int = int(data_boolean)
data_str = str(data_boolean)
data_float = float(data_boolean)
print("Data: ",data_int, " ,type = ",type(data_int))
print("Data: ",data_str, " ,type = ",type(data_str))
print("Data: ",data_float, " ,type = ",type(data_float))

print()
##STRING
data_str = "400"
print("Data: ", data_str, " ,type = ",type(data_str))

print("====STRING Fill====")
data_int = int(data_str)
data_float = float(data_str)
data_bool = bool(data_str)
print("Data: ",data_int, " ,type = ",type(data_int))
print("Data: ",data_float, " ,type = ",type(data_float))
print("Data: ",data_bool, " ,type = ",type(data_bool))

data_str = ""
print("Data: ", data_str, " ,type = ",type(data_str))

print("====STRING Empty====")
#data_int = int(data_str)
#data_float = float(data_str)
data_bool = bool(data_str)
#print("Data: ",data_int, " ,type = ",type(data_int))
#print("Data: ",data_float, " ,type = ",type(data_float))
print("Data: ",data_bool, " ,type = ",type(data_bool))