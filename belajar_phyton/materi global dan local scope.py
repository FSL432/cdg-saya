#aksses variable global atau fungsi
nama_global = "faisal" #ini variable global
def fungsi():
    print(f"fungsi menampilkan {nama_global}")


#akses variable dalam loop
for i in range(5):
    print(f"loop {i} - {nama_global}")

#percabangan if
if True:
    print(f"if menampilkan = {nama_global}")

# variable lokal scope

def fungsi2():
    nama_lokal = 'jana' #<-- ini variable lokal scope

fungsi2()#tidak dapat dipanggil karena bareda di dalam

#contoh1 penggunaan
def jana():
    print(f"hallo {nama}")
nama = "jana"#<-- ini terlebih dahulu
jana()#<-- baru ini yang akan mengeksekusi

# contoh2 merubah variable global
name = "rizki"
angka = 90
def ubah(nama_baru,angka_baru):
    global name #fungsi ini dapat merubah global
    global angka
    name = nama_baru
    angka = angka_baru

ubah("joko",43)
print(f"hasil = {name,angka}")

#contoh 3 for dan if dapat merubah global tidak perlu pakai (global)

angka = 0

for i in range(5):
    angka += 1

print(angka)
