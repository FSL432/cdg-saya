'''membuat fungsi / function'''

# def hello_world():
#     ''' fungsi menampilkan hello world'''
#     print("hello world")
#     print("hallo dunia")
#     print("hidup jokowi")
# hello_world()
# hello_world()

# def fungsi():
#    # '''pemanggilan fungsi harus setelah dibuat
#     jadi buat fungsi nya dulu baru panggil'''
#     print("ini fungsi")
# # fungsi()

'''fungsi dengan argument (input)'''
# def nama_fungsi():
    #definition,nama fungsi(argument/parameter/input)
    # print("ini fungsi")

'''
def nama fungsi(argumet):
    badan fungsi
'''

def hello_world(nama):
    '''fungsi hello world menerima input dengan variable nama'''
    print(f"selamat datang di dunia {nama}")
hello_world("agus")

#program tambah dengan angka
def tambah(angka1,angka2):
    '''fungsi tambah dengan angka'''
    hasil = angka1 + angka2
    print(f"{angka1} + {angka2} = {hasil}")
tambah(90,48)
tambah(76,43)

def nama_orang(grup):
    data_peserta = grup.copy()
    for peserta in data_peserta:
        print(f"yang terhormat kita panggil kan {peserta}")

anggota = ["anwar","ki jakar","mas joko"]

nama_orang(anggota)




