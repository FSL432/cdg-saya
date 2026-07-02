# break 
data_int = int(input('masukan angka = '))
angka = 0 
while True:
    angka += 1 
    print(f"angka sekarang -> {angka}")

    if angka == data_int:
        print("good")
        break
    print('hallo')
print('oke cukup')
