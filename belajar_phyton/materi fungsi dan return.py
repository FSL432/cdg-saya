'''fungsi dan return'''

#tempalate fungsi dan kembalian 
# def nama_fungsi(argument):
#    badan fungsi
#    return output

#fungsi kuadrat

def kuadrat(x):
    '''fungsi kuadrat'''
    output = x**2
    return output

y = kuadrat(9)
print(y)
c = kuadrat(8) / 8
print(c)


#fungsi tambah
# def tambah(a,b):
#     return a + b

# c = tambah(76,1)
# print(c)

def matematika(a,b):
    tambah = a + b
    kurang = a - b
    kali = a * b 
    bagi = a / b
    return tambah,kurang,kali,bagi

k,l,m,n = matematika(7,9)

print(f"hasil tambah ={k}")
print(f"hasil kurang ={l}")
print(f"hasil kali ={m}")
print(f"hasil bagi ={n}")









