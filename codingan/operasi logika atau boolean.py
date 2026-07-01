#operasi logika atau boolean

#not , or, and xor
print('=====NOT=====')
a = True
c = not a 
print('data a =',a)
print('---------------NOT')
print('data c =',c)

#OR (jika salah satu true maka true)
print('=====OR=====')
a = False
b = False
c = a  or b 
print(a,'OR',b,'=',c)
a = False
b = True
c = a or b 
print(a,'OR',b,' =',c)
a = True
b = False
c = a or b 
print(a,'OR',b,' =',c)
a = True
b = True
c = a or b 
print(a,'OR',b,'  =',c)

#OR (jika keduanya true maka true ,jika salah satu false maka false)
print('=====AND=====')
a = False
b = False
c = a  and b 
print(a,'and',b,'=',c)
a = False
b = True
c = a and b 
print(a,'and',b,' =',c)
a = True
b = False
c = a and b 
print(a,'and',b,' =',c)
a = True
b = True
c = a and b 
print(a,'and',b,'  =',c)

#OR (dia akan true jika salah satu true,jika dua maka  false)
print('=====XOR=====')
a = False
b = False
c = a ^ b 
print(a,'XOR',b,'=',c)
a = False
b = True
c = a ^ b 
print(a,'XOR',b,' =',c)
a = True
b = False
c = a ^ b 
print(a,'XOR',b,' =',c)
a = True
b = True
c = a ^ b 
print(a,'XOR',b,'  =',c)



