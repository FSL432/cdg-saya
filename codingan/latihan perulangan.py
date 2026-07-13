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

#belah ketupat
count = 1
spasi = int(sisi/2)
while True:
    if count%2:
        print("-"*spasi,"="*count)
        spasi -=1
        count +=1
    else:
        count+= 1
        continue
    if count > sisi:
            break
    
while True:
    if count%2:
        spasi+=1
        print(" "*spasi,"*"*count)
        count -=1
    else:
        count -=1
    if count == 0:
        break

while True:
     if count%2:
         spasi+=1
         print(" "*spasi,"*"*count)
         count -=1
     else:
         count -=1
     if count == 0:
         break

