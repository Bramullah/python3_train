### Looping Dict

friend={
    "A":"Dimaz",
    "B":"Dika",
    "C":"Purnama",
    "D":"Joko",
    "E":"Anwar",
    "Last":"~I don't have many friend"

}
##Get keys (if you know this was a dictionary)
for friends in friend:
    print(friends)

print("\n")
#Operator (If you dont know if this was a dictionary or no)
keys = friend.keys()
print(keys)

print("\n\n")
#values
value= friend.values()
print(value)

#items
item= friend.items()
print(item)



#combine
for key in friend.keys():
    print(key)

for value in friend.values():
    print(value)

for item in friend.items():
    print(item)
    #become tuple

for key,value in friend.items():
    print(f"Key: {key}, Value: {value}")
