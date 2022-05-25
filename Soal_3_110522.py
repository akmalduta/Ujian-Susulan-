# Soal 3

def nilai(list):
    x=list[0]
    y=list[0]
    for i in list:
        if x>i:
            x=i
        elif y<i:
            y=i
    print(f"Nilai Terbesar Dari Data Adalah = {x}")
    print(f"Nilai Terkecil Dari Data Adalah = {y}")
def sorting(list):
    x=[]
    for i in list:
        if len(x)==0 or i>x[-1]:
            x.append(i)
        else:
            for j in x:
                if i<=j:
                    x.insert(x.index(j),i)
                    break
                else:
                    continue
    print(f"Hasil Sorting : {x}")

kumpulanAngka=list(input('Masukan Angka : ').split())
for i in range(len(kumpulanAngka)):
    kumpulanAngka[i]=int(kumpulanAngka[i])

sorting(kumpulanAngka)
nilai(kumpulanAngka)