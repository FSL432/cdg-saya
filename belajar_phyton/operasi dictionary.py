#operator untuk dictionary

data_dict = {
    "jok":"jokowi",
    "wow":"prabowo",
    "dang":"dadang",

}

#panjang dicttionary
LENDICT = len(data_dict)
print(f"panjang dictionary = {LENDICT} ")

#mengecek keys exist atau tidak
KEY = "jok"
CHEKKEY = KEY in data_dict
print(f"apakah {KEY} ada di data dict = {CHEKKEY} ")

#mengakses value (read) dengan get 
# print(data_dict["anies"])#inin akan eror
print(data_dict.get("jok"))
print(data_dict.get("anies","tidak ada"))#ini akan none \ tidak ada

#mengupdate data
data_dict["jok"] = "mega chan" #ini untuk merubah isi data
print(data_dict)
data_dict["jang"] = "ujang kalem"
print(data_dict)

data_dict.update({"jangnur" : "jajang nurjaman"})#ini menambah d/ mengupdate isi data
print(data_dict)
data_dict.update({"jok" : "jokowi"})#ini merubah karena ada di dalam data
print(data_dict)


#mengdelete /menghapus 
del data_dict["jang"]
print(data_dict)

