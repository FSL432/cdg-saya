import datetime
import os
import string 
import random



template_mahasiswa = {
    'nama': 'nama',
    'nim' : '00000000',
    'sks_lulus' :0,
    'lahir':datetime.datetime(1111,1,11)
}
data_mahasiswa = {}
while True :
# os.system("cls") #untuk windows 
    os.system("cls")
    print(f"{"SELAMAT DATANG":^20}")
    print(F"{"DATA MAHASISWA":^20}")
    print("_"*20)

    mahasiswa = dict.fromkeys(template_mahasiswa.copy())

    mahasiswa['nama']= input("Nama Mahasiswa: ")
    mahasiswa['nim']= input("Nim Mahasiswa: ")
    mahasiswa['sks_lulus']= int(input("SKS lulus: "))
    TAHUN_LAHIR = int(input("Tahun lahir (YYYY)"))
    BULAN_LAHIR = int(input("Bulan lahir (MMMM))"))
    TANGGAL_LAHIR = int(input("Tanggal lahir (DDDD)"))
    mahasiswa['lahir']=datetime.datetime(TAHUN_LAHIR,BULAN_LAHIR,TANGGAL_LAHIR)

    KEY = ''.join((random.choice(string.ascii_uppercase) for i in range(6)))
    data_mahasiswa.update({KEY:mahasiswa})
    print(f"\n{'KEY':<6} {'NAMA':<17} {'SKS':<3} {'LAHIR':<10}" ) 
    print("_"*50) 

    for k in data_mahasiswa: 
     KEY = mahasiswa
     NAMA = data_mahasiswa[k]['nama']
     NIM = data_mahasiswa[k]['nim']
     SKS = data_mahasiswa[k]['sks_lulus']
     LAHIR = data_mahasiswa[k]['lahir'].strftime("%x")

     print(F"{k:<1} {NAMA:<17} {SKS:<2} {LAHIR:<10}" ) 
     print("\n")
    sudah_selesai = input("Sudah selesai (selesai/belum)?")
    if sudah_selesai == "selesai":
       break 

print("TERIMA KASIH")


