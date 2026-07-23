# program list


list_buku = []
while True:
    print(f"masukan data buku")
    judul = input("judul buku\t:")
    penulis = input(f"nama penulis\t :")

    buku_baru = [judul,penulis]
    list_buku.append(buku_baru)

    print("_"*35)
    for index,buku in enumerate(list_buku):
        print(f"{index+1} | {buku[0]} | {buku[1]} ")
    
    print("_"*35)
    jika_lanjut = input("apakah anda ingin melanjutkannya?(Y/T)")
    if jika_lanjut == "Y":
        print("tambah lagi bang terusin")
    elif jika_lanjut == "T":
        print("oke cukup terima kasih")
        break








