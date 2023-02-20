### Operasi pada dictionary

dictt={
    "KEY":"VALUE",
    "Name":"Ibrahim",
    "NPM":50420562, 
}

lendict=len(dictt)
print(lendict)

#CHECKDATA
key=input("Key: ")
checkkey=key in dictt
if key in dictt:
    print(f"There's {key} in {dictt}")
else:
    print(f"There's no {key} in {dictt}")


#Check none(or_else) data
print(dictt.get("USER"))
print(dictt.get("USER", 1))
print(dictt.get("USER", "Not Found"))

#Update Dict
--1
dictt["KEY"] = "Value"
dictt["Key"] = "Value"
print(dictt)
print()
--2
dictt.update({"key":"value","KEY":"VALUE"})
print(dictt)

#Delete dict
del dictt["key"]
print(dictt)


###Search it again for input user
# key=input("Key: ")
# checkkey=dictt.get(key)
# print(f"Is there {checkkey} in {dictt})")