numero1 = int(input('Ingrese un número: '))
numero2 = int(input('Ingrese un número: '))

if numero2 < numero1:
    aux = numero2
    numero2 = numero1
    numero1 = aux

print(f'{numero1} - {numero2}')

