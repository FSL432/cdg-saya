# list 2D / nasted list
# contoh penggunaan nya 
# peserta0 = ["joko",47,"laki-laki"]
# peserta1 = ["mega chan",43,"wanita"]
# peserta2 = ["supri",38,"laki-laki"]
# peserta3 = ["tuti",37,"wanita"]

# list_peserta = [peserta0,peserta1,peserta2,peserta3]
# print(f"peserta = {list_peserta}")

# for peserta in list_peserta:
#     print(f"nama\t {peserta[0]}")
#     print(f"umur\t {peserta[1]}")
#     print(f"gender\t {peserta[2]}\n")

#deep copy nasted list
data0 = [1,2]
data1 = [2,3]
data2D = [data0,data1,12]
data2D_copy = data2D.copy()

print(f"data = {data2D}")
print(f"data copy = {data2D_copy}")


#mengambil data dari nasted list
data = data2D[1][1]
print(f"data = {data}")

#addres semuanya
print(f"addres asli = {hex(id(data2D))}")
print(f"addres asli = {hex(id(data2D_copy))}")

print(f"\naddres dari member ke 1 ")
print(f"addres asli = {hex(id(data2D[0]))}")
print(f"addres copy = {hex(id(data2D_copy[0]))}")

data2D[1][0] = 7
data2D[2] = 5

print(f"data = {data2D}")
print(f"data copy = {data2D_copy}")

# gunakan deep copy
from copy import deepcopy

data2D = [data0,data1,12]
data2D_deepcopy = deepcopy(data2D)

print(f"\naddres dari member ke 1 ")
print(f"addres asli = {hex(id(data2D[0]))}")
print(f"addres deeep copy = {hex(id(data2D_deepcopy[0]))}")


data2D[1][0] = 400
print(f"data = {data2D}")
print(f"data copy = {data2D_copy}")
print(f"data deepcopy = {data2D_deepcopy}")















