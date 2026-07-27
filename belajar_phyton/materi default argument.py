'''default argument'''

#def fungsi(argument):
# def fungsi(argument= nilai defaultnya)
#contoh 1 
def say(nama = "ujang"):
    '''fungsi dengan default argument'''
    print(f"hallo {nama}")

say("iku")
say()

#contoh2
def sapa(nama,pesan = "apa kabar"):
    '''fungsi dengan satu default, dan satu biasa'''
    print(f"hai {nama}, {pesan}")

sapa("joko")
sapa("joko","gimana sehat")\

#contoh 3
def hitung(angka,pangkat):
    hasil = angka**pangkat
    return hasil

print(hitung(9,2))
hasil = hitung(pangkat = 3, angka = 7)
print(hasil)

# contoh 4

def fungsi(input1=1,input2=2,input3=3,input4=4):
    hasil = input1 + input2 + input3 + input4
    return hasil

print(fungsi())
print(fungsi(input3=40))

