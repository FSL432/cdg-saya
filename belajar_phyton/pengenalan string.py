data = 'ini adalah string'

print(type(data))
# cara membuat string

'''
 1. dengan menggunakan single quote'...'
 2. dengan menggunakan doble quote "..."
 3. dengan menggunakan tanda \
 4. string literal atau raw
'''

dot1 = 'ini string'
print(dot1)
dot2 = "ini string"
print(dot2)
print('ini str\'ing')

#blacklash
print('c\\user\\bagas')
#tab
print('saya \t\t\t jauh')
#backspace
print('saya \bdekat')
print('baris pertama \nbaris kedua')# LF -> line feed -> UNIX
print('baris pertama \rbaris kedua.')# CR -> carriage return -> commodore , acrn, lisp
print('baris pertama \n\rbaris kedua')#CRLF ->line feed carriage return -> dipakai oleh windows

#hati hati
print('c:\new folder') # akan aneh
print(r'c:\newfolder')

#multiline literal string
print(r"""
Nama : firdan
Umur : 19
email: firdan@gmail.com\unpad
""")