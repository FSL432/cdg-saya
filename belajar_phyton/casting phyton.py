#merubah dari satu tipe ke tipe lainnya
#data int
print("======INTEGER======")
data_int = 9;
print("data = ", data_int , ",type=", type(data_int))

data_float = float(data_int)
data_complex = complex(data_int)
data_str = str(data_int)
data_bool = bool(data_int)#akan false jika nilai 0
print("data =" , data_float, ",type =" ,type(data_float))
print("data =", data_complex, ",type=" ,type(data_complex))   
print("data =", data_str, ",type=" ,type(data_str))   
print("data = ", data_bool, ",type=" ,type(data_bool))

##float
print("======FLOAT======")
data_float = 0;
print("data = ", data_float , ",type=", type(data_float))

data_int = int(data_float)#akan dibulatkan ke bawah
data_str = str(data_float)
data_bool = bool(data_float)
print("data = ", data_int, ",type =" ,type(data_int))
print("data = ", data_str, ",type=" ,type(data_str))   
print("data = ", data_bool, ",type=" ,type(data_bool))

print("======BOOLEAN======")
data_bool = False;
print("data = ", data_bool , ",type=", type(data_bool))

data_complex = complex(data_bool)
data_int = int(data_bool)#
data_str = str(data_bool)
data_float = float(data_bool)
print("data = ", data_int, ",type =" ,type(data_int))
print("data = ", data_str, ",type=" ,type(data_str))   
print("data = ", data_float, ",type=" ,type(data_float))

print("======STRING======")
data_str ="false";
print("data = ", data_str , ",type=", type(data_str))

data_int = int(data_str) #harus berupa angka
data_complex = complex(data_str)
data_bool = bool(data_str) #false jika string kosong
data_float = float(data_str)
print("data = ", data_int, ",type=" ,type(data_int))   
print("data =", data_complex, ",type=" ,type(data_complex))
print("data = ", data_bool, ",type =" ,type(data_bool))
print("data = ", data_float, ",type=" ,type(data_float))
