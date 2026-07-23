# looping dictionary

my_friend = {
    "abil" : "bilal somebody pleasure",
    "jukki" : "zaaki nt terus",
    "Dan" : "firdan si king",
    "gus" : "agus member jmk"
}

#looping frist try
for teman in my_friend:
    print(teman)

#operator untuk mengambil item / iterables 
print("\nINI HASIL KEYS")
keys = my_friend.keys()
print(keys)

for key in my_friend.keys():
    print(my_friend.get(key))

#mengambil value
print("\nINI HASIL VALUE")
values = my_friend.values()
print(values)

for value in my_friend.values():
    print(value)

#items 
print("\nINI HASIL ITEM")
items = my_friend.items()
print(items)

for item in my_friend.items():
    print(item)
    
# keys dan velue
for key,value in my_friend.items():
    print(f"key = {key}, velue = {value}")




