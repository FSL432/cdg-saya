#-------0+++++++5-------8+++++++11------
masukan= float(input("masukan angka lebih dari 0 dan kurang dari 5 \n lebih dari 8 kurang dari 11: "))

lebihdarisatuan= (masukan >= 0)
kurangdarisatuan= (masukan <= 5)
lebihdari = (masukan >= 8)
kurangdari= (masukan <=11)
#print("kursng dari 5=", kurangdarisatuan)
#print("lebih dari 8=", lebihdari)
#print("lebih dari 0=", lebihdarisatuan)
#print("kurang dari 11=", kurangdari)

jawabanbenar = lebihdarisatuan and kurangdarisatuan 
print("masukan angka :",jawabanbenar)

jawabanbenar2 = lebihdari and kurangdari
print("masukan angka :",jawabanbenar2)

print("\n",10*"=","\n")
masukan= float(input("masukan angka: "))

lebihdarisatuan= (masukan <= 0)
kurangdarisatuan= (masukan >= 5)
lebihdari = (masukan <= 8)
kurangdari= (masukan >=11)

jawabanbenar = lebihdarisatuan or kurangdarisatuan 
print("masukan angka :",jawabanbenar)

jawabanbenar2 = lebihdari or kurangdari
print("masukan angka :",jawabanbenar2)






