# latihan perulangan membuat segitiga 

sisi = 8

# menggunakan for 
# dummy variable
# count = 6
# for i in range(count):
#     print("*"*count)
#     count +=1

# menggunakan while
# print('='*37)
# count = 1
# while True:
#     print("*"*count)
#     count +=1
#     if count > sisi:
#         break
# print("akhir dari while")

#hanya ganjil saja
# print('='*15,'ini while',"="*15)
# count = 1
# spasi = int(sisi/2)
# while True:
#     if count%2: 
#    #print jika ganjil
#      print(" "*spasi,"-"*count)
#      spasi -= 1
#      count += 1
#     else:
#         #akan kembali ke atas jika ganjil
#         count += 1
#         continue
#     #akan break jika count melebihi sisi
#     if count > sisi :
#         break
# print('akhir while')



#belah ketupat
# for i in range(1,sisi+1):
#  spasi = " " * (sisi - i)
#  bentuk = "=" * (2 * i - 1)
#  print(spasi + bentuk)
    
# for i in range(sisi,0,-1):
#  spasi = " " * (sisi - i)
#  bentuk = "=" * (2 * i - 1)
#  print(spasi + bentuk)

# count = 1
# for i in range (sisi):
    # print("*"*count)
    # count += 1
    # spasi = "-" * (sisi - i)
    # print(spasi)

# tinggi = int(input("masukan nilai tinngi ="))
# for i in range( tinggi,0,-1 ):
#     print("*"*i)

# tinggi = int(input("masukan nilai tinggi ="))
# for n in range(1,tinggi + 1):
#     if n == 1:#ini awal tinggi
#         print(" "* (tinggi - n) + "&")
#     elif n == tinggi:#batas tinggi
#         print("/" * (2 * tinggi - 1))
#     else :#mengisi yang kosong nya
#         print(" " * (tinggi - n) + "?" + "=" * (2 * n - 3) + "#")    

# for n in range(tinggi,0,-1):
#     if n == 1:
#         print(" "* (tinggi - n) + "&")
#     elif n == tinggi:
#         print("/" * (2 * tinggi - 1))
#     else :
#         print(" " * (tinggi - n) + "?" + "=" * (2 * n - 3) + "#")    
    

tinggi = 5
for i in range(1,tinggi + 1):
    jarak_kosong = " " * (tinggi - i)
    bintang = "*" * (2 * i - 1)
    print(jarak_kosong + bintang)

for i in range(tinggi - 1,0,-1):
    jarak_kosong = " " * (tinggi - i)
    bintang = "*" * (2 * i -1)
    print(jarak_kosong + bintang)