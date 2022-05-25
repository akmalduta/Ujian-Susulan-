#Soal 4
def balikKata(list):
    terbalik=''
    for i in range(len(list)):
        terbalik+=list[len(list)-(i+1)]
    print(terbalik)

Kata=input('Masukan Sebuah Kalimat : ')

balikKata(Kata)