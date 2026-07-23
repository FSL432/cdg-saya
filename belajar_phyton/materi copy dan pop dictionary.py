#materi copy dictionary

my_friend = {
    "Dan" : "diantara nada",
    "jok" : "jokowi",
    "Hai" : "hari akhir indah",
    "jum" : "juara umum muji",
}

teman = my_friend.copy()

print(f"my friend = {my_friend}\n")
print(F"teman = {teman}\n")

my_friend["jok"] = "jangan otoriter kau"
print(f"my friend = {my_friend}\n")
print(F"teman = {teman}\n")

#pop dictionary
datajum = teman.pop("jum")#berdasarkan key
print(f"ini data jum = {datajum}\n")
print(f"ini data teman = {teman}\n")

#popitem dictionary 
dataterakhir = teman.popitem()#hanya terakhir saja
print(f"ini data terakhir = {dataterakhir}\n")
print(f"ini data teman = {teman}\n")






















