data_angka = [2,3,6,7,8,9,4,6,2,3,1,6,8,]
print(f"data angka  = \n{data_angka}")

#count data 
jumlah_angka6_padadata = data_angka.count(6)
jumlah_angka8_padadata = data_angka.count(8)
print(f"jumlah angka 6 = {jumlah_angka6_padadata}")
print(f"jumlah angka 8 = {jumlah_angka8_padadata}")


#ambil posisi data (index)
data_nama = ['ganjar','sby','ginanjar','roky gerung','mega chan']
index_roky = data_nama.index('ganjar')
index_mega = data_nama.index('mega chan')

print(f'index roky gerung = {index_roky}')
print(f'index roky gerung = {index_mega}')

#mengurutkan list
print(f'ini sebelum di urutkan = {data_angka}')

data_angka.sort()
print(f'ini data setelah di sort = \n{data_angka}')

data_nama.sort()
print(f'ini data nama setlah di sort = \n{data_nama}')

#kebalikan dari terbesar -> ke terkecil
data_angka.reverse()
data_nama.reverse()

print(f'ini data angka setelah di balik = \n{data_angka}')
print(f'ini data nama setelah di balik = \n{data_nama}')







