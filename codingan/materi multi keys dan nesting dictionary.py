
import datetime

mahasiswa1 = {
    'nama' : 'ujang supratman',
    'nim' : '863468763',
    'sks_lulus' : 130 ,
    'beasiswa' : False,
    'lahir' : datetime.datetime(2000,4,12)
}

mahasiswa2 = {
    'nama' : 'heru jaya',
    'nim' : '863468776',
    'sks_lulus' : 127 ,
    'beasiswa' : True,
    'lahir' : datetime.datetime(2008,9,17)
}

mahasiswa3 = {
    'nama' : 'nanang jayana',
    'nim' : '8634689876',
    'sks_lulus' : 120 ,
    'beasiswa' : False,
    'lahir' : datetime.datetime(2011,1,11)
}

data_mahasigma = {
    'MAH001' : mahasiswa1,
    'MAH002' : mahasiswa2,
    'MAH003' : mahasiswa3,
}
print(F"{'KEY':<6} {'NAMA':<17} {'SKS':<3} {'BEASISWA':<10} {'LAHIR':<10}" ) 
print("_"*50)

for mahasiswa in data_mahasigma:
    KEY = mahasiswa
    NAMA = data_mahasigma[KEY]['nama']
    NIM = data_mahasigma[KEY]['nim']
    SKS = data_mahasigma[KEY]['sks_lulus']
    BEASISWA = data_mahasigma[KEY]['beasiswa']
    LAHIR = data_mahasigma[KEY]['lahir'].strftime("%x")

    print(F"{KEY:<6} {NAMA:<17} {SKS:<3} {BEASISWA:^10} {LAHIR:<10}" ) 










