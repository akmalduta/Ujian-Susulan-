import math as mp


# Soal 1
print("Soal no 1")

print('balonku ada lima\n\t rupa rupa warnanya\n\t\t hijau kuning kelabu\n\t\t\t \ merah muda dan biru\n meletus balon hijau\n\t hatiku sangat kacau\n\t\t balon ku tinggal empat\n\t\t\t kupegang erat erat')

# Soal 2
print("Soal no 2")

r_circle = float(input("Jari-jari circle: "))
luas = mp.pi*r_circle**2
keliling = mp.pi*r_circle*2
print("Luas Circle: ", mp.floor(luas))
print("keliling Circle:",mp.floor(keliling))

# Soal 3
print("Soal no 3")

kalimat_Utama = str(input("masukkan sebuah kalimat: "))
kalimat_pengganti =int(input("masukkan kalimat pengganti: "))


# Soal 4
print("Soal no 4")


# Soal 5
print("Soal no 5")

r_cy1 = float(input("jari-jari alas Cylinder: "))
h_cy1 = float(input("tinggi Cylinder: "))
vol_cy1 = mp.pi*h_cy1*r_cy1**2
luas_cy1 = 2*(mp.pi*r_cy1**2) + 2*(mp.pi*h_cy1*r_cy1)
print("Volume Cylinder: ", vol_cy1)
print("luas permukaan Cylinder: ",luas_cy1)
