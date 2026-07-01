#format string 
#contoh generic
#strinf
nama = 'ujang'
format_str = f'hello {nama} '
print(format_str)

#boolean 
boolean = True
format_str = f'boolean = {boolean}'
print(format_str)

#angka 
angka = 2026.7
format_str = 'angka =' + str(angka)
print(format_str)

# bilanga bulat
angka = 15
format_str = f'bilangan bulat = {angka:d}'
print(format_str)


# bilanga ribuan
angka = 4000
format_str = f'bilangan ribuan = {angka:,}'
print(format_str)


# bilangan desimal
angka = 2026.7876
format_str =f'desimal = {angka:.3f}'
print(format_str)


# menampilkan leading zero
angka = 2026.7876
format_str =f'desimal = {angka:+09.3f}'
print(format_str)


#menampilkan tanda + dan -

minus = -9
positif = 9
format_minus = f'minus= {minus:-d}'
format_positif = f'positif = {positif:+d}'


print(format_positif)
print(format_minus)

# format %
persentase = 0.765
format_persentase = f'persentase = {persentase:.1%}'
print('persentase nya adalah =',(format_persentase))

#melakukan operasi aritmatika di dalam placeholde
harga = 50000
jumlah = 5

format_string = f'harga total = Rp {harga*jumlah:,}'
print(format_string)

print(20*'=')

#format angka lain (binary,octal,hexdecimal)
angka = 765
binary =f'binary = {bin(angka)}'
octal =f'octal = {oct(angka)}'
hex =f'hexadecimal = {hex(angka)}'

print ('binary = ' + (binary))
print ('hexadecimal = '+ (hex))
print ('octal = '+ (octal))
print('nilai :','binary :',angka,format(angka,'08b'))

