#operasi aritmatika

a = 7
b = 3

#operasi tambah
hasil = a+b
print(a,'+',b, '=',hasil)

#operasi pengurangan 
hasil = a-b
print(a,'-',b, '=',hasil)

#operasi kali
hasil = a*b
print(a,'*',b, '=',hasil)

#operasi pembagian
hasil = a/b
print(a,'/',b, '=',hasil)

#operasi eksponen (pangkat)
hasil = a**b
print(a,'**',b, '=',hasil)

#operasi modulus % (sisa pembagian)
hasil = a%b
print(a,'%',b, '=',hasil)

#operasi floor division // (membulatkan hasil)
hasil = a//b
print(a,'//',b, '=',hasil)

#prioritas, operasional precedence
'''
1.()
2. exponen
3. perkalian dan teman teman (kali,bagi,modulus,floor devision)
'''
x= 3
y= 7
z= 8

hasil = x ** y * (z + x) / y - y % z // x 
print( x,'**',y,'*',z,'+',x,'/',y,'-',y,'%',z,'//',x,'=', hasil )

#kurung akan mengambil langkah pertama
hasil = x + y * z
print(x,'+',y,'*',z,'=',hasil ) 
hasil = (x + y) * z
print('(',x,'+',y,') *',z,'=', hasil )