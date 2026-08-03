# memasukan dat argument

#materi args

def fungsi(*args):
    nama = args[0]
    tinggi = args[1]
    berat = args[2]
    print(f"{nama} punya tinggi {tinggi} dan berat {berat}")

fungsi("juned",165,70)

#studi kasus
def tambah(*data):
    output = 0
    for angka in data:
        output += angka
    return output

hasil = tambah(1,2,3,4,5,6,7,8,9)
print(hasil)
hasil = tambah(10,40,5)
print(hasil)

'''**kwargs'''
def fungsi(**kwargs):
    '''fungsi kwargs'''
    nama = kwargs["nama"]
    tinggi = kwargs["tinggi"]
    berat = kwargs["berat"]
    print(f"{nama} punya tinggi {tinggi} dan berat {berat}")
    

fungsi(nama = "kiko", tinggi = 165, berat = 60)

# studi kasus

def math(*args,**kwargs):
    output = 0
    if kwargs ["option"] == "tambah":
        for angka in args:
            output += angka
    elif kwargs ["option"] == "kali":
        output = 1
        for angka in args :
            output *= angka
    else:
        print("tidak ada opeasi")
    return output
hasil = math(1,2,3,4,option = "tambah")
print(f"ini hasil tambah ={hasil}")       
hasil = math(1,2,3,4,option = "kali")       
print(f"ini hasil kali ={hasil}")
