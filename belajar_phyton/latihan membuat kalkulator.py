# password = input('masukan password :')

# if password == "1234" :
#     print('benar')
# else:
#     print('coba lagi')

# kalkulator sederhana
while True:
  print(10*"=" + " KALKULATOR SEDERHANA " + 10*"=")
  ke1 = float(input('masukan angka ke 1 ='))
  operator = input('operator (+,-,*,/, =)')
  ke2 = float(input("masukan angka ke dua ="))


# percabangan nya
  if operator == "+":
    hasil = ke1 + ke2 
    print(f'hasilnya adalah={hasil}')
  elif operator == "-":
    hasil = ke1 - ke2 
    print(f'hasilnya adalah={hasil}')
  elif operator == '*':
    hasil = ke1 * ke2
    print(f'hasilnya adalah={hasil}')
  elif operator == "/":
    hasil = ke1 / ke2 
    print(f'hasilnya adalah={hasil}')
  elif operator == "**":
    hasil = ke1 ** ke2
    print(f'hasilnya adalah={hasil}')
  elif operator == "%":
    hasil = ke1 % ke2 
    print(f'hasilnya adalah={hasil}')

  else :
    print('kalo ngeinput yang bener mas!!!')







