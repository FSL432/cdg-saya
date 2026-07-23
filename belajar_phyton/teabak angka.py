angka = int(input("tebak angka dari 1 sampai 20 ="))

if angka >= 20:
    print(f"{angka} kejauhan")
elif angka >=17:
    print(f"{angka} dikit lagi")
elif angka >= 12:
    print(f"{angka} udah deket banget")
elif angka <= 0:
    print(f"{angka} kekecilan")
elif angka <= 7:
    print(f"{angka} mulai panas nih")
elif angka == 11:
    print(f"{angka} good job")
if angka == 11:
    print('permainan selesai')
    