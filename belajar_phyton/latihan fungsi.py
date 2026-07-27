''' latihan fungsi '''
import os

#program menghitung luas dan keliling persegi panjang
#membuat header program

# os.system("cls")

# print(f"{'PROGRAM MENGHITUNG LUAS':^40}")
# print(f"{'DAN KELILING PERSEGI PANJANG':^40}")
# print(F"{'-'*40:^40}")

# #Mengambil input user 
# LEBAR = int(input("masukan nilai lebar ="))
# PANJANG = int(input("masukan nilai panjang ="))

# #menghitung
# LUAS = PANJANG*LEBAR
# KELILING = 2*(PANJANG+LEBAR)

# #tampilkan hasil 
# print(f"hasil perhitungan luas = {LUAS}")
# print(f"hasil perhitungan keliling = {KELILING}")

def header():
    '''ini fungsi header'''
    os.system("cls")

    print(f"{'PROGRAM MENGHITUNG LUAS':^40}")
    print(f"{'DAN KELILING PERSEGI PANJANG':^40}")
    print(F"{'-'*40:^40}")

def input_user():
    # #Mengambil input user 
    lebar = int(input("masukan nilai lebar ="))
    panjang = int(input("masukan nilai panjang ="))
    return lebar,panjang 

def hitungluas(lebar,panjang):
    # #menghitung
    return lebar*panjang

def hitunghkeliling(lebar,panjang):
    return 2*(lebar+panjang)

def display(message,value):
    '''fungsi display'''

    print(f"hasil perhitungan = {message}, {value}")
#program utama
while True:
    header()
    option = input("luas atau keliling =")
    if option == "luas":
        LEBAR,PANJANG = input_user()
        LUAS = hitungluas(LEBAR,PANJANG)
        display(f"luas =",LUAS)
    elif option == "keliling":
        LEBAR,PANJANG = input_user()
        KELILING = hitunghkeliling(LEBAR,PANJANG)
        display(f"keliling =",KELILING)

    iscontinue = input(f"apakah lanjut (ya/tidak) ")
    if iscontinue == "tidak":
        break 
print("akhir program")


