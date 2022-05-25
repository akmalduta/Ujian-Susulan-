# Soal 2

def rata2(list):
    x=0
    for i in list:
        x+=i
    return x/len(list)

def var(list):
    sum=0
    for i in list:
        x=i-rata2(list)
        x**=2
        sum+=x
    return sum/((len(list)-1))

def stdev(list):
    x=math.sqrt(var(list))
    return x

banyakData=input('Masukkan Banyaknya Data : ')
data=[]

for i in range(int(banyakData)):
    data.append(int(input(f'Data ke -{i+1} : ')))
print(data)

print(f'Rata-Ratanya Adalah {rata2(data)}')

print(f'Variansinya Adalah {var(data)}')
   


print(f'Standar Deviasinya Adalah {stdev(data)}')