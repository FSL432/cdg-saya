import saint.module
from saint import fisika
from saint.fisika import gaya as force



hasil_tambah = saint.module.tambah(1,2,3,4,5)
print(f"ini hasul tambah = {hasil_tambah}")

gaya = fisika.gaya(90,10)
print(f"gaya adalah = {gaya}")

gaya = force(70,10)
print(f"gaya adalah = {gaya}")




