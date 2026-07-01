# tipe data : angka sataun (integer)
data_integer = 1
print(data_integer)
print("data : ", data_integer, " , bertipe : ", type(data_integer))

# tipe data float angka dengan koma(float)
data_float = 2,9
print("data : ", data_float)
print("- bertipe : ", type(data_float))

#tipe data string kumpulan karakter (string)
data_string = "aden"
print("data : ", data_string)
print("- bertipe :", type(data_string))

#tipe data boolean true/false (boolean)
data_boolean = False 
print("data : ", data_boolean)
print("- bertipe :", type(data_boolean))

#tipe data khusus 
# bilangan kompleks 
data_complex = complex(8,7)
print("data :", data_complex)
print("- bertipe : ", type(data_complex))

# tipe data dari bahasa C 
from ctypes import c_double 
# c_double c_char c_long 
data_c = c_double(10.5)
print("data :", data_c)
print("- bertipe : ", type(data_c))

