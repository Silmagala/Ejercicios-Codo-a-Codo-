def suma(num):
    s = 0
    num1 = str(num)
    for x in num1:
        x1 = int(x)
        s = x1 + s
    return s

ss = 0
numero = int(input('Ingrese un número o 0 para finalizar: '))
while numero != 0:
    print(f'Suma de digitos {suma(numero)}')
    ss += numero
    numero = int(input('Ingrese un número o 0 para finalizar: '))
print(f'suma = {ss}')
print(f'Suma de digitos {suma(ss)}')

