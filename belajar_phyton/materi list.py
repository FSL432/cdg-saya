## ===== LIST =====
# kumpulan data numbers
angka = [1,2,3,6,7,8]
print(angka)

#kumpulan data string
string = ["jokowi","prabowo","anies"]
print(string)

# kumpulan dta boolean
bool = [True,False,True,True]
print(bool)

# kumpulan campuran 
campuran = [1,'jokowi',2,'anies',3,'ganjar',"mahmud",True,'gibran',False]
print(campuran)

# alternatif membuat list 
# range = range(0,10,2)# range(start,stop,step)
# print(range)
# data_list = list(range)
# print(data_list)

#membuat list dengan for loop ,list comprehensif
list_pake_for = [i**8 for i in range(0,10)]
print(list_pake_for)

# membuat list pake for pake if 
list_pake_for_dan_if = [i for i in range(0,20) if i != 6]
print(list_pake_for_dan_if)

list_pake_for_dan_if = [i**3 for i in range(0,20) if i%3 !=0]
print(list_pake_for_dan_if)











