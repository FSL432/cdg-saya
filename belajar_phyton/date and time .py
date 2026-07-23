# date and time

import datetime as dt
hari_ini = dt.date.today()

print(hari_ini)
print(f"hari ini adalah hari = {hari_ini:%A}")
tanggal = dt.date(2007,2,24)
print(tanggal)



import datetime as dt
print('masukan tanggal lahir anda')
tanggal = int(input("tanggal\t:"))
bulan =int(input("bulan\t:"))
tahun =int(input("tahun\t:"))

tanggal_lahir = dt.date(tahun,bulan,tanggal)
print(f"tanggal lahir anda adalah =" , tanggal_lahir)
print(f"hari nya adalah =  , {tanggal_lahir :%A} ")

hari_ini = dt.date.today()
print(f"hari ini tanggal : {hari_ini}")
umur = hari_ini - tanggal_lahir
tahun = umur.days // 365
bulan = umur.days // 12
sisa = (umur.days % 365) // 12
print(f'umur anda adalah = {umur},{bulan}')
print(F'umur anda adalah = {tahun} tahun, {sisa}bulan')













