# latihan perulangan membuat segitiga 

sisi = 10

# menggunakan for 
# dummy variable
# count = 6
# for i in range(sisi):
#     print("*"*count)
#     count +=1

# menggunakan while
print('='*37)
count = 1
while True:
    print("*"*count)
    count +=1
    if count > sisi:
        break
print("akhir dari while")

#hanya ganjil saja
print('='*15,'ini while',"="*15)
count = 1
spasi = int(sisi/2)
while True:
    if count%2: 
   #print jika ganjil
     print(" "*spasi,"-"*count)
     spasi -= 1
     count += 1
    else:
        #akan kembali ke atas jika ganjil
        count += 1
        continue
    #akan break jika count melebihi sisi
    if count > sisi :
        break
print('akhir while')











