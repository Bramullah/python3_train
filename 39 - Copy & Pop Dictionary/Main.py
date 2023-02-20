### List = Dict
## Where the data = data will be changes, bcs got the same address

friend={
    "A":"Dimaz",
    "B":"Dika",
    "C":"Purnama",
    "D":"Joko",
    "E":"Anwar",
    "Last":"~I don't have many friend"
}

#copy
print()
copy= friend.copy()
print(copy)

#pop = take/transfer  |  mengambil data
print()
pop=copy.pop("B")
print(pop)

#pop item
print()
pop_item=copy.pop("Last")
print(pop_item)

print(friend)