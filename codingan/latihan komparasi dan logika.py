#latihan logika dan komparasi
#membuat gabungan are rentang dari angka 
#+++++++++3-----------10++++++++
inputUser = float(input('masukan angka yang bernilai \n kurang dari 3 \n atau\n lebih besar dari 10  :'))

# ++++++++3---------------------
#memriksa angka kurang dari 3
iskurangdari = (inputUser < 3)
print("kurang dari 3=", iskurangdari)

#memeriksa angka lebih dari 10
islebihdari = (inputUser > 10)
print("lebih dari 10= ",islebihdari )

#+++++++3----------10++++++++++
iscoorect = iskurangdari or islebihdari
print("masukan angka :", iscoorect)


#------3++++++++10---------
#kasus irisan
print("\n",10*"=","\n")
inputUser = float(input('masukan angka yang bernilai \n lebih dari 3 \n dan\n kurang dari 10  :'))

#------3+++++++++++++++++++++++
#lebih dari 3
islebihdari = (inputUser > 3)
print("lebih dari 3=", islebihdari)

#++++++++++++++++++10----------
#memriksa angka lebih dari 10
iskurangdari = (inputUser < 10)
print("lebih dari 10=",iskurangdari)

#------3++++++++10---------
iscoorect = iskurangdari and islebihdari
print("masukan angka :", iscoorect)
