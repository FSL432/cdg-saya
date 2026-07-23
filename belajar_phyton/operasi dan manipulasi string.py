#operasi dan manipulasi 
# 1. menyambung string (concatenate)

nama_pertama = "Udin"
nama_kedua = "petot"
nama_ketiga = "reza"
nama_lengkap = nama_pertama +" "+nama_kedua +" "+ nama_ketiga
print(nama_lengkap)

# 2. menghitung panjang string
panjang = len(nama_lengkap)
print("panjang dari " + nama_lengkap + "=" + str(panjang))

# 3. operator untuk string 
# mengeek apakah ada komponen char atau string di string
d = "d"
stat = d in nama_lengkap
print( d + "=" + "ada di " + nama_lengkap + "=" +str(stat))

U = "U"
stat = U in nama_lengkap
print( U + "=" + "ada di " + nama_lengkap + "=" +str(stat))

D = "D"
stat = D not in nama_lengkap
print( D + "=" + "tidak ada di " + nama_lengkap + "=" +str(stat))

# mengulang string
print(20*'awok')
print('awok'*10)
#indexing
print("indek ke-0 :"+ nama_lengkap[0])
print("indek ke-14 :"+ nama_lengkap[14])
print("indek ke-(-2) :"+ nama_lengkap[-2])
print("indek ke-[0:5] :"+ nama_lengkap[0:5])
print("indek ke-[5:10] :"+ nama_lengkap[5:11])
print("indek ke-[0,3,5,7,9,11] :"+ nama_lengkap[0:12:2])

#item paling kecil
print("paling kecil :" + min(nama_lengkap))
#item paling kecil
print("paling besar :" + max(nama_lengkap))

#asciicode = ord(" ")
#print("ASCII code untuk spasi adalah " + str(asciicode))
data = 200
print("char untuk ASCII code 200 adalah " + chr(data))

# 4 operator dalam bentuk method 

data = "kaki ku kena paku kata kaka ku "
jumlah = data.count("a")# data(adalah objek),count (adalah method)
print("jumlah a pada "+ data + "=" + str(jumlah))

#merubah case dari string
# merubah semua ke upper case

salam = 'bro!!'
print("normal =" + salam)
salam = salam.upper()
print('upper =' + salam)

# merubah semua ke lower case 
alay = ('Aku Suka PraBoWo Dan GiBrAN')
alay = alay.lower()
print('lower = ' + alay)
 # pengecekan isX
salam = ("hallo")
apakah_lower = salam.islower()#ini hasilnya bool
print(salam , "is lower=" + str(apakah_lower))
apakah_upper = salam.isupper()#ini hasilnya bool
print(salam , "is upper=" + str(apakah_upper))
apakah_alpha = salam.isalpha()#mengecek semuanya huruf
print(salam , "is alpaha=" + str(apakah_alpha))
apakah_isalnum = salam.isalnum()#mengecek huruf dan angka 
print(salam , "is alnum=" + str(apakah_isalnum))
apakah_isdecimal = salam.isdecimal()#mengecek angka 
print(salam , "is decimal=" , str(apakah_isdecimal))
apakah_isspace = salam.isspace()#mengecek spasi,tab,new line \n 
print(salam , "is space=" , str(apakah_isspace))
apakah_istittle= salam.istitle()# hasil bool(mengecek judul huruf besar semua)
print(salam , "is tittle =" , str(apakah_istittle))


# pengecekan komponen startswith() endswith() 
cek_awal = "jokowi dua Periode".startswith("jokowi")
print('cek =', str(cek_awal))

cek_akhir = "jokowi dua Periode".endswith("Periode")
print('cek =', str(cek_akhir))


#penggabungan komponen join () split ()
pisah = ['aku','kamu','juga']
gabung = ','.join(pisah)
print(gabung)


gabung = ' '.join(pisah)
print(gabung)

gabung = ' ehm '.join(pisah)
print(gabung)

gabung = "akuehmkamuehmjuga"
print(gabung.split('ehm'))

#alokasi karkater rjust(), ljust, center()

kanan = "kanan".rjust(20)
print("'"+kanan+"'")

kiri = "kiri".ljust(20)
print("'"+kiri+"'")

center = "center".center(20,"=")
print("'"+center+"'")


# menghilangkan strip()
center = center.strip("=")
print("'"+center+"'")