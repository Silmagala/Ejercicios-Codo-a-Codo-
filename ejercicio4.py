num1 = int(input('Digite el primer número: '))
num2 = int(input('Digite el segundo número: '))
num3 = int(input('Digite el tercer número: '))

if num1 > num2:
    if num2 > num3:
        suma = num1 + num2
    else:
        suma = num1 + num3
else:
    if num1 > num3:
        suma = num2 + num1
    else:
        suma = num2 + num3
print(f'Suma = {suma}')