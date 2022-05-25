from tkinter import E


massa = float(input('Massa dalam Kg: '))
tinggi = float(input('Tinggi dalam Cm: '))
tinggi_m = tinggi/100
imt = massa / (tinggi**2)
print(f'Massa{massa} Kg, Tinggi{tinggi} Meter')
if imt < 18.5:
    print(f'IMT = {imt}, berat badan kurang')
elif imt >= 18.5 and imt < 24.9:
    print(f'IMT = {imt}, berat badan ideal')
elif imt >= 25 and imt < 29.9:
    print(f'IMT = {imt}, berat badan berlenih')
elif imt >= 30 and imt < 39.9:
    print(f'IMT = {imt}, berat badan sangat berlebih')
else:#IMT > 39.9
    print(f'IMT = {imt}, Obeitas')