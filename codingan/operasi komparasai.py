# operasi kompirasi 
#setiap hail dsri operasi kompirasi adalah
# >,<,>=,<=,==,!=,is,is not

a =6
b=3

#lebih besar dari >
print("_____LEBIH BESAR DARI___>__")
hasil = a > 4
print(a,'>',4,'=',hasil )
hasil = b > 6
print(b,'>',6,'=',hasil)


#kurang dari dari <
print("_____KURANG DARI___<__")
hasil = a < 4
print(a,'<',4,'=',hasil )
hasil = b < 6
print(b,'<',6,'=',hasil)


#lebih dari sama dengan  >=
print("_____LEBIH DARI SAMA DENGAN___>=__")
hasil = a >= 6
print(a,'>=',6,'=',hasil )
hasil = b >= 3
print(b,'>=',3,'=',hasil)

#lebih dari sama dengan  <=
print("_____KURANG DARI SAMA DENGAN___<=__")
hasil = a <= 9
print(a,'<=',9,'=',hasil )
hasil = b <= 2
print(b,'<=',2,'=',hasil)

# sama dengan  ==
print("_____SAMA DENGAN___==__")
hasil = a == 6
print(a,'==', 9,'=',hasil )
hasil = b == 2
print(b,'==',2,'=',hasil)

# TIDAK sama dengan  !=
print("_____TIDAK SAMA DENGAN___==__")
hasil = a != 6
print(a,'!=', 9,'=',hasil )
hasil = b != 2
print(b,'!=',2,'=',hasil)

print("_____OBJECT IDENTITY___(IS)__")
#is sebagai komparasi object identity
x = 5 # ini adalah assigment membuat object 
y = 5
print ('nilai x =,',x,',id =', hex(id(x)))
print ('nilai x =,',y,',id =', hex(id(y)))
hasil = x is y 
print('x is y =',hasil)

print("_____OBJECT IDENTITY___(is not)__")
x = 5 
y = 6
print ('nilai x =,',x,',id =', hex(id(x)))
print ('nilai x =,',y,',id =', hex(id(y)))
hasil = x is y 
print('x is y =',hasil)
