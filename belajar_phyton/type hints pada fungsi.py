'''type hints pada fungsi'''

#bentuk standar fungsi yang sudah di pelajari
'''def fungsi(parameter):
    hasil = parameter
    print(hasil)

fungsi(1)
fungsi("ucup")
fungsi(True)
'''
import string
import os
os.system("cls")
print(f"{"materi type hints pada fungsi":^40}")

#prnggunaan type hints
def pangkat_sepuluh(argument:int) -> int:
    '''fungsi dengan hints'''
    output = 10**argument
    return output
HASIL = pangkat_sepuluh(2)
print(HASIL)

def display(argument:string):
    print(argument)
display("joko")

















