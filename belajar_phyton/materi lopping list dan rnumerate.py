# materi looping dari list
# for loop
print("for loop")
kumpulan_angka = [1,5,8,3,4,9,5,]

for angka in kumpulan_angka:
    print(f"angka = {angka}")

peserta = ["joko","owi","bahlil","mega"]

for nama in peserta:
    print(f"nama = {nama}")

#for loop dam range
print("\nfor loop dan range")
kumpulan_angka = [3,5,6,7,8,9]
panjang = len(kumpulan_angka)
for a in range(panjang):
    print(f"angka = {kumpulan_angka[a]}")

# while loop
print("\nwhile loop")
kumpulan_angka = [3,4,6,5,7,]
panjang = len(kumpulan_angka)
i = 0
while i < panjang:
    print(f"angka = {kumpulan_angka[i]}")
    i += 1

# list comprehension
print(f"\nlist comprehension")
data = ["prabowo",0,2,6,"jokowi"]
[print(f"data = {i}") for i in data]

angka = [80,7,5,6,4]
kuadrat = [i**2 for i in angka]
print(f"hasil = {kuadrat}")

#enumerate
print(f"\nenumerate")
data_list = ["prabowo",0,2,6,"jokowi"]

for index,data in enumerate(data_list):
    print(f"ini index = {index} ,ini data = {data}")











