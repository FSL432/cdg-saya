# materi method

#index   0(-3)    1(-2)      2(-1)
data = ["jokowi","prabowo","gibran"]


# mengambil data dari list ini 
data0 = data[0]
print(data0)

data2 = data[-2]
print(f"ini data ke 2 = {data2}")

data3 = data[-1]
print(f"ini data ke 3 = {data3}")

#mengambil info jumlah data dalam list

panjang_data= len(data)
print(f"ini panjang datan = {panjang_data}")

#manipulasi data list
# menambahkan list pada list sesuai posisi

print(f"ini data sebelum di ubah = {data}")

data.insert(1,"mahfud")
print(f"data sesudah dita,bahkan = {data}")

# menambahkan list pada posisi akhir
data.append("ganjar")
print(f"data sesudah dita,bahkan = {data}")

#menggabungkan sebuah list
databaru = ["anwar","deni","sule"]
data.extend(databaru)
print(f"data digabungkan = \n{data}")

#menghapus salah satu sata

data.remove("jokowi")
print(f"data dihapus = \n{data}")
#jika nama data tidak ada di list maka akan eror

#menghapus data paling belakang
data.pop()
print(f"data dihapus paling belakang = \n{data}")







