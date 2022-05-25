##Soal 5
def banyakKapital(x):
    jumlahKapital=0
    kapital=list('QWERTYUIOPASDFGHJKLZXCVBNM')
    for i in x:
        if i in kapital:
            jumlahKapital+=1
    return jumlahKapital

def banyakHurufKecil(x):
    jumlahHurufKecil=0
    hurufKecil=list('qwertyuiopasdfghjklzxcvbnm')
    for i in x:
        if i in hurufKecil:
            jumlahHurufKecil+=1
    return jumlahHurufKecil
Kalimat=input('Masukkan Sebuah Kalimat : ')

print(f'Kalimat Original : {Kalimat}')
print(f'Banyaknya Jumlah Huruf Kapital Dalam Kalimat Adalah : {banyakKapital(Kalimat)}')
print(f'Banyaknya Jumlah Huruf NonKapital Dalam Kalimat Adalah : {banyakHurufKecil(Kalimat)}')