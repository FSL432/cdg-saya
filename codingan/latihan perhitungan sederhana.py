# latihan konversi setuan temperatur
#program konversi celcius ke satuan lain

print("\nPROGRAM KONVERSI TEMPERATUR\n")
celcius = float (input('masuka suhu dalam celcius :'))
print("suhu adalah",celcius,"celcius" )

#reamur
reamur = 4/5*celcius
print("suhu dalam reamur adalah",reamur,"reamur")

#farenheat
farenheat = ((9/5)* celcius) + 32
print("suhu dalam fahrenheat adalah",farenheat,"fahrenheat")


#kelvin
kelvin = celcius  + 273
print("suhu dalam kelvin adalah",kelvin,"kelvin")

