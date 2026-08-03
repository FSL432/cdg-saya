# lamda function
import os
os.system("cls")

# output = lamda argument:expression
kuadart = lambda angka:angka**2
print(f"ini hasil lambda kuadrat = {kuadart(4)}")

pangkat = lambda num,pow : num**pow
print(f"iini hasil lamdba pangkat = {pangkat(4,5)}")

# kegunaan lambda
data_list = ["joko","anwar","ibran"]
data_list.sort()
print(f"sorted list = {data_list}")

# sorting pakai panjang
def panjang_nama(nama):
    return len(nama)
data_list.sort(key=panjang_nama)
print(f"sorted by panjang = {data_list}")

# sort pakai lambda 

data_list = ["joko","anwar","ibran"]
data_list.sort(key=lambda nama :len(nama))
print(f"sorted by lambda = {data_list}")

# filter
data_angka = [1,2,3,4,5,6,7,8,9,10,11,12]

def kurang_dari_lima(angka):
    return angka > 5
data_angka_baru = list(filter(lambda x:x<=8,data_angka))
print(data_angka_baru)

# kasus genap
data_genap = list(filter(lambda x:(x%2==0),data_angka))
print(f"ini hasil data ganjil = {data_genap}")

#kasus ganjil
data_ganjil = list(filter(lambda x:(x%2!=0),data_angka))
print(f"ini hasil data ganjil = {data_ganjil}")

#anonymous function
# currying <- haskell curry

def pangkat(x):
    return lambda angka:angka**x
print(f"pangkat bebas = {pangkat(4)(9)}")
print(f"ini hasilnya = {pangkat(3)(3)}")


