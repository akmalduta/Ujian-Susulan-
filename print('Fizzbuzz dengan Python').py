print('Fizz Buzz dengan Python')

x = int(input("masukkan angkanya : "))

if x % 3 == 0 and x % 5 == 0:
    print(f'FizzBuzz')
elif x % 3 == 0:
    print('Fizz')
elif x % 5 == 0:
    print('buzz')
else: 
    print('error')