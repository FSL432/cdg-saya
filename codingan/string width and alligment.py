#width anf multiline

nama = 'agus' 
umur = '20'
tinggi = '180'
nomor_sepatu = '42'

#string standar (dengan menggunakan enter atau newline \n)
data_string = f'nama = {nama}, umur = {umur}, tinngi = {tinggi}, nomor sepatu = {nomor_sepatu}'

#string multiline (kutip triplet)
center = "multiline".center(20,"=")
print("'"+center+"'")
data_string = f'nama = {nama},\numur = {umur},\ntinngi = {tinggi},\nnomor sepatu = {nomor_sepatu}'
print(data_string)

data_string = f""""
nama = {nama} , tinggi = {tinggi} cm
umur = {umur}
nomor sepatu = {nomor_sepatu}
"""
print(data_string)

# mengatur lebar nya
data_string = f""""
nama   = {nama:>3}.
tinggi = {tinggi:>4} cm
umur   = {umur:>5} th
sepatu = {nomor_sepatu:>6}
"""
print(data_string)




