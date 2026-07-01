# continue and pass 
# pass -> dia berfungsi sebagai dummy , tidak akan di eksekusi

# angka = 0
# while angka < 5:
#     angka += 1
#     if angka == 3:
#         pass # tidak akan di eksekusi
#     print(angka)

#continue

angka = 0 
print(f"angka sekarang -> {angka}")

while angka < 5 :
    angka += 1
    print(f"angka sekarang -> {angka}")
    if angka == 2 :
        print("good")
        continue # ankan membuat loop meloncat ke step selanjutnya
    print("hallooooooo")






