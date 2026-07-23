# teknik menduplikat list


a = ['owo','owi','joko']
print(f'a = {a}')
b = a #ini bukan menduplikat
print(f'b = {b}')

#merubah isi dari list
a[1] = 'ganjar'
b.sort()
print(f'a = {a}')
print(f'b = {b}')

#addres dari list a dan b
print(f' a = {hex(id(a))}')
print(f' b = {hex(id(b))}')

#menduplikat dengan menggunakn copy
print('='*20)
c = a.copy() #ini data duplikat (copy)
print(f' a = {hex(id(a))}')
print(f' b = {hex(id(b))}')
print(f' b = {hex(id(c))}')


print(f'a = {a}')
print(f'b = {b}')
print(f'b = {c}')

c[1] = 'gibran'
print(f'b = {c}')




